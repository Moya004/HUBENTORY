import { useContext, createContext, useState, useEffect } from "react";

interface AuthProviderProps{
    children: React.ReactNode;
}

const AuthContext = createContext({
    isAuthenticated: false, 
});

export function AuthProvider({children}: AuthProviderProps){

    // autentificacion para que pase a la informacion protegida enviada del backend al fronted

    const [isAuthenticated, setIsAuthenticated] = useState(true); //donde se encuentran estos valores de verificacion se cambian por las variables creadas por mario del backend

    return (<AuthContext.Provider value={{isAuthenticated}}>{children}</AuthContext.Provider>);
}

export const useAuth = () => useContext(AuthContext);