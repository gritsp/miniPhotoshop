import { Button, Card, InputNumber, Row, Col,Space, Divider } from 'antd';
import axios from 'axios';
import React, { useEffect, useState } from 'react';

const Filtering = ({image}) => {
  const [kBF,setKBF] = useState(0)
  const [kGF,setKGF] = useState(0)
  const [kMF,setKMF] = useState(0)
  const [sigma,setSigma] = useState(0)
  const [sharpen,setSharpen] = useState(0)

  const post = (value,fn)=>{
    axios.post(`http://127.0.0.1:5000/${fn}`,value)
    .then(doc=>{
      if(doc.data.data){
        image("data:image/jpg;base64,"+doc.data.data)
      }
      console.log(doc)
    })
  }

  const handleBF = async () =>{
    let data = {
      k:kBF
    }
    await post(data,'blurBox')
  }
  const handleGF = async () =>{
    let data = {
      k:kGF
    }
    await post(data,'blurGaussian')
  }
  const handleMF = async () =>{
    let data = {
      k:kMF
    }
    await post(data,'blurMedian')
  }
  const handleSharpen = async () =>{
    let data = {
      k:sharpen
    }
    await post(data,'sharpen')
  }
  const handleEdgeDetect = async () =>{
    let data = {
      sigma
    }
    console.log(data)
    await post(data,'edgeDetect')
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
          <Divider>Blur an image with Box filter</Divider>
          <Space>
            <InputNumber addonBefore='K' min={0} onChange={e=>setKBF(e)} />
            <Button onClick={handleBF}>Ok</Button>
          </Space>
        </Row>
        <Row>
          <Divider>Blur an image with Gaussian filter</Divider>
          <Space>
            <InputNumber addonBefore='K' min={0} onChange={e=>setKGF(e)} />
            <Button onClick={handleGF}>Ok</Button>
          </Space>
        </Row>
        <Row>
          <Divider>Blur an image with Median filter</Divider>
          <Space>
            <InputNumber addonBefore='K' min={0} onChange={e=>setKMF(e)} />
            <Button onClick={handleMF}>Ok</Button>
          </Space>
        </Row>
        <Row>
          <Divider>Sharpen</Divider>
          <Space>
            <InputNumber addonBefore='K' min={0} onChange={e=>setSharpen(e)} />
            <Button onClick={handleSharpen}>Ok</Button>
          </Space>
        </Row>
        <Row>
          <Divider>Edge detect</Divider>
          <Space>
            <InputNumber addonBefore='Sigma' min={0} max={1} onChange={e=>setSigma(e)} />
            <Button onClick={handleEdgeDetect}>Ok</Button>
          </Space>
        </Row>
      </Card>
    </>
  )
}
export default Filtering;