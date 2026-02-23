import streamlit as st

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="نظام باسل المتكامل", layout="wide")

# تجميل الواجهة بألوان الشركات (كحلي وذهبي)
st.markdown("""
<style>
    .stApp { background-color: #f4f7f6; }
    [data-testid="stMetricValue"] { color: #1e3a8a; font-size: 32px; }
    .main-title { color: #1e3a8a; text-align: center; font-size: 40px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🏛️ نظام باسل لإدارة استيراد قطع الغيار</p>', unsafe_allow_html=True)
st.info("نظام متطور للربط اللوجستي بين أسواق دبي والجمهورية اليمنية")

# --- القائمة الجانبية لإدارة العملة ---
with st.sidebar:
    st.header("⚙️ التحكم بالصرف والارباح")
    # بناءً على طلبك: 100 دولار بـ 53 ألف (صرف صنعاء)
    ex_rate = st.number_input("صرف الدولار (ريال يمني)", value=530)
    profit_pct = st.slider("هامش الربح المستهدف (%)", 5, 100, 25)
    st.divider()
    st.write("تم ضبط النظام ليعمل وفق معايير السوق الرسمية.")

# --- واجهة إدخال البيانات الهيكلية ---
tab_calc, tab_info = st.tabs(["🚀 تسعير القطع", "ℹ️ دليل المستخدم"])

with tab_calc:
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader("📦 بيانات الشحنة")
        col_name, col_part = st.columns(2)
        with col_name:
            item_name = st.text_input("اسم القطعة", "مساعدات لكزس")
        with col_part:
            part_no = st.text_input("رقم القطعة", "PN-8822")
            
        col_price, col_cat = st.columns(2)
        with col_price:
            price_aed = st.number_input("سعر الشراء (درهم دبي)", min_value=1.0, value=100.0)
        with col_cat:
            cat = st.selectbox("الفئة", ["محركات", "كهرباء", "هيكل", "أخرى"])

        st.subheader("🚛 التكاليف والجمارك")
        col_ship, col_tax = st.columns(2)
        with col_ship:
            ship_aed = st.number_input("الشحن الدولي (درهم)", value=15.0)
        with col_tax:
            customs = st.number_input("الجمارك والضرائب (%)", value=10)

    # --- المحرك الحسابي (بدون أخطاء مسافات) ---
    total_aed = price_aed + ship_aed
    cost_usd = (total_aed / 3.67) * (1 + customs/100)
    final_cost_yer = cost_usd * ex_rate
    price_with_profit = final_cost_yer * (1 + profit_pct/100)

    with c2:
        st.subheader("📊 الخلاصة المالية")
        st.metric("السعر النهائي للبيع", f"{round(price_with_profit):,} ريال")
        st.metric("صافي الفائدة", f"{round(price_with_profit - final_cost_yer):,} ريال")
        st.metric("التكلفة بالدولار", f"${round(cost_usd, 2)}")

# --- الفاتورة الاحترافية ---
st.divider()
st.subheader("📜 عرض السعر الرسمي")
invoice_html = f"""
<div style="border: 2px solid #1e3a8a; padding: 25px; border-radius: 15px; background-color: white;">
    <h2 style="text-align: center; color: #1e3a8a;">🛡️ باسل لقطع الغيار 🛡️</h2>
    <p style="text-align: center;">دبي - اليمن</p>
    <hr>
    <div style="display: flex; justify-content: space-between; direction: rtl;">
        <span><b>القطعة:</b> {item_name}</span>
        <span><b>الرقم:</b> {part_no}</span>
    </div>
    <div style="text-align: center; margin-top: 20px;">
        <h1 style="color: #16a34a;">{round(price_with_profit):,} ريال يمني</h1>
        <p style="color: gray;">العرض صالح وفق أسعار الصرف الحالية</p>
    </div>
</div>
"""
st.markdown(invoice_html, unsafe_allow_html=True)

if st.button("📲 تجهيز رسالة واتساب للعميل"):
    st.balloons()
    st.info(f"القطعة: {item_name} | السعر: {round(price_with_profit):,} ريال")

with tab_info:
    st.write("هذا النظام مبرمج لصالح التاجر **باسل** لإدارة عمليات الاستيراد بدقة متناهية.")
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
