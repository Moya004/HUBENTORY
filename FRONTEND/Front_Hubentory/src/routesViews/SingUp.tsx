import './singUp.css'; 
import React from 'react';
import { useNavigate } from 'react-router-dom';
import img_logo from '../assets/img_logo.png';
const singUp:React.FC = () =>{
    const navigate = useNavigate();

    const handleCustomPathClick = () => {
        navigate('/'); 
    };

    return(
        <div className='background-rectangle'>
            <form className="singup-form">
                <img src={img_logo} />
                <h2>Sing Up</h2>
                <label htmlFor="id">Id:</label>
                <input type="text" id="id" />

                <label htmlFor="name">Nombre Completo:</label>
                <input type="text" id="name" />

                <label htmlFor="password">Contraseña:</label>
                <input type="password" id="password" />

                <label htmlFor="verify_password">Confirmar Contraseña:</label>
                <input type="password" id="verify_password" />

                <label htmlFor="id_inv">Id de inventario:</label>
                <input type="text" id="id" />

                <label htmlFor="name_inv">Nombre de inventario:</label>
                <input type="text" id="name" />

                <button type="submit">Registrarte</button>

                <button type="submit" className='login' onClick={handleCustomPathClick}>inicia sesion</button>

            </form>
        </div>
    );
}

export default singUp;