import React from "react";
import * as S from "./style";

// Definição das propriedades do componente de botão
interface ButtonProps {
  onClick?: () => void;
  children: React.ReactNode;
  type?: "button" | "submit" | "reset";
}

// Componente de botão reutilizável
const BasicButton: React.FC<ButtonProps> = ({
  onClick,
  children,
  type = "button",
}) => {
  return (
    <S.StyledButton type={type} onClick={onClick}>
      {children}
    </S.StyledButton>
  );
};

export default BasicButton;
