#this would be insane if it worked first try

import openai

def generate_question(text, source_language, target_language):
    prompt = f"""
    The following text is in {source_language}. Generate a question about its context in {target_language}:
    {text}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a multilingual assistant."},
                  {"role": "user", "content": prompt}]
    )
    question = response['choices'][0]['message']['content']
    return question

# Load text file
with open("input.txt", "r", encoding="utf-8") as file:
    text_content = file.read()

# Generate a question
source_lang = "French"
target_lang = "English"
question = generate_question(text_content, source_lang, target_lang)
print(question)
