import React, { Component } from "react";
import { Button } from "reactstrap";
import ApiCard from "./ApiCard";
import { Container, Row, Col } from "reactstrap";

class Collider extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: {
        left: { title: "", description: "" },
        right: { title: "", description: "" }
      }
    };
  }

  componentDidMount() {
    this.refreshData();
  }

  refreshData = () => {
    fetch("api/collide", {
      mode: "cors",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      }
    })
      .then(results => results.json())
      .then(data => {
        this.setState({
          data: data
        });
        console.log("state", this.state);
      });
  };

  render() {
    return (
      <Row style={{ paddingTop: 50 + "px", paddingBottom: 20 }}>
        <Col sm="5">
          <ApiCard
            title={this.state.data.left.title}
            description={this.state.data.left.description}
          />
        </Col>
        <Col sm="2" className="text-center">
          <h1 style={{ paddingTop: "30px" }}>💥</h1>
        </Col>
        <Col sm="5">
          <ApiCard
            title={this.state.data.right.title}
            description={this.state.data.right.description}
          />
        </Col>
        <Col sm={{ size: 2, offset: 5 }}>
          <button
            className="buttonmain"
            color="primary"
            onClick={this.refreshData}
          >
            Refresh
          </button>
        </Col>
      </Row>
    );
  }
}
/*
<div className="App">



  <header className="App-header">
    <h1>{this.state.data.left.title} </h1>
    <p></p>
  </header>
  <button onClick={this.refreshData}>Refresh</button>
  <Button color="danger">Danger!</Button>
  <h1>{this.state.data.right.title} </h1>
  <p>{this.state.data.right.description}</p>
</div>
*/

export default Collider;
