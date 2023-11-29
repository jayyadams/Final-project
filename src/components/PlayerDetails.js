import { useState } from "react";
import React from "react";


function PlayerDetails({ team, name, price, avg_points, pos_rank, position, img, }) {


    const [isFlipped, setIsFlipped] = useState(false);
    const [inCart, setInCart] = useState(false);

    const flipCard = () => {
        setIsFlipped(!isFlipped)
    }

    const cardToggle = isFlipped ? "flipped" : '';

    const addToCart = () => {
        setInCart(!inCart);

    }
    

    return (
        <div className={`card ${cardToggle}`} onClick={flipCard}>
            <div className="card-inner">
                <div className="card-front">
                    <img src={img} alt={name} />
                    <h2>{name}</h2>
                </div>
                <div className="card-back">
                    <p>{name}</p>
                    <h5>{position}</h5>
                    <p>{pos_rank}</p>
                    <p>{avg_points}</p>
                    <p>{team}</p>
                    <p>price: ${price.toFixed(2)}</p>
                    {inCart ? (
                        <button onClick={addToCart}>Remove from Cart</button>
                    ) : (
                        <button onClick={addToCart}>Add to Cart</button>
                    )}
                </div>
            </div>
        </div>
            );
}


export default PlayerDetails