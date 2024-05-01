import React, { ChangeEvent } from "react";
import * as S from "./style";

// Definição das propriedades do componente
interface InputProps {
  type: string;
  placeholder?: string;
  value?: string;
  onChange: (e: ChangeEvent<HTMLInputElement>) => void; // Alterado o tipo de onChange
}

// Componente de input reutilizável
const BasicInput: React.FC<InputProps> = ({
  type,
  placeholder,
  value,
  onChange,
}) => {
  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    onChange(e); // Passando o evento diretamente para a função onChange
  };

  return (
    <S.StyledInput
      type={type}
      placeholder={placeholder}
      value={value}
      onChange={handleChange}
    />
  );
};

export default BasicInput;
