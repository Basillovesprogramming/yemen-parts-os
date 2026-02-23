import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# 1. الإعدادات السيادية للنظام (دمج عقول الذكاء الاصطناعي في التصميم)
st.set_page_config(page_title="BASIL | Basil Global", layout="wide", initial_sidebar_state="expanded")

# تصميم UI/UX فائق الفخامة (Dark & Professional Gold Theme)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    /* تنسيق العنوان الملكي */
    .royal-header {
        background: linear-gradient(90deg, #1e3a8a, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 50px;
        font-weight: 900;
        padding: 20px;
        letter-spacing: 2px;
        border-bottom: 2px solid #3b82f6;
    }
    /* تنسيق الكروت الإحصائية لتبدو كأنها شاشات طيران */
    [data-testid="stMetric"] {
        background-color: #1a1f2c !important;
        border: 1px solid #3b82f6 !important;
        border-radius: 20px !important;
        padding: 25px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5) !important;
    }
    [data-testid="stMetricValue"] { color: #60a5fa !important; font-size: 35px !important; }
    [data-testid="stMetricLabel"] { color: #94a3b8 !important; font-size: 20px !important; }
    
    /* تنسيق الجداول والتبويبات */
    .stTabs [data-baseweb="tab-list"] { background-color: #1a1f2c; border-radius: 15px; }
    .stTabs [data-baseweb="tab"] { color: #94a3b8 !important; font-size: 18px; }
    .stTabs [aria-selected="true"] { color: #60a5fa !important; border-bottom-color: #60a5fa !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. محرك البيانات الاستراتيجي
if 'inv' not in st.session_state: st.session_state.inv = []
if 'sales_book' not in st.session_state: st.session_state.sales_book = []

# --- القائمة الجانبية (مركز التحكم العالمي) ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #60a5fa;'>BGSL CONTROL</h1>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/2906/2906274.png", width=100)
    st.divider()
    usd_yer = st.number_input("💵 سعر صرف الدولار الحالي", value=530)
    sar_yer = st.number_input("🇸🇦 سعر صرف السعودي الحالي", value=140)
    target_profit = st.slider("🎯 مستهدف الربح (%)", 5, 100, 25)
    st.divider()
    st.write(f"🛡️ الحالة: نظام باسل نشط")

# العنوان الرئيسي الفخم
st.markdown('<p class="royal-header">BASSEM GLOBAL STRATEGIC LOGISTICS</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 20px;'>INTEGRATED SUPPLY CHAIN & FINANCIAL INTELLIGENCE</p>", unsafe_allow_html=True)

# --- نظام التبويبات المتقدم ---
t1, t2, t3, t4 = st.tabs(["💎 المشتريات الدولية", "📦 الأصول والمخزون", "💰 مركز المبيعات", "📈 التحليل الاستراتيجي"])

# 1. المشتريات والتسعير
with t1:
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.subheader("🛠️ تسعير وتكويد بضاعة جديدة")
        item = st.text_input("وصف القطعة (Item Name)")
        oem = st.text_input("الرقم المرجعي (OEM Reference)")
        p_aed = st.number_input("تكلفة الشراء - دبي (AED)", min_value=0.0, value=1000.0)
        s_aed = st.number_input("تكلفة الشحن الدولي (Shipment)", value=100.0)
        tax = st.number_input("الرسوم والضرائب الجمركية (%)", value=10)
        
        # العملية الحسابية الاحترافية
        landed_cost_usd = ((p_aed + s_aed) / 3.67) * (1 + tax/100)
        cost_yer = landed_cost_usd * usd_yer
        sell_yer = cost_yer * (1 + target_profit/100)

    with c2:
        st.subheader("📊 ذكاء التسعير")
        st.metric("سعر البيع المقترح (YER)", f"{round(sell_yer):,}")
        st.metric("سعر البيع المقترح (SAR)", f"{round(sell_yer/sar_yer):,}")
        st.metric("صافي الربح المتوقع", f"{round(sell_yer - cost_yer):,}")
        
        if st.button("🚀 تعميد الصفقة وإرسالها للأصول"):
            st.session_state.inv.append({
                "ID": len(st.session_state.inv)+1,
                "القطعة": item,
                "OEM": oem,
                "التكلفة_YER": round(cost_yer),
                "البيع_YER": round(sell_yer)
            })
            st.success("تم نقل البيانات بنجاح إلى قاعدة الأصول")

# 2. المخزون
with t2:
    st.subheader("📦 إدارة الأصول والمخزون الحالي")
    if st.session_state.inv:
        st.dataframe(pd.DataFrame(st.session_state.inv), use_container_width=True)
    else:
        st.info("بانتظار وصول شحنات جديدة لجدولتها")

# 3. صالة المبيعات
with t3:
    if st.session_state.inv:
        st.subheader("🛒 تنفيذ عملية بيع استراتيجية")
        choice = st.selectbox("اختر الصنف من المخزن", [f"{i['القطعة']} | {i['OEM']}" for i in st.session_state.inv])
        client = st.text_input("اسم العميل / الشركة")
        
        if st.button("✅ تأكيد البيع وإصدار الفاتورة"):
            data = next(i for i in st.session_state.inv if f"{i['القطعة']} | {i['OEM']}" == choice)
            st.session_state.sales_book.append({
                "التاريخ": datetime.now().strftime("%Y-%m-%d"),
                "العميل": client,
                "الصنف": choice,
                "الإيراد": data['البيع_YER'],
                "الربح_الصافي": data['البيع_YER'] - data['التكلفة_YER']
            })
            st.balloons()
            st.success("تمت العملية وأرشفة البيانات")
    else:
        st.warning("المستودع خالي، لا يمكن تنفيذ مبيعات")

# 4. التحليل الاستراتيجي (عقل الذكاء الاصطناعي)
with t4:
    st.subheader("📈 تقارير النمو والذكاء المالي")
    if st.session_state.sales_book:
        df = pd.DataFrame(st.session_state.sales_book)
        m1, m2, m3 = st.columns(3)
        m1.metric("إجمالي حجم التداول", f"{df['الإيراد'].sum():,} YER")
        m2.metric("صافي الأرباح المحققة", f"{df['الربح_الصافي'].sum():,} YER")
        m3.metric("عدد الصفقات المنفذة", len(df))
        
        st.divider()
        fig = px.area(df, x="التاريخ", y="الربح_الصافي", title="منحنى نمو الأرباح الاستراتيجي", 
                      color_discrete_sequence=['#60a5fa'])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("بانتظار أول عملية بيع لتوليد المصفوفات التحليلية")

st.markdown("---")
st.caption("BGSL Platform v6.0 | Engineered by Basil's Digital Partner")
