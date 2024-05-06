import { Route, RouteComponentProps } from "wouter";
import { useAuth } from "../contexts/auth";
import AccountPage from "../pages/accountPage/account_page";

interface PrivateRouteProps {
  path: string;
  component: React.ComponentType<RouteComponentProps<any>>;
}

const PrivateRoute: React.FC<PrivateRouteProps> = ({ path, component }) => {
  const { signed } = useAuth();

  return <Route path={path} component={signed ? component : AccountPage} />;
};

export default PrivateRoute;
