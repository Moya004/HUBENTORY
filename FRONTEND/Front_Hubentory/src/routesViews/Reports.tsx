import NavBar from "../Components/navBar";
import ReportsTable from '../Components/tableReports';
import Modal from '../Components/add';
import logo from '../assets/logo.png';
import img_left from '../assets/left.png';
import img_right from '../assets/right.png';
import btn_alerts from '../assets/alerts.png';
import { useNavigate } from 'react-router-dom';
import {useState} from 'react';
import './stylesproducts.css';
import '../Components/styleHeaded.css';

// es necesario que  aqui revis elos estilos
export default function Products() {
    const navigate = useNavigate();
    const [isModalOpen, setIsModalOpen] = useState(false);

    const handlePreviousClick = () => {
        navigate(-1); 
    };

    const handleNextClick = () => {
        navigate(1); 
    };

    const handleModalToggle = () => {
        setIsModalOpen(!isModalOpen);
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
                <div className="Reports-content">
                    <div className="Reports-header">
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
                    <div className="headedR_aux">
                        <h1>Informes</h1>
                        <button className='btn_add' onClick={handleModalToggle}>Agregar</button>
                    </div>
                    <p>Historial de informes generados en el inventario</p>
                </div>
                <ReportsTable />
            </div>
            <Modal isOpen={isModalOpen} onClose={handleModalToggle}>
                <h2>Selecciona</h2>
            </Modal>
        </div>
    );
}
