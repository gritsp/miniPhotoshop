import cv2
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import random

class MiniPhotoshop:
  # def __init__(self):
    # img = cv2.imread(pathImg)
    # self.pathImg = pathImg
    # return img

  def load(self,pathImg):
    image = cv2.imread(pathImg)
    print('read img from:',pathImg)
    return image

  def save(self,img,name):
    print("Saving image name:",name)
    cv2.imwrite(name,img)
    print("Done")

  def flip(self,img,code):
    print('flip vertical') if code==0 else print('flip horizon')
    image = cv2.flip(img,code)
    return image

  def rotate(self,img,degree=0):
    print("rotate",degree)
    (h, w) = img.shape[:2]
    (cX, cY) = (w//2,h//2)
    degree = -90 if degree == "cw" else 90 if degree == "ccw" else degree 
    M = cv2.getRotationMatrix2D((cX, cY), degree, 1.0)
    image = cv2.warpAffine(img, M, (w, h))
    return image

  def crop(self,img,x,y,h,w):
    print('crop image at ',x,y,'size',h,w)
    image = img[y:y+h, x:x+w]
    return image

  def convert2gray(self,img):
    print("covert to gray")
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return image

  def resize(self,img,scale_width=100,scale_height=100):
    width = int(img.shape[1] * scale_width / 100)
    height = int(img.shape[0] * scale_height / 100)
    dim = (width, height)
    # resize image
    print('old size:',img.shape[1],img.shape[0])
    image = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    print('resize scale width:',scale_width,'scale hight:',scale_width)
    print('new size:',width,height)
    return image

  def changeScale(self,value, inMin, inMax, outMin, outMax):
    return float((value-inMin) * (outMax-outMin) / (inMax-inMin) + outMin)

  def addBrightnessAndContrast(self,img,brightness=0,contrast=1):
    img2 = img.copy()
    brightness = int(self.changeScale(brightness, -100, 100, -255, 255))
    contrast = int(self.changeScale(contrast, -100, 100, -127, 127))

    if brightness != 0:
      if brightness > 0:
        shadow = brightness
        highlight = 255
      else:
        shadow = 0
        highlight = 255 + brightness
      alpha = (highlight - shadow)/255
      gamma = shadow
      image = cv2.addWeighted(img, alpha, img2, 0, gamma)
    else:
      image = img2

    if contrast != 0:
      image2 = image.copy() 
      f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
      alpha = f
      gamma = 127*(1-f)
      image = cv2.addWeighted(image, alpha, image2, 0, gamma)
    print("add brightness:",brightness,"contrast:",contrast)
    return image
  
  def invert(self,img):
    image = cv2.bitwise_not(img)
    print("inver color image")
    return image

  def calHistogram(self,img):
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    # cdf = hist.cumsum()
    # cdf_normalized = cdf * float(hist.max()) / cdf.max()
    fig = plt.figure()
    plt.plot(hist, color = 'b')
    # plt.hist(img.flatten(),256,[0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend(('histogram'), loc = 'upper left')
    # plt.show()
    fig.savefig('calhist.jpg')

  def addSultAndPaperNoise(self,img,prob):
    output = np.zeros(img.shape,np.uint8)
    thres = 1 - self.changeScale(prob,0,1,0,0.5) 
    for i in range(img.shape[0]):
      for j in range(img.shape[1]):
        rdn = random.random()
        if rdn < prob:
            output[i][j] = 0
        elif rdn > thres:
            output[i][j] = 255
        else:
            output[i][j] = img[i][j]
    return output

  def addGaussianNoise(self,img,prob):
    gaussian_noise = np.zeros((img.shape[0], img.shape[1]),dtype=np.uint8)
    cv2.randn(gaussian_noise, 0, 128)
    gaussian_noise = (gaussian_noise*prob).astype(np.uint8)
    image = cv2.add(img,gaussian_noise)
    return image
  
  def blurBox(self,img,k):
    image = cv2.blur(img,(k, k))
    return image
  
  def blurGaussian(self,img,k):
    image = cv2.GaussianBlur(img, (k, k),0)
    return image

  def blurMedian(self,img,k):
    image = cv2.medianBlur(img, k)
    return image
#  cv2.medianBlur(image, figure_size)
  
  def sharpen(self,img,k):
    k = self.changeScale(k,0,100,1,2)
    print('sharpen :',k)
    smoothed = cv2.GaussianBlur(img, (9, 9), 10)
    # print(smoothed) 
    # sharpFilter = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    image = cv2.addWeighted(img, k, smoothed, -0.5, 0)
    # image = cv2.filter2D(img,k,sharpFilter)
    return image
  
  def edgeDetect(self,img, sigma=0.33):
    blurred = cv2.GaussianBlur(img, (3, 3), 0)
    v = np.median(blurred)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(blurred, lower, upper)
    return edged

  def subtract(self,img1,img2):
    h,w = img1.shape[:2]
    img2 = cv2.resize(img2, (h,w), interpolation = cv2.INTER_AREA)

    image = cv2.subtract(img1, img2)
    return image
  
  def blend(self,img1,img2,alpha):
    h,w = img1.shape[:2]
    img2 = cv2.resize(img2, (h,w), interpolation = cv2.INTER_AREA)
    alpha = self.changeScale(alpha,0,100,0,1)

    beta = (1.0 - alpha)
    dst = cv2.addWeighted(img1, alpha, img2, beta, 0.0)
    return dst
  
  def whiteBalance(self,img):
    b, g, r = cv2.split(img)
    r_avg = cv2.mean(r)[0]
    g_avg = cv2.mean(g)[0]
    b_avg = cv2.mean(b)[0]
    # Find the gain occupied by each channel
    k = (r_avg + g_avg + b_avg)/3
    kr = k/r_avg
    kg = k/g_avg
    kb = k/b_avg
    
    r = cv2.addWeighted(src1=r, alpha=kr, src2=0, beta=0, gamma=0)
    g = cv2.addWeighted(src1=g, alpha=kg, src2=0, beta=0, gamma=0)
    b = cv2.addWeighted(src1=b, alpha=kb, src2=0, beta=0, gamma=0)
    
    image = cv2.merge([b, g, r])
    return image
  
  def addRGB(self,img,red,green,blue):
    h,w = img.shape[:2]
    b, g, r = cv2.split(img)
    print(b[0][0])
    for i in range(h):
      for j in range(w):
        b[i][j] = 0 if (b[i][j] + blue)<=0 else b[i][j] + blue if (b[i][j] + blue)<=255 else 255
        g[i][j] = 0 if (g[i][j] + green)<=0 else g[i][j] + green if (g[i][j] + green)<=255 else 255
        r[i][j] = 0 if (r[i][j] + red)<=0 else r[i][j] + red if (r[i][j] + red)<=255 else 255
    print(b[0][0])
    merged = cv2.merge([b, g, r])
    return merged

  def addHSV(self,img,hue,sat,val):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hight,width = img.shape[:2]
    h, s, v = cv2.split(hsv)
    # print(b[0][0])
    for i in range(hight):
      for j in range(width):
        h[i][j] = 0 if (h[i][j] + hue)<=0 else h[i][j] + hue if (h[i][j] + hue)<=255 else 255
        s[i][j] = 0 if (s[i][j] + sat)<=0 else s[i][j] + sat if (s[i][j] + sat)<=255 else 255
        v[i][j] = 0 if (v[i][j] + val)<=0 else v[i][j] + val if (v[i][j] + val)<=255 else 255
    # print(b[0][0])
    merged = cv2.merge([h, s, v])
    image = cv2.cvtColor(merged,cv2.COLOR_HSV2BGR)
    return image

  def shape(self,img):
    h,w = img.shape[:2]
    return (h,w)
  
  def showHistogramRGB(self,img):
    bgr_planes = cv2.split(img)
    histSize = 256
    hist_h = 400
    histRange = (0, 256) # the upper boundary is exclusive
    accumulate = False
    b_hist = cv2.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
    g_hist = cv2.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate)
    r_hist = cv2.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate)
    
    b = cv2.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
    g = cv2.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
    r = cv2.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
    fig = plt.figure()

    plt.plot(b, color = 'b')
    plt.plot(g, color = 'g')
    plt.plot(r, color = 'r')
    # plt.hist(img.flatten(),256,[0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend(('histogram'), loc = 'upper left')
    fig.savefig('histRGB.jpg')
    # plt.show()