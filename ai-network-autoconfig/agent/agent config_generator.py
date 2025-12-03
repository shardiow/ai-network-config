# agent/config_generator.py

import openai
import os # <--- ADD THIS

# Set the API key from the environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY") # <--- ADD THIS

def generate_config(vendor, intent):
   # ... (rest of the function is the same)
 
   response = openai.ChatCompletion.create(
        model="gpt-5.1",
        messages=[{"role": "user", "content": prompt}]
   )
 
   return response["choices"][0]["message"]["content"]
