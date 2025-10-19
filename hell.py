from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyAtzWm83cMs_JdwTeiZel6QXu12KjqzIQ8")
while True:
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=input("Enter your prompt: ")
    )
    print(response.text)