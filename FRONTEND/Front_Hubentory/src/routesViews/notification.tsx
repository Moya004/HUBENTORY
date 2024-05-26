import NavBar from "../Components/navBar";
import DataTable from '../Components/tableProducts';
import Modal from '../Components/add';
import logo from '../assets/logo.png';
import img_left from '../assets/left.png';
import img_right from '../assets/right.png';
import btn_alerts from '../assets/alerts.png';
import { useNavigate } from 'react-router-dom';
import {useState} from 'react';

const Notification = () => {
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
                        <h1>Notificaciones</h1>
                        <button className='btn_add' onClick={handleModalToggle}>Agregar</button>
                    </div>
                    <p>Todas las notificaciones recibidas hasta el momento</p>
                </div>
            </div>
            <Modal isOpen={isModalOpen} onClose={handleModalToggle}>
                <h2>Selecciona</h2>
            </Modal>
        </div>
    );    
}

export default Notification;