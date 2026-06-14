import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


messages = [
        {
            "role": "system",
            "content": "You are a Purepower Expert"
        }
 
    ]
 
print("chat started! Type 'exit' to quit.\n")
    
while True:
    user_input = input("you:")
        
    if user_input.lower()== 'exit':
            print("AI GOODBYE!")
            break
    messages.append({"role": "user", "content": user_input})
        
    try:
        response = client.chat.completions.create(
             model="llama-3.1-8b-instant",
             messages=messages
                
            )
        
        ai_reply = response.choices[0].message.content
        print(f"AI: {ai_reply}\n")
    
        messages.append({"role":"assistant", "content": ai_reply})

    except Exception as e:
        print(f"error:{e}")
    
   


