import React, {useState, useEffect}from "react";

function Search({ setSearchTerm }){

    // const handleChange = (e) => {
    //     setSearchTerm(e.target.value);
    
    //     onSearch(e.target.value);
    //   }
    
    //   const handleSubmit = (e) => {
    //     e.preventDefault();
    //     onSearch(searchTerm);
    //   }
    
    
      return(
        <input className="searcher"
        type="text" 
        name="searchBar" 
        placeholder="Search..." 
        onChange={e=>setSearchTerm(e.target.value)}/>
    )
}

export default Search;