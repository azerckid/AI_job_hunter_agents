import os
from pathlib import Path
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

# Load environment variables
load_dotenv()

def load_resume():
    """Load the resume from knowledge directory"""
    resume_path = Path(__file__).parent / "knowledge" / "resume.txt"
    if resume_path.exists():
        return resume_path.read_text()
    else:
        raise FileNotFoundError(f"Resume not found at {resume_path}")

def main():
    print("🚀 Job Hunter Agent - Powered by Gemini")
    print("=" * 50)
    
    # Get user inputs
    position = input("\n📋 What position are you looking for? (e.g., Full Stack Developer): ").strip() or "Full Stack Developer"
    level = input("📊 What level? (e.g., Senior, Mid, Junior): ").strip() or "Senior"
    location = input("📍 What location? (e.g., Remote, Copenhagen, Denmark): ").strip() or "Remote"
    
    print(f"\n🔍 Searching for {level} {position} jobs in {location}...")
    print("=" * 50)
    
    # Configure Gemini LLM
    gemini_llm = LLM(
        model="gemini/gemini-2.0-flash-exp",
        api_key=os.getenv("GEMINI_API_KEY")
    )
    
    # Load resume as knowledge source
    resume_content = load_resume()
    resume_knowledge = StringKnowledgeSource(
        content=resume_content,
        metadata={"source": "user_resume"}
    )
    
    # Load agents from YAML
    agents_config = Path(__file__).parent / "config" / "agents.yaml"
    tasks_config = Path(__file__).parent / "config" / "tasks.yaml"
    
    # Create agents with Gemini LLM
    job_search_agent = Agent(
        config=agents_config,
        agent_name="job_search_agent",
        llm=gemini_llm
    )
    
    job_matching_agent = Agent(
        config=agents_config,
        agent_name="job_matching_agent",
        llm=gemini_llm,
        knowledge_sources=[resume_knowledge]
    )
    
    resume_optimization_agent = Agent(
        config=agents_config,
        agent_name="resume_optimization_agent",
        llm=gemini_llm,
        knowledge_sources=[resume_knowledge]
    )
    
    company_research_agent = Agent(
        config=agents_config,
        agent_name="company_research_agent",
        llm=gemini_llm
    )
    
    interview_prep_agent = Agent(
        config=agents_config,
        agent_name="interview_prep_agent",
        llm=gemini_llm
    )
    
    # Create tasks
    job_extraction_task = Task(
        config=tasks_config,
        task_name="job_extraction_task",
        agent=job_search_agent,
        context_variables={
            "position": position,
            "level": level,
            "location": location
        }
    )
    
    job_matching_task = Task(
        config=tasks_config,
        task_name="job_matching_task",
        agent=job_matching_agent,
        context=[job_extraction_task]
    )
    
    job_selection_task = Task(
        config=tasks_config,
        task_name="job_selection_task",
        agent=job_matching_agent,
        context=[job_matching_task]
    )
    
    resume_rewriting_task = Task(
        config=tasks_config,
        task_name="resume_rewriting_task",
        agent=resume_optimization_agent,
        context=[job_selection_task]
    )
    
    company_research_task = Task(
        config=tasks_config,
        task_name="company_research_task",
        agent=company_research_agent,
        context=[job_selection_task]
    )
    
    interview_prep_task = Task(
        config=tasks_config,
        task_name="interview_prep_task",
        agent=interview_prep_agent,
        context=[job_selection_task, resume_rewriting_task, company_research_task]
    )
    
    # Create crew
    crew = Crew(
        agents=[
            job_search_agent,
            job_matching_agent,
            resume_optimization_agent,
            company_research_agent,
            interview_prep_agent
        ],
        tasks=[
            job_extraction_task,
            job_matching_task,
            job_selection_task,
            resume_rewriting_task,
            company_research_task,
            interview_prep_task
        ],
        process=Process.sequential,
        verbose=True
    )
    
    # Execute the crew
    print("\n🤖 Starting AI agents workflow...")
    print("=" * 50)
    
    try:
        result = crew.kickoff()
        
        print("\n" + "=" * 50)
        print("✅ Job Hunter Agent completed successfully!")
        print("=" * 50)
        print("\n📁 Output files generated:")
        print("  - output/rewritten_resume.md")
        print("  - output/company_research.md")
        print("  - output/interview_prep.md")
        print("\n💡 Check the output directory for your personalized job application materials!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        raise


if __name__ == "__main__":
    main()
