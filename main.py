import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="نظام باسل المتكامل", layout="wide")

st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>🛡️ نظام باسل لإدارة قطع الغيار</h1>", unsafe_allow_html=True)
st.markdown("---")

# 2. القائمة الجانبية (الصرف والربح)
with st.sidebar:
    st.header("⚙️ الإعدادات المركزية")
    ex_rate = st.number_input("صرف الدولار (ريال يمني)", value=530)
    profit_pct = st.slider("نسبة الربح (%)", 5, 100, 25)

# 3. واجهة الإدخال
col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 بيانات القطعة")
    name = st.text_input("اسم القطعة", "مساعدات تويوتا")
    price_aed = st.number_input("السعر في دبي (درهم)", min_value=1.0, value=100.0)

with col2:
    st.subheader("🚛 التكاليف")
    ship_aed = st.number_input("الشحن (درهم)", value=15.0)
    customs = st.number_input("الجمارك (%)", value=10)

# 4. المحرك الحسابي (مختصر لمنع الأخطاء)
total_aed = price_aed + ship_aed
usd_cost = (total_aed / 3.67) * (1 + customs/100)
final_price = (usd_cost * ex_rate) * (1 + profit_pct/100)

# 5. عرض النتائج والفاتورة
st.divider()
kpi1, kpi2 = st.columns(2)
kpi1.metric("السعر النهائي للبيع", f"{round(final_price):,} ريال")
kpi2.metric("صافي فائدتك", f"{round(final_price - (usd_cost * ex_rate)):,} ريال")

st.subheader("🧾 الفاتورة الاحترافية")
invoice = f"""
<div style="border: 2px solid #1e3a8a; padding: 20px; border-radius: 10px; text-align: right;">
    <h3>باسل لقطع الغيار</h3>
    <p><b>القطعة:</b> {name}</p>
    <h2 style="color: #16a34a;">{round(final_price):,} ريال يمني</h2>
</div>
"""
st.markdown(invoice, unsafe_allow_html=True)
