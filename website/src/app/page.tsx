
// import Topnav from "@/Components/Topnav/topnav"; 

// import "./topnav.style.css";
// import"./image.style.css";
// import xx from './pictures/Picture.png';

// export default function Page() {
//   return (
//     <div>
//       <div className="topnav">
//         <Topnav />
//       </div>
//         <img src={xx.src} alt="Big robot photo" className="imgstyle"/>
//     </div>
//   );
// };

"use client";

import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router";

import"./image.style.css";
import xx from './pictures/Picture.png';

import About from './about';
import Tutorial from './tutorial'

import "./topnav.style.css";
import Topnav from '../Components/Topnav/topnav';

function Page() {
  return (<>
    <img src={xx.src} alt="Big robot photo" className="imgstyle"/>
  </>);
};
 
export default function App() {
   return (
      <BrowserRouter>
         <Topnav />
         <div>
            <Routes>
               <Route path="/" element={<Page/>} />
               <Route path="/home" element={<Page/>} />
               <Route path="/aboutus" element={<About/>} />
               <Route path="/tutorial" element={<Tutorial/>} />
            </Routes>
         </div>
      </BrowserRouter>
   );
};