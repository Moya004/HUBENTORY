import NavBar from "../Components/navBar";
import logo from '../assets/logo.png';
import './stylesReports.css';

export default function  Reports(){
    return (
        <>
            <NavBar>
                <img className="logo-hub" src={logo}></img>
            </NavBar>
        </>

    );
}