import openai

class GPTModel:
  def __init__(self, api_key):
    openai.api_key = api_key
  def generate_response(self, prompt_text):
    completion = openai.completions.create(
      model="gpt-3.5-turbo",
      prompt=prompt_text,
      max_tokens=100,
      temperature=0
    )

    return completion.choices[0].text