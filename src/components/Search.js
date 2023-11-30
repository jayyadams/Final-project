import React, {useState, useEffect} from "react";

function Search({ setSearchTerm, playersArr }){
    



      return(
        <input className="search-bar"
        type="text" 
        name="searchBar" 
        placeholder="Search..." 
        onChange={e=>setSearchTerm(e.target.value)}/>
    )
}

export default Search;