import React, { useState } from "react";
import "./Form.css";

const Form = ({ onSearch }) => {
  const [bookName, setBookName] = useState("");
  const [author, setAuthor] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch({ bookName, author });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Book Name
        <input
          type="text"
          value={bookName}
          onChange={(e) => setBookName(e.target.value)}
        />
      </label>
      <label>
        Author
        <input
          type="text"
          value={author}
          onChange={(e) => setAuthor(e.target.value)}
        />
      </label>
      <button type="submit">Search</button>
    </form>
  );
};

export default Form;
