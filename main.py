import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# 1. الإعدادات السيادية للنظام (تصميم Basil الخاص)
st.set_page_config(page_title="Basil Global Systems", layout="wide", initial_sidebar_state="expanded")

# تصميم UI/UX فائق الفخامة (ألوان الهوية الاحترافية)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    /* العنوان الملكي باسم باسل */
    .royal-header {
        background: linear-gradient(90deg, #1e3a8a, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 55px;
        font-weight: 900;
        padding: 10px;
        margin-bottom: 0px;
    }
    .sub-text { color: #94a3b8; text-align: center; font-size: 20px; margin-bottom: 30px; }
    
    /* تنسيق كروت الأرقام (Metrics) لضمان الوضوح التام */
    [data-testid="stMetric"] {
        background-color: #1a1f2c !important;
        border: 1px solid #3b82f6 !important;
        border-radius: 20px !important;
        padding: 25px !important;
    }
    [data-testid="stMetricValue"] { color: #60a5fa !important; font-size: 35px !important; font-weight: bold !important; }
    [data-testid="stMetricLabel"] { color: #ffffff !important; font-size: 18px !important; }
    
    /* تنسيق الأزرار والتبويبات */
    .stButton>button { width: 100%; border-radius: 10px; background-color: #1e3a8a; color: white; height: 50px; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #3b82f6; border: none; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; background-color: #1a1f2c; padding: 10px; border-radius: 15px; }
    .stTabs [data-baseweb="tab"] { color: #94a3b8 !important; font-size: 18px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. نظام حفظ البيانات (الذاكرة المركزية للنظام)
if 'inventory' not in st.session_state: st.session_state.inventory = []
if 'sales_ledger' not in st.session_state: st.session_state.sales_ledger = []

# --- لوحة التحكم الجانبية (Control Center) ---
with st.sidebar:
    st.markdown(f"<h1 style='text-align: center; color: #60a5fa;'>Basil Control</h1>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
    st.divider()
    st.markdown("### 💹 إدارة العملات")
    usd_rate = st.number_input("💵 سعر صرف الدولار (يمني)", value=530)
    sar_rate = st.number_input("🇸🇦 سعر صرف السعودي (يمني)", value=140)
    st.divider()
    profit_margin = st.slider("📈 تحديد هامش الربح (%)", 5, 100, 25)
    st.divider()
    st.write(f"🛡️ حالة النظام: Basil OS نشط")

# واجهة النظام الرئيسية
st.markdown('<p class="royal-header">BASIL GLOBAL LOGISTICS</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">منصة باسل المتكاملة لإدارة الاستيراد، المخازن، والذكاء المالي</p>', unsafe_allow_html=True)

# --- التبويبات الرئيسية ---
tab1, tab2, tab3, tab4 = st.tabs(["🚀 مشتريات دبي", "📦 المستودع الذكي", "🛒 مركز المبيعات", "📊 تحليل النمو"])

# 1. قسم المشتريات والتسعير
with tab1:
    col_input, col_view = st.columns([1.5, 1])
    with col_input:
        st.subheader("📥 إدخال شحنة جديدة")
        item_name = st.text_input("اسم قطعة الغيار")
        part_number = st.text_input("رقم القطعة (OEM No.)")
        c1, c2 = st.columns(2)
        price_aed = c1.number_input("سعر الشراء (درهم)", min_value=0.0)
        shipping_aed = c2.number_input("تكلفة الشحن (درهم)", value=15.0)
        customs_pct = st.number_input("الجمارك والضرائب (%)", value=10)
        
        # معادلات التحليل المالي
        total_aed = price_aed + shipping_aed
        cost_usd = (total_aed / 3.67) * (1 + customs_pct/100)
        cost_yer = cost_usd * usd_rate
        suggested_sell = cost_yer * (1 + profit_margin/100)

    with col_view:
        st.subheader("💰 التحليل المالي")
        st.metric("سعر البيع المقترح (يمني)", f"{round(suggested_sell):,} YER")
        st.metric("سعر البيع المقترح (سعودي)", f"{round(suggested_sell/sar_rate):,} SAR")
        st.metric("صافي الربح المتوقع", f"{round(suggested_sell - cost_yer):,} YER")
        
        if st.button("✅ تعميد وإضافة للمخزن"):
            st.session_state.inventory.append({
                "ID": len(st.session_state.inventory)+1,
                "القطعة": item_name,
                "OEM": part_number,
                "التكلفة_يمني": round(cost_yer),
                "البيع_يمني": round(suggested_sell)
            })
            st.success(f"تمت إضافة {item_name} بنجاح")
            st.balloons()

# 2. المستودع
with tab2:
    st.subheader("📦 إدارة أصول المستودع")
    if st.session_state.inventory:
        df_inv = pd.DataFrame(st.session_state.inventory)
        st.dataframe(df_inv, use_container_width=True)
    else:
        st.info("المستودع فارغ حالياً")

# 3. المبيعات
with tab3:
    if st.session_state.inventory:
        st.subheader("🛒 تنفيذ عملية بيع")
        options = [f"{i['القطعة']} | {i['OEM']}" for i in st.session_state.inventory]
        selection = st.selectbox("اختر الصنف المراد بيعه", options)
        buyer = st.text_input("اسم المشتري / الزبون")
        
        if st.button("💾 إتمام البيع والأرشفة"):
            item_data = next(i for i in st.session_state.inventory if f"{i['القطعة']} | {i['OEM']}" == selection)
            st.session_state.sales_ledger.append({
                "التاريخ": datetime.now().strftime("%Y-%m-%d"),
                "الزبون": buyer,
                "الصنف": selection,
                "المبلغ": item_data['البيع_يمني'],
                "الربح": item_data['البيع_يمني'] - item_data['التكلفة_يمني']
            })
            st.success("تمت عملية البيع وحفظ الفاتورة")
    else:
        st.warning("يجب إضافة بضاعة للمستودع أولاً")

# 4. التقارير والذكاء المالي
with tab4:
    st.subheader("📊 ذكاء الأعمال والنمو الاستراتيجي")
    if st.session_state.sales_ledger:
        df_sales = pd.DataFrame(st.session_state.sales_ledger)
        m1, m2, m3 = st.columns(3)
        m1.metric("إجمالي الإيرادات", f"{df_sales['المبلغ'].sum():,} YER")
        m2.metric("صافي أرباح Basil", f"{df_sales['الربح'].sum():,} YER")
        m3.metric("عدد العمليات", len(df_sales))
        
        st.divider()
        st.write("📈 منحنى نمو الأرباح:")
        fig = px.area(df_sales, x="التاريخ", y="الربح", color_discrete_sequence=['#60a5fa'])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("بانتظار تنفيذ أول عملية بيع لعرض المصفوفات التحليلية")

st.markdown("---")
st.caption(f"Basil Strategic Platform v7.0 | {datetime.now().year} ©")
