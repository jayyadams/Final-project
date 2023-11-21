import React, {useState} from "react";
import StoreFront from "./StoreFront";

function HomePlayers( { description, name, price, quantity, store, type, img } ){


return (
            <div className="home-player-card">
                <div className="home-player-info">
                    <img src={img} alt = {name}/>
                    <h1>{name}</h1>
                    <h3>{type}</h3>
                    <h6>Price: ${price.toFixed(2)}</h6>
                    <p>{quantity}</p>
                    
                </div>
            </div>
)}

export default HomePlayers