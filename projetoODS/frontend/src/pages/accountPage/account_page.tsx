import React, { useState, ChangeEvent, useEffect } from "react";
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
  const [csrfToken, setCSRFToken] = useState("");

  useEffect(() => {
    const fetchCSRFToken = async () => {
      try {
        const response = await axios.get("http://localhost:8000/csrf/");
        const csrfToken = response.data.csrfToken;
        setCSRFToken(csrfToken);
      } catch (error) {
        console.error("Failed to fetch CSRF token:", error);
      }
    };
    fetchCSRFToken();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (isLogin) {
      try {
        const response = await axios.post(
          "http://localhost:8000/postsignIn/",
          {
            email: email,
            pass: password,
          },
          {
            withCredentials: true,
            headers: {
              "X-CSRFToken": csrfToken,
            },
          }
        );
        console.log("OK");
        console.log(response.data);
        // Logic for redirection after successful login
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
        const response = await axios.post(
          "http://localhost:8000/postsignUp/",
          {
            email: email,
            pass: password,
            name: user,
          },
          {
            headers: {
              "X-CSRFToken": csrfToken,
            },
            withCredentials: true,
          }
        );
        console.log(response.data);
        // Logic for redirection after successful registration
      } catch (error) {
        console.error(error);
        // Logic for registration error handling
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
