# 📘 Book Summarizer Agent
An AI-powered command-line tool that reads any chapter, article, or text and returns a professional summary with title, key ideas, and saved output. Built using LangChain and Google Gemini 2.5.

### 🚀 Features
🔍 Reads any book chapter, story, or article

🧠 Uses Google Gemini 2.5 Flash for accurate summarization

📄 Outputs a structured summary with title and key points

💾 Automatically saves the summary to a timestamped .txt file

🛠️ Built with LangChain's tool-calling agents

### 🧰 Requirements
Python 3.8+

Google Generative AI API Key (Gemini)

.env file with the API key

### 📦 Installation
1. Clone the repo:
```bash
git clone https://github.com/your-username/book-summarizer-agent.git
cd book-summarizer-agent
```
2. Create and activate virtual environment (optional but recommended):
```bash\
python -m venv venv
venv\Scripts\activate      # Windows
# OR
source venv/bin/activate   # Mac/Linux
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Set up your .env file:
Create a file named .env in the project root:
```bash
GOOGLE_API_KEY=your-google-api-key-here
```

### 🧪 Usage
Run the application:
```bash
python main.py
```

You’ll see:
```
📘 Book Summarizer Agent — paste a chapter or section below
```
Paste any long-form content (book chapter, essay, article), and the app will:

Analyze the content

Return a clean summary with title

Save the summary in /summaries folder

### 🖼️ Example Output
```yaml
📖 Title: The Brave Knight
📝 Summary:
This story follows a knight who courageously saves a village from a dragon...
💾 Saved at: summaries/The_Brave_Knight_20250723_121433.txt
```

### 🔧 Tools Used
LangChain

Google Generative AI (Gemini)

Python’s dotenv, pydantic, and file I/O

### 🧠 Future Ideas
Add auto-title generation from first sentence

Create a web-based UI with Flask or Streamlit

Add support for PDF/book uploads

### 👨‍💻 Author
Made with ❤️ by Muhammad Osama Noor
