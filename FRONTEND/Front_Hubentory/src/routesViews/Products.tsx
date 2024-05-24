import NavBar from "../Components/navBar";
import DataTable from '../Components/tableProducts';
import logo from '../assets/logo.png';
import './stylesproducts.css';


export default function Products() {
    return (
        <div className="container">
            <NavBar>
                <img className="logo-hub" src={logo}></img>
            </NavBar>
            <div>
                <div className="content">
                    <h1>Productos</h1>
                </div>
                <DataTable />
            </div>
        </div>
    );
}
