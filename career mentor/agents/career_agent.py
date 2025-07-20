def CareerAgent(user_input):
    # You can expand this later using OpenAI API if needed
    if "data" in user_input.lower():
        return "Data Scientist"
    elif "design" in user_input.lower():
        return "UI/UX Designer"
    else:
        return "Web Developer"
