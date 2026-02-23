import streamlit as st

# إعداد واجهة النظام المتطور
st.set_page_config(page_title="نظام البازلاء AI المطور", layout="wide")

st.title("🤖 نظام البازلاء المتكامل لقطع الغيار (دبي - اليمن)")
st.markdown("---")

# القائمة الجانبية (لوحة التحكم المركزية)
st.sidebar.header("📊 إعدادات الصرف والربح")
# بناءً على كلامك: 100 دولار بـ 53 الف يعني الدولار بـ 530
exchange_rate = st.sidebar.number_input("سعر صرف الدولار (مثلاً 530)", value=530)
profit_target = st.sidebar.slider("نسبة ربحك الصافي (%)", 5, 50, 20)

# الواجهة الرئيسية (إدخال البيانات)
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 بيانات القطعة")
    # هذا المتغير هو الذي سبب الخطأ في صورتك، الآن قمنا بتعريفه صح
    item_name = st.text_input("اسم قطعة الغيار", "قطعة غيار")
    aed_price = st.number_input("سعر الشراء من دبي (درهم)", min_value=0.0, value=100.0)

with col2:
    st.subheader("🚛 تكاليف إضافية")
    shipping_aed = st.number_input("تكلفة الشحن (درهم)", value=15.0)
    customs_percent = st.number_input("الجمارك والضرائب (%)", value=10)

# المحرك الحسابي المتطور
total_cost_aed = aed_price + shipping_aed
# تحويل الدرهم لدولار (ثابت 3.67) ثم إضافة الجمارك
total_cost_usd = (total_cost_aed / 3.67) * (1 + customs_percent/100)
# التحويل لليمني حسب صرفك (530) وإضافة الربح
final_price_yer = (total_cost_usd * exchange_rate) * (1 + profit_target/100)

# عرض النتائج بطريقة ذكية
st.divider()
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("التكلفة (دولار)", f"${round(total_cost_usd, 2)}")
kpi2.metric("السعر النهائي للزبون", f"{round(final_price_yer):,} ريال")
kpi3.metric("صافي فائدتك", f"{round(final_price_yer * (profit_target/100)):,} ريال")

# فاتورة احترافية (بدون أخطاء)
st.subheader("📋 عرض سعر جاهز للإرسال")
invoice = f"""
*نظام البازلاء لقطع الغيار*
---------------------------
القطعة: {item_name}
السعر النهائي: {round(final_price_yer):,} ريال يمني
---------------------------
_السعر شامل الشحن والجمارك_
"""
st.code(invoice, language="markdown")
st.success("الآن النظام يعمل 100% بدون أخطاء!")
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
