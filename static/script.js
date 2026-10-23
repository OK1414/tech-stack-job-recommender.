
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const skillsInput = document.querySelector("#skills");
    const submitButton = form?.querySelector('button[type="submit"]');

    if (!form || !skillsInput || !submitButton) {
        return;
    }

    // Create a small helper message below the input.
    const message = document.createElement("p");
    message.className = "input-message";
    message.setAttribute("aria-live", "polite");
    skillsInput.insertAdjacentElement("afterend", message);

    // Add quick skill suggestions.
    const suggestions = [
        "Python",
        "SQL",
        "JavaScript",
        "React",
        "Node.js",
        "Excel",
        "Power BI"
    ];

    const suggestionSection = document.createElement("div");
    suggestionSection.className = "suggestions";

    const suggestionTitle = document.createElement("p");
    suggestionTitle.textContent = "Popular skills — click to add";

    const suggestionList = document.createElement("div");
    suggestionList.className = "suggestion-list";

    suggestions.forEach((skill) => {
        const skillButton = document.createElement("button");

        skillButton.type = "button";
        skillButton.className = "suggestion-button";
        skillButton.textContent = `+ ${skill}`;

        skillButton.addEventListener("click", () => {
            const currentSkills = skillsInput.value
                .split(",")
                .map((item) => item.trim())
                .filter(Boolean);

            const alreadyAdded = currentSkills.some(
                (item) => item.toLowerCase() === skill.toLowerCase()
            );

            if (alreadyAdded) {
                showMessage(`${skill} is already in your list.`);
                return;
            }

            currentSkills.push(skill);
            skillsInput.value = currentSkills.join(", ");
            showMessage(`${skill} added.`);
            skillsInput.focus();
        });

        suggestionList.appendChild(skillButton);
    });

    suggestionSection.append(suggestionTitle, suggestionList);
    skillsInput.closest("form").appendChild(suggestionSection);

    // Show feedback under the input.
    function showMessage(text, isError = false) {
        message.textContent = text;
        message.classList.toggle("error", isError);
        message.classList.add("visible");
    }

    // Normalize the input and remove duplicate skills.
    form.addEventListener("submit", (event) => {
        const enteredSkills = skillsInput.value
            .split(",")
            .map((skill) => skill.trim())
            .filter(Boolean);

        if (enteredSkills.length === 0) {
            event.preventDefault();
            showMessage("Please enter at least one skill.", true);
            skillsInput.focus();
            return;
        }

        const uniqueSkills = [
            ...new Map(
                enteredSkills.map((skill) => [
                    skill.toLowerCase(),
                    skill
                ])
            ).values()
        ];

        skillsInput.value = uniqueSkills.join(", ");

        submitButton.disabled = true;
        submitButton.textContent = "Finding your matches...";

        // The browser submits the form to Flask after this handler.
    });

    // Clear the field with Escape when it is focused.
    skillsInput.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            skillsInput.value = "";
            showMessage("Skills cleared.");
        }
    });

    // Remove the warning when the user starts editing.
    skillsInput.addEventListener("input", () => {
        message.textContent = "";
        message.classList.remove("visible", "error");
    });
});
