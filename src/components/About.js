import React, {useEffect} from "react";

function About() {

    useEffect(() => {
        // Update the volume when the component mounts
        const audio = document.getElementById("backgroundMusic");
        audio.volume = 0.5; // Adjust the volume as needed
      }, []);


    return (
    <div className="about-div">
      {/* Add the audio element for background music */}
      <audio id="backgroundMusic" autoPlay loop>
        <source src="/background-music.mp3" type="audio/mp3" />
      </audio>

      <img src="https://patch.com/img/cdn20/users/22982853/20180201/090232/styles/raw/public/processed_images/eagles-1517492978-5068.jpg" alt="Eagles" />
      <h1>Thats it!!!!</h1>
    </div>
  );
}


export default About;