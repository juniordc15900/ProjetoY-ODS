import styled from 'styled-components';

export const AppContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-image: url(./img/wallpaper.png);
  background-size: cover;
  background-repeat: no-repeat;
  padding-top: 120px;
  min-height: calc(100vh - 120px);
`;