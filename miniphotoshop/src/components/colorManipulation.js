import { Button, Card, InputNumber, Row, Col,Space, Divider } from 'antd';
import axios from 'axios';
import React, { useEffect, useState } from 'react';

const ColorManipulation = ({image}) => {
  const [red,setRed] = useState(0)
  const [green,setGreen] = useState(0)
  const [blue,setBlue] = useState(0)
  const [hue,setHue] = useState(0)
  const [sat,setSat] = useState(0)
  const [val,setValue] = useState(0)
  const post = (value,fn)=>{
    axios.post(`http://127.0.0.1:5000/${fn}`,value)
    .then(doc=>{
      if(doc.data.data){
        image("data:image/jpg;base64,"+doc.data.data)
      }
      console.log(doc)
    })
  }
  const handleWB = async () =>{
    await post({},'whiteBalance')
  }

  const handleRGB = async () =>{
    let data = {
      red,green,blue
    }
    await post(data,'addRGB')
  }
  const handleHSV = async () =>{
    let data = {
      hue,sat,val
    }
    await post(data,'addHSV')
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
            <Button onClick={handleWB}>White Balance</Button>
          </Space>
        </Row>
        <Row>
          <Divider>Adjust image colors with separate RGB</Divider>
          <Space>
            <InputNumber addonBefore='Red' min={-255} max={255} onChange={e=>setRed(e)} />
            <InputNumber addonBefore='Green' min={-255} max={255} onChange={e=>setGreen(e)} />
            <InputNumber addonBefore='Blue' min={-255} max={255} onChange={e=>setBlue(e)} />
            <Button onClick={handleRGB}>Ok</Button>
          </Space>
        </Row>
        <Row>
          <Divider>Adjust image colors with HSV</Divider>
          <Space>
            <InputNumber addonBefore='Hue' min={-255} max={255} onChange={e=>setHue(e)} />
            <InputNumber addonBefore='Sat' min={-255} max={255} onChange={e=>setSat(e)} />
            <InputNumber addonBefore='Value' min={-255} max={255} onChange={e=>setValue(e)} />
            <Button onClick={handleHSV}>Ok</Button>
          </Space>
        </Row>
      </Card>
    </>
  )
}
export default ColorManipulation;