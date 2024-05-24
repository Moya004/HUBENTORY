import React from 'react';
import { Link } from 'react-router-dom';
import '../layout/stylesNavBar.css'
interface NavBarProps {
    children: React.ReactNode;
}

const NavBar: React.FC<NavBarProps> = ({ children }) => {
    return (
        <div className='navbar'>
            <header>
                <nav>
                    <ul>
                        <li>
                            <Link to="/Products">Productos</Link>
                        </li>
                        <li>
                            <Link to="/Reports">Informes</Link>
                        </li>
                    </ul>
                </nav>
            </header>
            <main>{children}</main>
        </div>
    );
};

export default NavBar;
