import React, {useState} from "react";
import StoreFront from "./StoreFront";

function HomePlayers( { team, name, price, avg_points, store, pos_rank, img, position } ){


return (
            <div className="home-container">
                <div className="home-player-info">
                    <img className="player-img" src={img} alt = {name}/>
                    <h1>{name}</h1>
                    <h3>{position}</h3>
                    <p>{pos_rank}</p>
                    <p>{team}</p>
                    <p>{avg_points}</p>
                    <h6>Price: ${price.toFixed(2)}</h6>
                    
                </div>
            </div>
)}

export default HomePlayers