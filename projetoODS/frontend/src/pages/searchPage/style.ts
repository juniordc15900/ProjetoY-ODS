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
  min-height: calc(100vh - 120px); /* 100vh - padding-top do Header */
`;

export const Content = styled.div`
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 90%;
  max-width: 800px;
  padding: 20px;
  /* background-color: rgba(255, 255, 255, 0.8); */

  .gif-loading {
    width: 12px;
  }
`;

export const SearchContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 20px;
  width: 100%;
`;

export const SearchResultsContainer = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: space-around;
  flex-direction: column;
`;

export const SearchResultItem = styled.div`
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  margin-bottom: 20px;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
`;

export const SearchResultTitle = styled.h3`
  margin-bottom: 10px;
  color: #333;
`;

export const SearchResultDetail = styled.p`
  margin: 0;
  color: #666;
  line-height: 1.6;
  text-transform: capitalize;

  strong {
    font-weight: bold;
    color: #000;
  }
`;

export const SearchResultsWrapper = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
`;