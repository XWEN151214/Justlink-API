import google.generativeai as genai

API_KEY = ""
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash-latest")
