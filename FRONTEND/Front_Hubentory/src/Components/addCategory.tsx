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
            <div className="Category-content">
                <button className="Category-close" onClick={onClose}>
                    <img src={close} alt="Close" />
                </button>
                {children}
                <form className="category-form">
                    <input className="id_cat" type="text" id="id_category" placeholder="   ID Categoria"/>
                </form>
                <div className='container-btnadd'>
                    <button className='btnCancel_C' onClick={onClose}>Cancelar</button>
                    <button className='btnadd_C'>Generar</button>
                </div>
            </div>
        </div>
    );
};

export default AddCategory;
