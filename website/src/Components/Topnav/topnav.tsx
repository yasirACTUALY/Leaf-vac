import { Link } from "react-router";

export default function Topnav() {
  return (
    <>
      <div className="topnav">
        <Link className="active" to="/">Graspy</Link>
        {/* <Link className="active" to="/">Home</Link> */}
        <Link to="/tutorial">How it Works</Link>
        <Link to="/design-process">Design Process</Link>

        <div className="topnav-right">
          <div className="dropdown">
            <button className="dropbtn">
              About
              <i className="fa fa-caret-down"></i>
            </button>
            <div className="dropdown-content">
              <Link to="/contact">Contact Us</Link>
              <Link to="/aboutus">About Us</Link>
              <Link to="/faq">FAQ</Link>
            </div>
          </div>
          <Link to="/search">Search</Link>
        </div>
      </div>
    </>
  );
}
