import { AuthProvider } from "./contexts/auth";
import { RoutesApp } from "./routes";

function App() {
  return (
    <>
      <AuthProvider>
        <RoutesApp />
      </AuthProvider>
    </>
  );
}

export default App;
