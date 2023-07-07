import { useState } from 'react'
import './App.css'
import { Routes, Route} from 'react-router-dom';
import {Home} from './components/Home'
import {Create} from './components/Create'
import {Existing} from './components/Existingform'
import {Entry} from './components/Entry'
import {Entry2} from './components/Entry2'
import {View} from './components/View'
import {View2} from './components/View2'



function App() {

  return (
    <div>
    <Routes>
      <Route path='/' element={<Home />}></Route>

      <Route path='existing' element={<Existing />} />


      <Route path='existing/entry/:tableName' element={<Entry />} />
      <Route path='existing/entry2/:tableName' element={<Entry2 />} />
      <Route path='existing/view/:tableName' element={<View />} />
      <Route path='existing/view2/:formName' element={<View2 />} />
      <Route path='create' element={<Create />}></Route>
      
    </Routes>
    </div>

  )
}

export default App
