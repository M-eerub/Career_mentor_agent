from termcolor import colored
import colorama
colorama.init()
from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent

def print_title(text):
    print(colored(f"\n💼 {text} 💼", 'cyan', attrs=['bold']))

def print_section(title, items, emoji):
    print(colored(f"\n{emoji} {title}", 'green', attrs=['bold']))
    for item in items:
        print(colored(f"   ➤ {item}", 'yellow'))

def main():
    print(colored("👋 Welcome to your Personal Career Mentor CLI!", 'magenta', attrs=['bold']))
    interest = input(colored("\n✨ What are your interests? ", 'blue', attrs=['bold']))

    # CareerAgent
    print_title("Analyzing Your Interests...")
    career = CareerAgent(interest)
    print(colored(f"🔍 Suggested Career Path: {career}", 'cyan', attrs=['bold']))

    # SkillAgent
    print_title("Building Your Skill Roadmap...")
    skills = SkillAgent(career)
    print_section("Recommended Skills", skills, "🧠")

    # JobAgent
    print_title("Exploring Real-World Opportunities...")
    jobs = JobAgent(career)
    print_section("Job Roles", jobs, "🚀")

    print(colored("\n✅ Done! Start learning and chase your dream career! 🚀", 'green', attrs=['bold']))

if __name__ == "__main__":
    main()
