import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import time

# ==========================================
# 1- الإعدادات والهوية (The Sovereign Identity)
# ==========================================
st.set_page_config(page_title="BASIL GLOBAL OS", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    .stApp { background: #05070a; color: #ffffff; }
    [data-testid="stMetric"] {
        background: #161b22; border: 1px solid #30363d;
        border-radius: 15px; padding: 20px;
    }
    [data-testid="stMetricValue"] { color: #00ff88 !important; }
    .main-header { font-size: 40px; font-weight: 900; color: #58a6ff; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2- قاعدة البيانات (Database Logic)
# ==========================================
if 'stock' not in st.session_state:
    st.session_state.stock = pd.DataFrame([
        {"الكود": "P-01", "القطعة": "مكينة تويوتا", "الكمية": 5, "التكلفة_درهم": 12000},
        {"الكود": "P-02", "القطعة": "جير لكزس", "الكمية": 3, "التكلفة_درهم": 8500}
    ])

if 'debts' not in st.session_state:
    st.session_state.debts = pd.DataFrame([
        {"الزبون": "شركة الأمل", "المبلغ_يمني": 5000000, "الحالة": "متبقي"},
        {"الزبون": "محل البركة", "المبلغ_يمني": 1200000, "الحالة": "خالص"}
    ])

# ==========================================
# 3- القائمة الجانبية (Control Center)
# ==========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown("### BASIL ADMIN")
    st.divider()
    ex_rate = st.number_input("سعر الصرف اليوم (AED/YER)", value=145.0)
    st.divider()
    st.write("📞 الدعم الفني: +967-XXXXXXX")
    st.audio("https://www.soundjay.com/buttons/sounds/button-20.mp3")

# ==========================================
# 4- المحتوى الرئيسي (The 7 Pillars)
# ==========================================
st.markdown('<p class="main-header">BASIL GLOBAL STRATEGIC OS</p>', unsafe_allow_html=True)

tab_fin, tab_stock, tab_logistics, tab_debts, tab_media = st.tabs([
    "💰 المالية والارباح", "📦 المخزن والكتالوج", "🚛 الشحن والجمارك", "📝 سجل الديون", "🎥 الوسائط"
])

# --- التبويب 1: المالية ---
with tab_fin:
    st.subheader("تحليل الأرباح والخسائر")
    c1, c2, c3 = st.columns(3)
    total_cost_aed = (st.session_state.stock['التكلفة_درهم'] * st.session_state.stock['الكمية']).sum()
    c1.metric("رأس مال المخزن (AED)", f"{total_cost_aed:,.0f}")
    c2.metric("قيمة المخزن (YER)", f"{total_cost_aed * ex_rate:,.0f}")
    c3.metric("صافي الربح المتوقع", "22%", "+5%")
    
    # حاسبة الجمارك التفاعلية
    st.divider()
    st.write("### 🧮 حاسبة التكلفة النهائية")
    price = st.number_input("سعر القطعة في دبي", value=1000)
    ship = st.number_input("تكلفة الشحن", value=200)
    customs = st.slider("نسبة الجمارك %", 0, 50, 15)
    total = (price + ship) * (1 + customs/100)
    st.info(f"التكلفة النهائية باليمني: {total * ex_rate:,.0f} ريال")

# --- التبويب 2: المخزن ---
with tab_stock:
    st.subheader("📦 إدارة المخزون المركزي")
    st.dataframe(st.session_state.stock, use_container_width=True)
    with st.expander("➕ إضافة صنف جديد"):
        c_n = st.text_input("اسم القطعة")
        c_q = st.number_input("الكمية", min_value=1)
        c_p = st.number_input("التكلفة بالدرهم")
        if st.button("حفظ في المخزن"):
            new_item = {"الكود": f"P-0{len(st.session_state.stock)+1}", "القطعة": c_n, "الكمية": c_q, "التكلفة_درهم": c_p}
            st.session_state.stock = pd.concat([st.session_state.stock, pd.DataFrame([new_item])], ignore_index=True)
            st.rerun()

# --- التبويب 3: اللوجستيات ---
with tab_logistics:
    st.subheader("🚛 مسار الإمداد الدولي")
    
    st.info("📍 الشحنة الحالية: **منفذ شحن الحدودي**")
    st.progress(70)
    st.write("📑 **البند 7 (القانون):** تأكد من مطابقة أرقام المكائن مع بوليصة الشحن لتجنب الحجز.")

# --- التبويب 4: الديون والعملاء ---
with tab_debts:
    st.subheader("📝 سجل المديونيات والزبائن")
    st.table(st.session_state.debts)
    if st.button("تنبيه الزبائن المتأخرين"):
        st.warning("تم إرسال إشعارات آلية للزبائن الذين عليهم مبالغ متبقية.")

# --- التبويب 5: الوسائط ---
with tab_media:
    st.subheader("📽️ المعرض التفاعلي")
    col_v, col_a = st.columns(2)
    with col_v:
        st.video("https://www.youtube.com/watch?v=36YnV9STBqc")
    with col_a:
        st.image("https://img.freepik.com/free-photo/industrial-design-concept-with-engine_23-2150141323.jpg")
        if st.button("🎉 تفعيل احتفال الأرباح"):
            st.balloons()
            st.audio("https://www.soundjay.com/misc/sounds/bell-ringing-01.mp3")

st.divider()
st.caption(f"BASIL GLOBAL v27.0 | The Industrial Masterpiece | © {datetime.now().year}")
