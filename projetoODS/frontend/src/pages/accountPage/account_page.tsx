import React, { ChangeEvent, useState } from "react";
import BasicInput from "../../components/Inputs/BasicInput";
import BasicButton from "../../components/Buttons/BasicButton";
import BasicTitle from "../../components/Titles";
import { Container, FormContainer, ImageContainer, Image, Text } from "./style";
import LinkButton from "../../components/Buttons/LinkButton";
import { useAuth } from "../../contexts/auth";

const AccountPage: React.FC = () => {
  const { signin, signup } = useAuth();
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [isLogin, setIsLogin] = useState(true);
  const [errorMessage, setErrorMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (isLogin) {
      try {
        await signin(email, password);
        console.log("Login bem-sucedido");
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
        await signup(email, password);
        console.log("Cadastro bem-sucedido");
        // Lógica de redirecionamento após o cadastro bem-sucedido
      } catch (error) {
        console.error(error);
      }
    }
  };

  const toggleForm = () => {
    setIsLogin(!isLogin);
    setErrorMessage("");
  };

  const handleUsernameChange = (e: ChangeEvent<HTMLInputElement>) => {
    setUsername(e.target.value);
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
                <BasicButton type="submit">Fazer Login</BasicButton>
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
                  value={username}
                  onChange={handleUsernameChange}
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
