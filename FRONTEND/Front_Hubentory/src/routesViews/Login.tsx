import './stylesLogin.css'; 
import React from 'react';
import { useNavigate } from 'react-router-dom';
import img_logo from '../assets/img_logo.png';
const Login:React.FC = () => {
    const navigate = useNavigate();

    const handleCustomPathClick = () => {
        navigate('/singUp'); 
    };


    return (
        
        <div className='containerlogin'>
            <div className='background-rectangle'></div>
            <form className="login-form">
                <img src={img_logo} />
                <h1>Login</h1>
                <label htmlFor="id">id</label>
                <input type="text" id="id" />

                <label htmlFor="password">Password:</label>
                <input type="password" id="password" />

                <button type="submit">Iniciar sesion</button>

                <button type="submit" className='singup' onClick={handleCustomPathClick}>Registrarse</button>
            </form>
        </div>
    );    
}

export default Login;