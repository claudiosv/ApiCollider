import React, { Component } from "react";
import {
  Container,
  Button,
  Col,
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  UncontrolledDropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem
} from "reactstrap";
import Collider from "./Collider";

class App extends Component {
  render() {
    // let colliders = [];
    // for(let i = 0; i < 25; i++)
    // {
    //   colliders.push(<Collider key={i} />);
    // }
    return (
      <div>
        <div>
          <Navbar color="white" light expand="md">
            <NavbarBrand href="/">
              <img height="50px" src="apicollider_logo.png" />
            </NavbarBrand>
            <NavbarToggler onClick={this.toggle} />
            <Collapse navbar>
              {/* isOpen={this.state.isOpen}  */}
              {/* <Nav className="ml-auto" navbar>
                <NavItem>
                  <NavLink href="/components/">Components</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink href="https://github.com/reactstrap/reactstrap">
                    GitHub
                  </NavLink>
                </NavItem>
                <UncontrolledDropdown nav inNavbar>
                  <DropdownToggle nav caret>
                    Options
                  </DropdownToggle>
                  <DropdownMenu right>
                    <DropdownItem>Option 1</DropdownItem>
                    <DropdownItem>Option 2</DropdownItem>
                    <DropdownItem divider />
                    <DropdownItem>Reset</DropdownItem>
                  </DropdownMenu>
                </UncontrolledDropdown>
              </Nav> */}
            </Collapse>
          </Navbar>
        </div>
        <Container>
          {/* {colliders} */}
          <Collider />
        </Container>
      </div>
    );
  }
}

export default App;
