"use client";
import ReactDOM from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router";

import Page from './page.tsx';
// import About from './about.tsx';
import Tutorial from './tutorial.tsx'
 
export default function App() {
   return (
      <BrowserRouter>
         <Routes>
            <Route exact path="/" element={<Page/>} />
            <Route path="/home" element={<Page/>} />
            {/* <Route path="/About us" element={<About/>} /> */}
            <Route path="/tutorial" element={<Tutorial/>} />
         </Routes>
      </BrowserRouter>
   );
};

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(<App />);