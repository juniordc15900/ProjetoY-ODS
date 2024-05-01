import styled from 'styled-components';

export const AppContainer = styled.div`
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
  width: 100%;
  height: 100vh;
  background-image: url(./img/wallpaper.png);
`;

export const Content = styled.div`
  margin-top: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 10%;
  width: 80%;
  
  .search {
    display: flex;
    gap: 10%;
    width: 60%;
  }

`;