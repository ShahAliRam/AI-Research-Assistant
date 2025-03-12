import os
from mistralai import Mistral

# Load API key from environment variables
api_key = os.environ["API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def critique_paper(summary_text):
    prompt = f"Analyze the strengths and weaknesses of the following research paper:\n{summary_text}. Make sure you don't cross the word limit"
    
    response = client.chat.complete(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0,  # Adjust for variation
        top_p=0.9,        # Adjust diversity
        max_tokens=300    # Enough for a detailed critique
    )
    
    return response.choices[0].message.content

papers = [
    {
        'title' : 'Swin Transformer',
        'summary': """ This paper was the alternative to Vision Transformers.
                    The main contributions of this paper are the linear time complexity achieved through Shifted Window Attention
                     mechanism, and it also is scale-invariant due to the hierarchical methodology of its attention formulation.
        """
    }
]

# Example usage: Critiquing multiple papers
for paper in papers:
    paper["critique"] = critique_paper(paper["summary"])
    print(paper["title"], "\nCritique:", paper["critique"], "\n")
