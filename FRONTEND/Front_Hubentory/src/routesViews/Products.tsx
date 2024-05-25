import NavBar from "../Components/navBar";
import DataTable from '../Components/tableProducts';
import logo from '../assets/logo.png';
import img_left from '../assets/left.png';
import img_right from '../assets/right.png';
import btn_alerts from '../assets/alerts.png';
import { useNavigate } from 'react-router-dom';
import './stylesproducts.css';
import '../Components/styleHeaded.css';


// export default function Products() {
//     return (
//         <div className="container">
//             <NavBar>
//                 <img className="logo-hub" src={logo}></img>
//             </NavBar>
//             <div>
//                 <div className="content">
//                     <h1>Productos</h1>
//                 </div>
//                 <DataTable />
//             </div>
//         </div>
//     );
// }

export default function Products() {
    const navigate = useNavigate();

    const handlePreviousClick = () => {
        navigate(-1); // Navegar a la vista anterior
    };

    const handleNextClick = () => {
        navigate(1); // Navegar a la vista siguiente
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
                        <button className='btn-alerts'>
                            <img src={btn_alerts} alt="Alerts" />
                        </button>
                    </div>
                    <h1>Productos</h1>
                    <p>Todos los productos registrados actualmente en el inventario</p>
                </div>
                <DataTable />
            </div>
        </div>
    );
}
