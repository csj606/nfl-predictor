import dotenv from "dotenv"
import { team_names } from "./constants"
dotenv.config()

/**
 * Gets the current week's game schedule
 * 
 * @returns {JSON} An object containing a Game object
 */
async function getGames(){
    const currentTime = new Date
    const day = currentTime.getDay()
    const month = currentTime.getMonth()
    const year = currentTime.getFullYear()

    await fetch(`https://${import.meta.env.VITE_BACKEND_URL}/games?year=${year}month=${month}day=${day}`)
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
async function getTeamRecord(name: string): Promise<string>{
    if(verifyName(name)){
        fetch(`https://${import.meta.env.VITE_BACKEND_URL}/records?name=${name}`)
        .then(result => {
            if(!result.ok){
                throw Error
            }else{
                var j: JSON = result.json() as JSON
                return j.teamName
            }
        })
    }else{
        return "Error"
    }
}
/**
 * Gets the photo fo the team logo
 * @param name Name of the team, must match internal records
 * @returns {string} Path of logo for website to display
 */
async function getLogoPath(name: string): Promise<string>{
    if(verifyName(name)){
        fetch(`https://${import.meta.env.VITE_BACKEND_URL}/logo?name=${name}`)
        .then(result => {
            if(!result.ok){
                throw Error
            }else{
                var j: JSON = result.json() as JSON
                return j.logo
            }
        })
    }else{
        return "Error"
    }
}

/**
 * Gets the link for a team
 * @param name Name of the team, must match internal records
 * @returns {string} Path that team page must follow
 */
async function getLinkPath(name: string){
    return "TODO"
}

/**
 * Gets the prediction of the game point differential from the backend
 */
async function getPrediction(team1: string, team2: string): Promise<Number>{
    if(verifyName(team1) && verifyName(team2)){
        fetch(`https://${import.meta.env.VITE_BACKEND_URL}/predit?team=${team1}opponent=${team2}`)
        .then(result => {
            if(!result.ok){
                throw Error
            }else{
                var j: JSON = result.json() as JSON
                return j.predict
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
async function getStanding(name: string): Promise<string>{
    if(verifyName(name)){
        fetch(`https://${import.meta.env.VITE_BACKEND_URL}/predit?team=${team}`)
        .then(result => {
            if(!result.ok){
                throw Error
            }else{
                var j: JSON = result.json() as JSON
                return j.standing
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