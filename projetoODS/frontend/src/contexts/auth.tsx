import { createContext, ReactNode, useContext, useState } from "react";
import axios from "axios";

type User = {
  email: string;
  password: string;
};

type AuthContextType = {
  user: User | null;
  signed: boolean;
  signin: (email: string, password: string) => Promise<void>;
  signup: (email: string, password: string) => Promise<void>;
  signout: () => void;
};

export const AuthContext = createContext<AuthContextType>({
  user: null,
  signed: false,
  signin: async () => {},
  signup: async () => {},
  signout: () => {},
});

type AuthProviderProps = {
  children: ReactNode;
};

export const AuthProvider = ({ children }: AuthProviderProps) => {
  const [user, setUser] = useState<User | null>(null);

  const signin = async (email: string, password: string) => {
    try {
      const response = await axios.post("/postsignIn/", { email, password });
      setUser({ email, password });
      localStorage.setItem("user_token", JSON.stringify(response.data));
    } catch (error) {
      throw new Error(
        "Credenciais inválidas! Por favor, verifique seus dados."
      );
    }
  };

  const signup = async (email: string, password: string) => {
    try {
      const response = await axios.post("/postsignUp/", { email, password });
      setUser({ email, password });
      localStorage.setItem("user_token", JSON.stringify(response.data));
    } catch (error) {
      throw new Error("Erro ao criar usuário. Tente novamente.");
    }
  };

  const signout = () => {
    setUser(null);
    localStorage.removeItem("user_token");
  };

  return (
    <AuthContext.Provider
      value={{ user, signed: !!user, signin, signup, signout }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
