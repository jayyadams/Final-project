import React, {useEffect} from "react";

function Checkout({items }) {

    useEffect(() => {
        // Update the volume when the component mounts
        const audio = document.getElementById("backgroundMusic");
        audio.volume = 0.5; // Adjust the volume as needed
      }, []);

    return (
    <div align='center'>
        <img src="/images/cart.gif" />
        <h2>Stretch goals were not hit during this presentation 😭 </h2>
        <p>{items}</p>
        <audio id="backgroundMusic" autoPlay loop>
            <source src="/Depression.mp3" type="audio/mp3" />
        </audio>
    </div>
)}

export default Checkout