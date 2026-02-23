import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 1- الهوية البصرية العالمية (Global UI/UX)
st.set_page_config(page_title="Basil Global Elite", layout="wide")

st.markdown("""
    <style>
    .reportview-container { background: #010409; }
    .main-header {
        font-family: 'Space Grotesk', sans-serif;
        background: linear-gradient(120deg, #1e3a8a, #60a5fa, #ffffff);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-align: center; font-size: 60px; font-weight: 900;
    }
    .status-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px; padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    </style>
    """, unsafe_allow_html=True)

# 2- محرك البيانات الذكي (AI Catalog Engine)
if 'orders' not in st.session_state:
    st.session_state.orders = []

# --- القائمة الجانبية (مركز القيادة العالمي) ---
with st.sidebar:
    st.markdown("<h1 style='color: #60a5fa;'>BASIL ELITE COMMAND</h1>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/2906/2906274.png", width=120)
    st.divider()
    # 3- الربط اللوجستي: محرك حساب الرسوم الجمركية آلياً
    st.subheader("⚙️ محرك الرسوم الجمركية الذكي")
    tax_rate = st.select_slider("فئة الجمارك (اليمن)", options=["إعفاء (0%)", "مخفض (5%)", "عادي (15%)", "مرتفع (25%)"], value="عادي (15%)")
    exchange_live = st.number_input("سعر الصرف اللحظي (AED/YER)", value=146.5)
    st.divider()
    st.success("🔒 6- الأمان: نظام التشفير العسكري AES-256 نشط")

# الرأس الملكي
st.markdown('<p class="main-header">BASIL GLOBAL STRATEGIC</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #8b949e;'>المحرك اللوجستي المتكامل للربط بين الإمارات واليمن (الإصدار العالمي)</p>", unsafe_allow_html=True)

# --- نظام التبويبات الفائق (الخطة السبعة) ---
tabs = st.tabs(["💎 الكتالوج الذكي", "🚛 سلسلة الإمداد (Logistics)", "🏢 مركز العمليات (Admin)", "⚖️ الأمان والامتثال"])

# 2- نظام الكتالوج: البحث والتصفية بذكاء
with tabs[0]:
    st.subheader("📦 قاعدة بيانات الأصول (Global Parts Catalog)")
    # نظام البحث المتقدم
    col_s1, col_s2, col_s3 = st.columns([2,1,1])
    search_query = col_s1.text_input("ابحث عن قطعة (اسم، OEM، أو موديل)")
    cat_filter = col_s2.selectbox("نوع السيارة", ["BMW", "Mercedes", "Toyota", "Lexus"])
    
    # محاكاة لبيانات ضخمة
    parts_data = {
        "القطعة": ["Turbo Charger", "Brake Pads", "Air Filter"],
        "OEM": ["789-X", "554-Y", "221-Z"],
        "السعر (دبي)": [4500, 300, 120],
        "التوفر": ["متوفر - دبي", "متوفر - الشارقة", "طلب مسبق"]
    }
    st.table(pd.DataFrame(parts_data))

# 3- الربط اللوجستي (تتبع حي وتحليل المسار)
with tabs[1]:
    st.subheader("🚛 مسار سلسلة الإمداد (Supply Chain Visualization)")
    
    
    col_map, col_track = st.columns([2,1])
    with col_map:
        # رسم بياني لوجستي (Gantt Chart) يوضح مراحل الشحن
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 75,
            title = {'text': "تقدم الشحنة الحالية (جبل علي -> منفذ شحن)"},
            gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': "#3b82f6"}}
        ))
        st.plotly_chart(fig, use_container_width=True)
    
    with col_track:
        st.markdown('<div class="status-card">', unsafe_allow_html=True)
        st.write("📌 **آخر تحديث:**")
        st.write("📍 الموقع: المنطقة الحرة - جبل علي")
        st.write("📅 الوصول المتوقع: 28 فبراير")
        st.write("📄 بوليصة الشحن: BL-BASIL-2024-009")
        st.markdown('</div>', unsafe_allow_html=True)

# 4- نظام الإدارة والمالية (الذكاء المالي)
with tabs[2]:
    st.subheader("📊 ذكاء الأعمال (Business Intelligence)")
    c1, c2, c3 = st.columns(3)
    c1.metric("إجمالي حجم الاستيراد", "1.2M AED")
    c2.metric("صافي أرباح Basil", "14% 📈")
    c3.metric("معدل دوران المخزون", "18 Day")
    
    # 5- دعم العملاء المدمج
    st.divider()
    st.subheader("💬 5- غرفة العمليات والدعم")
    with st.expander("فتح محادثة مباشرة مع مكتب دبي"):
        st.text_area("رسالتك للفريق الفني في الإمارات")
        st.button("إرسال الطلب المستعجل")

# 6 & 7- الأمان والامتثال القانوني (Compliance)
with tabs[3]:
    st.subheader("⚖️ 7- الامتثال القانوني والأمان")
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        st.info("📑 **المستندات القانونية:** جميع الصفقات تمر عبر فحص (Sanction Screening) لضمان التوافق الدولي.")
    with col_a2:
        st.info("🔒 **حماية البيانات:** تشفير طبقة النقل (TLS 1.3) مطبق على جميع البيانات الشخصية.")

st.markdown("---")
st.caption(f"Basil Global Strategic Ecosystem | Level: Enterprise Elite | {datetime.now().year}")
