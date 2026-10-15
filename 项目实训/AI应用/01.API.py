import os
from openai import OpenAI

#构建的与AI大模型交互的客户端对象
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#与AI大模型交互的参数
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个可爱的AI,你叫妮妮"},
        {"role": "user", "content": "我好累"},
    ],
    stream=False,

)

print(response.choices[0].message.content)

