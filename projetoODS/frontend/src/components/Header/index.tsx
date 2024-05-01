import React from "react";
import * as S from "./style";
import BasicButton from "../Buttons/BasicButton";
import LinkButton from "../Buttons/LinkButton";

const Header: React.FC = () => {
  return (
    <S.HeaderContainer>
      <S.LeftMenu>
        <LinkButton onClick={() => null}>Home</LinkButton>
        <LinkButton onClick={() => null}>Sobre</LinkButton>
        <LinkButton onClick={() => null}>Contato</LinkButton>
      </S.LeftMenu>
      <S.RightMenu>
        <BasicButton onClick={() => null}>Cadastrar</BasicButton>
        <LinkButton onClick={() => null}>Login</LinkButton>
      </S.RightMenu>
    </S.HeaderContainer>
  );
};

export default Header;
