import React, { useState } from "react";
import Form from "./components/Form";
import ResultWindow from "./components/ResultWindow";

function App() {
  const [searchResults, setSearchResults] = useState([]);

  const handleSearch = (results) => {
    setSearchResults(results);
  };

  return (
    <div className="App">
      <Form onSearch={handleSearch} />
      {searchResults.map((result, index) => (
        <ResultWindow key={index} result={result} />
      ))}
    </div>
  );
}

export default App;
