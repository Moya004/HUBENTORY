import React from 'react';
import close from '../assets/close.png';
import '../Components/styleCategory.css';

interface AddCategoryProps {
    isOpen: boolean;
    onClose: () => void;
    children: React.ReactNode;
}

const AddCategory: React.FC<AddCategoryProps> = ({ isOpen, onClose, children }) => {
    if (!isOpen) return null;

    return (
        <div className="modal-overlay">
            <div className="modal-content">
                <button className="modal-close" onClick={onClose}>
                    <img src={close} alt="Close" />
                </button>
                {children}
                <div className='container-btnadd'>
                    <button className='btnCancel' onClick={onClose}>Cancelar</button>
                    <button className='btnadd'>Generar</button>
                </div>
            </div>
        </div>
    );
};

export default AddCategory;
