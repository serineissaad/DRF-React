import React from "react";
import { Row, Col } from "react-bootstrap";
import Home from "../components/Home";
import { homes } from "../homes";

function HomeScreen() {
  return (
    <div>
      <h1>latest houses</h1>
      <Row>
        {homes.map((homes) => (
          <Col key={homes.id} sm={12} md={6} lg={4} xl={3}>
            <Home homes={homes} />
          </Col>
        ))}
      </Row>
    </div>
  );
}

export default HomeScreen;
