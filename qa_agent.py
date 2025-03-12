import os
from mistralai import Mistral

# Load API key from environment variables
api_key = os.environ["API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def answer_question(query, papers):
    context = "\n\n".join([f"Title: {p['title']}\nSummary: {p['summary']}" for p in papers])
    prompt = f"Using the research papers provided, answer this question:\n{query}\n\nContext:\n{context}"
    
    response = client.chat.complete(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0,  # Adjust for response variation
        top_p=0.9,        # Increase diversity
        max_tokens=300    # Adjust for detailed responses
    )
    
    return response.choices[0].message.content

# Example usage
question = "What are the main advantages of Swin Transformer?"
papers = [
    {
        'title' : 'Swin Transformer',
        'summary': """ This paper was the alternative to Vision Transformers.
                    The main contributions of this paper are the linear time complexity achieved through Shifted Window Attention
                     mechanism, and it also is scale-invariant due to the hierarchical methodology of its attention formulation.
        """
    }
]

answer = answer_question(question, papers)
print("Answer:", answer)
