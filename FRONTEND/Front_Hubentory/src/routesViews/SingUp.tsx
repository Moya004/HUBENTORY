import './singUp.css'; 
import React from 'react';
const singUp:React.FC = () =>{
    return(
        <div>
            <form className="singup-form">
                <h1>Sing Up</h1>
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

            </form>
        </div>
    );
}

export default singUp;