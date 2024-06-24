import React from "react";
import * as S from "../searchPage/style";
import Header from "../../components/Header";
import StripeCheckout from "../../components/Stripe/CheckoutForm";

const PaymentPage: React.FC = () => {
  return (
    <S.AppContainer>
      <Header />
      <S.Content>
        <StripeCheckout />
      </S.Content>
    </S.AppContainer>
  );
};

export default PaymentPage;
