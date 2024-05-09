import React from "react";
import * as S from "./style";

// Definição das propriedades do componente de título
interface TitleProps {
  children: React.ReactNode;
}

// Componente de título reutilizável
const BasicTitle: React.FC<TitleProps> = ({ children }) => {
  return <S.StyledTitle>{children}</S.StyledTitle>;
};

export default BasicTitle;
