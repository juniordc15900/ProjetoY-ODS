// import { Route, Switch, Router } from "router";
import { Route, Routes, BrowserRouter } from 'react-router-dom';
import AccountPage from "../pages/accountPage/account_page";
import SearchPage from "../pages/searchPage/search_page";

export const RoutesApp = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" Component={SearchPage} />
        <Route path="/home" Component={SearchPage} />
        <Route path="/register" Component={AccountPage} />
        <Route path="/login" Component={AccountPage} />
      </Routes>
    </BrowserRouter>
  );
};
