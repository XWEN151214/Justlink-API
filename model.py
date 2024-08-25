import google.generativeai as genai

API_KEY = "AIzaSyDxx8Po9zoJr0UGa2p8ybnI4PPlzMVwE_U"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash-latest")
