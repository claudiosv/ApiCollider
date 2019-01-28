

import React, { Component } from 'react';
import { Card, CardImg, CardText, CardBody,
CardTitle, CardSubtitle, Button } from 'reactstrap';

class ApiCard extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <Card>
          <CardBody>
            <CardTitle>{this.props.title}</CardTitle>
            <CardText>{this.props.description}</CardText>
          </CardBody>
        </Card>
      </div>
    );
  }
}

export default ApiCard;
