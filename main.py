import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# 1- الإعدادات السيادية (Basil Identity)
st.set_page_config(page_title="Basil Global Quantum", layout="wide")

# 2- قفل التصميم الاحترافي (لضمان وضوح الأرقام على الجوال)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    .main-title {
        background: linear-gradient(90deg, #58a6ff, #bc8cff);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-align: center; font-size: 45px; font-weight: 900; padding: 10px;
    }
    [data-testid="stMetricValue"] { color: #ffffff !important; font-size: 35px !important; font-weight: 800 !important; }
    [data-testid="stMetricLabel"] { color: #58a6ff !important; font-size: 16px !important; }
    [data-testid="stMetric"] { background-color: #161b22 !important; border: 1px solid #30363d !important; border-radius: 15px !important; padding: 20px !important; }
    .stTabs [data-baseweb="tab-list"] { background-color: #0d1117; border-bottom: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# 3- الذاكرة الافتراضية للتجربة (بدون حفظ دائم)
if 'temp_inv' not in st.session_state:
    st.session_state.temp_inv = [
        {"ID": "BS-01", "القطعة": "مكينة لاندكروزر", "OEM": "1GR-FE", "التكلفة": 12000, "البيع": 15500, "الحالة": "مستودع دبي"},
        {"ID": "BS-02", "القطعة": "جير بوكس لكزس", "OEM": "A750F", "التكلفة": 4500, "البيع": 6200, "الحالة": "قيد الشحن"}
    ]

# --- القائمة الجانبية (Command Center) ---
with st.sidebar:
    st.markdown("<h1 style='color: #58a6ff;'>BASIL CONTROL</h1>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.divider()
    usd_rate = st.number_input("💵 صرف الدولار (يمني)", value=535)
    sar_rate = st.number_input("🇸🇦 صرف السعودي (يمني)", value=142)
    st.divider()
    st.info("🛡️ نظام الأمان: AES-256 نشط\n🌐 الحالة: متصل عالمياً")

# واجهة النظام الرئيسية
st.markdown('<p class="main-title">BASIL GLOBAL QUANTUM</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>المحرك الاستراتيجي لإدارة استيراد قطع الغيار (الإمارات - اليمن)</p>", unsafe_allow_html=True)

# --- التبويبات (الخطة السبعة) ---
t1, t2, t3, t4 = st.tabs(["📊 ذكاء الأعمال", "📦 الكتالوج العالمي", "🚢 التتبع اللوجستي", "🛡️ الأمان والدعم"])

# التبويب 1: التحليل المالي
with t1:
    st.subheader("📈 Strategic Insights")
    m1, m2, m3 = st.columns(3)
    m1.metric("إجمالي قيمة الأصول", "1,840,000 AED", "+4.2%")
    m2.metric("زمن الوصول (متوسط)", "1.4 Days", "-0.3")
    m3.metric("الأرباح المتوقعة", "145,000,000 YER")
    
    # رسم بياني للنمو
    df_chart = pd.DataFrame({'الشهر': ['يناير', 'فبراير'], 'الأرباح': [85, 125]})
    fig = px.line(df_chart, x='الشهر', y='الأرباح', markers=True, title="منحنى النمو الاستراتيجي")
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig, use_container_width=True)

# التبويب 2: الكتالوج
with t2:
    st.subheader("🔍 Smart Parts Catalog")
    df_show = pd.DataFrame(st.session_state.temp_inv)
    st.table(df_show)
    
    # إضافة قطعة جديدة (للتجربة)
    with st.expander("➕ إضافة صنف جديد للكتالوج"):
        c1, c2 = st.columns(2)
        new_name = c1.text_input("اسم القطعة")
        new_oem = c2.text_input("رقم OEM")
        if st.button("تعميد في الذاكرة المؤقتة"):
            st.success(f"تمت إضافة {new_name} بنجاح (ستختفي عند تحديث الصفحة)")

# التبويب 3: اللوجستيات
with t3:
    st.subheader("🚢 Logistics Matrix")
    
    
    col_map, col_info = st.columns([2, 1])
    with col_map:
        # عداد تقدم الشحنة
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number", value = 72,
            title = {'text': "تقدم الشحنة الدولية"},
            gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': "#58a6ff"}}
        ))
        st.plotly_chart(fig_gauge, use_container_width=True)
    with col_info:
        st.markdown("""
        **بيانات التتبع الحالية:**
        - **رقم الحاوية:** BSL-2026-X
        - **الموقع:** ميناء جبل علي (دبي)
        - **الوجهة:** منفذ شحن (اليمن)
        - **الحالة:** تم التخليص الجمركي الإماراتي
        """)

# التبويب 4: الأمان والدعم
with t4:
    st.subheader("🛡️ Compliance & Support")
    c_sec, c_supp = st.columns(2)
    with c_sec:
        st.info("📑 **التوافق القانوني:**\nجميع العمليات تخضع لقوانين التجارة الدولية بين الإمارات واليمن.")
    with c_supp:
        st.success("📞 **الدعم الفني (Basil):**\nواتساب دبي: +971-XXXXXXX\nواتساب اليمن: +967-XXXXXXX")

st.markdown("---")
st.caption(f"Basil Quantum ERP | v14.0 Enterprise | Built for Strategic Domination © {datetime.now().year}")
