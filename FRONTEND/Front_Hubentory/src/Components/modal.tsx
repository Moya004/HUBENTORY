import React from 'react';
import close from '../assets/close.png';
import '../Components/stylesmodal.css';

interface ModalProps {
    isOpen: boolean;
    onClose: () => void;
    children: React.ReactNode;
}

const Modal: React.FC<ModalProps> = ({ isOpen, onClose, children }) => {
    if (!isOpen) return null;

    return (
        <div className="modal-overlay">
            <div className="modal-content">
                <button className="modal-close" onClick={onClose}>
                    <img src={close} alt="Close" />
                </button>
                {children}
            </div>
        </div>
    );
};

export default Modal;
