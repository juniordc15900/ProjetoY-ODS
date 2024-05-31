import React from "react";
import * as S from "./style";
import BasicButton from "../Buttons/BasicButton";
import LinkButton from "../Buttons/LinkButton";
import { useLocation } from "wouter";

const Header: React.FC = () => {
  const [, setLocation] = useLocation();

  return (
    <S.HeaderContainer>
      <S.LeftMenu>
        <LinkButton onClick={() => setLocation("/home")}>Home</LinkButton>
        <LinkButton onClick={() => setLocation("/")}>Sobre</LinkButton>
        <LinkButton onClick={() => setLocation("/")}>Contato</LinkButton>
      </S.LeftMenu>
      <S.RightMenu>
        <BasicButton onClick={() => setLocation("/register")}>
          Cadastrar
        </BasicButton>
        <LinkButton onClick={() => setLocation("/login")}>Login</LinkButton>
      </S.RightMenu>
    </S.HeaderContainer>
  );
};

export default Header;
