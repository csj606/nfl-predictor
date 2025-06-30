import { useState } from 'react'
import dotenv from 'dotenv'
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
    return <form>
        <label>First Name:</label>
        <input id="first_name" type="text"></input>
        <label>Last Name:</label>
        <input id="last_name" type="text"></input>
        <label htmlFor="email">Email:</label>
        <input id="email" type="email"></input>
        <label>Username:</label>
        <input></input>
        <label>Password:</label>
        <input></input>
        <label>Select your favorite team!</label>
        <select id="team_options">
            <option value=""></option>
        </select>
    </form>
}