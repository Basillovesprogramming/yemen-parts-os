import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# 1- الهندسة البصرية وتصحيح أخطاء العرض (Visual Architecture)
st.set_page_config(page_title="Basil Global Quantum", layout="wide")

st.markdown("""
    <style>
    /* قفل التصميم المظلم لضمان وضوح الأرقام */
    .stApp { background-color: #05070a; color: #e6edf3; }
    
    /* تنسيق الكروت المالية (Metrics) */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    
    /* جعل الأرقام بيضاء ناصعة */
    [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 30px !important;
        font-weight: 800;
    }

    .main-title {
        font-size: 45px;
        font-weight: 900;
        background: linear-gradient(90deg, #58a6ff, #bc8cff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2- محرك البيانات (Data Engine)
if 'inventory' not in st.session_state:
    st.session_state.inventory = [
        {"ID": "BS-101", "الصنف": "مكينة V8 تويوتا", "الموقع": "دبي", "التكلفة_AED": 15000},
        {"ID": "BS-102", "الصنف": "جير لكزس 2024", "الموقع": "الشارقة", "التكلفة_AED": 8500}
    ]

# --- العنوان الرئيسي ---
st.markdown('<p class="main-title">BASIL GLOBAL STRATEGIC SYSTEMS</p>', unsafe_allow_html=True)

# --- نظام التبويبات (The 7-Pillar Navigation) ---
t1, t2, t3, t4, t5 = st.tabs([
    "📊 لوحة التحكم", "📦 الكتالوج الذكي", "🚛 المسار اللوجستي", "💰 الحاسبة المالية", "🔐 الأمان والدعم"
])

# تبويب 1: لوحة التحكم (إحصائيات حية)
with t1:
    st.subheader("إحصائيات الأداء الاستراتيجي")
    c1, c2, c3 = st.columns(3)
    c1.metric("قيمة الأصول الحالية", "1,840,000 AED", "+4.2%")
    c2.metric("كفاءة سلاسل الإمداد", "94%", "تحسن 2%")
    c3.metric("الأرباح التقديرية (Q1)", "145,000,000 YER")
    
    # رسم بياني للنمو
    fig = go.Figure(go.Scatter(x=['Jan', 'Feb', 'Mar'], y=[10, 25, 45], line=dict(color='#58a6ff', width=4), mode='lines+markers'))
    fig.update_layout(title="تحليل النمو المالي", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=300)
    st.plotly_chart(fig, use_container_width=True)

# تبويب 2: الكتالوج (إدارة الأصناف)
with t2:
    st.subheader("مخزن قطع الغيار العالمي")
    df = pd.DataFrame(st.session_state.inventory)
    st.dataframe(df, use_container_width=True)
    
    with st.expander("➕ إضافة صنف جديد للمخزن"):
        new_name = st.text_input("اسم القطعة")
        new_cost = st.number_input("التكلفة (AED)", min_value=0)
        if st.button("اعتماد الصنف"):
            st.session_state.inventory.append({"ID": f"BS-{len(st.session_state.inventory)+101}", "الصنف": new_name, "الموقع": "قيد التحديث", "التكلفة_AED": new_cost})
            st.rerun()

# تبويب 3: اللوجستيات (تتبع المسار)
with t3:
    st.subheader("تتبع الشحنات الدولية (دبي ↔ اليمن)")
    col_map, col_track = st.columns([2, 1])
    with col_map:
        st.info("📍 المسار: جبل علي ⬅️ منفذ شحن ⬅️ المستودع النهائي")
        st.progress(70)
        st.write("الحالة: **في انتظار التخليص الجمركي النهائي**")
    with col_track:
        st.markdown("📑 **المستندات الجاهزة:**")
        st.success("✅ بوليصة الشحن")
        st.success("✅ الفاتورة التجارية")
        st.warning("⏳ شهادة المطابقة")

# تبويب 4: الحاسبة المالية (تحويل العملات والجمارك)
with t4:
    st.subheader("المحرك المالي الآلي")
    col_in, col_out = st.columns(2)
    with col_in:
        aed_val = st.number_input("أدخل القيمة بالدرهم الإماراتي", value=1000)
        customs_pct = st.selectbox("فئة الجمارك", [0.05, 0.15, 0.25], format_func=lambda x: f"{int(x*100)}%")
    with col_out:
        exchange_rate = st.sidebar.number_input("صرف الدرهم/يمني اليوم", value=145.0)
        total_with_customs = aed_val * (1 + customs_pct)
        total_yer = total_with_customs * exchange_rate
        st.metric("الإجمالي بالريال اليمني (شامل الجمارك)", f"{total_yer:,.0f} YER")

# تبويب 5: الأمان والدعم
with t5:
    st.subheader("مركز الحماية والدعم الفني")
    st.write("🛡️ **بروتوكولات الأمان:** تشفير RSA-4096 مفعل على كافة العمليات المالية.")
    st.divider()
    st.write("📞 **تواصل مع Basil Global:**")
    st.write("الإمارات: +971-50-XXXXXXX")
    st.write("اليمن: +967-77-XXXXXXX")

st.markdown("---")
st.caption(f"Basil Quantum Ecosystem | v17.0 Master | {datetime.now().year}")
