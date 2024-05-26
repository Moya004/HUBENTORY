import React, { useState } from 'react';
import close from '../assets/close.png';
import '../Components/styleaddProducts.css';

interface AddProductProps {
    isOpen: boolean;
    onClose: () => void;
    children: React.ReactNode;
}

const AddProduct: React.FC<AddProductProps> = ({ isOpen, onClose, children }) => {
    if (!isOpen) return null;
    // Estado para la opción seleccionada en la lista desplegable
    const [selectedOption, setSelectedOption] = useState('');

    // Manejador de cambio para la lista desplegable
    const handleSelectChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
        setSelectedOption(event.target.value);
    };
    
    return (
        <div className="modal-overlay">
            <div className="modal-wrapper">
                <button className="product-close" onClick={onClose}>
                    <img src={close} alt="Close" />
                </button>
                {children}
                <p>Introduce los siguientes datos para agregar los productos al
inventario</p>
                <form className="form-wrapper">
                    <input className="name_pro" type="text" id="name" placeholder="Nombre" />
                    <input className="lote_pro" type="text" id="lote" placeholder="Lote" />
                    <input className="id_product" type="text" id="id_product" placeholder="ID" />
                     <select className="category" value={selectedOption} onChange={handleSelectChange}>
                        <option value="">Selecciona una categoría</option>
                        <option value="category1">Categoría 1</option>
                        <option value="category2">Categoría 2</option>
                        <option value="category3">Categoría 3</option>
                    </select>
                    <label htmlFor="stock_nom">Existencias</label>
                    <input className="stock" type="text" id="stock" placeholder="0" />
                    <label htmlFor="date_nom">Caducidad</label>
                    <input className="Date" type="text" id="Date" placeholder="00/00/0000" />
                </form>
                <div className='buttons-wrapper'>
                    <button className='btnCancel_p' onClick={onClose}>Cancelar</button>
                    <button className='btnadd_p'>Generar</button>
                </div>
            </div>
        </div>
    );
};

export default AddProduct;
