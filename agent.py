
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o")
search_tool = TavilySearchResults(max_results=3)
memory = MemorySaver()

agent_executor = create_react_agent(
    model, 
    [search_tool], 
    checkpointer=memory,
    interrupt_before=["tools"] 
)