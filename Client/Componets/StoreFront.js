import React, { useState, useEffect } from "react";
import HomePlayers from "./HomePlayers";



function StoreFront({ playersArr, searchTerm }) {

    // console.log(PlayersArr)

    

    const filteredArr = playersArr.filter(playerobj => {
                
        return  playerobj.name.toLowerCase().includes(searchTerm.toLowerCase()) || playerobj.price.toString().includes(searchTerm) || playerobj.type.toLowerCase().includes(searchTerm.toLowerCase())

                
          // playerobj.quantitiy.toLowerCase().includes(searchTerm.toLowerCase()) || playerobj.store.toLowerCase().includes(searchTerm.toLowerCase()) ||  playerobj.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
                
    })
    

    const mappedHomePlayers = filteredArr.map((homePlayerObj) => {

        // console.log(homePlayerObj)


        return <HomePlayers
            key={homePlayerObj.id}
            name={homePlayerObj.name}
            pos_rank={homePlayerObj.pos_rank}
            position={homePlayerObj.position}
            team={homePlayerObj.team}
            avg_points={homePlayerObj.avg_points}
            price={homePlayerObj.price}
            store={homePlayerObj.store}
            img={homePlayerObj.img}
        />

})

    return (
        <>
            <div className="home-player-container">
                {mappedHomePlayers}
            </div>
        </>
    )
}


export default StoreFront;