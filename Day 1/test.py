from langchain.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI, ChatAnthropic

llm = OpenAI(
  model_name="davinci-002",
  # openai_api_key=""
)

chat = ChatOpenAI()

a = llm.predict("How many planets are there?")

b = chat.predict("How many planets are there?")

print(a,b)