import { Button, Card, InputNumber, Row, Col,Space, Divider } from 'antd';
import axios from 'axios';
import React, { useEffect, useState } from 'react';

const PixelTrans = ({image}) => {
  const [brighness,setBrightness] = useState(0)
  const [contrast,setContrast] = useState(0)
  const [probSP,setProbSP] = useState(0)
  const [probGS,setProbGS] = useState(0)
  const [histPic,setHistPic] = useState(null)

  useEffect(()=>{
    console.log('histPic',histPic)
  },[histPic])
  const post = (value,fn)=>{
    axios.post(`http://127.0.0.1:5000/${fn}`,value)
    .then(doc=>{
      if(doc.data.data){
        if(fn=="calHistogram") setHistPic("data:image/jpg;base64,"+doc.data.hist)
        else image("data:image/jpg;base64,"+doc.data.data)
      }
      console.log(doc)
    })
  }
  const handle2gray = async () =>{
    await post({},'convert2gray')
  }

  const handleBC = async () =>{
    let data = {
      contrast,brighness
    }
    await post(data,'addBrightnessAndContrast')
  }

  const handleInvert = async () =>{
    await post({},'invert')
  }

  const handleHist = async ()=>{
    await post({},"calHistogram")
  }

  const handleCloseHist = ()=>{
    setHistPic(null)
  }

  const handleSP = async () =>{
    let data = {
      prob:probSP
    }
    await post(data,'addSultAndPaperNoise')
  }

  const handleGS = async () =>{
    let data = {
      prob:probGS
    }
    await post(data,'addGaussianNoise')
  }


  return (
    <>
      <Card
        size="small"
        // title="Geometric Transformation"
        style={{
          width: "100%",
        }}
      >
        <Row>
          <Space>
            <Button onClick={handle2gray}>Convert to gray-scale</Button>
            <Button onClick={handleInvert}>Invert Image</Button>
          </Space>
        </Row>
        <Row>
          <Divider>brightness and contrast</Divider>
          <Space>
            <InputNumber addonBefore='Brightness' min={-100} max={100} onChange={e=>setBrightness(e)} />
            <InputNumber addonBefore='Contrast' min={-100} max={100} onChange={e=>setContrast(e)} />
            <Button onClick={handleBC}>Ok</Button>
          </Space>
        </Row>
        <Row>
          <Divider>Histogram equalization</Divider>
          <Space direction='vertical'>
            
            {histPic?(<>
              <Button onClick={handleCloseHist}>Close</Button>
              
              <img src={histPic} width="100%"/>
            </>):(<Button onClick={handleHist}>Histogram</Button>)}
          </Space>
        </Row>
        <Row>
          <Divider>Add salt and pepper noise</Divider>
          <Space>
            <InputNumber addonBefore='Probability' min={0} max={1} onChange={e=>setProbSP(e)} />
            <Button onClick={handleSP}>Ok</Button>
          </Space>
        </Row>
        <Row>
          <Divider>Add Gaussian Noise</Divider>
          <Space>
            <InputNumber addonBefore='Probability' min={0} max={1} onChange={e=>setProbGS(e)} />
            <Button onClick={handleGS}>Ok</Button>
          </Space>
        </Row>
        {/* addGaussianNoise */}
      </Card>
    </>
  )
}
export default PixelTrans;