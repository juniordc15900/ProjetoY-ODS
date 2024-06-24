import styled from 'styled-components';

export const AppContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  background-image: url(./img/wallpaper.png);
  background-size: cover;
  background-repeat: no-repeat;
  padding-top: 120px;
  min-height: calc(100vh - 120px); /* 100vh - padding-top do Header */
  
`;

export const Content = styled.div`
  display: flex;
  width: 95%;
  overflow: hidden;
  padding: 20px;

`;

export const SearchContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  width: 40%;
  height: 100%;
  overflow-y: auto;
  padding: 10px;

  form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .gif-loading {
    width: 12px;
  }
`;

export const SearchResultsContainer = styled.div`
  display: flex;
  flex-direction: column;
  width: 60%;
  /* overflow-y: scroll;
  max-height: 350px; */
  justify-content: center;

  .link{
    text-decoration: none;
  }
`;

export const SearchResultItem = styled.a`
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  margin-bottom: 20px;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
`;

export const SearchResultTitle = styled.h3`
  margin-bottom: 10px;
  color: #333;
  display: flex;
  justify-content: space-between;
  align-items: center;
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
export const PaymentContainer = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(10, 23, 55, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;

  .payment-form {
    width: 100%;
  }


`;
