import styled from "styled-components";

// Estilizando o botão com styled-components
export const StyledButton = styled.button`
  color: black;
  cursor: pointer;
  transition: background-color 0.3s ease;
  background-color: transparent;
  border: none;
  outline: none;
  padding: 0;
  font: inherit;

  &:hover {
    text-decoration: underline;

  }
`;