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
        <div className="modal-overlay">
            <div className="modal-content">
                <button className="modal-close" onClick={onClose}>
                    <img src={close} alt="Close" />
                </button>
                {children}
                <form className="category-form">
                    <input className="id_cat" type="text" id="id_category" placeholder="   ID Categoria"/>
</form>
                <div className='container-btnadd'>
                    <button className='btnCancel' onClick={onClose}>Cancelar</button>
                    <button className='btnadd'>Retirar</button>
                </div>
            </div>
        </div>
    );
};

export default removal;
