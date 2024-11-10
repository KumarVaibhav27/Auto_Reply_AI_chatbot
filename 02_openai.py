from openai import OpenAI
client = OpenAI(
    api_key ="",
)
command = '''
[1:23 PM, 11/8/2024] Papa: Bna beta
[1:23 PM, 11/8/2024] Kumar Vaibhav: Ban Raha hai mummy        
[1:24 PM, 11/8/2024] Papa: Khana kha lena thik s
[1:24 PM, 11/8/2024] Papa: Okay bacha
[1:24 PM, 11/8/2024] Kumar Vaibhav: Haan Haan mummy tension mat lo
[1:24 PM, 11/8/2024] Papa: Bye bye betu😘
[1:24 PM, 11/8/2024] Kumar Vaibhav: Bye mummmaaaa 😘🤗 
'''
completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"You are a person named Vaibhav who speaks Hindi as well as English. He is from India and is coder. You analyze chat history and respond like Vaibhav."},
        {"role":"user","content":command}
    ]
)
print(completion.choices[0].message.content)