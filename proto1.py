import openai
api_key = "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"

import openai
openai.api_key = api_key


genre = input("What genre of story would you like to hear? ")
main_character = input("Who should be the main character? ")
age_group = input("What age group is this story for? ")
word_count = input("Length of story?")

prompt = f"Write a {genre} story about {main_character} in {word_count} words for a {age_group} year old kid."

completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)


generated_text = completions.choices[0].text
print(generated_text)
