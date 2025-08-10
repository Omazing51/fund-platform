import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import icono from './assets/menu_icon.png'

function App() {
  const [sidebarOpen, setSideBarOpen] = useState(false)
  const navItems = [
  { name: "Dashboard", icon: "🏠" },       // Vista general
  { name: "Funds", icon: "💰" },           // Dinero / inversiones
  { name: "Transactions", icon: "💳" },    // Movimientos
  { name: "Settings", icon: "⚙️" },    // Ajustes
]
  return (
    <>
      <div className='flex bg-gray-100 h-screen'>
        <div className= {`fixed bg-white w-64 h-screen shadow ${sidebarOpen?"translate-x-0" : "-translate-x-64"} lg:translate-x-0 lg:static`}>
           <div className='p-4 flex justify-between'>
            <div className='text-xl font-bold'>Funds-Platform</div>
            <button className='lg:hidden' onClick={() => setSideBarOpen(false)}>X</button>
           </div>
           <div className='p-4 space-y-2'>
            {navItems.map(item => {
              return (
                <div className='flex p-2'>
                  <div className='text-xl'>{item.icon}</div>
                  <div className='text-xl'>{item.name}</div>
                </div>
              )
            })}
           </div>
        </div>
        <main className='flex-1'>
          <header className='bg-white flex justify-between p-4'>
            <button className='p-2 text-xl font-bold lg:hidden'
            onClick={() => setSideBarOpen(true)}
            >
            <img src={icono} alt="Icono" className="w-5 h-5" />
            </button>
            <h1 className='text-2xl font-bold'>Dashboard</h1>
            <div className='bg-gray-300 w-10 h-10 rounded-full'></div>
          </header>
          <div>
            
          </div>
        </main>
      </div>
    </>
  )
}

export default App
