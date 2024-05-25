import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';
import ocultarNavBarImg from '../assets/hideNavbarImage.png';
import mostrarNavBarImg from '../assets/showNavbarImage.png';
import ocultarLinksImg from '../assets/hideLinks.png';
import mostrarLinksImg from '../assets/showlinks.png';
import closing from '../assets/closing.png';
import '../Components/stylesNavBar.css';

interface NavBarProps {
    children: React.ReactNode;
}

const NavBar: React.FC<NavBarProps> = ({ children }) => {
    const navigate = useNavigate();

    const [linksVisible, setLinksVisible] = useState(true);
    const [navbarVisible, setNavbarVisible] = useState(true);

    const toggleLinksVisibility = () => {
        setLinksVisible(!linksVisible);
    };

    const toggleNavbarVisibility = () => {
        setNavbarVisible(!navbarVisible);
    };

    const handleCustomPathClick = () => {
        navigate('/login'); // Navegar a una ruta específica aqui no se si le añades algo
    };

    return (
        <div className="navbar-container">
            {navbarVisible && (
                <div className={`navbar`}>
                    <button className='btnlinks' onClick={toggleLinksVisibility}>
                        <img src={linksVisible ? ocultarLinksImg : mostrarLinksImg} alt="Toggle Links" />
                    </button>
                    <button className='btnnavbar' onClick={toggleNavbarVisibility}>
                        <img src={navbarVisible ? ocultarNavBarImg : mostrarNavBarImg} alt="Toggle Navbar" />
                    </button>
                    
                    <button className='btnclosing'>
                        <img src={closing} onClick={handleCustomPathClick} alt="Cerrar sesión" />
                    </button>
                    <nav>
                        <ul className="links-list" style={{ display: linksVisible ? 'block' : 'none', padding: 0, margin: 0 }}>
                            <li className="products-link" style={{ marginBottom: '1rem' }}>
                                <Link to="/Products">Productos</Link>
                            </li>
                            <li className="reports-link" style={{ marginBottom: '1rem' }}>
                                <Link to="/Reports">Informes</Link>
                            </li>
                            {linksVisible && <div className='line'></div>}
                        </ul>
                    </nav>
                    <main>{children}</main>
                </div>
            )}
            {!navbarVisible && (
                <div className="navbar-placeholder">
                    <button className='btnnavbar2' onClick={toggleNavbarVisibility}>
                        <img src={navbarVisible ? ocultarNavBarImg : mostrarNavBarImg}  alt="Toggle Navbar" />
                    </button>
                </div>

            )}            
        </div>
    );
};

export default NavBar;
