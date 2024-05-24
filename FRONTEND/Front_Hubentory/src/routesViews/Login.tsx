import './Login.css'; 
import React from 'react';

const Login:React.FC = () => {
    return (
        <div>
            <form className="login-form">
                <h1>Login</h1>
                <label htmlFor="id">id</label>
                <input type="text" id="id" />

                <label htmlFor="password">Password:</label>
                <input type="password" id="password" />

                <button type="submit">Iniciar sesion</button>

                <button type="submit" className='singup'>Registrarse</button>
            </form>
        </div>
    );    
}

// revisa no entinedo porque me genera errores honestamente
export default Login;