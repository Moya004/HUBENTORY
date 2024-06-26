import NavBar from "../Components/navBar";
import DataTable from '../Components/tableProducts';
import Modal from '../Components/add';
import Removal from '../Components/removal';
import logo from '../assets/logo.png';
import img_left from '../assets/left.png';
import img_right from '../assets/right.png';
import btn_alerts from '../assets/alerts.png';
import { useNavigate } from 'react-router-dom';
import {useState} from 'react';
import './stylesproducts.css';
import '../Components/styleHeaded.css';

export default function Products() {
    const navigate = useNavigate();
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [isRemovalOpen, setIsRemovalOpen] = useState(false);

    const handlePreviousClick = () => {
        navigate(-1); // Navegar a la vista anterior
    };

    const handleNextClick = () => {
        navigate(1); // Navegar a la vista siguiente
    };

    const handleModalToggle = () => {
        setIsModalOpen(!isModalOpen);
    };

    const handleRemovalToggle = () => {
        setIsRemovalOpen(!isRemovalOpen);
    };

    const handleCustomPathClick = () => {
        navigate('/notification'); 
    };

    return (
        <div className="container">
            <NavBar>
                <img className="logo-hub" src={logo} alt="Logo" />
            </NavBar>
            <div>
                <div className="content">
                    <div className="header">
                        <button className='btn-previous' onClick={handlePreviousClick}>
                            <img src={img_left} alt="Previous" />
                        </button>
                        <button className='btn-next' onClick={handleNextClick}>
                            <img src={img_right} alt="Next" />
                        </button>
                        <button className='btn-alerts' onClick={handleCustomPathClick}>
                            <img src={btn_alerts}   alt="Alerts"  />
                        </button>
                    </div>
                    <div className="headed_aux">
                        <h1>Productos</h1>
                        <button className='btn_add' onClick={handleModalToggle}>Agregar</button>
                       
                    </div>
                    <div className="headed_aux2">
                        <button className='btn_eliminar' onClick={handleRemovalToggle}>Retirar</button>
                        <p>Todos los productos registrados actualmente en el inventario</p>
                    </div>

                </div>
                <DataTable />
            </div>
            <Modal isOpen={isModalOpen} onClose={handleModalToggle}>
                <h2>Selecciona</h2>
            </Modal>

            <Removal isOpen={isRemovalOpen} onClose={handleRemovalToggle}>
                <h2>Retirar productos</h2>
            </Removal>
        </div>
    );
}
