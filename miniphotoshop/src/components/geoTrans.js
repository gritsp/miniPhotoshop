import { Button, Card, InputNumber, Row, Col,Space, Divider } from 'antd';
import axios from 'axios';
import React, { useState } from 'react';
import { RedoOutlined,UndoOutlined } from '@ant-design/icons';

const GeoTrans = ({image}) => {
  const [width,setWidth] = useState(0)
  const [hight,setHight] = useState(0)
  const [xw,setXWidth] = useState(0)
  const [yh,setYHight] = useState(0)
  const [xStart,setX] = useState(0)
  const [yStart,setY] = useState(0)
  const [degree,setFlibDegree] = useState(0)
  const post = (value,fn)=>{
    axios.post(`http://127.0.0.1:5000/${fn}`,value)
    .then(doc=>{
      if(doc.data.data){
        image("data:image/jpg;base64,"+doc.data.data)
      }
      console.log(doc)
    })
  }
  const handleWH = async () =>{
    let data = {
      width,hight
    }
    await post(data,'resize')
  }

  const handleCW = async () =>{
    let data = {
      rotate:"cw"
    }
    await post(data,'rotate')
  }

  const handleCCW = async () =>{
    let data = {
      rotate:'ccw'
    }
    await post(data,'rotate')
  }

  const handleDegree = async () =>{
    let data = {
      rotate:degree
    }
    await post(data,'rotate')
  }
  const handleVer = async () =>{
    let data = {
      flip:0
    }
    await post(data,'flip')
  }
  const handleHor = async () =>{
    let data = {
      flip:0
    }
    await post(data,'flip')
  }

  const handleCrop = async () =>{
    let data = {
      x:xStart,
      y:yStart,
      w:xw,
      h:yh
    }
    await post(data,'crop')
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
          <Divider>Resize</Divider>
          <Space>
            <InputNumber addonBefore='width' addonAfter="%" min={0} onChange={e=>setWidth(e)} />
            <InputNumber addonBefore='hight' addonAfter="%" min={0} onChange={e=>setHight(e)} />
            <Button onClick={handleWH}>Ok</Button>
          </Space>
        </Row>
        <Row>
          <Divider>Rotate</Divider>
          <Space>
            <Button onClick={handleCW}><RedoOutlined /></Button>
            <Button onClick={handleCCW}><UndoOutlined /></Button>
            <InputNumber addonBefore='degree' min={0} onChange={e=>setFlibDegree(e)} />
            <Button onClick={handleDegree}>Ok</Button>
          </Space>
        </Row>
        <Row>
          <Divider>Flip</Divider>
          <Space>
            <Button onClick={handleVer}>Vertical</Button>
            <Button onClick={handleHor}>Horizontal</Button>
          </Space>
        </Row>
        <Row>
          <Divider>Crop</Divider>
          <Space>
            <Col>
              <InputNumber addonBefore='x-start' min={0} onChange={e=>setX(e)} />
              <InputNumber addonBefore='y-start' min={0} onChange={e=>setY(e)} />
            </Col>
            <Col>
              <InputNumber addonBefore='width' min={0} onChange={e=>setXWidth(e)} />
              <InputNumber addonBefore='hight' min={0} onChange={e=>setYHight(e)} />
            </Col>
            <Button onClick={handleCrop}>Ok</Button>
          </Space>
        </Row>
      </Card>
    </>
  )
}

export default GeoTrans;