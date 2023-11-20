import React from "react";
import "./ResultWindow.css";

const ResultWindow = ({ result }) => {
  return (
    <div className="result-window">
      <h3>{result.Title}</h3>
      <p>Author: {result.Author}</p>
      <p>Price: {result.Price}</p>
      <p>{result.Availability}</p>
      <a href={result.Link} target="_blank" rel="noopener noreferrer">
        View Details
      </a>
    </div>
  );
};

export default ResultWindow;
