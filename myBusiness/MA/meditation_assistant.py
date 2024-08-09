import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_meditation_suggestion(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that suggests suitable meditations to the user."},
                {"role": "user", "content": user_input}
            ]
        )
        meditation = response['choices'][0]['message']['content'].strip()
        return meditation
    except openai.error.OpenAIError as e:
        return f"There was a problem processing your request: {e}"

if __name__ == "__main__":
    user_input = input("Enter your state or need: ")
    meditation_suggestion = get_meditation_suggestion(user_input)
    print(f"Suggested Meditation: {meditation_suggestion}")
