from pydantic import BaseModel, Field

class BookSummary(BaseModel):
    title: str = Field(..., description="Title of the book or chapter")
    summary: str = Field(..., description="Condensed summary of the input")
    saved_path: str = Field(default="", description="Where the summary was saved")

# Escape curly braces in schema_json
raw_schema = BookSummary.schema_json(indent=2).replace("{", "{{").replace("}", "}}")

SYSTEM_PROMPT = f"""You are a professional book summarizer.
1. Read the input and extract key points.
2. Condense ideas in plain English.
3. Highlight themes, key events, or arguments.
4. Always save the output using save_summary.
Return JSON only in this format:
{raw_schema}
"""
