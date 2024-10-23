import openai 
from config import OPENAI_API_KEY 
'''
Hier wird die Vriable OPENAI_API_KEY  aus einer Separanten Datei
namnes 'cnfig.py importient.
Diese Datei enthält dfen API schlüssel, der für den Zugriff auf den OPENAI-API bnötigt wird.
Der API schlüssel ist eine geheime Zeichenfolge, die sicher 

aufbewahrt werden sollte, da er den Zugriff auf die Kostenpdlichtigen Dienste von OpenAI ermögliht.
''''

openai.api_key = OPENAI_API_KEY
'''
'openai.apkey = OPEN_API_KEY'
Indieser Zeile wird der importierte API-Xhlüssel 'OPENAI_API_KEY' der 'api_key'
Eigenschafft des 'openai' Moduls zugewiesen.
Dadurch authentifiziert sich das Skript bei OpenAI und kann API-Anfragen senden.
'''
def get_meditation_suggestion(user_input):
'''
def get_meditation_suggestion(user_input):
Hier beginnt die Definition einer Funnktion namens 'ge  ' 
'''


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
