import streamlit as st

#设置页面
st.set_page_config(
    page_title="小金的练习",
    page_icon="🧊",
    #布局
    layout="wide",
    #侧边栏
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
  )

#标题
st.title("浪漫地中海的明珠：圣托里尼")
st.header("伊亚镇的蓝顶教堂与迷人日落")
st.subheader("悬崖上的白房子与火山岛的传说")

#段落文子
st.write("圣托里尼是爱琴海上一颗璀璨的明珠，其最迷人的风景莫过于伊亚镇（Oia）。这里以层层叠叠、依悬崖而建的纯白色圆顶房屋和几座醒目的蓝色圆顶教堂而闻名于世")
st.write("漫步在伊亚镇迷宫般的窄巷中，你会被这里浓郁的浪漫气息所包围。游客们流连于俯瞰无垠爱琴海的观景台，或参观当地的手工艺品店和咖啡馆。这种悠闲、开放的地中海生活方式")
st.write("除了视觉上的享受，圣托里尼还拥有丰富的火山历史。它曾是巨大火山爆发的遗址，形成了现在独特的卡尔德拉悬崖地貌和新卡梅尼等火山岛")

#图片
st.image("./resources/img.png",width=500)

#表格
student_data = {
    "姓名": ["王林", "李慕婉", "贝罗", "莫历海", "石源"],
    "学号": ["20260001", "20260002", "20260003", "20260004", "20260005"],
    "语文": [98, 90, 59, 29, 88],
    "数学": [88, 78, 65, 70, 39],
    "英语": [99, 89, 87, 59, 62],
    "总分": [285, 257, 211, 158, 189]
}
st.table(student_data)

#输入框
name = st.text_input("请输入姓名")
st.write(name)

#密码
password = st.text_input("请输入密码",type="password")
st.write("成功")

#单选选项
gender=st.radio("请输入性别",["男","女"])
st.write(gender)