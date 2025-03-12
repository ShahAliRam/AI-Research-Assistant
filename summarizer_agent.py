import os
from mistralai import Mistral

# Load API Key from Environment Variable
api_key = os.environ["API_KEY"]
model = "mistral-large-latest"

# Initialize Mistral Client
client = Mistral(api_key=api_key)

def summarize_paper(summary_text):
    """Summarizes a research paper using Mistral API."""
    messages = [{"role": "user", "content": f"Summarize the following research paper:\n{summary_text}"}]

    response = client.chat.complete(
        model=model,
        messages=messages,
        response_format={"type": "text"},
        temperature=0.7,  # Adjust for more diverse responses
        max_tokens=150  # Control summary length
    )

    return response.choices[0].message.content.strip()

# Example List of Research Papers
papers = [
    {"title": "YotoR-You Only Transform One Representation", "summary": "A novel transformer architecture..."},
    {"title": "Degenerate Swin to Win", "summary": "Explores plain window-based transformers without complex operations..."}
]

# Summarize Each Paper
for paper in papers:
    paper["summary"] = summarize_paper(paper["summary"])
    print(f"📜 {paper['title']}\n📝 Summary: {paper['summary']}\n")
