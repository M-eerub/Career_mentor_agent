def JobAgent(career):
    jobs = {
        "Data Scientist": [
            "Data Scientist",
            "Machine Learning Engineer",
            "AI Analyst"
        ],
        "Web Developer": [
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Engineer"
        ],
        "UI/UX Designer": [
            "UX Researcher",
            "UI Designer",
            "Product Designer"
        ]
    }
    return jobs.get(career, ["No job roles found"])
