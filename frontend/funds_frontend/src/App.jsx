import { useState } from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import icono from './assets/menu_icon.png';

import SubscriptionContainer from './features/containers/SubscriptionContainer';
import FundsContainer from './features/containers/FundsContainer'; 
import TransactionsContainer from './features/containers/TransactionsContainer';
import { useBalance } from "./features/hooks/useBalance";
import BalanceDisplay from "./features/components/BalanceDisplay";

function App() {
  const [sidebarOpen, setSideBarOpen] = useState(false);
  const { balance, loading, error } = useBalance();

  const navItems = [
    { name: "Dashboard", icon: "🏠", path: "/" },
    { name: "Funds", icon: "💰", path: "/funds" },
    { name: "Transactions", icon: "💳", path: "/transactions" },
  ];

  return (
    <div className='flex bg-gray-100 h-screen'>
    
      <div className={`fixed bg-white w-64 h-screen shadow ${sidebarOpen ? "translate-x-0" : "-translate-x-64"} lg:translate-x-0 lg:static`}>
        <div className='p-4 flex justify-between'>
          <div className='text-xl font-bold'>Funds-Platform</div>
          <button className='lg:hidden' onClick={() => setSideBarOpen(false)}>X</button>
        </div>
        <div className='p-4 space-y-2'>
          {navItems.map(item => (
            <Link
              key={item.name}
              to={item.path}
              className='flex p-2 hover:bg-gray-100 rounded'
              onClick={() => setSideBarOpen(false)}
            >
              <div className='text-xl mr-2'>{item.icon}</div>
              <div className='text-xl'>{item.name}</div>
            </Link>
          ))}
        </div>
      </div>

      <main className='flex-1'>
        <header className='bg-white flex justify-between p-4'>
          <button
            className='p-2 text-xl font-bold lg:hidden'
            onClick={() => setSideBarOpen(true)}
          >
            <img src={icono} alt="Icono" className="w-5 h-5" />
          </button>
          <h1 className='text-2xl font-bold'>Dashboard</h1>
          <BalanceDisplay balance={balance} loading={loading} error={error} />
          <div className='bg-gray-300 w-10 h-10 rounded-full'></div>
        </header>

        <div className='grid grid-cols-1 md:grid-cols-1 lg:grid-cols-1 p-4 gap-4'>
          <Routes>
            <Route path="/" element={<SubscriptionContainer />} />
            <Route path="/funds" element={<FundsContainer />} />
             <Route path="/transactions" element={<TransactionsContainer />} />
          </Routes>
        </div>
      </main>
    </div>
  );
}

export default App;
