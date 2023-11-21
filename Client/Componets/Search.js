import React, {useState, useEffect}from "react";

function Search({ playersArr, setSearchTerm}){


    
    return(
        <input className="searcher"
        type="text" 
        name="searchBar" 
        placeholder="Search..." 
        onChange={e=>setSearchTerm(e.target.value)}/>
    )
}

export default Search;