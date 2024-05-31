import styled from "styled-components";

export const StyledTextArea = styled.textarea`
  padding: 8px;
  width: 100%;
  height: 60px;
  background-color: #fff;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  border: none;
  border-radius: 8px;
  font-family: 'Raleway', sans-serif;

  &:focus {
    outline: none;
  }

  &::placeholder {
    color: #354446;
  }
`;
