from copyreg import constructor
from flask import Flask,request
from mini import MiniPhotoshop
from flask_cors import CORS
import numpy as np
from PIL import Image,ImageOps
import json
import base64
import os
import cv2

mini = MiniPhotoshop()

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def convertStr2Img(image_string,name="tmp.jpg"):
  image_data = base64.b64decode(str(image_string).split(',')[-1])
  with open(name, "wb") as fh:
    fh.write(image_data)
  # return "./tmp.jpg"

def convertImg2Str(image):
  # im_pil = Image.fromarray(image)
  # buffered = io.BytesIO()
  # im_pil.save(buffered, format="PNG")
  # img = cv2.imread('test_image.jpg')
  jpg_img = cv2.imencode('.jpg', image)
  img_str = str(base64.b64encode(jpg_img[1]).decode('ascii'))
  return img_str

@app.route("/")
def init():
  img = mini.load("./tmp.jpg")
  strimg = convertImg2Str(img)
  # {"data":strimg}
  return strimg

@app.route("/delete")
def delete():
  os.remove("./tmp.jpg")
  return {"data":"deleted"}

@app.route("/upload",methods=['POST'])
def upload():
  req = json.loads(request.data)
  # print(req)
  image_string = req["data"]
  if image_string == '':
    return {"data": "no image found"}
  convertStr2Img(image_string)
  return {"data":image_string}

@app.route("/resize",methods=['POST'])
def resize():
  req = json.loads(request.data)
  # print(req['width'])
  try:
    width = req['width']
    hight = req['hight']
    img = mini.load("./tmp.jpg")
    img = mini.resize(img,width,hight)
    save = mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/flip",methods=['POST'])
def flip():
  req = json.loads(request.data)
  try:
    flip = req['flip']

    img = mini.load("./tmp.jpg")

    img = mini.flip(img,flip)
    
    save = mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/rotate",methods=['POST'])
def rotate():
  req = json.loads(request.data)
  try:
    rotate = req['rotate']

    img = mini.load("./tmp.jpg")

    img = mini.rotate(img,rotate)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/crop",methods=['POST'])
def crop():
  req = json.loads(request.data)
  print("req",req)
  try:
    x = req['x']
    y = req['y']
    w = req['w']
    h = req['h']

    img = mini.load("./tmp.jpg")

    img = mini.crop(img,x,y,h,w)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/convert2gray",methods=['POST'])
def convert2gray():
  # req = json.loads(request.data)
  try:

    img = mini.load("./tmp.jpg")

    img = mini.convert2gray(img)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/addBrightnessAndContrast",methods=['POST'])
def addBrightnessAndContrast():
  req = json.loads(request.data)
  try:
    brightness = req['brighness']
    contrast = req['contrast']
    img = mini.load("./tmp.jpg")

    img = mini.addBrightnessAndContrast(img,brightness,contrast)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/invert",methods=['POST'])
def invert():
  # req = json.loads(request.data)
  try:

    img = mini.load("./tmp.jpg")

    img = mini.invert(img)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/calHistogram",methods=['POST'])
def calHistogram():
  # req = json.loads(request.data)
  try:

    img = mini.load("./tmp.jpg")

    mini.calHistogram(img)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    hist = mini.load('./calhist.jpg')
    # print(hist)
    strhist = convertImg2Str(hist)
    return {"data":strimg,"hist":strhist}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/addSultAndPaperNoise",methods=['POST'])
def addSultAndPaperNoise():
  req = json.loads(request.data)
  try:
    prob = req['prob']
    img = mini.load("./tmp.jpg")

    img = mini.addSultAndPaperNoise(img,prob)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/addGossionNoise",methods=['POST'])
def addGossionNoise():
  req = json.loads(request.data)
  try:
    prob = req['prob']
    img = mini.load("./tmp.jpg")

    img = mini.addGossionNoise(img,prob)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/blurBox",methods=['POST'])
def blurBox():
  req = json.loads(request.data)
  try:
    k = req['k']
    img = mini.load("./tmp.jpg")

    img = mini.blurBox(img,k)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/blurGaussian",methods=['POST'])
def blurGaussian():
  req = json.loads(request.data)
  try:
    k = req['k']
    img = mini.load("./tmp.jpg")

    img = mini.blurGaussian(img,k)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/blurMedian",methods=['POST'])
def blurMedian():
  req = json.loads(request.data)
  try:
    k = req['k']
    img = mini.load("./tmp.jpg")

    img = mini.blurMedian(img,k)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/sharpen",methods=['POST'])
def sharpen():
  req = json.loads(request.data)
  try:
    k = req['k']
    img = mini.load("./tmp.jpg")

    img = mini.sharpen(img,k)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/edgeDetect",methods=['POST'])
def edgeDetect():
  req = json.loads(request.data)
  try:
    sigma = req['sigma']
    img = mini.load("./tmp.jpg")

    img = mini.edgeDetect(img,sigma)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/subtract",methods=['POST'])
def subtract():
  req = json.loads(request.data)
  try:
    image_string = req["data"]
    if image_string == '':
      return {"data": "no image found"}
    convertStr2Img(image_string,name='tmp2.jpg')

    img = mini.load("./tmp.jpg")
    img2 = mini.load("./tmp2.jpg")
    img = mini.subtract(img,img2)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/blend",methods=['POST'])
def blend():
  req = json.loads(request.data)
  try:
    image_string = req["data"]
    alpha = req["alpha"]
    
    convertStr2Img(image_string,name='tmp2.jpg')

    img = mini.load("./tmp.jpg")
    img2 = mini.load("./tmp2.jpg")
    img = mini.blend(img,img2,alpha)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/whiteBalance",methods=['POST'])
def whiteBalance():
  req = json.loads(request.data)
  try:

    img = mini.load("./tmp.jpg")
    img = mini.whiteBalance(img)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/addRGB",methods=['POST'])
def addRGB():
  req = json.loads(request.data)
  try:
    red = req["red"]
    green = req["green"]
    blue = req["blue"]

    img = mini.load("./tmp.jpg")

    img = mini.addRGB(img,red,green,blue)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/addHSV",methods=['POST'])
def addHSV():
  req = json.loads(request.data)
  try:
    hue = req["hue"]
    sat = req["sat"]
    val = req["val"]

    img = mini.load("./tmp.jpg")

    img = mini.addHSV(img,hue,sat,val)
    
    mini.save(img,'tmp.jpg')
    strimg = convertImg2Str(img)
    return {"data":strimg}
  except Exception as e:
    print(e)
    return {"data": "err"}

@app.route("/showHistogramRGB",methods=['GET'])
def showHistogramRGB():
  # req = json.loads(request.data)
  try:
    img = mini.load("./tmp.jpg")
    h,w = img.shape[:2]
    mini.showHistogramRGB(img)
    hist = mini.load('./histRGB.jpg')
    # print(hist)
    strhist = convertImg2Str(hist)
    strimg = convertImg2Str(img)
    return {"data":strimg,"hist":strhist,"h":h,"w":w}
  except Exception as e:
    print(e)
    return {"data": "err"}

if __name__ == '__main__':
  app.run(debug=True,port=5000)