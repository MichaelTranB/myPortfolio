//Typing Animation
document.addEventListener("DOMContentLoaded", function() {
    const lines = document.querySelectorAll(".typing-effect .line");
    
    let delay = 0;
    let typingDuration = 40;  // Time per character
    
    lines.forEach((line, index) => {
        let content = line.getAttribute('data-content');
        let length = content.length;
        line.textContent = "";

        setTimeout(() => {
            line.classList.remove("active-cursor");
            line.classList.add("solid-cursor");  

            let typeDelay = 0;
            for (let i = 0; i < length; i++) {
                setTimeout(() => {
                    line.textContent += content[i];

                    if (i === length - 1) {
                       
                        if (index !== lines.length - 1) {
                            setTimeout(() => {
                                line.classList.remove("solid-cursor");
                                lines[index + 1].classList.add("active-cursor"); 
                            }, typingDuration);
                        } else {
                            line.classList.add("active-cursor");
                        }
                    }
                }, typeDelay);
                typeDelay += typingDuration;
            }
        }, delay);
        delay += length * typingDuration + 400;  // Adding a pause after each line
    });
});




