import streamlit as st
import pandas as pd

st.set_page_config(page_title="نظام البازلاء لقطع الغيار", layout="wide")

# واجهة النظام
st.title("🏎️ نظام إدارة وتسعير قطع الغيار الذكي")
st.sidebar.header("⚙️ إعدادات الصرف والارباح")

# 1. إعدادات ثابتة (في الشريط الجانبي)
yer_rate = st.sidebar.number_input("سعر صرف الدولار (اليمن)", value=1650)
profit_percent = st.sidebar.slider("نسبة ربحك (%)", 5, 50, 20)
shipping_fixed = st.sidebar.number_input("تكلفة الشحن الثابتة (درهم)", value=15)

# 2. إدخال البيانات (الواجهة الرئيسية)
col1, col2 = st.columns(2)
with col1:
    item_name = st.text_input("اسم قطعة الغيار", "مساعدات خلفية")
    aed_price = st.number_input("السعر في دبي (درهم)", min_value=0.0, value=100.0)

with col2:
    category = st.selectbox("نوع القطعة", ["محركات", "كهرباء", "هيكل", "أخرى"])
    customs = st.number_input("الجمارك والضرائب (%)", value=10)

# 3. الحسبة البرمجية المتكاملة
total_aed = aed_price + shipping_fixed
total_usd = (total_aed * (1 + customs/100)) / 3.67
final_yer = total_usd * yer_rate * (1 + profit_percent/100)

# 4. عرض النتيجة النهائية بشكل احترافي
st.divider()
c1, c2, c3 = st.columns(3)
c1.metric("التكلفة بالدولار", f"${round(total_usd, 2)}")
c2.metric("السعر النهائي (ريال يمني)", f"{round(final_yer):,} YER")
c3.metric("صافي ربحك", f"{round(final_yer * (profit_percent/100)):,} YER")

# 5. ميزة إضافية: تجهيز فاتورة للواتساب
st.subheader("📝 فاتورة العميل")
invoice_text = f"""
*عرض سعر من نظام البازلاء*
- القطعة: {item_name}
- النوع: {category}
- السعر النهائي: {round(final_yer):,} ريال يمني
_شامل الشحن والجمارك_
"""
st.code(invoice_text, language="markdown")
if st.button("نسخ نص الفاتورة"):
    st.success("تم التجهيز! يمكنك نسخ النص أعلاه وإرساله للعميل.")
