import React, {useState, useEffect}from "react";

function Search({ playersArr, setSearchTerm, }){

    // const handleSubmit = (e) => {
    //     e.preventDefault();
    //     onSearch(searchText);
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