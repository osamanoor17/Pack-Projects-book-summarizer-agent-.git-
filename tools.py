import os
import datetime
from langchain.tools import Tool

def save_summary(text: str, title: str = "summary"):
    os.makedirs("summaries", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"summaries/{title.replace(' ', '_')}_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text.strip())
    return f"Saved to {filename}"

tools = [
    Tool(
        name="save_summary",
        func=save_summary,
        description="Save the summary with the given title."
    )
]
