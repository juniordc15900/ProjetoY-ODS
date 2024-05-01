import React, { ChangeEvent } from "react";
import * as S from "./style";

// Definição das propriedades do componente
interface InputProps {
  placeholder?: string;
  value?: string;
  onChange: (e: ChangeEvent<HTMLTextAreaElement>) => void; // Alterado o tipo de onChange
}

// Componente de input reutilizável
const TextInput: React.FC<InputProps> = ({ placeholder, value, onChange }) => {
  const handleChange = (e: ChangeEvent<HTMLTextAreaElement>) => {
    onChange(e); // Passando o evento diretamente para a função onChange
  };

  return (
    <S.StyledTextArea
      placeholder={placeholder}
      value={value}
      onChange={handleChange}
    />
  );
};

export default TextInput;
