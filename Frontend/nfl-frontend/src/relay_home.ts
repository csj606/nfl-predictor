import dotenv from "dotenv"
dotenv.config()

/**
 * Gets the current week's game schedule
 * 
 * @returns {JSON} An object containing a Game object
 */
export async function getGames(): Promise<Map<string, string>>{
    var r = ""
    await fetch(`https://${import.meta.env.VITE_BACKEND_URL}/games`)
    .then(result => {
        if(!result.ok){
            throw Error
        }else{
            r = JSON.stringify(result)
            return result.body
        }
    })
    .catch(result => {
        return result
    })
    return JSON.parse(r)
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