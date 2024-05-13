import React, { useState, ChangeEvent } from "react";
import BasicInput from "../../components/Inputs/BasicInput";
import BasicButton from "../../components/Buttons/BasicButton";
import BasicTitle from "../../components/Titles";
import { Container, FormContainer, ImageContainer, Image, Text } from "./style";
import LinkButton from "../../components/Buttons/LinkButton";
import axios from "axios";

const useLoginForm = () => {
  const [user, setUser] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [isLogin, setIsLogin] = useState(true);
  const [errorMessage, setErrorMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (isLogin) {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/gemini/teste",
          {}
        );
        console.log("OK");
        console.log(response.data);
        // Lógica de redirecionamento após o login bem-sucedido
      } catch (error) {
        setErrorMessage(
          "Credenciais inválidas! Por favor, verifique seus dados."
        );
      }
    } else {
      if (password !== confirmPassword) {
        setErrorMessage("As senhas não coincidem!");
        return;
      }
      try {
        const response = await axios.post("/postsignUp/", {
          email: email,
          pass: password,
          name: user,
        });
        console.log(response.data);
        // Lógica de redirecionamento após o cadastro bem-sucedido
      } catch (error) {
        console.error(error);
        // Lógica para tratamento de erro de cadastro
      }
    }
  };

  const toggleForm = () => {
    setIsLogin(!isLogin);
    setErrorMessage("");
  };

  return {
    user,
    setUser,
    email,
    setEmail,
    password,
    setPassword,
    confirmPassword,
    setConfirmPassword,
    isLogin,
    handleSubmit,
    toggleForm,
    errorMessage,
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
    confirmPassword,
    setConfirmPassword,
    isLogin,
    handleSubmit,
    toggleForm,
    errorMessage,
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

  const handleConfirmPasswordChange = (e: ChangeEvent<HTMLInputElement>) => {
    setConfirmPassword(e.target.value);
  };

  return (
    <Container>
      <FormContainer>
        <BasicTitle>ProjODS</BasicTitle>
        {!!isLogin && (
          <>
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
                <BasicButton type="submit">Login</BasicButton>
                <LinkButton onClick={toggleForm}>Criar conta</LinkButton>
              </div>
            </form>
            {errorMessage && <Text>{errorMessage}</Text>}
          </>
        )}
        {!isLogin && (
          <>
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
                  value={confirmPassword}
                  onChange={handleConfirmPasswordChange}
                />
              </div>
              <div className="forms-buttons">
                <BasicButton type="submit">Cadastrar</BasicButton>
                <LinkButton onClick={toggleForm}>Fazer login</LinkButton>
              </div>
            </form>
            {errorMessage && <Text>{errorMessage}</Text>}
          </>
        )}
      </FormContainer>
      <ImageContainer>
        <Image src="./img/manworking.png" alt="" />
      </ImageContainer>
    </Container>
  );
};

export default AccountPage;
