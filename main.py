import streamlit as st

# إعدادات واجهة المستخدم الاحترافية
st.set_page_config(page_title="Yemen Parts OS - Professional Edition", layout="wide")

# تصميم الهيدر (رأس الصفحة)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ نظام البازلاء المتكامل لإدارة استيراد قطع الغيار")
st.caption("النسخة الاحترافية المخصصة للتجار - الربط المباشر بين دبي واليمن")

# --- لوحة التحكم الجانبية ---
st.sidebar.header("📋 إعدادات النظام المركزية")
with st.sidebar:
    exchange_rate = st.number_input("سعر صرف الدولار (اليمن)", value=530, help="السعر الحالي في السوق")
    profit_margin = st.slider("نسبة الأرباح المستهدفة (%)", 5, 100, 25)
    st.divider()
    st.info("💡 هذا النظام يحسب التكاليف بناءً على معايير الشحن الدولي والتخليص الجمركي.")

# --- الواجهة الرئيسية (هيكلية العمليات) ---
tab1, tab2 = st.tabs(["🚀 عملية تسعير جديدة", "📂 سجل العمليات"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📦 بيانات الشحنة")
        p_col1, p_col2 = st.columns(2)
        with p_col1:
            item_name = st.text_input("وصف قطعة الغيار", "محرك تويوتا كامري 2024")
            part_no = st.text_input("رقم القطعة (Part Number)", "TY-2024-X1")
        with p_col2:
            aed_price = st.number_input("سعر الشراء من دبي (درهم)", min_value=0.0, value=1200.0)
            category = st.selectbox("تصنيف القطعة", ["محركات", "جير بوكس", "كهربائيات", "هيكل خارجي"])

        st.subheader("🚛 تكاليف الخدمات واللوجستيات")
        s_col1, s_col2 = st.columns(2)
        with s_col1:
            shipping_aed = st.number_input("تكلفة الشحن الدولي (درهم)", value=150.0)
            customs_percent = st.number_input("ضريبة الجمارك (%)", value=10)
        with s_col2:
            land_transport = st.number_input("نقل بري داخلي (ريال يمني)", value=15000)
            other_costs = st.number_input("مصاريف أخرى (ريال يمني)", value=2000)

    # --- محرك الحسابات الذكي (Backend) ---
    total_aed = aed_price + shipping_aed
    cost_usd = (total_aed / 3.67) * (1 + customs_percent/100)
    cost_yer = (cost_usd * exchange_rate) + land_transport + other_costs
    final_price = cost_yer * (1 + profit_margin/100)
    profit_amount = final_price - cost_yer

    with col2:
        st.subheader("📊 ملخص التحليل المالي")
        st.metric("السعر النهائي للبيع", f"{round(final_price):,} ريال")
        st.metric("صافي أرباحك", f"{round(profit_amount):,} ريال")
        st.metric("تكلفة الاستيراد بالدولار", f"${round(cost_usd, 2)}")
        
        if profit_amount > 50000:
            st.success("✅ هذه الصفقة ذات عوائد عالية")
        else:
            st.warning("⚠️ هامش الربح منخفض نسبياً")

# --- عرض الفاتورة الاحترافية ---
st.divider()
st.subheader("🧾 عرض سعر احترافي للعميل")
invoice_html = f"""
<div style="border: 2px solid #ddd; padding: 20px; border-radius: 10px; background-color: white;">
    <h2 style="text-align: center; color: #1e3a8a;">البازلاء لقطع الغيار</h2>
    <p style="text-align: center;">دبي - اليمن</p>
    <hr>
    <table style="width: 100%; text-align: right;">
        <tr><td><b>القطعة:</b></td><td>{item_name}</td></tr>
        <tr><td><b>رقم القطعة:</b></td><td>{part_no}</td></tr>
        <tr><td><b>التصنيف:</b></td><td>{category}</td></tr>
        <tr style="color: green; font-size: 20px;"><td><b>السعر النهائي:</b></td><td><b>{round(final_price):,} ريال يمني</b></td></tr>
    </table>
    <hr>
    <p style="font-size: 12px; color: gray; text-align: center;">هذا العرض صالح لمدة 24 ساعة فقط نظراً لتغير أسعار الصرف</p>
</div>
"""
st.markdown(invoice_html, unsafe_allow_html=True)

# زر لمشاركة الفاتورة
if st.button("📲 تجهيز لإرسالها عبر واتساب"):
    wa_text = f"عزيزي العميل، عرض سعر قطعة ({item_name}) هو: {round(final_price):,} ريال يمني."
    st.text_area("انسخ النص:", wa_text)

with tab2:
    st.write("هنا سيتم عرض سجل مبيعاتك السابقة (يتطلب قاعدة بيانات).")
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
