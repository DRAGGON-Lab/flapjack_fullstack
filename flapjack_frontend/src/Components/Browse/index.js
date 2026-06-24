import React from 'react'
import { Tabs, BackTop } from 'antd'
import Studies from './Studies'
import Assays from './Assays'
import Plasmids from './Plasmids'
import Medias from './Medias'
import Strains from './Chassis'
import Signals from './Signals'

const Browse = () => {
  return (
    <>
      <BackTop />
      <Tabs defaultActiveKey="1">
        <Tabs.TabPane tab="Studies" key="1">
          <Studies />
        </Tabs.TabPane>
        <Tabs.TabPane tab="Assays" key="2">
          <Assays />
        </Tabs.TabPane>
        <Tabs.TabPane tab="Plasmids" key="3">
          <Plasmids />
        </Tabs.TabPane>
        <Tabs.TabPane tab="Medias" key="4">
          <Medias />
        </Tabs.TabPane>
        <Tabs.TabPane tab="Chassis" key="5">
          <Chassis />
        </Tabs.TabPane>
        <Tabs.TabPane tab="Signals" key="6">
          <Signals />
        </Tabs.TabPane>
      </Tabs>
    </>
  )
}

Browse.propTypes = {}

export default Browse
