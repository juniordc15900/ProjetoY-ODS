import styled from "styled-components";

// Estilizando o botão com styled-components
export const StyledButton = styled.button`
  padding: 8px 16px;
  background-color: #111B47;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  height: 20%;
  width: 100%;

  &:hover {
    background-color: #0056b3;
  }
`;