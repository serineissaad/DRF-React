import React from "react";
import { Card } from "react-bootstrap";
import Rating from "./Rating";
import { Link } from "react-router-dom";

function Home({ homes }) {
  return (
    <Card className="my-3 p-3 rounder">
      <Link to={`/house/${homes.id}`}>
        <Card.Img src={homes.picture} />
      </Link>

      <Card.Body>
        <Link to={`/house/${homes.id}`}>
          <Card.Title as="div">
            <strong>{homes.location}</strong>
          </Card.Title>
        </Link>
        <Card.Text as="div">
          <div className="me-3 ">{homes.status}</div>
        </Card.Text>

        <Card.Text as="div">
          <div className="me-3 ">
            {/* {homes.rating} from {homes.numberOfRatings} reviews */}
            <Rating
              value={homes.rating}
              text={`${homes.numberOfRatings} reviews`}
              color={"#f8e825"}
            />
          </div>
        </Card.Text>

        <Card.Text as="h3">${homes.price}</Card.Text>
      </Card.Body>
    </Card>
  );
}

export default Home;
