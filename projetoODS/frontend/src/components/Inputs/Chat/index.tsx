import React, { useRef } from "react";
import * as S from "./style";
import axios from "axios";

interface Message {
  id: number;
  text: string;
}

interface ChatProps {
  messages: Message[];
  inputValue: string;
  onInputChange: (value: string) => void;
  onSendMessage: () => void;
}

const Chat: React.FC<ChatProps> = ({
  messages,
  inputValue,
  onInputChange,
  onSendMessage,
}) => {
  const nextId = useRef(
    messages.length > 0 ? messages[messages.length - 1].id + 1 : 1
  );

  const handleSendMessage = async () => {
    if (inputValue.trim() === "") return;

    onSendMessage();

    nextId.current += 1;

    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/gemini/gemini-dominios?palavras=${inputValue.trim()}`
      );
      console.log(response.data);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      handleSendMessage();
    }
  };

  return (
    <S.Container>
      <S.ChatBox>
        {messages.map((message) => (
          <S.Message key={message.id}>{message.text}</S.Message>
        ))}
      </S.ChatBox>
      <S.Input
        type="text"
        value={inputValue}
        onChange={(e) => onInputChange(e.target.value)}
        onKeyPress={handleKeyPress}
        placeholder="Digite sua mensagem"
      />
    </S.Container>
  );
};

export default Chat;
