import openai

# Setze deinen OpenAI API-Schlüssel (ersetze 'dein-openai-api-key' mit deinem tatsächlichen API-Schlüssel)
openai.api_key = 'dein-openai-api-key'

def get_meditation_suggestions(user_input):
    try:
        # Anfrage an den OpenAI API-Assistenten-Endpunkt
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Du bist ein Meditationsassistent."},
                {"role": "user", "content": f"Schlage eine Meditation für den folgenden Input vor: {user_input}"}
            ],
            max_tokens=100,
            temperature=0.7
        )
        # Extrahiere die Antwort
        suggestions = response.choices[0].message['content'].strip()
        return suggestions
    except Exception as e:
        return f"Fehler bei der API-Anfrage: {e}"

if __name__ == "__main__":
    # Nutzer-Input einholen
    user_input = input("Gib deinen aktuellen Zustand oder was du benötigst ein: ")
    # Meditationsvorschläge abrufen
    suggestions = get_meditation_suggestions(user_input)
    # Vorschläge ausgeben
    print("Vorgeschlagene Meditation:")
    print(suggestions)
