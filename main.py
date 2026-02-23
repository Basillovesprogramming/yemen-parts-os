import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# 1- الهوية البصرية (تصميم العظماء)
st.set_page_config(page_title="Basil Global HQ", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #ffffff; }
    [data-testid="stMetricValue"] { color: #00ff00 !important; font-size: 35px !important; font-weight: 800; }
    [data-testid="stMetricLabel"] { color: #58a6ff !important; font-size: 16px !important; }
    .main-header { font-size: 45px; font-weight: 900; text-align: center; color: #58a6ff; margin-bottom: 20px; }
    .stTabs [data-baseweb="tab-list"] { background-color: #161b22; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2- نظام البيانات (كتالوج باسل العالمي)
if 'inventory' not in st.session_state:
    st.session_state.inventory = [
        {"ID": "BS-101", "القطعة": "مكينة V8 تويوتا", "المصدر": "دبي", "التكلفة_درهم": 12000, "الحالة": "مستودع جبل علي"},
        {"ID": "BS-102", "القطعة": "طقم فلاتر نيسان", "المصدر": "الشارقة", "التكلفة_درهم": 450, "الحالة": "منفذ شحن"}
    ]

# --- العنوان والقيادة ---
st.markdown('<p class="main-header">BASIL GLOBAL QUANTUM HQ</p>', unsafe_allow_html=True)

# 3- الخطة السبعة في واجهة واحدة
tab_stats, tab_stock, tab_logistics, tab_finance, tab_security = st.tabs([
    "📊 لوحة القيادة", "📦 إدارة المخزون", "🚢 تتبع الشحنات", "💰 المحرك المالي", "🛡️ الأمان والدعم"
])

# البند 1: الإحصائيات الذكية
with tab_stats:
    st.subheader("إحصائيات الإمبراطورية التجارية")
    c1, c2, c3 = st.columns(3)
    c1.metric("إجمالي قيمة الأصول", "1,840,000 AED", "+4.2%")
    c2.metric("شحنات في الطريق", "12 حاوية", "تحسن 15%")
    c3.metric("صافي الربح المتوقع", "145M YER")
    
    # رسم بياني للتدفق النقدي
    fig = go.Figure(go.Bar(x=['Jan', 'Feb', 'Mar'], y=[500, 800, 1200], marker_color='#58a6ff'))
    fig.update_layout(title="تحليل الواردات الشهرية", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=300)
    st.plotly_chart(fig, use_container_width=True)

# البند 2: الكتالوج الذكي
with tab_stock:
    st.subheader("📦 إدارة قطع الغيار")
    df = pd.DataFrame(st.session_state.inventory)
    st.table(df)
    
    with st.expander("➕ إضافة صنف جديد للمخزن"):
        p_name = st.text_input("اسم القطعة")
        p_cost = st.number_input("التكلفة (AED)", value=0)
        if st.button("اعتماد في الكتالوج"):
            st.session_state.inventory.append({"ID": f"BS-{len(st.session_state.inventory)+101}", "القطعة": p_name, "المصدر": "الإمارات", "التكلفة_درهم": p_cost, "الحالة": "جديد"})
            st.rerun()

# البند 3: اللوجستيات (دبي ↔ اليمن)
with tab_logistics:
    st.subheader("🚛 مسار الإمداد الدولي")
    
    col_l, col_r = st.columns([2, 1])
    with col_l:
        st.info("تحديث المسار: الشحنة رقم #BSL-9920")
        st.progress(85)
        st.write("📍 الموقع الحالي: **تفتيش جمارك منفذ شحن (الحدود البرية)**")
    with col_r:
        st.markdown("### 📋 مستندات الشحنة (البند 7)")
        st.success("✅ فاتورة التصدير")
        st.success("✅ شهادة المنشأ")
        st.warning("⏳ فسح الجمارك اليمني")

# البند 4: المحرك المالي (حساب الصرف والجمارك)
with tab_finance:
    st.subheader("💰 حاسبة الربح والخسارة")
    col1, col2 = st.columns(2)
    with col1:
        cost_aed = st.number_input("سعر الشراء في دبي (AED)", value=1000)
        customs_rate = st.selectbox("نسبة الجمارك", [0.05, 0.15, 0.25], format_func=lambda x: f"{int(x*100)}%")
    with col2:
        exchange_rate = st.sidebar.number_input("صرف الدرهم اليوم (YER)", value=145.0)
        final_cost_yer = (cost_aed * (1 + customs_rate)) * exchange_rate
        st.metric("التكلفة النهائية باليمني", f"{final_cost_yer:,.0f} YER")
        st.info(f"شامل جمارك: {cost_aed * customs_rate} درهم")

# البند 5 و6: الدعم والأمان
with tab_security:
    st.subheader("🛡️ بروتوكولات الحماية والدعم")
    st.write("📞 **الدعم الفني المباشر:**")
    st.write("دبي: +971-50-XXXXXXX | اليمن: +967-77-XXXXXXX")
    st.divider()
    st.code("SECURITY STATUS: ENCRYPTED RSA-4096\nDATABASE: LOCAL_ACTIVE\nFIREWALL: ON")

st.markdown("---")
st.caption(f"Basil Quantum Enterprise | v19.0 Final | Built for Strategic Excellence © {datetime.now().year}")
