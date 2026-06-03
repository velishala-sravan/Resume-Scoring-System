function analyzeResume() {

    const file = document.getElementById("resume").files[0];
    const jd = document.getElementById("jobDescription").value;

    if (!file || jd.trim() === "") {
        alert("Please upload a resume and enter a job description.");
        return;
    }

    document.getElementById("result").classList.remove("hidden");

    // Dummy frontend data
    const score = 82;

    const matched = [
        "Python",
        "SQL",
        "Machine Learning",
        "Flask",
        "AWS"
    ];

    const missing = [
        "Docker",
        "Kubernetes",
        "Terraform"
    ];

    const suggestions = [
        "Add Docker-related projects.",
        "Mention Kubernetes deployment experience.",
        "Include more cloud technologies."
    ];

    document.getElementById("score").innerText = score + "%";

    const matchedList = document.getElementById("matchedSkills");
    const missingList = document.getElementById("missingSkills");
    const suggestionList = document.getElementById("suggestions");

    matchedList.innerHTML = "";
    missingList.innerHTML = "";
    suggestionList.innerHTML = "";

    matched.forEach(skill => {
        matchedList.innerHTML += `<li>✅ ${skill}</li>`;
    });

    missing.forEach(skill => {
        missingList.innerHTML += `<li>❌ ${skill}</li>`;
    });

    suggestions.forEach(item => {
        suggestionList.innerHTML += `<li>${item}</li>`;
    });
}