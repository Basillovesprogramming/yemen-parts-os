import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import time

# ==========================================
# 1- بروتوكول "الهيبة السوداء" (Cinematic UI)
# ==========================================
st.set_page_config(page_title="BASIL SUPREMACY", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    /* خلفية سينمائية عميقة */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.9)), 
                    url('https://images.unsplash.com/photo-1511447333015-45b65e60f6d5?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        color: #ffffff;
    }
    
    /* تصميم الكروت "الزمردية" المتحركة */
    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.03) !important;
        border-left: 5px solid #00ff88 !important;
        border-radius: 10px !important;
        backdrop-filter: blur(10px);
        padding: 30px !important;
        box-shadow: 10px 10px 20px rgba(0,0,0,0.5);
    }
    
    [data-testid="stMetric"]:hover {
        background: rgba(0, 255, 136, 0.1) !important;
        transform: scale(1.02);
        box-shadow: 0 0 30px rgba(0, 255, 136, 0.3);
    }

    /* نصوص ناصعة كالألماس */
    [data-testid="stMetricValue"] { color: #00ff88 !important; font-size: 45px !important; font-weight: 900 !important; }

    .hero-title {
        font-size: 80px; font-weight: 900; text-align: center;
        letter-spacing: 15px; color: white;
        text-shadow: 0 0 20px #00ff88, 0 0 40px #00ff88;
        margin-top: -50px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2- القائمة الجانبية (The Sovereign Sidebar)
# ==========================================
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #00ff88;'>BASIL HQ</h1>", unsafe_allow_html=True)
    # جيف سينمائي يعبر عن التكنولوجيا
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Y2Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/I5xV5HnSIno/giphy.gif", width=250)
    
    st.divider()
    st.subheader("🎵 نظام التنبيهات الصوتي")
    st.audio("https://www.soundjay.com/buttons/sounds/button-20.mp3")
    
    st.divider()
    st.write("🌍 **النفوذ العالمي:** دبي | صنعاء | طوكيو")
    st.progress(100)
    
    if st.button("🔱 تفعيل السلطة المطلقة"):
        st.balloons()
        st.toast("Access Granted: Welcome Master Basil")

# ==========================================
# 3- لوحة القيادة (The Command Center)
# ==========================================
st.markdown('<p class="hero-title">BASIL</p>', unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #8b949e; letter-spacing: 5px;'>QUANTUM GLOBAL TRADING SYSTEM</h3>", unsafe_allow_html=True)

# صف الإحصائيات العملاق (البند 1)
col1, col2, col3 = st.columns(3)
col1.metric("ASSET VALUE", "1.84M AED", "TOP TIER")
col2.metric("LOGISTICS FLIGHTS", "14 ACTIVE", "IN-TRANSIT")
col3.metric("NET REVENUE", "145M YER", "98% ACCURACY")

# ==========================================
# 4- الوسائط التفاعلية (The Multi-Media Hub)
# ==========================================
st.divider()
tab1, tab2, tab3 = st.tabs(["⚡ الرادار الذكي", "📽️ الكواليس والوسائط", "📈 مصفوفة الأرباح"])

with tab1:
    st.subheader("تتبع الأقمار الصناعية للشحنات")
    
    # رسم بياني ثلاثي الأبعاد للأرباح المتوقعة
    fig = go.Figure(data=[go.Surface(z=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], colorscale='Viridis')])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=500)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("🎬 الوسائط والمؤثرات")
    c_v, c_i = st.columns([2, 1])
    with c_v:
        st.video("https://www.youtube.com/watch?v=36YnV9STBqc") # فيديو برومو تقني
    with c_i:
        st.image("https://img.freepik.com/free-photo/industrial-design-concept-with-engine_23-2150141323.jpg", caption="The Power Unit")
        st.image("https://img.freepik.com/free-photo/logistics-transportation-container-cargo-ship_335224-659.jpg", caption="Global Hub")

with tab3:
    st.subheader("🧮 حاسبة الصرف الفوري")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("#### أدخل القيمة بالدرهم (AED)")
        val_in = st.number_input("", value=10000)
    with col_b:
        st.markdown("#### القيمة بالريال اليمني (YER)")
        st.markdown(f"<h1 style='color: #00ff88;'>{val_in * 145:,.0f}</h1>", unsafe_allow_html=True)
        st.progress(75)

# ==========================================
# 5- التفاعل الحي (The Final Interaction)
# ==========================================
st.divider()
st.subheader("🕹️ وحدة التحكم التفاعلية")
if st.button("🔥 إطلاق إعصار الأرباح"):
    with st.spinner('برمجة النجاح...'):
        time.sleep(1)
        st.snow()
        st.audio("https://www.soundjay.com/misc/sounds/bell-ringing-01.mp3")
        st.success("تم التفعيل! أنت الآن في القمة يا باسل.")

# تذييل الصفحة
st.caption(f"BASIL SUPREMACY v26.0 | The Final Multi-Media OS | © {datetime.now().year}")
