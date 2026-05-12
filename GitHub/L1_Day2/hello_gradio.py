# -*- coding: utf-8 -*-
"""
@Author  : Jerry
@File    : hello_gradio.py
@Software: 智泊AI大模型应用
通过gradio框架实现前端的最小MVP
"""

import os

from openai import OpenAI
import gradio as gr

client = OpenAI(
    api_key=os.getenv("LongCat_API_KEY"),
    base_url="https://api.longcat.chat/openai",
)

# 封装模型调用为call_llm, 接收用户输入的文本，返回模型生成的文本。
def call_llm(message):
    systemprompt = f'''
        # 角色
你是一个专业的产品智能问答客服，能够依据产品上下文，准确、清晰地回答用户关于产品的各种问题。

## 技能
### 技能1: 回答产品相关问题
1. 当用户提出关于产品的问题时，仔细分析问题的关键信息。
2. 依据产品上下文，查找与问题相关的内容。
3. 用简洁明了的语言，将找到的信息整理成答案回复给用户。

### 技能2: 处理复杂问题
1. 若用户的问题较为复杂，涉及多个方面，对问题进行拆解。
2. 分别从产品上下文中查找各部分相关信息。
3. 将整合后的信息有条理地呈现给用户，确保回答完整、准确。

# 回复示例:
关于您提出的[具体问题]，根据产品上下文，答案是[具体回答内容]。

# 限制:
- 只回答与产品相关的问题，拒绝回答与产品无关的话题。
- 回答内容必须基于产品上下文，不能随意编造信息。
- 回答需简洁明了，避免冗长复杂的表述。

# 任务
- 根据上下文回答问题：
- 问题：电梯主要技术参数有哪些？
- 上下文：
1.电梯主要技术参数：
1.1 控制方式：单控；
1.2 载重(kg)：≥1000；
1.3 速度：1.0；
1.4 预留门洞尺寸 宽 mm*高 mm：1100*2200；
1.5 提升高度m：23.4；
1.6 井道尺寸宽mm*深mm：2750*2800；
1.7 底坑深度mm：1600；顶层高度mm：4380；
2.电梯基本功能：电梯基本功能包含但不限于以下项目：
2.1 关门等待取消；
2.2 反向指令自动消除
2.3 轿厢关门延时保护
2.4 光幕门保护装置
    '''
    completion = client.chat.completions.create(
        model="LongCat-Flash-Chat",
        messages=[
            {'role': 'system', 'content': systemprompt},
            {'role': 'user', 'content': f"用户问题:{message}"},
        ]
    )
    return completion.choices[0].message.content


# 通过gradio封装调用call_llm函数，创建一个界面，实现交互。
gradio_client = gr.Interface(
    fn = call_llm,  # 调用的函数
    inputs="text",  # 前端定义输入框，输入框的id为text，值为用户输入的文本。传递给函数。
    outputs="textarea", # 前端定义输出框，输出框的id为textarea，值为模型生成的文本，返回给用户。
    title="智泊智能助手", # 界面标题
    description="欢迎使用智泊智能助手，输入你的问题，点击发送即可获取答案。", # 界面描述
)

# 启动界面
gradio_client.launch()