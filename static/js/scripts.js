document.addEventListener(
    "DOMContentLoaded",
    function () {


        const intro =
            document.getElementById("intro");


        const website =
            document.getElementById("website");


        const enterButton =
            document.getElementById("enter-button");


        const music =
            document.getElementById("music");


        const musicButton =
            document.getElementById("music-button");


        let musicPlaying = false;



        // ==========================================
        // ENTER WEBSITE
        // ==========================================

        enterButton.addEventListener(
            "click",
            function () {   


                // Sembunyikan intro

                intro.classList.add("hide");


                // Tampilkan website

                website.classList.remove("hidden");


                // Mainkan musik

                if (music) {

                    music.volume = 0.55;


                    music.play()
                        .then(function () {

                            musicPlaying = true;

                            musicButton.innerHTML =
                                "🎵";

                        })
                        .catch(function () {

                            musicPlaying = false;

                        });

                }


                // Hujan hati

                createHearts(25);


            }
        );



        // ==========================================
        // MUSIC BUTTON
        // ==========================================

        musicButton.addEventListener(
            "click",
            function () {


                if (!music) {
                    return;
                }


                if (musicPlaying) {


                    music.pause();


                    musicPlaying = false;


                    musicButton.innerHTML =
                        "🔇";


                }

                else {


                    music.play()
                        .then(function () {

                            musicPlaying = true;

                            musicButton.innerHTML =
                                "🎵";

                        });


                }

            }
        );



        // ==========================================
        // HEART PARTICLES
        // ==========================================

        setInterval(
            function () {

                if (
                    !website.classList.contains(
                        "hidden"
                    )
                ) {

                    createHearts(1);

                }

            },
            3000
        );


    }
);



// ==============================================
// CREATE HEARTS
// ==============================================

function createHearts(amount) {


    for (
        let i = 0;
        i < amount;
        i++
    ) {


        const heart =
            document.createElement("div");


        heart.className =
            "heart-particle";


        heart.innerHTML =
            Math.random() > .5
                ? "❤️"
                : "♡";


        heart.style.left =
            Math.random() * 100 + "vw";


        heart.style.fontSize =
            (
                12 +
                Math.random() * 22
            ) + "px";


        heart.style.animationDuration =
            (
                5 +
                Math.random() * 5
            ) + "s";


        heart.style.opacity =
            .4 +
            Math.random() * .5;


        document.body.appendChild(
            heart
        );


        setTimeout(
            function () {

                heart.remove();

            },
            11000
        );


    }

}