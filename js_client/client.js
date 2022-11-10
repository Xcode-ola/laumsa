const loginform = document.getElementById('login_form')
const baseEndpoint = "https://localhost:8000/"

if (loginform) {
    loginform.addEventListener('submit', handleLogin)
}

function handleLogin(event) {
    console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/user/token/`
    const options = {
        method:"POST",
        header:{
            "Content":"application/json"
        },
        body:"",
    }
    fetch(loginEndpoint, options)
}
