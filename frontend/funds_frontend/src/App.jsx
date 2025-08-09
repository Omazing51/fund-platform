import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import icono from './assets/menu_icon.png'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className='bg-gray-100 h-screen'>
        {/*SIDEBAR*/}

        
        <main>
          <header className='bg-white flex justify-between p-4'>
            <button className='p-2 text-xl font-bold lg:hidden'>
            <img src={icono} alt="Icono" className="w-5 h-5" />
            </button>
            <h1 className='text-2xl font-bold'>Dashboard</h1>
            <div className='bg-gray-300 w-10 h-10 rounded-full'></div>
          </header>
        </main>
      </div>
    </>
  )
}

export default App
