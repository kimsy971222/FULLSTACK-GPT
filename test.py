from langchain.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI, ChatAnthropic

llm = OpenAI(
  model_name="davinci-002",
  openai_api_key="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"
)

chat = ChatOpenAI()

a = llm.predict("How many planets are there?")

b = chat.predict("How many planets are there?")

print(a,b)