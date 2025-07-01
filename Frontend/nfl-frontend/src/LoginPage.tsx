import { useState } from 'react'
import dotenv from 'dotenv'
import {team_names} from './constants.tsx'
dotenv.config()
const backendURL = import.meta.env.VITE_BACKEND_URL

const [message, setMessage] = useState("")

function errorMessage(){
    return <p>{message}</p>
}

function loginForm(){
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const submission = async (e: any) => {
        e.preventDefault()
        await fetch(`${backendURL}/login`, {
            method: 'GET',
            body: JSON.stringify(
                {"username": username, "password": password}
            )
        }).then(
            (res) => {
                if (res.status === 400){
                    setMessage("Error while logging in")
                }else{
                    setMessage("Login Successful")
                }
            }
        )
    }

    return <form onSubmit={submission}>
        <label htmlFor="username_input">Username:</label>
        <input type="text" id="username_input" value={username} onChange={(e) => setUsername(e.target.value)}/>
        <label htmlFor='password'>Password:</label>
        <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)}/>
        <input type="submit" value="Login"/>
    </form>
}

function registerForm(){
    const [first_name, changeFirstName] = useState("")
    const [last_name, changeLastName] = useState("")
    const [email, changeEmail] = useState("")
    const [username, changeUsername] = useState("")
    const [password, changePassword] = useState("")
    const [favoriteTeam, changeFavoriteTeam] = useState("")

    const submission = async (e: any) => {
        e.preventDefault()
        await fetch(`${backendURL}/register`, {
            method: "POST",
            body: JSON.stringify({
                first_name: first_name,
                last_name: last_name,
                email: email,
                username: username,
                favoriteTeam: favoriteTeam
            })
        }).then(
            (res) => {
                if(res.status == 401){
                    setMessage("Error on user registration")
                }
            }
        ).catch(

        )
    }

    return <form onSubmit = {submission}>
        <label htmlFor='first_name'>First Name:</label>
        <input id="first_name" type="text" value={first_name} onChange={(e) => changeFirstName(e.target.value)}></input>
        <label htmlFor='last_name'>Last Name:</label>
        <input id="last_name" type="text" value={last_name} onChange={(e) => changeLastName(e.target.value)}></input>
        <label htmlFor="email">Email:</label>
        <input id="email" type="email" value={email} onChange={(e) => changeEmail(e.target.value)}></input>
        <label htmlFor='username'>Username:</label>
        <input id='username' value={username} onChange={(e) => changeUsername(e.target.value)}></input>
        <label htmlFor='password'>Password:</label>
        <input id ='password' value={password} onChange={(e) => changePassword(e.target.value)}></input>
        <label htmlFor='team_options'>Select your favorite team!</label>
        <select id="team_options" onChange={(e) => changeFavoriteTeam(e.target.value)}>
            {
                team_names.map((item: string) => (
                    <option key={item} value={item}></option>
                ))
            }
        </select>
    </form>
}