from dotenv import load_dotenv; load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.messages import HumanMessage, AIMessage

from tools import tools
from schema import BookSummary, SYSTEM_PROMPT

# Initialize model and parser
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.4)
parser = PydanticOutputParser(pydantic_object=BookSummary)

# Define prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}")
]).partial(format_instructions=parser.get_format_instructions())

# Create agent and executor
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Main loop
chat_history = []
print("📘 Book Summarizer Agent — paste a chapter or section below")

while True:
    text = input("\nPaste content or type 'exit': ")
    if text.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=text))
    response = executor.invoke({"query": text, "chat_history": chat_history})

    try:
        result = parser.parse(response["output"])
        print(f"\n📖 Title: {result.title}\n📝 Summary:\n{result.summary}\n💾 Saved at: {result.saved_path}")
        chat_history.append(AIMessage(content=result.summary))
    except Exception as e:
        print("❌ Error:", e)
        print("Raw output:\n", response.get("output"))