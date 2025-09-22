import { useEffect, useState } from 'react'
import './App.css'
import { getGames } from './relay_home'

function gameDisplay(homeTeamName: String, awayTeamName: string){
  return (
    <div className='weekly-game'>
      <div className='home-team-info'>
        <p>{homeTeamName}</p>
      </div>
      <p className='versus'>Versus</p>
      <div className='away-team-info'>
        <p>{awayTeamName}</p>
      </div>
      <p></p>
    </div>
  )
}



function App() {
  const [games, setGames] = useState([] as any[]);

  useEffect(() => {
    async function grabGames(){
      const thisWeeksGames = await getGames()
      var games= (thisWeeksGames.get("games") as unknown as any[]) ?? []
      setGames(games)
    }
    grabGames()
  }, [])

  return (
    <>
      {games.map(game => {
        gameDisplay(game["team"], game["oppo_team"])
      })}
    </>
  )
}

export default App
