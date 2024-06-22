import React, { useState, useEffect } from "react";
import * as S from "./style";
import axios from "axios";
import BasicButton from "../../components/Buttons/BasicButton";
import Header from "../../components/Header";
import BasicTitle from "../../components/Titles";
import Chat from "../../components/Inputs/Chat";

interface Message {
  id: number;
  text: string;
}

const formatPrice = (price: string | number): string => {
  const numericPrice =
    typeof price === "string"
      ? parseFloat(price.replace(",", "")) / 1000000
      : (price as number) / 1000000;
  return numericPrice.toLocaleString("en-US", {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  });
};

const ChatPage: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState("");
  const [searchResults, setSearchResults] = useState<string[]>([]); // Initialize as string[] for domain names
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const storedMessages = localStorage.getItem("chatMessages");
    if (storedMessages) {
      setMessages(JSON.parse(storedMessages));
    }
  }, []);

  useEffect(() => {
    localStorage.setItem("chatMessages", JSON.stringify(messages));
  }, [messages]);

  const handleSendMessage = async () => {
    if (!inputValue.trim()) {
      alert("Por favor, insira um texto para buscar.");
      return;
    }

    const newMessage: Message = {
      id: messages.length + 1,
      text: inputValue.trim(),
    };

    setMessages([...messages, newMessage]);
    setInputValue("");

    setLoading(true);
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/gemini/gemini-dominios?palavras=${inputValue}`
      );
      console.log(response);

      if (Array.isArray(response.data.dominios)) {
        const domains: string[] = response.data.dominios;
        setSearchResults(domains);
        console.log(domains);
      } else {
        console.error("Unexpected response structure:", response.data);
      }
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await handleSendMessage();
  };

  return (
    <S.AppContainer>
      <Header />
      <BasicTitle>Escreva sobre seu empreendimento:</BasicTitle>
      <S.Content>
        <S.SearchContainer>
          <form onSubmit={handleSubmit}>
            <Chat
              messages={messages}
              inputValue={inputValue}
              onInputChange={setInputValue}
              onSendMessage={handleSendMessage}
            />
            <BasicButton type="submit" disabled={loading}>
              {loading ? (
                <img
                  className="gif-loading"
                  src="/img/loading.gif"
                  alt="loading"
                />
              ) : (
                "Buscar"
              )}
            </BasicButton>
          </form>
        </S.SearchContainer>
        <S.SearchResultsContainer>
          {searchResults.length > 0 && (
            <>
              {searchResults.map((domainObject, index) => (
                <S.SearchResultItem key={index}>
                  <S.SearchResultTitle>
                    {Object.values(domainObject)}
                  </S.SearchResultTitle>
                  <hr />
                  {/* Render details for each domain if needed */}
                </S.SearchResultItem>
              ))}
            </>
          )}
        </S.SearchResultsContainer>
      </S.Content>
    </S.AppContainer>
  );
};

export default ChatPage;
