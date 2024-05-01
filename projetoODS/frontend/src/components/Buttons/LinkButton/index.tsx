import React from "react";
import * as S from "./style";

// Definição das propriedades do componente de botão
interface ButtonProps {
  onClick: () => void;
  children: React.ReactNode;
}

// Componente de botão reutilizável
const LinkButton: React.FC<ButtonProps> = ({ onClick, children }) => {
  return <S.StyledButton onClick={onClick}>{children}</S.StyledButton>;
};

export default LinkButton;
