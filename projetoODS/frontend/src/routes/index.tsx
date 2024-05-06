import { Route, Switch, Router } from "wouter";
import AccountPage from "../pages/accountPage/account_page";
import SearchPage from "../pages/searchPage/search_page";
import PrivateRoute from "./private";

const RoutesApp = () => {
  return (
    <Router>
      <Switch>
        {/* <PrivateRoute path="/" component={SearchPage} />
        <PrivateRoute path="/home" component={SearchPage} /> */}
        <Route path="/" component={SearchPage} />
        <Route path="/home" component={SearchPage} />
        <Route path="/register" component={AccountPage} />
        <Route path="/login" component={AccountPage} />
      </Switch>
    </Router>
  );
};

export default RoutesApp;
