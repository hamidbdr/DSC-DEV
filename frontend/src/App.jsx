import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Footer from './Components/Footer/Footer.jsx'
import NavBar from './Components/NavBar/NavBar.jsx'
import Plot   from './Components/PlotComponent/Plot.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <NavBar/>
    <Plot/>
    <Footer/>
    </>
  )
}

export default App
