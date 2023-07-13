

import openai

# Set up your OpenAI API credentials
openai.api_key = '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'
def generate(prompt:str)->str:
    # Define your story prompt
 
    # Generate the story using the OpenAI Language API
    response = openai.Completion.create(
      engine='text-davinci-003',
      prompt=prompt,
      max_tokens=64,
      temperature=0,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["\"\"\""],
    )

    # Extract the generated story from the API response
    story = response.choices[0].text.strip()

    # Print the generated story
    return story
