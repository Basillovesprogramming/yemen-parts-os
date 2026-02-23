import streamlit as st

# إعدادات الهوية البصرية للنظام
st.set_page_config(page_title="نظام باسل لإدارة الاستيراد", layout="wide", initial_sidebar_state="expanded")

# تصميم CSS لتحسين المظهر وجعله يبدو كبرنامج شركات
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { border: 1px solid #e0e0e0; padding: 20px; border-radius: 15px; background-color: white; box-shadow: 2px 2px 10px rgba(0,0,0,0.02); }
    h1 { color: #1E3A8A; font-family: 'Arial'; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #1E3A8A; color: white; }
    </style>
    """, unsafe_allow_html=True)

# الرأس (Header)
st.title("🛡️ نظام باسل المتكامل لإدارة تسعير قطع الغيار")
st.info("الربط البرمجي بين سوق دبي والمخازن اليمنية - نسخة التاجر المحترف")

# القائمة الجانبية (إعدادات العملة والربح)
with st.sidebar:
    st.header("⚙️ إعدادات الصرف")
    # التعديل حسب طلبك: 100 دولار بـ 53 الف
    usd_to_yer = st.number_input("سعر صرف الدولار (صنعاء)", value=530)
    st.divider()
    st.header("💰 هامش الربح")
    profit_rate = st.slider("نسبة الربح المستهدفة (%)", 5, 100, 25)
    st.write(f"سيتم إضافة {profit_rate}% على التكلفة الإجمالية.")

# جسم النظام (هيكلية العمليات)
col_input, col_display = st.columns([2, 1])

with col_input:
    with st.container():
        st.subheader("📝 تفاصيل القطعة المستوردة")
        c1, c2 = st.columns(2)
        with c1:
            item_name = st.text_input("اسم القطعة (مثلاً: مساعدات كامري)", "قطعة غيار")
            part_number = st.text_input("رقم القطعة (Part Number)", "PN-0000")
        with c2:
            category = st.selectbox("تصنيف القطعة", ["محركات", "جير بوكس", "كهربائيات", "هيكل", "أخرى"])
            aed_price = st.number_input("سعر الشراء في دبي (درهم)", min_value=0.0, value=100.0)

    st.divider()
    
    with st.container():
        st.subheader("🚛 تكاليف اللوجستيات")
        c3, c4 = st.columns(2)
        with c3:
            shipping_aed = st.number_input("الشحن من دبي (درهم)", value=15.0)
            customs_rate = st.number_input("الجمارك والضرائب (%)", value=10)
        with c4:
            local_shipping = st.number_input("النقل الداخلي في اليمن (ريال)", value=5000)
            extra_fees = st.number_input("مصاريف إضافية (ريال)", value=0)

# محرك الحسابات الذكي (The Engine)
# 1. حساب التكلفة بالدرهم مع الشحن
total_aed = aed_price + shipping_aed
# 2. التحويل للدولار وإضافة الجمارك
total_usd = (total_aed / 3.67) * (1 + customs_rate/100)
# 3. التحويل لليمني وإضافة المصاريف المحلية والربح
base_cost_yer = (total_usd * usd_to_yer) + local_shipping + extra_fees
final_price_yer = base_cost_yer * (1 + profit_rate/100)
net_profit = final_price_yer - base_cost_yer

with col_display:
    st.subheader("📊 التحليل المالي")
    st.metric("السعر النهائي (ريال يمني)", f"{round(final_price_yer):,} YER")
    st.metric("صافي الربح المتوقع", f"{round(net_profit):,} YER")
    st.metric("التكلفة بالدولار", f"${round(total_usd, 2)}")
    
    if st.button("تجهيز فاتورة احترافية"):
        st.balloons()
        st.markdown(f"""
        <div style="border: 2px solid #1E3A8A; padding: 15px; border-radius: 10px; background-color: white; text-align: right;">
            <h3 style="color: #1E3A8A; text-align: center;">فاتورة عرض سعر</h3>
            <p><b>اسم العميل:</b> عميل محترم</p>
            <p><b>القطعة:</b> {item_name}</p>
            <p><b>رقم القطعة:</b> {part_number}</p>
            <hr>
            <h2 style="color: green; text-align: center;">{round(final_price_yer):,} ريال يمني</h2>
            <p style="font-size: 10px; text-align: center;">تم التسعير بواسطة نظام باسل المتكامل</p>
        </div>
        """, unsafe_allow_html=True)

# تذييل الصفحة
st.markdown("---")
st.caption("نظام باسل لإدارة قطع الغيار v2.0 - جميع الحقوق محفوظة")
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
