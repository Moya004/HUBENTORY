import React, { useState } from 'react';
import close from '../assets/close.png';
import AddProduct from '../Components/addProducts';
import AddCategory from '../Components/addCategory';
import '../Components/stylesadd.css';

interface ModalProps {
    isOpen: boolean;
    onClose: () => void;
    children: React.ReactNode;
}

const Modal: React.FC<ModalProps> = ({ isOpen, onClose, children }) => {
    const [isAddProductOpen, setIsAddProductOpen] = useState(false);
    const [isAddCategoryOpen, setIsAddCategoryOpen] = useState(false);

    const handleProductsToggle = () => {
        setIsAddProductOpen(true);
    };

    const handleCategoryToggle = () => {
        setIsAddCategoryOpen(true);
    };

    const handleAddProductClose = () => {
        setIsAddProductOpen(false);
    };

    const handleAddCategoryClose = () => {
        setIsAddCategoryOpen(false);
    };

    if (!isOpen) return null;

    return (
        <>
            <div className="modal-overlay">
                <div className="modal-content">
                    <button className="modal-close" onClick={onClose}>
                        <img src={close} alt="Close" />
                    </button>
                    {children}
                    <div className='container-btnOp'>
                        <button className='btn-prod' onClick={handleProductsToggle}>Productos</button>
                        <button className='btn-Categoria' onClick={handleCategoryToggle}>Categoria</button>
                    </div>
                    <div className='container-btnadd'>
                        <button className='btnCancel' onClick={onClose}>Cancelar</button>
                    </div>
                </div>
            </div>
            {isAddProductOpen && (
                <AddProduct isOpen={isAddProductOpen} onClose={handleAddProductClose}>
                    <h2>Agregar producto</h2>
                </AddProduct>
            )}
            {isAddCategoryOpen && (
                <AddCategory isOpen={isAddCategoryOpen} onClose={handleAddCategoryClose}>
                    <h2>Agregar Categoría</h2>
                </AddCategory>
            )}
        </>
    );
};

export default Modal;
