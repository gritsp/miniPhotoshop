import { UploadOutlined } from '@ant-design/icons';
import { Button, message, Upload } from 'antd';
import React, { useEffect, useState } from 'react';
import axios from 'axios';

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
    axios.post('http://127.0.0.1:5000/upload',{
      data:result
    }).then(doc=>{
      if(doc.data.data){
        image(doc.data.data)
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

export default UploadImage;