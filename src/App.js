import React from "react";
import Form from "./components/Form";

function App() {
  const handleSearch = (searchData) => {
    // Process the search data (bookName and author) here
    console.log("Search Data:", searchData);
  };

  return (
    <div className="App">
      <Form onSearch={handleSearch} />
    </div>
  );
}

export default App;
