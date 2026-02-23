import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات النظام المتقدمة
st.set_page_config(page_title="Bassem Business OS", layout="wide")

# تصميم الواجهة (Professional Dark/Light Theme)
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #d1d5db; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #f8f9fa; border-radius: 10px 10px 0 0; gap: 1px; padding: 10px 20px; }
    .stTabs [aria-selected="true"] { background-color: #1e3a8a !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown("<h1 style='text-align: right; color: #1e3a8a;'>🏛️ نظام باسل المتكامل لإدارة تجارة قطع الغيار</h1>", unsafe_allow_html=True)

# 2. إدارة البيانات في ذاكرة النظام (Session State)
if 'sales_history' not in st.session_state:
    st.session_state.sales_history = []

# --- لوحة التحكم الجانبية (إعدادات السوق العالمية) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3252/3252894.png", width=100)
    st.header("🌐 لوحة تحكم العملات")
    usd_to_yer = st.number_input("صرف الدولار/يمني (صنعاء)", value=530)
    sar_to_yer = st.number_input("صرف السعودي/يمني", value=140)
    st.divider()
    profit_margin = st.slider("هامش الربح العام (%)", 5, 100, 25)
    st.success(f"النظام يعمل بصرف: 100$ = {usd_to_yer * 100:,} ريال")

# --- الأقسام الرئيسية للنظام ---
tab1, tab2, tab3 = st.tabs(["🚀 التسعير الفوري", "📦 إدارة المخزون", "📊 تقارير الأرباح"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 تفاصيل الشحنة الجديدة")
        with st.container():
            c1, c2 = st.columns(2)
            item_name = c1.text_input("اسم القطعة", "مساعدات تويوتا")
            part_no = c2.text_input("رقم القطعة (Oem No.)", "TY-880")
            
            c3, c4 = st.columns(2)
            purchase_price_aed = c3.number_input("سعر الشراء (درهم دبي)", min_value=0.0, value=100.0)
            shipping_aed = c4.number_input("تكلفة الشحن (درهم)", value=15.0)
            
            customs_pct = st.number_input("نسبة الجمارك والضرائب (%)", value=10)

    # المحرك الحسابي المتكامل
    total_aed = purchase_price_aed + shipping_aed
    cost_usd = (total_aed / 3.67) * (1 + customs_pct/100)
    cost_yer = cost_usd * usd_to_yer
    final_price_yer = cost_yer * (1 + profit_margin/100)
    final_price_sar = final_price_yer / sar_to_yer

    with col2:
        st.subheader("💰 عرض السعر")
        st.metric("بالريال اليمني", f"{round(final_price_yer):,} YER")
        st.metric("بالريال السعودي", f"{round(final_price_sar):,} SAR")
        st.metric("التكلفة ($)", f"${round(cost_usd, 2)}")
        
        if st.button("✅ تسجيل العملية وحفظ الفاتورة"):
            new_sale = {
                "الوقت": datetime.now().strftime("%H:%M:%S"),
                "القطعة": item_name,
                "التكلفة($)": round(cost_usd, 2),
                "البيع(يمني)": round(final_price_yer),
                "الربح(يمني)": round(final_price_yer - cost_yer)
            }
            st.session_state.sales_history.append(new_sale)
            st.balloons()

    st.divider()
    st.subheader("📄 عرض سعر للعميل")
    st.markdown(f"""
    <div style="border: 2px solid #1e3a8a; padding: 20px; border-radius: 10px; background-color: white; text-align: right;">
        <h2 style="color: #1e3a8a; text-align: center;">باسل لقطع الغيار</h2>
        <p><b>القطعة:</b> {item_name} | <b>الرقم:</b> {part_no}</p>
        <hr>
        <h1 style="color: #16a34a; text-align: center;">{round(final_price_yer):,} ريال يمني</h1>
        <p style="text-align: center; color: gray;">السعر شامل الشحن والجمارك وضمان الاستلام</p>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.subheader("📦 المخزون المتوفر")
    # محاكاة لجدول مخزون
    inventory_data = pd.DataFrame([
        {"القطعة": "مساعدات", "الكمية": 12, "المصدر": "دبي"},
        {"القطعة": "فلاتر", "الكمية": 50, "المصدر": "دبي"},
        {"القطعة": "بواجي", "الكمية": 100, "المصدر": "اليابان"}
    ])
    st.table(inventory_data)

with tab3:
    st.subheader("📊 سجل عمليات اليوم")
    if st.session_state.sales_history:
        df = pd.DataFrame(st.session_state.sales_history)
        st.dataframe(df, use_container_width=True)
        total_daily_profit = df["الربح(يمني)"].sum()
        st.success(f"إجمالي أرباحك المسجلة الآن: {total_daily_profit:,} ريال يمني")
    else:
        st.write("لا توجد عمليات مسجلة بعد.")

st.markdown("---")
st.caption("نظام باسل المتكامل v3.0 - إدارة ذكية للتجارة الدولية")
