import { PageHeader, Col, Row, Image, Button, Space } from 'antd';
import React, { useState } from 'react';
import {UploadImage,HeaderTool} from './components'
import axios from 'axios';

const App = () => {
  const [img,setImg] = useState(null)
  const [showUpload,setShowUpload] = useState(true)
  const handleImg = (value) =>{
    if(value){
      setImg(value)
      setShowUpload(false)
    }
    console.log("value",value)
  }
  const handleCancle = ()=>{
    axios.get("http://127.0.0.1:5000/delete").then(data=>console.log(data.data))
    setImg(null)
    setShowUpload(true)
  }
  function debugBase64(base64URL){
    var win = window.open();
    win.document.write('<iframe src="' + base64URL  + '" frameborder="0" style="border:0; top:0px; left:0px; bottom:0px; right:0px; width:100%; height:100%;" allowfullscreen></iframe>');
}
  const handleSave = ()=>{
    debugBase64(img)
    // window.location = img
  }
  return(
    <div>
      <Row>
        <Col offset={2} span={20}>
          <PageHeader
            title="Mini Photoshop"
          />
          <Row>
          <Col span={14} style={{paddingLeft:10}}>
            {showUpload?(<UploadImage image={handleImg}/>):(
            <Space direction="vertical">
              <img src={img}/>
              <Button onClick={handleCancle}>Cancle</Button>
              <Button><a href={img} download="img.jpg">Save Image</a></Button>
            </Space>
            )}
            
          </Col>
          <Col span={10}>
            <HeaderTool image={handleImg}/>
          </Col>
          </Row>
        </Col>
      </Row>
    </div>
  );
}

export default App;