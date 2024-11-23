export default function Topnav() {
  return (<>
    <div className="topnav">
      <a className="active" href = "#home">Graspy</a>
      <a className="active" href="#home">Home</a>
      <a href="#tutorial">How it Works</a>
      <a href="design process">Design Process</a>
  
      <div className="topnav-right">
  
        <div className="dropdown">
          <button className="dropbtn">About
            <i className="fa fa-caret-down"></i>
          </button>
          <div className="dropdown-content">
            <a href="contact">Contact us</a>
            <a href="aboutus">About Us</a>
            <a href="#FAQ">FAQ</a>
          </div>
        </div>
        <a href="#search">Search</a>

      </div>
    </div>
  </>);
}
  