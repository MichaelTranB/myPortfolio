//Typing Animation
document.addEventListener("DOMContentLoaded", function() {
    const lines = document.querySelectorAll(".typing-effect .line");
    let delay = 0;
    const typingDuration = 40; // Adjust for typing speed
    const cursorClass = 'active-cursor'; // Cursor class to toggle

    function typeLine(line, content, index) {
        let i = 0;
        function type() {
            if (i < content.length) {
                line.textContent += content.charAt(i);
                i++;
                setTimeout(type, typingDuration);
            } else {
                // Remove cursor from the current line
                line.classList.remove(cursorClass);
                // Only add cursor to the next line if not the last line; otherwise, re-add the cursor to the last line
                if (index < lines.length - 1) {
                    lines[index + 1].classList.add(cursorClass);
                } else {
                    // This ensures the cursor remains on the last line
                    line.classList.add(cursorClass);
                }
            }
        }
        setTimeout(type, delay);
        delay += content.length * typingDuration + 500; // Adjust delay for the next line
    }

    // Initially add the cursor class to the first line
    if (lines.length > 0) {
        lines[0].classList.add(cursorClass);
    }

    lines.forEach((line, index) => {
        const content = line.getAttribute('data-content');
        line.textContent = ""; // Clear the line before typing
        typeLine(line, content, index);
    });
});
