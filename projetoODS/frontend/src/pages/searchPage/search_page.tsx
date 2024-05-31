import React, { useState } from "react";
import * as S from "./style";
import axios from "axios";
import TextInput from "../../components/Inputs/TextInput";
import BasicButton from "../../components/Buttons/BasicButton";
import Header from "../../components/Header";
import BasicTitle from "../../components/Titles";

interface SearchResult {
  [key: string]: any;
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

const SearchPage: React.FC = () => {
  const [searchText, setSearchText] = useState("");
  const [searchResults, setSearchResults] = useState<SearchResult | undefined>(
    undefined
  ); // Estado para armazenar a resposta da pesquisa
  const [loading, setLoading] = useState(false); // Estado para controlar a exibição do gif de loading

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!searchText.trim()) {
      alert("Por favor, insira um texto para buscar.");
      return;
    }

    setLoading(true);
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/gemini/gemini-dominios?palavras=${searchText}`
      );
      setSearchResults(response.data.resultados); // Atualizar o estado com os resultados da pesquisa
    } catch (error) {
      console.error("Error:", error);
      // Lógica para lidar com erros na solicitação
    } finally {
      setLoading(false);
    }
  };

  return (
    <S.AppContainer>
      <Header />
      <S.Content>
        <form onSubmit={handleSubmit}>
          <S.SearchContainer>
            <BasicTitle>Escreva sobre seu empreendimento:</BasicTitle>
            <TextInput
              value={searchText}
              onChange={(e) => setSearchText(e.target.value)}
              placeholder="Escreva sobre seu empreendimento:"
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
          </S.SearchContainer>
        </form>
        <S.SearchResultsContainer>
          {searchResults && (
            <>
              {Object.entries(searchResults).map(([dominio, info]) => (
                <S.SearchResultItem key={dominio}>
                  <S.SearchResultTitle>{dominio}</S.SearchResultTitle>
                  <hr />
                  <ul>
                    {Object.entries(info).map(([chave, valor]) => (
                      <li key={chave}>
                        <S.SearchResultDetail>
                          <strong>{chave}:</strong>{" "}
                          {typeof valor === "string"
                            ? valor
                            : JSON.stringify(formatPrice(valor as string))}
                        </S.SearchResultDetail>
                      </li>
                    ))}
                  </ul>
                </S.SearchResultItem>
              ))}
            </>
          )}
        </S.SearchResultsContainer>
      </S.Content>
    </S.AppContainer>
  );
};

export default SearchPage;
