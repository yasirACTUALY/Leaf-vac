
import Topnav from "@/Components/Topnav/topnav"; 


// import 
import "./topnav.style.css";
import"./image.style.css";
import xx from './pictures/Picture.png';

export default function Page() {
  return (
    <div>
      <div className="topnav">
        <Topnav />
      </div>
        <img src={xx.src} alt="Big robot photo" className="imgstyle"/>
    </div>
  );
};
