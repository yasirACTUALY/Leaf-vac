export default function Topnav() {
  return (<>
    <div className="topnav">
      <a className="active" href = "#home">Graspy</a>
      <a className="active" href="#home">Home</a>
      <a href="#news">News</a>
      <a href="#contact">Contact</a>
  
      
        
        {/* <div className = "topnav.dropbtn">
          <a href="#about">About</a>
        </div> */}
      
      <div className="topnav-right">
        
        <div className="dropdown">
          <button className="dropbtn">About
            <i className="fa fa-caret-down"></i>
          </button>
          <div className="dropdown-content">
            <a href="#">Contact us</a>
            <a href="#">About Us</a>
            <a href="#">FAQ</a>
          </div>
        </div>
        <a href="#search">Search</a>

      </div>
    </div>
  </>);
}
  