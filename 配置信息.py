#配置信息


client = OpenAI(
    api_key=os.getenv("LongCat_API_KEY"),
    base_url="https://api.longcat.chat/openai",
)

# 封装模型调用为call_llm, 接收用户输入的文本，返回模型生成的文本。
def call_llm(message):
    completion = client.chat.completions.create(
        model="LongCat-Flash-Chat",
        messages=[
            {'role': 'user', 'content': message},
        ]
    )
    return completion.choices[0].message.content