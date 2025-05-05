document.addEventListener("DOMContentLoaded", function() {
    const collapsibles = document.querySelectorAll(".collapsible");

    collapsibles.forEach(button => {
        button.addEventListener("click", function() {
            // Toggle the active class and show/hide the content
            const content = this.nextElementSibling;
            content.style.display = content.style.display === "block" ? "none" : "block";
            this.classList.toggle("active");
        });
    });
});
