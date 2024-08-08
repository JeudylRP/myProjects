import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_meditation_suggestion(user_input):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Der Benutzer sagt: {user_input}\nBitte schlage eine passende Meditation vor.",
            max_tokens=150,
            temperature=0.7
        )
        meditation = response.choices[0].text.strip()
        return meditation
    except openai.error.OpenAIError as e:
        return f"Es gab ein Problem bei der Verarbeitung deiner Anfrage: {e}"

if __name__ == "__main__":
    user_input = input("Gib deinen Zustand oder Bedarf ein: ")
    meditation_suggestion = get_meditation_suggestion(user_input)
    print(f"Vorgeschlagene Meditation: {meditation_suggestion}")
