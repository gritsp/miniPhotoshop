import { UploadOutlined } from '@ant-design/icons';
import { Button, Card, InputNumber, Row, Col,Space, Divider, Upload } from 'antd';
import axios from 'axios';
import React, { useState } from 'react';

const convertBase64 = (file) => {
  return new Promise((resolve, reject) => {
    const fileReader = new FileReader();
    fileReader.readAsDataURL(file)
    fileReader.onload = () => {
      resolve(fileReader.result);
    }
    fileReader.onerror = (error) => {
      reject(error);
    }
  })
}


const UploadImage = ({image})=> {
  
  const handleChange = async (value)=>{
    let result = await convertBase64(value.file.originFileObj)
    // console.log("reader.result",result)
    axios.post('http://127.0.0.1:5000/subtract',{
      data:result
    }).then(doc=>{
      if(doc.data.data){
        image("data:image/jpg;base64,"+doc.data.data)
      }
      // console.log(doc)
    })
  }
  return (
    <>
      <Upload onChange={handleChange}>
        <Button icon={<UploadOutlined />}>Click to Upload</Button>
      </Upload>
    </>
  )
}

const ImgArithmetic = ({image}) => {
  const [alpha,setAlpha] = useState(0)
  const [img,setBlend] = useState(null)
  const post = (value,fn)=>{
    axios.post(`http://127.0.0.1:5000/${fn}`,value)
    .then(doc=>{
      if(doc.data.data){
        image("data:image/jpg;base64,"+doc.data.data)
      }
      console.log(doc)
    })
  }
  const handleSubtract = async (value) =>{
    image(value)
  }
  const handleImg = async (value)=>{
    let result = await convertBase64(value.file.originFileObj)
    setBlend(result)
  }
  const handleBlend =async ()=>{
    let data = {
      data:img,
      alpha
    }
    await post(data,'blend')
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
          <Divider>Add/Subtract 2 images</Divider>
          <Space>
            <UploadImage image={handleSubtract} />
          </Space>
        </Row>
        <Row>
          <Divider>Blend 2 images</Divider>
          <Space>
            <Upload onChange={handleImg}>
              <Button icon={<UploadOutlined />}>Click to Upload</Button>
            </Upload>
            <InputNumber addonBefore='transparency' min={0} onChange={e=>setAlpha(e)} />
            <Button onClick={handleBlend}>Ok</Button>
          </Space>
        </Row>
      </Card>
    </>
  )
}

export default ImgArithmetic;