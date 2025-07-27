import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function gameDisplay(homeTeamName: String, homeTeamRecord: String, awayTeamName: String, awayTeamRecord: String){
  //TODO
  return (
    <div className='weekly-game'>
      <img src="" className="teamLogo"/>
      <div className='home-team-info'>
        <a href="">{homeTeamName}</a>
        <p>{homeTeamRecord}</p>
      </div>
      <p className='versus'>Versus</p>
      <div className='away-team-info'>
        <a href="">{awayTeamName}</a>
        <p>{awayTeamRecord}</p>
      </div>
      <img src="" className="teamLogo"/>
    </div>
  )
}


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
