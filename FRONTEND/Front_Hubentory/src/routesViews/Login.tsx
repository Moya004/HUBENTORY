import './Login.css'; 

export default function login(){
    return (
        <div>
            <form className="login-form">
                <h1>Login</h1>
                <label htmlFor="id">id</label>
                <input type="text" id="id" />

                <label htmlFor="password">Password:</label>
                <input type="password" id="password" />

                <button type="submit">login</button>
            </form>
        </div>
    );
}