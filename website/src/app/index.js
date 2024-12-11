import React from "react";
import ReactDOM from "react-dom/client";
import App from "./routing"; // Import your main App component
// import "./index.css"; // Import global styles (optional)

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <BrowserRouter>
    <App />
    </BrowserRouter>
);
