import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import HomeScreen from "./screens/HomeScreen";
import HouseScreen from "./screens/HouseScreen";
import { Container } from "react-bootstrap";

function App() {
  return (
    <div>
      <Router>
        <Header />
        <main>
          <Container className="py-3">
            <Routes>
              <Route path="/" element={<HomeScreen />} />
              <Route path={"/house/:id"} element={<HouseScreen />} />
            </Routes>
          </Container>
        </main>
        <Footer />
      </Router>
    </div>
  );
}

export default App;
