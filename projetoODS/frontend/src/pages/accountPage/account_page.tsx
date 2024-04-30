import React, { useState, ChangeEvent } from "react";
import BasicInput from "../../components/basicInput";
import BasicButton from "../../components/Button/basicButton";
import BasicTitle from "../../components/basicTitle";
import { Container, FormContainer, ImageContainer, Image } from "./style";
import LinkButton from "../../components/Button/linkButton";

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

  const handleUserChange = (e: ChangeEvent<HTMLInputElement>) => {
    setUser(e.target.value);
  };

  const handleEmailChange = (e: ChangeEvent<HTMLInputElement>) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e: ChangeEvent<HTMLInputElement>) => {
    setPassword(e.target.value);
  };

  return (
    <Container>
      <FormContainer>
        <BasicTitle>ProjODS</BasicTitle>
        {!!isLogin && (
          <form onSubmit={handleSubmit}>
            <div className="forms-inputs">
              <BasicInput
                type="email"
                placeholder="Email"
                value={email}
                onChange={handleEmailChange}
              />
              <BasicInput
                type="password"
                placeholder="Senha"
                value={password}
                onChange={handlePasswordChange}
              />
            </div>
            <div className="forms-buttons">
              <BasicButton onClick={() => null}>Fazer Login</BasicButton>
              <LinkButton onClick={toggleForm}>Criar conta</LinkButton>
            </div>
          </form>
        )}
        {!isLogin && (
          <form onSubmit={handleSubmit}>
            <div className="forms-inputs">
              <BasicInput
                type="text"
                placeholder="Usuário"
                value={user}
                onChange={handleUserChange}
              />
              <BasicInput
                type="email"
                placeholder="Email"
                value={email}
                onChange={handleEmailChange}
              />
              <BasicInput
                type="password"
                placeholder="Senha"
                value={password}
                onChange={handlePasswordChange}
              />
              <BasicInput
                type="password"
                placeholder="Confirmar senha"
                value={password}
                onChange={handlePasswordChange}
              />
            </div>
            <div className="forms-buttons">
              <BasicButton onClick={() => null}>Cadastrar</BasicButton>
              <LinkButton onClick={toggleForm}>Fazer login</LinkButton>
            </div>
          </form>
        )}
      </FormContainer>
      <ImageContainer>
        <Image src="./img/manworking.png" alt="" />
      </ImageContainer>
    </Container>
  );
};

export default AccountPage;
