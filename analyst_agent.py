from dotenv import load_dotenv
from smolagents import CodeAgent
from smolagents.models import OpenAIServerModel
import os
from analyst_tools import table_metadata_loader

# Load environment variables
load_dotenv()

# Create the analyst code agent
analyst = CodeAgent(
    name="analyst",
    description="""
    A professional data analyst that can analyze and create plots to answer users' questions.
    Always use the tables mentioned in the metadata. Do not use any other data or fake data.
    If the user asks for a plot, create it and return the image.
    """,
    tools=[table_metadata_loader],
    model=OpenAIServerModel('gpt-4o-2024-08-06', api_key=os.getenv("OPENAI_API_KEY")),
    additional_authorized_imports=["pandas", "matplotlib.pyplot"]
)