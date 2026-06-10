from dotenv import load_dotenv
import os
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query):
    """ this is asearch engine. it will take the user query and search and will give the output
    arg: 
        query:
    Returns:
        the search result is:"""
    print(f'searching for {query}')
    return tavily.search(query=query)

llm= ChatOpenAI()
tools = [search]
agent = create_agent(model = llm, tools= tools)

def main():
    print('Hello! I am Langchain agent')
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main()