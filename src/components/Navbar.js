import React, { useState, useContext } from "react";
import { NavLink } from "react-router-dom";
import Search from "./Search";
import { SearchContext } from "../Helpers/Context";

function Navbar({ playersArr, storeLogged }) {

  const [toggle, setToggle] = useState(true)
  const [searchToggle, setToggleSearch] = useState(false)
  const {SearchTerm, setSearchTerm} = useContext(SearchContext)

  function toggleNav(e) {
    e.preventDefault()
    setToggle(!toggle)
    console.log('clicked')
  }
  function toggleSearch(e) {
    e.preventDefault()
    setToggleSearch(!searchToggle)
    console.log('clicked')
  }


  const nav = (toggle ? <button className="tool-button" id="navButton" onClick={toggleNav}>ToolBar</button> :
    <nav id="navbar" >
      <div className="navbar">
        <button id="closebtn" onClick={toggleNav}>X</button>
        <NavLink className='link' to="/" activeClassName="active">Home</NavLink>
        <NavLink className='link' to="/Players" activeClassName="active" >Players</NavLink>
        <NavLink className='link' to="/About" activeClassName="active" >About</NavLink>
        {storeLogged &&
        <NavLink className='link' to="/customers" activeClassName="active" >Clients</NavLink>}
      </div>
    </nav>)

 
  return (
    
      <div id="navarea">
        <button className="login-butt" onClick={toggleSearch}>Search</button>
        {searchToggle ? <Search setSearchTerm={setSearchTerm} playersArr={playersArr} /> : null}
        {nav}
      </div>
    
  );
}

export default Navbar;