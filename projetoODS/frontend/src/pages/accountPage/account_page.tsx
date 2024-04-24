import React, { useState } from "react";

const useLoginForm = () => {
  const [user, setUser] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isLogin, setIsLogin] = useState(true);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (isLogin) {
      // Lógica de login
      console.log("Login:", email, password);
    } else {
      // Lógica de cadastro
      console.log("Signup:", user, email, password);
    }
  };

  const toggleForm = () => {
    setIsLogin(!isLogin);
  };

  return {
    user,
    setUser,
    email,
    setEmail,
    password,
    setPassword,
    isLogin,
    handleSubmit,
    toggleForm,
  };
};

const AccountPage: React.FC = () => {
  const {
    user,
    setUser,
    email,
    setEmail,
    password,
    setPassword,
    isLogin,
    handleSubmit,
    toggleForm,
  } = useLoginForm();

  return (
    <>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "100vh",
        }}
      >
        <div style={{ width: "50%", padding: "20px", boxSizing: "border-box" }}>
          <h1>Projeto Y ODS</h1>
          {!!isLogin && (
            <form onSubmit={handleSubmit}>
              <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                style={{ marginBottom: "10px", padding: "8px", width: "100%" }}
              />
              <input
                type="password"
                placeholder="Senha"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                style={{ marginBottom: "10px", padding: "8px", width: "100%" }}
              />
              <button type="submit" style={{ padding: "8px", width: "100%" }}>
                Fazer Login
              </button>
              <p>Não tem uma conta?</p>
              <button
                onClick={toggleForm}
                style={{ padding: "8px", width: "100%" }}
              >
                Criar conta
              </button>
            </form>
          )}
          {!isLogin && (
            <form onSubmit={handleSubmit}>
              <input
                type="text"
                placeholder="Usuário"
                value={user}
                onChange={(e) => setUser(e.target.value)}
                required
                style={{ marginBottom: "10px", padding: "8px", width: "100%" }}
              />
              <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                style={{ marginBottom: "10px", padding: "8px", width: "100%" }}
              />
              <input
                type="password"
                placeholder="Senha"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                style={{ marginBottom: "10px", padding: "8px", width: "100%" }}
              />
              <input
                type="password"
                placeholder="Confirmar senha"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                style={{ marginBottom: "10px", padding: "8px", width: "100%" }}
              />
              <button type="submit" style={{ padding: "8px", width: "100%" }}>
                Cadastrar
              </button>
              <p>Já tem uma conta?</p>
              <button
                onClick={toggleForm}
                style={{ padding: "8px", width: "100%" }}
              >
                Fazer login
              </button>
            </form>
          )}
        </div>
        <div style={{ width: "50%" }}>
          <img
            src="./img/manworking.png"
            alt=""
            style={{ maxWidth: "100%", height: "auto" }}
          />
        </div>
      </div>
    </>
  );
};

export default AccountPage;
