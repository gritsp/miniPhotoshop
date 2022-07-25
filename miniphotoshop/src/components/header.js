import { Button, Descriptions, PageHeader, Statistic, Tabs } from 'antd';
import React from 'react';
import GeoTrans from './geoTrans';
import PixelTrans from './pixelTrans';
import Filtering from './filter';
import ImgArithmetic from './imgArithmetic';
import ColorManipulation from './colorManipulation';
import Information from './information';
const { TabPane } = Tabs;


const HeaderTool = ({image}) => {
  const handleImg = (value)=>{
    image(value)
  }
  return(
  <PageHeader
    title="Tools"
    // subTitle="This is a subtitle"
    footer={
      <Tabs defaultActiveKey="1">
        <TabPane tab="Geometric Transformation" key="1" ><GeoTrans image={handleImg}/></TabPane>
        <TabPane tab="Pixel Transformation" key="2" ><PixelTrans image={handleImg}/></TabPane>
        <TabPane tab="Filtering" key="3" ><Filtering image={handleImg}/></TabPane>
        <TabPane tab="Image Arithmetic" key="4" ><ImgArithmetic image={handleImg}/></TabPane>
        <TabPane tab="Color Manipulation" key="5" ><ColorManipulation image={handleImg}/></TabPane>
        <TabPane tab="Information" key="6" ><Information image={handleImg}/></TabPane>
      </Tabs>
    }
  >
  </PageHeader>
)};

export default HeaderTool;