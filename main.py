import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

# ==========================================
# 1- بروتوكول القيادة العليا (The Neuralink UI)
# ==========================================
st.set_page_config(page_title="BASIL X-VISION", layout="wide", page_icon="🚀")

st.markdown("""
    <style>
    /* خلفية الفضاء العميق */
    .stApp {
        background: url('https://getwallpapers.com/wallpaper/full/1/3/4/621151.jpg');
        background-size: cover;
        color: #ffffff;
    }
    
    /* الكروت الزجاجية (Glassmorphism) */
    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 20px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        transition: 0.4s;
    }
    [data-testid="stMetric"]:hover {
        transform: scale(1.03) translateY(-5px);
        border: 1px solid #00d4ff !important;
        box-shadow: 0 0 25px #00d4ff;
    }

    /* نصوص إيلون ماسك ناصعة البياض */
    [data-testid="stMetricValue"] { color: #00d4ff !important; font-family: 'Orbitron', sans-serif; font-weight: 900 !important; }

    /* العناوين المستقبلية */
    .elon-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 65px;
        text-align: center;
        letter-spacing: 10px;
        background: linear-gradient(to right, #00d4ff, #ffffff, #00d4ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2- القائمة الجانبية (The Mission Control)
# ==========================================
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #00d4ff;'>MASTERMIND</h1>", unsafe_allow_html=True)
    # صورة تعبيرية توحي بالقوة والسيطرة
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndm0zd3J6Mms0Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKVUn7iM8FMEU24/giphy.gif", width=250)
    
    st.divider()
    st.write("🌌 **حالة الإمبراطورية:**")
    st.info("جميع الأنظمة تعمل بكفاءة 100% (Alpha-Mode)")
    
    st.divider()
    if st.button("🚀 إطلاق القمر الصناعي Basil-1"):
        st.toast("Connecting to Starlink...")
        st.balloons()
        st.audio("https://www.soundjay.com/buttons/sounds/button-21.mp3")

# ==========================================
# 3- لوحة التحكم المركزية (The Command Deck)
# ==========================================
st.markdown('<p class="elon-title">BASIL X-VISION</p>', unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #8b949e;'>GLOBAL LOGISTICS & QUANTUM TRADING</h4>", unsafe_allow_html=True)

# الإحصائيات (البند 1 من الخطة)
col1, col2, col3 = st.columns(3)
col1.metric("إجمالي الثروة النشطة", "1,840,000 AED", "+12% 📈")
col2.metric("أسطول الحاويات", "42 حاوية", "تحت السيطرة")
col3.metric("توقعات الربح السنوي", "$45,000,000", "Target Locked")

# ==========================================
# 4- الوسائط المتعددة (البند 2 و 3)
# ==========================================
st.divider()
t1, t2, t3 = st.tabs(["🛰️ رادار التتبع", "📦 مخزن الأسلحة التجارية", "💹 الذكاء المالي"])

with t1:
    st.subheader("تتبع الشحنات عبر الأقمار الصناعية (Real-time)")
    # رسم بياني ثلاثي الأبعاد تفاعلي (يذهل أي مستخدم)
    fig = go.Figure(data=[go.Scatter3d(
        x=[1, 2, 3, 4], y=[10, 20, 15, 25], z=[5, 5, 5, 5],
        mode='lines+markers',
        line=dict(color='#00d4ff', width=10)
    )])
    fig.update_layout(
        scene=dict(xaxis_backgroundcolor="#05070a", yaxis_backgroundcolor="#05070a", zaxis_backgroundcolor="#05070a"),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    st.success("📍 الموقع الحالي للحاوية الكبرى: **ميناء جبل علي - رصيف 4**")

with t2:
    st.subheader("الكتالوج الرقمي (The Arsenal)")
    col_img, col_data = st.columns([1, 2])
    with col_img:
        st.image("https://img.freepik.com/free-photo/industrial-design-concept-with-engine_23-2150141323.jpg", caption="Quantum Engine V12")
    with col_data:
        st.table(pd.DataFrame({
            "القطعة": ["محرك تيسلا", "جير بوكس لاندكروزر", "نظام تعليق لكزس"],
            "الحالة": ["متاح", "في الطريق", "تم البيع"],
            "السعر": ["$45,000", "$12,000", "$8,500"]
        }))

with t3:
    st.subheader("محرك الحسابات الكمي (Quantum Finance)")
    c_a, c_b = st.columns(2)
    with c_a:
        st.write("أدخل القيمة (AED):")
        val = st.number_input("", value=10000)
    with c_b:
        st.write("النتيجة بالريال اليمني (صرف إيلون ماسك):")
        st.title(f"{val * 145:,.0f} YER")
        st.progress(85) # شريط طاقة يوضح قوة الصفقة

# ==========================================
# 5- المؤثرات الصوتية والتفاعل (البند 5 و 6)
# ==========================================
st.divider()
st.subheader("🎮 مركز التحكم التفاعلي")
if st.button("🔥 تفعيل وضع الهجوم التجاري (Attack Mode)"):
    with st.spinner('Calculating profits...'):
        time.sleep(2)
        st.snow()
        st.audio("https://www.soundjay.com/misc/sounds/wind-chime-01.mp3")
        st.warning("⚠️ تحذير: نسبة الأرباح ستتجاوز قدرة البنوك على التحمل!")

st.caption(f"BASIL GLOBAL X-VISION v25.0 | Multi-Media OS | © {datetime.now().year}")
