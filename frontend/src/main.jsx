import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import Footer from './Components/Footer/Footer.jsx'
import NavBar from './Components/NavBar/NavBar.jsx'
import Plot   from './Components/PlotComponent/Plot.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <NavBar/>
    <Plot/>
    <App />
    <Footer/>
  </React.StrictMode>,
)
