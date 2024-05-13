import React from "react";
import * as S from "./style";

// Definição das propriedades do componente de botão
interface ButtonProps {
  onClick?: () => void;
  children: React.ReactNode;
  type?: "button" | "submit" | "reset";
  disabled?: boolean; // Adicionando a propriedade disabled
}

// Componente de botão reutilizável
const BasicButton: React.FC<ButtonProps> = ({
  onClick,
  children,
  type = "button",
  disabled,
}) => {
  return (
    <S.StyledButton type={type} onClick={onClick} disabled={disabled}>
      {" "}
      {/* Adicionando a propriedade disabled */}
      {children}
    </S.StyledButton>
  );
};

export default BasicButton;
