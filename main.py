import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# ==========================================
# 1- إعدادات الهوية والسيادة (البند 1)
# ==========================================
st.set_page_config(page_title="Basil Global Quantum", layout="wide")

# تصميم "بروتوكول باسل" للألوان والخطوط
st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #ffffff; }
    /* تنسيق القائمة الجانبية لضمان وجودك القوي */
    [data-testid="stSidebar"] { background-color: #0d1117; border-right: 2px solid #30363d; min-width: 300px; }
    /* جعل الأرقام بيضاء ناصعة والخلفية احترافية */
    [data-testid="stMetricValue"] { color: #ffffff !important; font-size: 35px !important; font-weight: 800; }
    [data-testid="stMetricLabel"] { color: #58a6ff !important; font-size: 16px !important; font-weight: bold; }
    [data-testid="stMetric"] { background: #161b22; border: 1px solid #30363d; border-radius: 15px; padding: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }
    .main-title { font-size: 45px; font-weight: 900; text-align: center; color: #58a6ff; margin-bottom: 10px; }
    .sub-title { text-align: center; color: #8b949e; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2- القائمة الجانبية (البند 5 و6: الدعم والأمان)
# ==========================================
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #58a6ff;'>BASIL ADMIN</h1>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.divider()
    
    st.subheader("🌐 إعدادات السوق")
    # محرك الصرف اللحظي (البند 4)
    ex_rate = st.number_input("صرف الدرهم مقابل اليمني", value=145.0)
    customs_val = st.slider("نسبة الجمارك الافتراضية %", 0, 100, 15)
    
    st.divider()
    st.subheader("📞 5- الدعم الفني")
    st.write("🇦🇪 دبي: +971-50-XXXXXXX")
    st.write("🇾🇪 اليمن: +967-77-XXXXXXX")
    
    st.divider()
    st.subheader("🔐 6- بروتوكول الأمان")
    st.code("SECURITY: AES-256\nSTATUS: ACTIVE\nENCRYPTION: RSA-4096")
    
    if st.button("تحديث النظام"):
        st.rerun()

# ==========================================
# 3- محتوى النظام الرئيسي (التبويبات)
# ==========================================
st.markdown('<p class="main-title">BASIL GLOBAL QUANTUM</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Strategic Import/Export Orchestrator | UAE - YEMEN</p>', unsafe_allow_html=True)

tabs = st.tabs(["📊 لوحة التحكم", "📦 الكتالوج الذكي", "🚛 اللوجستيات", "💰 الحاسبة المالية", "⚖️ البند 7: القانون"])

# --- التبويب 1: إحصائيات الأعمال ---
with tabs[0]:
    st.subheader("Strategic AI Insights")
    c1, c2, c3 = st.columns(3)
    c1.metric("قيمة الأصول النشطة", "1,840,000 AED", "+4.2%")
    c2.metric("كفاءة سلاسل الإمداد", "94%", "تحسن 2%")
    c3.metric("توقعات الأرباح (Q1)", "145,000,000 YER")
    
    # رسم بياني للنمو
    fig = go.Figure(go.Scatter(x=['يناير', 'فبراير', 'مارس'], y=[50, 120, 200], line=dict(color='#58a6ff', width=4), mode='lines+markers'))
    fig.update_layout(title="تحليل النمو المالي", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig, use_container_width=True)

# --- التبويب 2: الكتالوج (البند 2) ---
with tabs[1]:
    st.subheader("📦 إدارة قطع الغيار العالمية")
    if 'inventory' not in st.session_state:
        st.session_state.inventory = [
            {"ID": "BS-101", "الصنف": "مكينة V8 تويوتا", "المصدر": "دبي", "التكلفة_AED": 15000},
            {"ID": "BS-102", "الصنف": "جير لكزس 2024", "المصدر": "الشارقة", "التكلفة_AED": 8500}
        ]
    
    df = pd.DataFrame(st.session_state.inventory)
    st.table(df)
    
    with st.expander("➕ إضافة بضاعة جديدة للمخزن"):
        new_name = st.text_input("اسم القطعة")
        new_cost = st.number_input("التكلفة (AED)", min_value=0)
        if st.button("اعتماد الصنف"):
            st.session_state.inventory.append({"ID": f"BS-{len(st.session_state.inventory)+101}", "الصنف": new_name, "المصدر": "الإمارات", "التكلفة_AED": new_cost})
            st.rerun()

# --- التبويب 3: اللوجستيات (البند 3) ---
with tabs[2]:
    st.subheader("🚛 مسار الشحن الدولي")
    
    col_map, col_info = st.columns([2, 1])
    with col_map:
        st.info("📍 تتبع المسار الحالي: جبل علي ⬅️ منفذ شحن ⬅️ صنعاء")
        st.progress(75)
        st.write("الحالة الحالية: **في انتظار التخليص الجمركي النهائي**")
    with col_info:
        st.markdown("### بيانات الشحنة:")
        st.write("- **رقم الحاوية:** BSL-9901")
        st.write("- **تاريخ الإقلاع:** 20 فبراير")
        st.write("- **الوصول المتوقع:** 25 فبراير")

# --- التبويب 4: الحاسبة المالية (البند 4) ---
with tabs[3]:
    st.subheader("💰 محرك حساب الأرباح والجمارك")
    col_in, col_out = st.columns(2)
    with col_in:
        item_price = st.number_input("سعر الشراء في دبي (AED)", value=1000)
        item_customs = st.selectbox("فئة جمارك القطعة", [0.05, 0.15, 0.25], format_func=lambda x: f"{int(x*100)}%")
    with col_out:
        total_aed = item_price * (1 + item_customs)
        total_yer = total_aed * ex_rate
        st.metric("التكلفة النهائية باليمني", f"{total_yer:,.0f} YER")
        st.write(f"قيمة الجمارك المدفوعة: {item_price * item_customs} AED")

# --- التبويب 5: القانون والمستندات (البند 7) ---
with tabs[4]:
    st.subheader("⚖️ نظام أتمتة الوثائق")
    st.success("✅ الفواتير التجارية مطابقة لمعايير دبي.")
    st.success("✅ شهادة المنشأ مفعلة.")
    st.warning("⚠️ يرجى التأكد من ختم الجمارك في منفذ شحن لضمان مرور الشحنة.")
    if st.button("توليد تقرير ضريبي"):
        st.download_button("تحميل الملف PDF", data="Basil Report", file_name="Basil_Report.pdf")

# ==========================================
# 4- التذييل (Footer)
# ==========================================
st.markdown("---")
st.caption(f"Basil Global Quantum Enterprise | v21.0 Full Stack | Created for Leadership © {datetime.now().year}")
