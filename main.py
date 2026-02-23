import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

# 1- إعدادات الانفجار البصري (Vibrant UI)
st.set_page_config(page_title="BASIL COMMAND", layout="wide")

st.markdown("""
    <style>
    /* خلفية متحركة وألوان نيون */
    .stApp {
        background: radial-gradient(circle, #001d3d 0%, #000814 100%);
        color: #00fbff;
    }
    
    /* جعل الكروت تتوهج (Neon Glow) */
    [data-testid="stMetric"] {
        background: rgba(0, 247, 255, 0.05) !important;
        border: 2px solid #00fbff !important;
        box-shadow: 0 0 15px #00fbff;
        border-radius: 30px !important;
        transition: 0.5s;
    }
    [data-testid="stMetric"]:hover { transform: scale(1.05); box-shadow: 0 0 30px #ff00c8; border-color: #ff00c8 !important; }
    
    /* الأزرار بنمط الألعاب */
    .stButton>button {
        background: linear-gradient(45deg, #ff00c8, #58a6ff);
        border: none; color: white; font-weight: bold; font-size: 20px;
        border-radius: 50px; height: 3em; box-shadow: 0 5px 15px rgba(255, 0, 200, 0.4);
    }
    
    .title-neon {
        font-size: 70px; font-weight: 900; text-align: center;
        color: #fff; text-shadow: 0 0 10px #00fbff, 0 0 20px #00fbff, 0 0 40px #00fbff;
        font-family: 'Courier New', Courier, monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# 2- القائمة الجانبية (Sidebar)
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>👑 باسل</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndm0zd3J6Mms0Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKVUn7iM8FMEU24/giphy.gif", width=250)
    st.divider()
    st.audio("https://www.soundjay.com/buttons/sounds/button-20.mp3")
    st.write("🔴 الحالة: **مسيطر بالكامل**")

# 3- العنوان التفاعلي
st.markdown('<p class="title-neon">BASIL QUANTUM</p>', unsafe_allow_html=True)

# 4- تفاعل الوسائط (مشروع وسائط حقيقي)
col_v1, col_v2 = st.columns([2, 1])

with col_v1:
    st.markdown("### 🎥 فيديو العمليات الاستراتيجية")
    # فيديو بخلفية سينمائية
    st.video("https://www.youtube.com/watch?v=36YnV9STBqc") 

with col_v2:
    st.markdown("### 🔈 أوامر صوتية")
    if st.button("🚨 تفعيل إنذار الأرباح"):
        st.toast("تحذير: الأرباح تتجاوز التوقعات!")
        st.balloons()
        st.audio("https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3")

# 5- الرسوم البيانية التفاعلية (وسائط متحركة)
st.divider()
st.subheader("📊 خريطة السيطرة المالية")
fig = go.Figure(data=[go.Mesh3d(x=[0, 1, 2, 0], y=[0, 0, 1, 2], z=[0, 2, 0, 1], color='#ff00c8', opacity=0.5)])
fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
st.plotly_chart(fig, use_container_width=True)

# 6- تبويبات الوسائط المتعددة
t1, t2, t3 = st.tabs(["💎 الجوهرة المالية", "🚚 الرادار اللوجستي", "📱 مركز التفاعل"])

with t1:
    c1, c2, c3 = st.columns(3)
    c1.metric("رأس المال النفاذ", "1,840,000 AED")
    c2.metric("الصرف المباشر", "145.0 YER")
    c3.metric("النمو السنوي", "300%", "FIRE")

with t2:
    st.markdown("### 🗺️ تتبع الحاويات عبر الأقمار الصناعية")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Y2Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/I5xV5HnSIno/giphy.gif")
    st.progress(90)
    st.info("📍 الشحنة تقترب من سواحل اليمن..")

with t3:
    st.subheader("العب وتفاعل مع مشروعك")
    if st.button("🚀 إطلاق القمر الصناعي لباسل"):
        with st.spinner('جاري الاتصال بالأقمار الصناعية...'):
            time.sleep(2)
            st.success("تم الاتصال! العالم تحت يدك الآن.")
            st.snow()

st.divider()
st.caption("Basil Global Cyber-Systems v24.0 | No Limits")
