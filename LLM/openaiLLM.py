import requests
import json
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()  # 加载 .env 文件中的环境变量

client = OpenAI()

def openaiLLM(messages,model="gpt-4o",temperature=0.5,top_p=1,max_tokens=1024,api_key="",api_port=8000):
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p
        )
        return completion.choices[0].message.content
    except Exception as e:
        return {"error": str(e)}
if __name__ == '__main__':

    messages = [
        {"role": "system", "content": "你是一个专业的天气助手。"},
        {"role": "user", "content": "天空为何是蓝色的？"},
    ]
    api_key = "api_key"
    response = openaiLLM(messages, api_key=api_key)
    print(response) 
