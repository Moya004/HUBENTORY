import { Outlet ,  Navigate } from "react-router-dom";
import { useAuth } from "../Auth/AuthProvider";
export default function protectedroutes(){
    const auth = useAuth()
    
    return auth.isAuthenticated ? <Outlet /> : <Navigate to="/" />

}