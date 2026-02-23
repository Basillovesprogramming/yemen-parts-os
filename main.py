import streamlit as st

# إعدادات النظام المتقدمة
st.set_page_config(page_title="نظام البازلاء AI المطور", layout="wide")

# تصميم الواجهة
st.title("🤖 نظام الذكاء البرمجي المتكامل لقطع الغيار")
st.markdown("---")

# القائمة الجانبية (لوحة التحكم المركزية)
st.sidebar.header("📊 لوحة تحكم السوق")
market_type = st.sidebar.selectbox("منطقة البيع (لتحديد الصرف التلقائي)", ["صنعاء وما حولها", "عدن والمحافظات الأخرى", "تخصيص يدوي"])

if market_type == "صنعاء وما حولها":
    exchange_rate = 530
elif market_type == "عدن والمحافظات الأخرى":
    exchange_rate = 1650
else:
    exchange_rate = st.sidebar.number_input("أدخل سعر الصرف اليدوي", value=530)

profit_target = st.sidebar.slider("نسبة الربح المستهدفة (%)", 10, 100, 25)

# الواجهة الرئيسية (إدخال البيانات)
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("📝 بيانات القطعة")
    part_name = st.text_input("اسم القطعة (مثلاً: جير بوكس تويوتا)", "قطعة غيار")
    aed_price = st.number_input("سعر الشراء من دبي (درهم)", min_value=0.0, value=500.0)
    shipping_cost = st.number_input("تكاليف الشحن الدولي (درهم)", value=50.0)

with col_b:
    st.subheader("🚛 تكاليف التخليص")
    customs_percent = st.number_input("نسبة الجمارك والضرائب (%)", value=10)
    internal_shipping = st.number_input("نقل داخلي في اليمن (ريال)", value=5000)

# المحرك الحسابي (المتطور)
cost_in_aed = aed_price + shipping_cost
cost_in_usd = (cost_in_aed * (1 + customs_percent/100)) / 3.67
base_cost_yer = (cost_in_usd * exchange_rate) + internal_shipping
final_selling_price = base_cost_yer * (1 + profit_target/100)
net_profit = final_selling_price - base_cost_yer

# عرض النتائج بطريقة ذكية
st.markdown("### 📈 تحليل التكاليف والارباح")
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("التكلفة الإجمالية (ريال)", f"{round(base_cost_yer):,}")
kpi2.metric("سعر البيع المقترح", f"{round(final_selling_price):,}", delta=f"{profit_target}% ربح")
kpi3.metric("صافي الفائدة", f"{round(net_profit):,}")

# ميزة الذكاء الاصطناعي (توصية النظام)
st.info("💡 **توصية النظام:** بناءً على أسعار الصرف الحالية، يفضل البيع بالريال السعودي أو الدولار لضمان ثبات الربح.")

# فاتورة احترافية
st.subheader("📋 عرض سعر للعميل")
invoice = f"""
*نظام البازلاء لقطع الغيار*
---------------------------
القطعة: {part_name}
السعر النهائي: {round(final_selling_price):,} ريال يمني
الحالة: متوفر (شحن دبي)
---------------------------
*شكراً لثقتكم بنا*
"""
st.code(invoice, language="markdown")

if st.button("تجهيز الرسالة للإرسال"):
    st.success("تم التجهيز! انسخ النص وارسله مباشرة.")
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
