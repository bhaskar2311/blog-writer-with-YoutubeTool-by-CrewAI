from crewai import Agent
from tools import yt_tool


## Create a Senior Blog Content Researcher

blog_researcher = Agent(
    role = "Blog Researcher from Youtube Videos",
    goal = "Get the relevant video contnwet for the topic{topic} from Youtube Channel",
    verbose = True,
    memory = True,
    backstory = (
        "Expert in understanding in AI in Data Science, Machine Learning and GEN AI and providing suggestions."
    ),
    tools = [yt_tool],
    allow_delegation=True
)

## Create a Senior Blog Writer Agent with Youtube Tool

blog_writer = Agent(
    role = "Tech Blog Writer",
    goal = "Narrate compelling tech stories about the video {topic} from Youtube Channel",
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner."
    ),
    tools = [yt_tool],
    allow_delegation=False
)



