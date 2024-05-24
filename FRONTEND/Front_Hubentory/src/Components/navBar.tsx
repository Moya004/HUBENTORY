import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import ocultarNavBarImg from '../assets/hideNavbarImage.png';
import mostrarNavBarImg from '../assets/hideNavbarImage.png';
import ocultarLinksImg from '../assets/hideLinks.png';
import mostrarLinksImg from '../assets/showlinks.png';
import '../Components/stylesNavBar.css';

interface NavBarProps {
    children: React.ReactNode;
}

const NavBar: React.FC<NavBarProps> = ({ children }) => {
    const [linksVisible, setLinksVisible] = useState(true);
    const [navbarVisible, setNavbarVisible] = useState(true);

    const toggleLinksVisibility = () => {
        setLinksVisible(!linksVisible);
    };

    const toggleNavbarVisibility = () => {
        setNavbarVisible(!navbarVisible);
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
                    <nav>
                        <ul className="links-list" style={{ display: linksVisible ? 'block' : 'none', padding: 0, margin: 0 }}>
                            <li className="products-link" style={{ marginBottom: '1rem' }}>
                                <Link to="/Products">Productos</Link>
                            </li>
                            <li className="reports-link" style={{ marginBottom: '1rem' }}>
                                <Link to="/Reports">Informes</Link>
                            </li>
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
