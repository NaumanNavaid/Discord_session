from agents import Runner, set_tracing_disabled 
from dotenv import load_dotenv
import os
from my_config.gemini_config import run_config
from useable_agents.my_agents import supervisor_agent, math_agent, next_js_agent, python_agent

# Load environment variables
load_dotenv()
set_tracing_disabled(True)

prompt= input("Enter your prompt: ")

response= Runner.run_sync(
    starting_agent=supervisor_agent,\
    run_config=run_config,
    input=prompt
  ,
    )

print(response.final_output)