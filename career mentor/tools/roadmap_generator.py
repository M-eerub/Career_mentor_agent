def get_career_roadmap(career):
    roadmaps = {
        "Data Scientist": ["📊 Python", "📈 Pandas", "🤖 Machine Learning", "🗃 SQL"],
        "Web Developer": ["🌐 HTML", "🎨 CSS", "⚙️ JavaScript", "⚛ React", "🖥 Node.js"],
        "UI/UX Designer": ["🖌 Figma", "📐 Wireframing", "🔍 User Research"]
    }
    return roadmaps.get(career, ["❌ No roadmap found for this career"])
