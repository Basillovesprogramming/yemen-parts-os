import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# 1. إعدادات النظام المتقدمة (Layout)
st.set_page_config(page_title="Bassem Global Parts", layout="wide", initial_sidebar_state="expanded")

# 2. تصميم الواجهة بهوية تجارية فخمة (CSS)
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-top: 5px solid #1e3a8a; }
    .stTabs [data-baseweb="tab-list"] { background-color: #1e3a8a; border-radius: 12px; padding: 8px; }
    .stTabs [data-baseweb="tab"] { color: white !important; font-size: 18px; font-weight: bold; }
    .invoice-card { background: white; border: 2px solid #1e3a8a; padding: 30px; border-radius: 20px; text-align: right; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# 3. إدارة البيانات (Database Emulation)
if 'inventory' not in st.session_state:
    st.session_state.inventory = []
if 'sales' not in st.session_state:
    st.session_state.sales = []

# --- لوحة التحكم الجانبية (الأعصاب المركزية للنظام) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown("### ⚙️ إدارة العملات")
    usd_to_yer = st.number_input("💵 الدولار مقابل اليمني", value=530)
    sar_to_yer = st.number_input("🇸🇦 السعودي مقابل اليمني", value=140)
    st.divider()
    default_profit = st.slider("📈 نسبة الربح العام (%)", 10, 100, 25)
    st.divider()
    st.info(f"إجمالي قيمة المخزن: {len(st.session_state.inventory)} قطعة")

# --- واجهة النظام الرئيسية ---
st.markdown(f"<h1 style='text-align: center; color: #1e3a8a;'>🛡️ نظام باسل المتكامل لإدارة المبيعات الدولية</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: gray;'>التاريخ: {datetime.now().strftime('%Y-%m-%d')}</p>", unsafe_allow_html=True)

# الأقسام الهيكلية الكبرى
tabs = st.tabs(["🚀 التسعير والتحليل", "📦 المستودع الذكي", "🛒 سجل المبيعات", "📊 التقارير والنمو"])

# --- القسم 1: المحرك الحسابي والذكاء المالي ---
with tabs[0]:
    col_input, col_result = st.columns([2, 1.2])
    
    with col_input:
        st.subheader("📥 إدخال شحنة دبي")
        with st.container():
            c1, c2 = st.columns(2)
            i_name = c1.text_input("اسم قطعة الغيار", "جير بوكس لكزس")
            i_oem = c2.text_input("رقم القطعة (OEM No.)", "LX-5500")
            
            c3, c4 = st.columns(2)
            i_cost_aed = c3.number_input("سعر الشراء (درهم)", min_value=1.0, value=1000.0)
            i_ship_aed = c4.number_input("تكلفة الشحن (درهم)", value=100.0)
            
            i_customs = st.number_input("الجمارك والرسوم (%)", value=10)

        # المعادلات البرمجية (The Logic)
        cost_usd = ((i_cost_aed + i_ship_aed) / 3.67) * (1 + i_customs/100)
        cost_yer = cost_usd * usd_rate if 'usd_rate' in locals() else cost_usd * usd_to_yer
        final_sell_yer = cost_yer * (1 + default_profit/100)
        final_sell_sar = final_sell_yer / sar_to_yer

    with col_result:
        st.subheader("💰 التحليل المالي")
        st.metric("السعر النهائي (يمني)", f"{round(final_sell_yer):,} ريال")
        st.metric("السعر النهائي (سعودي)", f"{round(final_sell_sar):,} ريال")
        st.metric("صافي الربح", f"{round(final_sell_yer - cost_yer):,} ريال")
        
        if st.button("➕ تعميد وإضافة للمخزن"):
            item = {"ID": len(st.session_state.inventory)+1, "القطعة": i_name, "OEM": i_oem, "التكلفة($)": round(cost_usd, 2), "سعر البيع": round(final_sell_yer)}
            st.session_state.inventory.append(item)
            st.success("تم التشفير والإضافة للمخزن!")
            st.balloons()

    st.divider()
    st.subheader("📜 فاتورة عرض السعر")
    st.markdown(f"""
    <div class="invoice-card">
        <h2 style="color: #1e3a8a; text-align: center;">🛡️ شركة باسل لاستيراد قطع الغيار</h2>
        <hr>
        <p><b>وصف القطعة:</b> {i_name} | <b>الرقم التسلسلي:</b> {i_oem}</p>
        <h1 style="color: #16a34a; text-align: center;">{round(final_sell_yer):,} YER</h1>
        <p style="text-align: center; font-size: 14px; color: gray;">السعر يشمل الشحن الدولي والتخليص الجمركي</p>
    </div>
    """, unsafe_allow_html=True)

# --- القسم 2: المستودع الذكي ---
with tabs[1]:
    st.subheader("🗄️ إدارة المخزون المركزي")
    if st.session_state.inventory:
        df_inv = pd.DataFrame(st.session_state.inventory)
        st.dataframe(df_inv, use_container_width=True)
    else:
        st.info("لا توجد بضاعة مسجلة حالياً.")

# --- القسم 3: سجل المبيعات والأرشفة ---
with tabs[2]:
    st.subheader("🛒 تسجيل بيعة جديدة")
    if st.session_state.inventory:
        inv_list = [f"{i['ID']} - {i['القطعة']}" for i in st.session_state.inventory]
        choice = st.selectbox("اختر القطعة من المخزن", inv_list)
        customer = st.text_input("اسم العميل")
        
        if st.button("💾 إتمام البيع والأرشفة"):
            sale_entry = {"التاريخ": datetime.now().strftime("%Y-%m-%d"), "العميل": customer, "البيعة": choice}
            st.session_state.sales.append(sale_entry)
            st.success(f"تم تسجيل البيع لـ {customer}")
    
    if st.session_state.sales:
        st.table(pd.DataFrame(st.session_state.sales))

# --- القسم 4: تقارير النمو (Analytics) ---
with tabs[3]:
    st.subheader("📊 ذكاء الأعمال والتقارير المالية")
    if st.session_state.sales:
        # رسم بياني توضيحي
        sales_df = pd.DataFrame(st.session_state.sales)
        st.write("ملخص الأداء الشهري")
        st.bar_chart(sales_df.index)
    else:
        st.warning("تحتاج لإتمام عمليات بيع لعرض التقارير.")
