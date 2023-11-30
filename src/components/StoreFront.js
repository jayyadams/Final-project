import React, { useState, useEffect } from "react";
import HomePlayers from "./HomePlayers";


function StoreFront({ playersArr, searchTerm }) {

    // console.log(PlayersArr)
    const [answerVisibility, setAnswerVisibility] = useState({
        answer1: false,
        answer2: false,
        answer3: false,
        answer4: false,
        answer5: false,
      });

      const toggleAnswerVisibility = (answerId) => {
        setAnswerVisibility((prevVisibility) => ({
          ...prevVisibility,
          [answerId]: !prevVisibility[answerId],
        }));
      };
    

    const filteredArr = playersArr.filter(playerobj => {
                
        return  playerobj.name && playerobj.name.toLowerCase().includes(searchTerm.toLowerCase()) || 
                playerobj.price && playerobj.price.toString().includes(searchTerm) ||
                playerobj.type && playerobj.type.toLowerCase().includes(searchTerm.toLowerCase())

                
                
    })
    

    const mappedHomePlayers = filteredArr.map((homePlayerObj) => {

        // console.log(homePlayerObj)


        return <HomePlayers
            key={homePlayerObj.id}
            name={homePlayerObj.name}
            position={homePlayerObj.position}
            pos_rank={homePlayerObj.pos_rank}
            team={homePlayerObj.team}
            avg_points={homePlayerObj.avg_points}
            price={homePlayerObj.price}
            store={homePlayerObj.store}
            img={homePlayerObj.img}
        />
            

})

    return (
        <div className="container">
        <h1 className="headerhome">Welcome to the Fantasy Football Shop! </h1>
        <ul className="jokeList">
          <li className="jokeItem">
            <p className="jokeText">
              Why don't fantasy football players ever make good detectives?
            </p>
            <button className="answerButton" onClick={() => toggleAnswerVisibility('answer1')}>
              {answerVisibility.answer1 ? 'Hide Answer' : 'Show Answer'}
            </button>
            {answerVisibility.answer1 && (
              <p className="answerText">
                Because they always struggle with finding a decent defense!
              </p>
            )}
          </li>
  
          <li className="jokeItem">
            <p className="jokeText">
              My girlfriend left me because I'm too obsessed with football.
            </p>
            <button className="answerButton" onClick={() => toggleAnswerVisibility('answer2')}>
              {answerVisibility.answer2 ? 'Hide Answer' : 'Show Answer'}
            </button>
            {answerVisibility.answer2 && (
              <p className="answerText">
                I'm absolutely gutted. I've been with her for nearly three seasons!
              </p>
            )}
          </li>
  
          <li className="jokeItem">
            <p className="jokeText">Why did the football coach go to the bank?</p>
            <button className="answerButton" onClick={() => toggleAnswerVisibility('answer3')}>
              {answerVisibility.answer3 ? 'Hide Answer' : 'Show Answer'}
            </button>
            {answerVisibility.answer3 && (
              <p className="answerText">He wanted his Quarterback.</p>
            )}
          </li>
  
          <li className="jokeItem">
            <p className="jokeText">How do you keep the Detroit Lions out of your front yard?</p>
            <button className="answerButton" onClick={() => toggleAnswerVisibility('answer4')}>
              {answerVisibility.answer4 ? 'Hide Answer' : 'Show Answer'}
            </button>
            {answerVisibility.answer4 && (
              <p className="answerText">Put up goal posts.</p>
            )}
          </li>

          <li className="jokeItem">
            <p className="jokeText">Whos going to win the superbowl this year?</p>
            <button className="answerButton" onClick={() => toggleAnswerVisibility('answer5')}>
              {answerVisibility.answer5 ? 'Hide Answer' : 'Show Answer'}
            </button>
            {answerVisibility.answer5 && (
              <p className="answerText">NOT THE GIANTS OR COWBOYS LOL</p>
            )}
          </li>
        </ul>
        <div className="front-players">
          {mappedHomePlayers}
        </div>
      </div>
    );
  }


export default StoreFront;