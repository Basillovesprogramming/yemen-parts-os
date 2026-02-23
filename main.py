import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات الهيكلية المتقدمة
st.set_page_config(page_title="نظام باسل الاحترافي", layout="wide")

# تصميم الواجهة بهوية تجارية
st.markdown("""
    <style>
    .main { background-color: #f4f7f9; }
    .stMetric { border-radius: 15px; background-color: white; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .stTabs [data-baseweb="tab-list"] { background-color: #1e3a8a; border-radius: 10px; padding: 5px; }
    .stTabs [data-baseweb="tab"] { color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. بناء قاعدة البيانات المؤقتة (حتى يتم الربط بـ SQL)
if 'inventory' not in st.session_state:
    st.session_state.inventory = []
if 'sales' not in st.session_state:
    st.session_state.sales = []

# --- لوحة التحكم الجانبية ---
with st.sidebar:
    st.title("👨‍💼 لوحة المدير")
    st.image("https://cdn-icons-png.flaticon.com/512/883/883039.png", width=80)
    usd_rate = st.number_input("صرف الدولار اليوم", value=530)
    sar_rate = st.number_input("صرف السعودي اليوم", value=140)
    global_profit = st.slider("نسبة الربح الافتراضية (%)", 5, 100, 25)
    st.divider()
    st.write("📊 **إحصائية سريعة:**")
    st.write(f"عدد القطع في المخزن: {len(st.session_state.inventory)}")
    st.write(f"إجمالي المبيعات: {len(st.session_state.sales)}")

# --- الأقسام الرئيسية (هيكلية الخطة) ---
st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>🏛️ منصة باسل لإدارة الاستيراد والمبيعات</h1>", unsafe_allow_html=True)

tabs = st.tabs(["💰 حاسبة الاستيراد", "📦 إدارة المخازن", "🛒 سجل المبيعات", "📊 التقارير المالية"])

# --- القسم الأول: حاسبة الاستيراد الفوري ---
with tabs[0]:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("📥 تسعير شحنة جديدة")
        c1, c2 = st.columns(2)
        p_name = c1.text_input("اسم القطعة")
        p_oem = c2.text_input("رقم القطعة (OEM)")
        
        c3, c4 = st.columns(2)
        p_cost_aed = c3.number_input("سعر الشراء (درهم)", min_value=0.0)
        p_ship_aed = c4.number_input("شحن دبي (درهم)", value=15.0)
        
        p_customs = st.number_input("جمارك ومصاريف (%)", value=10)
        
        # الحسابات الذكية
        total_aed = p_cost_aed + p_ship_aed
        cost_usd = (total_aed / 3.67) * (1 + p_customs/100)
        cost_yer = cost_usd * usd_rate
        sell_price_yer = cost_yer * (1 + global_profit/100)
        
    with col2:
        st.subheader("💵 النتيجة")
        st.metric("سعر البيع (يمني)", f"{round(sell_price_yer):,} YER")
        st.metric("سعر البيع (سعودي)", f"{round(sell_price_yer/sar_rate):,} SAR")
        
        if st.button("➕ إضافة للمخزن"):
            item = {"القطعة": p_name, "OEM": p_oem, "التكلفة($)": round(cost_usd, 2), "السعر(يمني)": round(sell_price_yer)}
            st.session_state.inventory.append(item)
            st.success("تمت الإضافة للمخزن بنجاح!")

# --- القسم الثاني: إدارة المخازن ---
with tabs[1]:
    st.subheader("🗄️ قائمة البضاعة المتوفرة")
    if st.session_state.inventory:
        df_inv = pd.DataFrame(st.session_state.inventory)
        st.table(df_inv)
        if st.button("🗑️ تفريغ المخزن"):
            st.session_state.inventory = []
            st.rerun()
    else:
        st.warning("المخزن فارغ حالياً.")

# --- القسم الثالث: سجل المبيعات والفواتير ---
with tabs[2]:
    st.subheader("📝 تسجيل بيعة جديدة")
    if st.session_state.inventory:
        items_list = [i["القطعة"] for i in st.session_state.inventory]
        selected_item = st.selectbox("اختر القطعة المباعة", items_list)
        customer = st.text_input("اسم الزبون")
        
        if st.button("🧾 إصدار فاتورة وبيع"):
            sale_data = next(item for item in st.session_state.inventory if item["القطعة"] == selected_item)
            sale_entry = {
                "التاريخ": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "الزبون": customer,
                "القطعة": selected_item,
                "المبلغ": sale_data["السعر(يمني)"]
            }
            st.session_state.sales.append(sale_entry)
            st.balloons()
            st.success("تم تسجيل البيعة!")
    
    st.divider()
    if st.session_state.sales:
        st.write("📋 **آخر المبيعات:**")
        st.table(pd.DataFrame(st.session_state.sales))

# --- القسم الرابع: التقارير المالية ---
with tabs[3]:
    st.subheader("📈 تحليل الأداء المالي")
    if st.session_state.sales:
        df_sales = pd.DataFrame(st.session_state.sales)
        total_rev = df_sales["المبلغ"].sum()
        st.metric("إجمالي الإيرادات (يمني)", f"{total_rev:,} YER")
        st.line_chart(df_sales["المبلغ"])
    else:
        st.info("لا توجد بيانات مالية لتحليلها بعد.")

st.markdown("---")
st.caption(f"نظام باسل الإداري v4.0 | التاريخ: {datetime.now().strftime('%Y-%m-%d')}")
