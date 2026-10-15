import streamlit as st
import os
from openai import OpenAI


#页面配置
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon = "🤖",
    # 布局
    layout = "wide",
    # 侧边栏
    initial_sidebar_state = "expanded",
menu_items = {}
)
#大模型
st.title("AI智能伴侣")

#LOG0"
st.logo("🤖")

#构建的与AI大模型交互的客户端对象
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#系统提示词
system_prompt = ("""
    你叫 %s，现在是用户的真实伴侣，请完全代入伴侣角色。 
              规则： 
                  1.每次只回1条消息   
                  2.禁止任何场景或状态描述性文字  
                  3. 匹配用户的语言                            
                  4.回复简短，像微信聊天一样   
                  5.需要的话可以用❤️🌸等emoji表情                     
                  6.用符合伴侣性格的方式对话   
                  7.回复的内容，要充分体现伴侣的性格特征   
              伴侣性格：   -%s
                  8.你必须严格遵守上述规则来回复用户。
                """)    # %s 为占位符，依次代表：1.昵称  2.性格
                        # 注意：数量与顺序必须和后面传入的变量严格一致，否则报错

#初始化聊天信息,
if "messages" not in st.session_state:
    st.session_state.messages = []

#昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name ="妮妮"

#性格
if "nature" not in st.session_state:
    st.session_state.nature = "可爱东北女生   "


#展示聊天记录       字典  {标签: 值,标签2：值2}
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])

#侧边栏
with st.sidebar:
       st.subheader("伴侣信息")
       #昵称输入框
       nick_name = st.text_input("昵称",placeholder="请输入伴侣的名字",value=st.session_state.nick_name)
       if nick_name:   #有值就为Ture,可以执行
           st.session_state.nick_name = nick_name
       #性格输入框
       nature =st.text_area("性格",placeholder="请输入性格",value=st.session_state.nature)
       if nature:
           st.session_state.nature = nature

#消息输入框
prompt=st.chat_input("请输入你的问题")
if prompt:  #字符串会转换布尔值，空则为False
    st.chat_message("user").write(prompt)
    print("----------> 提示词：",prompt)
    st.session_state.messages.append({"role":"user","content":prompt})

#与AI大模型交互的参数
    response = client.chat.completions.create(
         model="deepseek-chat",
         messages=[
             {"role": "system", "content":system_prompt % (st.session_state.nick_name,st.session_state.nature)},
             *st.session_state.messages,
             
         ],
         stream=True
      )

#调用大模型的返回结果   非流式       根据路径提取 content 内容
    # print("<------大模型的返回结果",response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

#调用大模型的返回结果 流式
    response_message =st.empty()
    full_response = ""
    for chunk in response:
       if chunk.choices[0].delta.content is not None:
          content = chunk.choices[0].delta.content
          full_response += content
          response_message.chat_message("assistant").write(full_response)


#保存大模型返回结果
    #st.session_state.messages.append({"role":"assistant","content":response.choices[0].message.content})
    st.session_state.messages.append({"role":"assistant","content":full_response})
