import os
import dotenv
from pathlib import Path

dotenv.load_dotenv()

from crewai import Crew, Agent, Task
from crewai.project import CrewBase, task, agent, crew
from models import JobList, RankedJobList, ChosenJob
from tools import web_search_tool

@CrewBase
class JobHunterCrew:

    @agent
    def job_search_agent(self):
        return Agent(
            config=self.agents_config["job_search_agent"],
            tools=[web_search_tool],
        )

    @agent
    def job_matching_agent(self):
        return Agent(config=self.agents_config["job_matching_agent"])

    @agent
    def resume_optimization_agent(self):
        return Agent(config=self.agents_config["resume_optimization_agent"])

    @agent
    def company_research_agent(self):
        return Agent(config=self.agents_config["company_research_agent"])

    @agent
    def interview_prep_agent(self):
        return Agent(config=self.agents_config["interview_prep_agent"])

    @task
    def job_extraction_task(self):
        return Task(
            config=self.tasks_config["job_extraction_task"],
            output_pydantic=JobList,
        )

    @task
    def job_matching_task(self):
        return Task(
            config=self.tasks_config["job_matching_task"],
            output_pydantic=RankedJobList,
            output_file="output/ranked_jobs.json",
        )

    @task
    def job_selection_task(self):
        return Task(
            config=self.tasks_config["job_selection_task"],
            output_pydantic=ChosenJob,
            output_file="output/chosen_job.json",
        )

    @task
    def resume_rewriting_task(self):
        return Task(
            config=self.tasks_config["resume_rewriting_task"],
            context=[
                self.job_selection_task(),
            ],
        )

    @task
    def company_research_task(self):
        return Task(
            config=self.tasks_config["company_research_task"],
            context=[
                self.job_selection_task(),
            ],
        )

    @task
    def interview_prep_task(self):
        return Task(
            config=self.tasks_config["interview_prep_task"],
            context=[
                self.job_selection_task(),
                self.resume_rewriting_task(),
                self.company_research_task(),
            ],
        )

    @crew
    def crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )


def main():
    print("🚀 Job Hunter Agent - Powered by Gemini")
    print("=" * 50)
    
    # Read resume content
    try:
        resume_path = Path("resume.txt")
        if not resume_path.exists():
             # Fallback to knowledge/resume.txt if needed
             resume_path = Path("knowledge/resume.txt")
        
        if resume_path.exists():
            resume_content = resume_path.read_text()
            print("✅ Resume loaded successfully!")
        else:
            raise FileNotFoundError("Could not find resume.txt or knowledge/resume.txt")
            
    except Exception as e:
        print(f"❌ Error reading resume: {e}")
        return

    # Get user inputs
    position = input("\n📋 What position are you looking for? (e.g., Full Stack Developer): ").strip() or "Full Stack Developer"
    level = input("📊 What level? (e.g., Senior, Mid, Junior): ").strip() or "Senior"
    location = input("📍 What location? (e.g., Remote, Copenhagen, Denmark): ").strip() or "Remote"
    
    print(f"\n🔍 Searching for {level} {position} jobs in {location}...")
    print("=" * 50)
    print("\n🤖 Starting AI agents workflow...")
    print("=" * 50)
    
    try:
        # Execute the crew with inputs
        result = JobHunterCrew().crew().kickoff(
            inputs={
                "position": position,
                "level": level,
                "location": location,
                "resume_content": resume_content,
            }
        )
        
        print("\n" + "=" * 50)
        print("✅ Job Hunter Agent completed successfully!")
        print("=" * 50)
        print("\n📁 Output files generated:")
        print("  - output/ranked_jobs.json")
        print("  - output/chosen_job.json")
        print("  - output/rewritten_resume.md")
        print("  - output/company_research.md")
        print("  - output/interview_prep.md")
        print("\n💡 Check the output directory for your personalized job application materials!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        raise


if __name__ == "__main__":
    main()
