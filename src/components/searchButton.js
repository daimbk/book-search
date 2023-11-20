import React from 'react';

const SearchButton = ({ onClick }) => {
  return (
    <button onClick={onClick} type="button">
      Search
    </button>
  );
};

export default SearchButton;
