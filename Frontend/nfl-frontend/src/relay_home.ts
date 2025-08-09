import dotenv from "dotenv"
import { team_names } from "./constants"
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
 * Gets the team record 
 * @param name Name of the team, must match internal records
 * @returns {string} String containing the record of the specified team
 */
async function getTeamRecord(name: string){
    if(verifyName(name)){
        fetch(`https://${import.meta.env.VITE_BACKEND_URL}/records?name=${name}`)
        .then( async result => {
            if(!result.ok){
                throw Error
            }
            const data = await result.json()
            return data["record"]
        })
    }else{
        return "Error"
    }
}

/**
 * Gets the prediction of the game point differential from the backend
 */
async function getPrediction(team1: string, team2: string){
    if(verifyName(team1) && verifyName(team2)){
        fetch(`https://${import.meta.env.VITE_BACKEND_URL}/predict?team=${team1}opponent=${team2}`)
        .then( async result => {
            if(!result.ok){
                throw Error
            }else{
                var j = await result.json()
                return j["predict"]
            }
        })
    }else{
        return 0
    }
}

/**
 * Gets the team standing in the current season from the backend
 * @param name Name of the team, must match internal documentation
 * @returns {string} Formatted record
 */
async function getStanding(name: string){
    if(verifyName(name)){
        fetch(`https://${import.meta.env.VITE_BACKEND_URL}/standing?team=${name}`)
        .then(async result => {
            if(!result.ok){
                throw Error
            }else{
                var j = await result.json()
                return j["standing"]
            }
        })
    }else{
        return "Error"
    }
}

function verifyName(name: string): boolean{
    if(name in team_names){
        return true
    }else{
        return false
    }
}