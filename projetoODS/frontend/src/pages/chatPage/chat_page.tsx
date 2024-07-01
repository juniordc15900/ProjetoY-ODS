import React, { useState, useEffect } from "react";
import * as S from "./style";
import axios from "axios";
import BasicButton from "../../components/Buttons/BasicButton";
import Header from "../../components/Header";
import BasicTitle from "../../components/Titles";
import Chat from "../../components/Inputs/Chat";
import StripeCheckout from "../../components/Stripe/CheckoutForm";
import { Link } from "wouter";

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
  const [paymentScreen, setPaymentScreen] = useState(false);
  const [searchResults, setSearchResults] = useState<string[]>([]);
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

  const handlePayment = () => {
    console.log(paymentScreen);
    setPaymentScreen(!paymentScreen);
    console.log(paymentScreen);
  };

  const handleClosePaymentScreen = () => {
    setPaymentScreen(false);
  };

  const handleInnerClick = (e: React.MouseEvent) => {
    e.stopPropagation(); // Impede que o clique no StripeCheckout feche o contêiner
  };

  return (
    <>
      {paymentScreen && (
        <S.PaymentContainer onClick={handleClosePaymentScreen}>
          <div className="payment-form" onClick={handleInnerClick}>
            <StripeCheckout />
          </div>
        </S.PaymentContainer>
      )}
      <S.AppContainer>
        {!paymentScreen && <Header />}
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
                    <Link
                      className="link"
                      onClick={() => setPaymentScreen(!paymentScreen)}
                      href="#"
                    >
                      <S.SearchResultTitle>
                        {Object.values(domainObject)}
                      </S.SearchResultTitle>
                    </Link>
                  </S.SearchResultItem>
                ))}
              </>
            )}
            {/* <button
              onClick={() => setPaymentScreen(!paymentScreen)}
              type="button"
            >
              TESTE
            </button> */}
          </S.SearchResultsContainer>
        </S.Content>
      </S.AppContainer>
    </>
  );
};

export default ChatPage;
