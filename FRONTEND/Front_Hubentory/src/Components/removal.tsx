import React from 'react';
import close from '../assets/close.png';
import '../Components/styleremoval.css';

interface removalProps {
    isOpen: boolean;
    onClose: () => void;
    children: React.ReactNode;
}

const removal: React.FC<removalProps> = ({ isOpen, onClose, children }) => {
    if (!isOpen) return null;

    return (
        <div className="Removal-overlay">
            <div className="Removal-content">
                <button className="Removal-close" onClick={onClose}>
                    <img src={close} alt="Close" />
                </button>
                {children}
                <p>¿Estás seguro de esta acción?</p>
                <div className='container-removal'>
                    <button className='btnCancel_Re' onClick={onClose}>No</button>
                    <button className='btnRemoval'>Si, retirar</button>
                </div>
            </div>
        </div>
    );
};

export default removal;
