import React from "react";
import { Link } from "react-router-dom";
import { Row, Col, Image, ListGroup, Button, Card } from "react-bootstrap";
import Rating from "../components/Rating";
import { homes } from "../homes";
import { useParams } from "react-router-dom";

function HouseScreen() {
  const { id } = useParams();
  const home = homes.find((h) => h.id.toString() === id);

  if (!home) {
    return <h2>home not found</h2>;
  }

  const { _id, picture, location, price, rating, numReviews } = home;
  return (
    <div>
      <Link to="/" className="btn btn-light my-3">
        Go back
      </Link>
      <Row>
        <Col md={6}>
          <Image src={home?.picture} fluid />
        </Col>
        <Col md={3}>
          <ListGroup variant="flush">
            <ListGroup.Item>
              <h3>{home?.location}</h3>
            </ListGroup.Item>
            <ListGroup.Item>
              <Rating
                value={home?.rating}
                text={`${home?.numberOfRatings} reviews`}
                color={`#f8e825`}
              />
            </ListGroup.Item>
            <ListGroup.Item>Owner : {home?.owner}</ListGroup.Item>
            <ListGroup.Item>Price :${home?.price}</ListGroup.Item>
          </ListGroup>
        </Col>
        <Col md={3}>
          <Card>
            <ListGroup variant="flush">
              <ListGroup.Item>
                <Row>
                  <Col>Price :</Col>
                  <Col>
                    {" "}
                    <strong>${home?.price}</strong>
                  </Col>
                </Row>
              </ListGroup.Item>

              <ListGroup.Item>
                <Row>
                  <Col>Status:</Col>
                  <Col> {home?.status}</Col>
                </Row>
              </ListGroup.Item>

              <ListGroup.Item>
                <Button className="btn-block" type="button">
                  {home?.status == "for sale" ? "Buy" : "Rent"}
                </Button>
              </ListGroup.Item>
            </ListGroup>
          </Card>
        </Col>
      </Row>
    </div>
  );
}

export default HouseScreen;
