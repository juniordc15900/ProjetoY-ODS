import React from "react";
import * as S from "./style";
import TextInput from "../../components/Inputs/TextInput";
import BasicButton from "../../components/Buttons/BasicButton";
import Header from "../../components/Header";
import BasicTitle from "../../components/BasicTitle";

const App: React.FC = () => {
  return (
    <>
      <Header />
      <S.AppContainer>
        <S.Content>
          <BasicTitle>Escreva sobre seu empreendimento:</BasicTitle>
          <div className="search">
            <TextInput
              onChange={() => null}
              placeholder="Escreva sobre seu empreendimento:"
            />
            <BasicButton>Buscar</BasicButton>
          </div>
        </S.Content>
      </S.AppContainer>
    </>
  );
};

export default App;
