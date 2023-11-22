import React from "react";
import PlayerDetails from "./PlayerDetails";
import StoreFront from "./StoreFront";
// import Cart from "./Cart";

function Inventory({ playersArr }) {

    const mappedPlayersArr = playersArr.map((player) => {
        return <playerDetails
            key={player.id}
            pId={player.id}
            name={player.name}
            position={player.position}
            pos_rank={player.pos_rank}
            team={player.team}
            avg_points={player.avg_points}
            price={player.price}
            store={player.store}
            img={player.img}
        />
    }
    )
    return (
        <div>
            <div className="card-container">
                {mappedPlayersArr}
            </div>
        </div>
    )
}

export default Inventory