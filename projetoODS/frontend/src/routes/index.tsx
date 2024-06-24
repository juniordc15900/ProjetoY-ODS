import { Route, Switch, Router } from "wouter";
import AccountPage from "../pages/accountPage/account_page";
import SearchPage from "../pages/searchPage/search_page";
import ChatPage from "../pages/chatPage/chat_page";
import PaymentPage from "../pages/paymentPage/payment_page";

export const RoutesApp = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" component={SearchPage} />
        <Route path="/home" component={SearchPage} />
        <Route path="/chat" component={ChatPage} />
        <Route path="/register" component={AccountPage} />
        <Route path="/login" component={AccountPage} />
        <Route path="/payment" component={PaymentPage} />
      </Switch>
    </Router>
  );
};
