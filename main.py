import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# ==========================================
# 1- الهندسة التفاعلية (التصميم البصري والرسوم)
# ==========================================
st.set_page_config(page_title="Basil Multimedia Project", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #05070a, #0d1117); color: #ffffff; }
    /* تأثيرات الأزرار التفاعلية */
    .stButton>button {
        width: 100%; border-radius: 20px; height: 3em;
        background-color: #1f6feb; color: white; border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover { background-color: #58a6ff; transform: scale(1.05); }
    [data-testid="stMetric"] { background: #161b22; border: 2px solid #30363d; border-radius: 20px; padding: 20px; }
    .main-title { font-size: 55px; font-weight: 900; text-align: center; background: -webkit-linear-gradient(#58a6ff, #bc8cff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2- القائمة الجانبية (مركز التحكم والوسائط)
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>👑 القائد باسل</h2>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
    st.divider()
    
    # تفاعل صوتي (إضافة مؤثر صوتي عند العمل)
    st.write("🎵 **المؤثرات الصوتية:**")
    st.audio("https://www.soundjay.com/buttons/sounds/button-3.mp3") # صوت تنبيه تفاعلي
    
    st.divider()
    st.subheader("⚙️ إعدادات المشروع")
    ex_rate = st.sidebar.slider("سعر الصرف اللحظي", 140.0, 160.0, 145.0)
    
    st.success("🔒 النظام محمي ومشفر")

# ==========================================
# 3- المحتوى التفاعلي الرئيسي (الهدف من المشروع)
# ==========================================
st.markdown('<p class="main-title">إمبراطورية الوسائط: مشروع باسل</p>', unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>هدف المشروع: أتمتة سلاسل الإمداد بين دبي واليمن بصرياً وتفاعلياً</h4>", unsafe_allow_html=True)

# استخدام التبويبات لتنظيم الوسائط (صور، رسوم، تفاعل)
t_intro, t_gallery, t_interactive, t_analytics = st.tabs(["📖 المقدمة", "📸 معرض الصور", "🎮 التفاعل", "📊 الرسوم البيانية"])

# --- تبويب 1: المقدمة (الهدف) ---
with t_intro:
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("لماذا هذا المشروع؟")
        st.write("""
        يهدف هذا المشروع إلى تبسيط عملية استيراد قطع الغيار من خلال:
        1. **الوضوح البصري:** رؤية القطع وحالتها فوراً.
        2. **الدقة المالية:** حساب التكاليف والجمارك آلياً.
        3. **السرعة اللوجستية:** تتبع حي للشحنات عبر الموانئ.
        """)
    with col2:
        # إضافة فيديو توضيحي (وسائط)
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # مثال لفيديو، ضع رابط فيديو مشروعك هنا

# --- تبويب 2: معرض الصور (وسائط بصرية) ---
with t_gallery:
    st.subheader("🖼️ معرض قطع الغيار والخدمات")
    cols = st.columns(3)
    with cols[0]:
        st.image("https://img.freepik.com/free-photo/car-engine-parts_23-2148970367.jpg", caption="محركات بجودة عالية")
    with cols[1]:
        st.image("https://img.freepik.com/free-photo/logistics-transportation-container-cargo-ship_335224-659.jpg", caption="عمليات الشحن اللوجستي")
    with cols[2]:
        st.image("https://img.freepik.com/free-photo/financial-report-charts-graphs-analysis-with-calculator_335224-954.jpg", caption="التحليل المالي الذكي")

# --- تبويب 3: التفاعل (أزرار ووسائل تفاعلية) ---
with t_interactive:
    st.subheader("🎮 جرب التفاعل مع النظام")
    col_btn1, col_btn2, col_btn3 = st.columns(3)
    
    if col_btn1.button("🔔 إرسال تنبيه للمستودع"):
        st.balloons() # رسوم متحركة تفاعلية
        st.write("✅ تم إرسال التنبيه الصوتي للمستودع في دبي!")
        
    if col_btn2.button("📦 تحديث حالة الشحنة"):
        st.toast("جاري تحديث البيانات من منفذ شحن...")
        st.write("📍 الشحنة الآن في **نقطة التفتيش الثالثة**")
        
    if col_btn3.button("💰 حساب الربح السريع"):
        st.snow() # رسوم متحركة أخرى
        st.info("نسبة الربح المتوقعة لهذه الشحنة: **22%**")

# --- تبويب 4: الرسوم البيانية (رسوم تفاعلية) ---
with t_analytics:
    st.subheader("📈 تحليلات البيانات التفاعلية")
    # رسم بياني تفاعلي (يتحرك مع الماوس)
    fig = go.Figure(data=[go.Pie(labels=['محركات', 'جير', 'فلاتر', 'إطارات'], values=[4500, 2500, 1050, 600], hole=.3)])
    fig.update_layout(template="plotly_dark", title_text="توزيع المخزون العالمي")
    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# 4- التذييل (نهاية المشروع)
# ==========================================
st.divider()
st.markdown("<p style='text-align: center;'>جميع الحقوق محفوظة © إمبراطورية باسل للوسائط المتعددة 2026</p>", unsafe_allow_html=True)
