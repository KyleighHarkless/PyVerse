from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from tools import search_tool, handle_tool_errors
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool
from langchain_core.messages import ToolMessage
from langchain.agents.middleware import wrap_tool_call


search = DuckDuckGoSearchRun()

@tool
def search_tool(query: str) -> str:
    """Use DuckDuckGo to search for recent information."""
    results = search.run(query)
    return f"Results for:  {results}"

@wrap_tool_call
def handle_tool_errors(request, handler):
    """Handle tool execution errors with custom messages."""
    try:
        return handler(request)
    except Exception as e:
        # Return a custom error message to the model
        return ToolMessage(
            content=f"Tool error: Please check your input and try again. ({str(e)})",
            tool_call_id=request.tool_call["id"]
        )

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
)
    
agent = create_agent(
    model, 
    tools=[search_tool],
    middleware=[handle_tool_errors],
    system_prompt="You are an intelligent " \
    "assistant that provides accurate information."
)

question = input("Enter your question: ")

for chunk in agent.stream({"messages": [{"role": "user", "content": "why sky blue?"}]}, stream_mode="updates"):
    print(chunk)