import React, { useState } from "react";
import * as S from "./style";
import axios from "axios";
import TextInput from "../../components/Inputs/TextInput";
import BasicButton from "../../components/Buttons/BasicButton";
import Header from "../../components/Header";
import BasicTitle from "../../components/Titles";

const SearchPage: React.FC = () => {
  const [searchText, setSearchText] = useState("");
  const [searchResults, setSearchResults] = useState<any>(); // Estado para armazenar a resposta da pesquisa

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/gemini/gemini-dominios?palavras=${searchText}`
      );
      setSearchResults(response.data.resultados); // Atualizar o estado com os resultados da pesquisa
    } catch (error) {
      console.error("Error:", error);
      // Lógica para lidar com erros na solicitação
    }
  };

  return (
    <>
      <Header />
      <S.AppContainer>
        <S.Content>
          <BasicTitle>Escreva sobre seu empreendimento:</BasicTitle>
          <form onSubmit={handleSubmit}>
            <div className="search">
              <TextInput
                value={searchText}
                onChange={(e) => setSearchText(e.target.value)}
                placeholder="Escreva sobre seu empreendimento:"
              />
              <BasicButton type="submit">Buscar</BasicButton>
            </div>
          </form>
          <div className="search-results">
            <h2>Resultados da pesquisa:</h2>
            <br></br>

            <ul>
              {searchResults &&
                Object.entries(searchResults).map(([dominio, info]) => (
                  <li key={dominio}>
                    <strong>{dominio}</strong>:
                    <ul>
                      {Object.entries(info).map(([chave, valor]) => (
                        <li key={chave}>
                          <span>{chave}: </span>
                          <span>{valor}</span>
                        </li>
                      ))}
                    </ul>
                    <br></br>
                  </li>
                ))}
            </ul>
          </div>
        </S.Content>
      </S.AppContainer>
    </>
  );
};

export default SearchPage;
