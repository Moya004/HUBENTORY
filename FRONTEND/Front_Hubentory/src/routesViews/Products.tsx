import NavBar from "../Components/navBar";
import DataTable from '../Components/tableProducts';
import logo from '../assets/logo.png';
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
                <img className="logo-hub" src={logo} alt="Logo"></img>
            </NavBar>
            <div>
                <div className="content">
                  <div className="header">
                    <button onClick={handlePreviousClick}>Vista Anterior</button>
                    <button onClick={handleNextClick}>Vista Siguiente</button>
                  </div>
                    <h1>Productos</h1>
                </div>
                <DataTable />
            </div>
        </div>
    );
}
