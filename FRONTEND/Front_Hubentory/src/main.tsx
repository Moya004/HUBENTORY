import React from 'react'
import ReactDOM from 'react-dom/client'
// import App from './App.tsx'
import './index.css'
import Login from './routesViews/Login.tsx'
import SingUp from './routesViews/SingUp.tsx'
import Products from './routesViews/Products.tsx'
import Reports from './routesViews/Reports.tsx'
import ProtectedRoutes from './routesViews/ProtectedRoutes.tsx'
import { AuthProvider } from './Auth/AuthProvider.tsx'

// esto es para crear las vistas en la navegación en una aplicación web creada con React
import { createBrowserRouter , RouterProvider } from "react-router-dom";

// creamos el router - es un arreglo
const router = createBrowserRouter([
  {
    path:"/login",
    element: <Login/>,
  },
  {
    path:"/singUp",
    element: <SingUp />,
  },
  {
    // que rutas son protegidas a partir de dashboard
    path:"/", //busca la raiz y luego valida que si es verdadero pasa a dashboard
    element: <ProtectedRoutes/>,
    // propiedad que solicita un arreglo
    children: [
      {
        path:"/Products",
        element: <Products />,
      },
      {
        path:"/Reports",
        element: <Reports />,
      }
    ],
  },
]);

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <AuthProvider>
      <RouterProvider router = {router} />
    </AuthProvider>
  </React.StrictMode>,
)
