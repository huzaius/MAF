document.addEventListener("DOMContentLoaded", () => {
  // --- DOM Elements ---
  const sortDropdown = document.getElementById("sort-dropdown");
  const sortButton = document.getElementById("sort-button");
  const themeIconContainer = document.getElementById("theme-icon-container");
  const htmlTag = document.documentElement;
  const askQuestionForm = document.getElementById("ask-question-form");

  // --- Event Listeners ---
  if (sortDropdown) {
    sortDropdown.addEventListener("click", (e) => {
      if (e.target.tagName === "A" && e.target.dataset.sort) {
        e.preventDefault();
        const criteria = e.target.dataset.sort;
        // Update button text
        sortButton.textContent = `Sort by: ${e.target.textContent}`;
        // Create URL and navigate for server-side sorting
        const currentUrl = new URL(window.location);
        currentUrl.searchParams.set('sort', criteria);
        window.location.href = currentUrl.href;
        
        if (document.activeElement) document.activeElement.blur();
      }
    });
  }

  if (themeIconContainer) {
    themeIconContainer.addEventListener("click", (e) => {
      const button = e.target.closest(".theme-btn");
      if (button && button.dataset.themeValue) {
        const theme = button.dataset.themeValue;
        htmlTag.setAttribute("data-theme", theme);
        // Persist theme choice
        localStorage.setItem('theme', theme);
      }
    });
  }

  if (askQuestionForm) {
    askQuestionForm.addEventListener("submit", (e) => {
      e.preventDefault();
      // This is client-side for demonstration.
      // In a real app, this would be an HTMX POST request.
      const title = document.getElementById("modal-title").value;
      const body = document.getElementById("modal-body").value;

      if (title && body) {
        console.log("New Question Submitted (client-side):", { title, body });
        askQuestionForm.parentElement.parentElement.close(); // Close modal
        askQuestionForm.reset();
        // Reload the page to see the new question (in a real app, HTMX would handle this)
        window.location.reload();
      } else {
        alert("Please fill out all fields.");
      }
    });
  }
});
