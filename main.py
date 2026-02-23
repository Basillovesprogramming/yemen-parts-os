import streamlit as st

# إعداد الصفحة لتكون احترافية وهيكلية
st.set_page_config(page_title="Yemen Parts OS - Bassem Edition", layout="wide")

# تجميل الواجهة (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    [data-testid="stMetricValue"] { color: #1e3a8a; font-size: 28px; font-weight: bold; }
    .invoice-box { border: 2px solid #1e3a8a; padding: 25px; border-radius: 15px; background-color: white; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>🏛️ نظام باسل المتكامل لإدارة قطع الغيار</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>نسخة التجار المحترفين - الربط اللوجستي بين دبي واليمن</p>", unsafe_allow_html=True)

# القائمة الجانبية (لوحة التحكم بالصرف)
with st.sidebar:
    st.header("⚙️ إعدادات السوق")
    ex_rate = st.number_input("سعر صرف الدولار (مثلاً 530)", value=530)
    profit_margin = st.slider("هامش الربح المستهدف (%)", 5, 100, 25)
    st.divider()
    st.info("💡 يتم الحساب بناءً على سعر صرف الدولار العالمي مقابل الدرهم (3.67).")

# الهيكلية الأساسية (Tabs)
tab1, tab2 = st.tabs(["🚀 عملية تسعير جديدة", "📊 تحليل الأرباح"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📦 تفاصيل الشحنة")
        p1, p2 = st.columns(2)
        with p1:
            item_name = st.text_input("اسم قطعة الغيار", "مساعدات تويوتا")
            part_no = st.text_input("رقم القطعة (Part Number)", "PN-XYZ")
        with p2:
            aed_price = st.number_input("سعر الشراء من دبي (درهم)", min_value=1.0, value=100.0)
            category = st.selectbox("الفئة", ["محركات", "كهرباء", "هيكل", "أخرى"])

        st.subheader("🚛 التكاليف اللوجستية والجمارك")
        s1, s2 = st.columns(2)
        with s1:
            ship_aed = st.number_input("تكلفة الشحن الدولي (درهم)", value=15.0)
        with s2:
            customs_pct = st.number_input("نسبة الجمارك والضرائب (%)", value=10)

    # محرك الحسابات (Engine)
    total_aed = aed_price + ship_aed
    cost_usd = (total_aed / 3.67) * (1 + customs_pct/100)
    cost_yer = cost_usd * ex_rate
    final_price = cost_yer * (1 + profit_margin/100)
    net_profit = final_price - cost_yer

    with col2:
        st.subheader("📈 الخلاصة المالية")
        st.metric("السعر النهائي (ريال يمني)", f"{round(final_price):,} YER")
        st.metric("صافي الربح", f"{round(net_profit):,} YER")
        st.metric("التكلفة بالدولار", f"${round(cost_usd, 2)}")
        
        if st.button("📲 تجهيز فاتورة الواتساب"):
            st.balloons()

# عرض الفاتورة الاحترافية في الأسفل
st.divider()
st.subheader("🧾 عرض سعر رسمي")
invoice_html = f"""
<div class="invoice-box">
    <h2 style="color: #1e3a8a; text-align: center;">🛡️ باسل لقطع الغيار 🛡️</h2>
    <hr>
    <p><b>اسم القطعة:</b> {item_name}</p>
    <p><b>رقم القطعة:</b> {part_no}</p>
    <p><b>التصنيف:</b> {category}</p>
    <h1 style="color: #16a34a; text-align: center;">{round(final_price):,} ريال يمني</h1>
    <p style="text-align: center; font-size: 12px; color: gray;">السعر شامل كافة تكاليف الشحن والجمارك</p>
</div>
"""
st.markdown(invoice_html, unsafe_allow_html=True)

with tab2:
    st.subheader("📊 إحصائيات العمليات")
    st.write("هنا تظهر تقارير الأرباح الشهرية (سيتم تفعيلها عند ربط قاعدة البيانات).")
