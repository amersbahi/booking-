      // script.js
      document.addEventListener("DOMContentLoaded", function() {
        // Text to be animated
        var textToAnimate = "إرتاح في بيتك ودكتورك بكون عندك";
     
        // Function to perform the typing animation
        function typeText() {
            var index = 0;
            var typingInterval = setInterval(function() {
                document.querySelector('.typing-text').textContent += textToAnimate[index];
                index++;
     
                // Stop the interval when the entire text is typed
                if (index === textToAnimate.length) {
                    clearInterval(typingInterval);
     
     
                }
            }, 100); // Adjust the interval duration for typing speed
        }
     
        // Trigger the typing animation when the page loads
        window.onload = function() {
            typeText();
        };
     });

     