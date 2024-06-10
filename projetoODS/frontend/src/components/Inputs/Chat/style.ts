import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  font-family: Arial, sans-serif;
`;

export const ChatBox = styled.div`
  width: 350px;
  height: 220px;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  overflow-y: scroll;
`;

export const Message = styled.div`
  padding: 5px;
  border-bottom: 1px solid #eee;
`;

export const Input = styled.input`
  width: 350px;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
`;

export const Button = styled.button`
  padding: 10px 20px;
  border-radius: 5px;
  border: none;
  background: #007bff;
  color: white;
  cursor: pointer;
`;
