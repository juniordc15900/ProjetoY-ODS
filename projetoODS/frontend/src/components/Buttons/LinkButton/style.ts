import styled from "styled-components";

// Estilizando o botão com styled-components
export const StyledButton = styled.button`
  cursor: pointer;
  transition: background-color 0.3s ease;
  background-color: transparent;
  border: none;
  outline: none;
  padding: 0;
  font: inherit;
  color: #111B47;
  font-weight: bold;
  text-decoration: none;
  font-size: 15px;
  font-weight: bold;
  width: 100%;


  &:hover {
    text-decoration: underline;
    color: #0056b3;
  }
`;