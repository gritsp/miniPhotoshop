import { Button, Card, InputNumber, Row, Col,Space, Divider } from 'antd';
import axios from 'axios';
import React, { useEffect, useState } from 'react';

const Information = ({image}) => {
  const [width,setWidth] = useState(null)
  const [hight,setHight] = useState(null)
  const [histPic,setHistPic] = useState(null)

  const handleHist = ()=>{
    axios.get(`http://127.0.0.1:5000/showHistogramRGB`)
    .then(doc=>{
      setHistPic("data:image/jpg;base64,"+doc.data.hist)
      setHight(doc.data.h)
      setWidth(doc.data.w)
    })
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
          <Space direction='vertical'>
            
            {histPic?(<>
              <Space>
                <InputNumber addonBefore="Width" disabled={true} defaultValue={width} />
              <InputNumber addonBefore="Hight" disabled={true} defaultValue={hight} />
                </Space>
              
              <img src={histPic} width="100%"/>
            </>):(<Button onClick={handleHist}>Show</Button>)}
          </Space>
        </Row>
        
      </Card>
    </>
  )
}
export default Information;