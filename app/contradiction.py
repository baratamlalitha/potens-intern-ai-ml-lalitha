from app.llm import client

def check_contradiction(text1, text2):

    prompt = f"""
You are an AI system that detects contradictions.

Analyze the following two policy statements.

Statement 1:
{text1}

Statement 2:
{text2}

Determine whether:
- they contradict
- partially contradict
- or agree

Explain briefly.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content