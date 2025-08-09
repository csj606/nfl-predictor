import { useState } from 'react'
import './App.css'
import { Link } from 'react-router-dom'
import { team_names } from './constants'
import 

function gameDisplay(homeTeamName: String, homeTeamRecord: String, awayTeamName: String, awayTeamRecord: String){
  const homePath = `/team/${homeTeamName}`
  const awayPath = `/team/${homeTeamName}`
  return (
    <div className='weekly-game'>
      <div className='home-team-info'>
        <Link to={homePath} >{homeTeamName}</Link>
        <p>{homeTeamRecord}</p>
      </div>
      <p className='versus'>Versus</p>
      <div className='away-team-info'>
        <Link to={awayPath} >{awayTeamName}</Link>
        <p>{awayTeamRecord}</p>
      </div>
    </div>
  )
}
import { getGames } from './relay_home'


function App() {
  const [teams, setTeams] = useState(team_names)
  const [games, setGames] = useState([])

  useEffect(() => {
    async function grabGames(){
      const thisWeeksGames = getGames()
      setGames(thisWeeksGames)
    }
    grabGames()
  })

  return (
    <>
      {teams.map(team => {
        gameDisplay()
      })}
    </>
  )
}

export default App
