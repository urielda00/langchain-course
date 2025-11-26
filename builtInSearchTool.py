from dotenv import load_dotenv


load_dotenv()


from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch


llm = ChatOpenAI()
tools = [TavilySearch()]
agent = create_agent(model=llm,tools=tools)


def main():
    result = agent.invoke({"messages":HumanMessage("What is the weather in Tokyo")})
    print(result)


if __name__ == "__main__":
    main()