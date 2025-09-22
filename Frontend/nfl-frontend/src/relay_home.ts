import dotenv from "dotenv"
dotenv.config()

/**
 * Gets the current week's game schedule
 * 
 * @returns {JSON} An object containing a Game object
 */
export async function getGames(){
    await fetch(`https://${import.meta.env.VITE_BACKEND_URL}/games`)
    .then(result => {
        if(!result.ok){
            throw Error
        }else{
            return result.body
        }
    })
}

/**
 * Gets the prediction of the game point differential from the backend
 */
async function getPrediction(team1: string, team2: string){
    fetch(`https://${import.meta.env.VITE_BACKEND_URL}/predict?team=${team1}opponent=${team2}`)
        .then( async result => {
            if(!result.ok){
                throw Error
            }else{
                var j = await result.json()
                return j["predict"]
            }
    })
}