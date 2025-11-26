from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel,Field
load_dotenv()


from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

class Source(BaseModel):
    """Scheme for a source used by the agent"""
    url:str = Field(description="the url of the response")

class AgentResponse(BaseModel):
    """scheme for the agent response"""
    answer:str = Field(description="the agent answer to the query")
    sources:List[Source] = Field(default_factory=list,description="list of sources used to generate the answer")
tavily = TavilyClient()

@tool
def search(query:str)->str:
    """
    Tool that search over internet
    Args:
         query: The query to search for
    Returns:
          The search result
    """
    print(f"searching for {query}")
    return tavily.search(query=query)

llm = ChatOpenAI(model="gpt-4o-mini")
tools = [search]
agent = create_agent(model=llm,tools=tools,response_format= AgentResponse)


def main():
    result = agent.invoke({"messages":HumanMessage("What is the weather in Tokyo")})
    print(result)


if __name__ == "__main__":
    main()