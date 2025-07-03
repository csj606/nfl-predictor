import dotenv from 'dotenv'

function NavBar(){

    dotenv.config()

    const back = import.meta.env.VITE_BACKEND_URL
    const homeUrl = `${back}`
    const teamUrl = `${back}/teams`
    const rankingsUrl = `${back}/rankings`
    const challengesURL = `${back}/challenges`
    const leagueURL = `${back}`
    const login = `${back}/accounts/login`

    return (
        <div id="navbar">
            <a href={homeUrl}/>
            <a href={teamUrl}/>
            <a href={rankingsUrl}/>
            <a href={challengesURL}/>
            <a href={leagueURL}/>
            <a href={login}/>
        </div>
    )
}