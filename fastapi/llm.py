from langchain_openai import AzureChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
import os

os.environ["SSL_CERT_FILE"] = "ca-bundle-full.crt"

llm = AzureChatOpenAI(
    openai_api_version="2024-10-21",
    deployment_name="openai.gpt-4-1-nano-2025-04-14",
    azure_endpoint="<your-azure-endpoint>",
    openai_api_type="azure",
    openai_api_key="<your-azure-api-key>",
    temperature=1,
    max_tokens=500,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
)


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_agent(
    llm,
    [get_weather],
    system_prompt="You are a helpful assistant that provides weather information.",
)


async def invoke_agent(user_input: str) -> str:
    result = agent.invoke({"messages": [HumanMessage(user_input)]})
    return result["messages"][3].content
