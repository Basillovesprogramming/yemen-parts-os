import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# 1. إعدادات الهوية الفخمة للنظام
st.set_page_config(page_title="Bassem Global Systems", layout="wide", initial_sidebar_state="expanded")

# تصميم CSS مخصص لواجهة احترافية (ألوان كحلية وذهبية ورمادية)
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f9; }
    .main-header { color: #1e3a8a; text-align: center; font-size: 45px; font-weight: bold; text-shadow: 2px 2px 4px #d1d5db; margin-bottom: 0px; }
    .sub-header { color: #666; text-align: center; font-size: 18px; margin-bottom: 30px; }
    .stMetric { background-color: white; padding: 25px; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.05); border-bottom: 5px solid #1e3a8a; }
    .invoice-box { background: white; border: 3px solid #1e3a8a; padding: 40px; border-radius: 25px; text-align: right; box-shadow: 0 15px 35px rgba(0,0,0,0.1); font-family: 'Arial'; }
    .stTabs [data-baseweb="tab-list"] { background-color: #1e3a8a; border-radius: 15px; padding: 10px; gap: 20px; }
    .stTabs [data-baseweb="tab"] { color: white !important; font-size: 20px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. نظام حفظ البيانات الذكي (Session State)
if 'inventory' not in st.session_state:
    st.session_state.inventory = []
if 'sales' not in st.session_state:
    st.session_state.sales = []

# --- لوحة التحكم الجانبية (مركز العمليات) ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>👑 لوحة المدير باسل</h2>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
    st.divider()
    st.markdown("### 💹 أسعار الصرف اللحظية")
    usd_rate = st.number_input("💵 الدولار مقابل اليمني", value=530)
    sar_rate = st.number_input("🇸🇦 السعودي مقابل اليمني", value=140)
    st.divider()
    global_profit = st.slider("📈 هامش الربح المستهدف (%)", 5, 100, 25)
    st.divider()
    st.info(f"إجمالي المبيعات اليوم: {len(st.session_state.sales)}")

# الواجهة العلوية
st.markdown('<p class="main-header">🛡️ منصة باسل الدولية لقطع الغيار</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">النظام المتكامل لإدارة الاستيراد، المخازن، والتحليل المالي الذكي</p>', unsafe_allow_html=True)

# --- توزيع الأقسام الهيكلية (Tabs) ---
tab_calc, tab_stock, tab_sales, tab_charts = st.tabs(["🚀 التسعير والتحليل", "📦 المستودع الذكي", "🛒 صالة المبيعات", "📊 ذكاء الأعمال"])

# 1. قسم التسعير والتحليل المالي
with tab_calc:
    col_in, col_res = st.columns([1.5, 1])
    
    with col_in:
        st.subheader("📥 مدخلات الشحنة (دبي)")
        c1, c2 = st.columns(2)
        p_name = c1.text_input("اسم القطعة الميكانيكية", "محرك تويوتا")
        p_oem = c2.text_input("رقم القطعة (OEM No.)", "TY-9900")
        
        c3, c4 = st.columns(2)
        cost_aed = c3.number_input("سعر الشراء (درهم)", min_value=1.0, value=500.0)
        ship_aed = c4.number_input("تكلفة الشحن الدولي (درهم)", value=50.0)
        
        customs_pct = st.number_input("نسبة التخليص والجمارك (%)", value=10)

        # المحرك الحسابي (The Engine)
        total_aed = cost_aed + ship_aed
        cost_usd = (total_aed / 3.67) * (1 + customs_pct/100)
        cost_yer = cost_usd * usd_rate
        final_price_yer = cost_yer * (1 + global_profit/100)
        final_price_sar = final_price_yer / sar_rate

    with col_res:
        st.subheader("💰 التحليل المالي للصفقة")
        st.metric("السعر النهائي (يمني)", f"{round(final_price_yer):,} YER")
        st.metric("السعر النهائي (سعودي)", f"{round(final_price_sar):,} SAR")
        st.metric("صافي الربح المتوقع", f"{round(final_price_yer - cost_yer):,} YER", delta=f"{global_profit}%")
        
        if st.button("➕ تعميد وإضافة للمخزن المركز"):
            new_item = {
                "التاريخ": datetime.now().strftime("%Y-%m-%d"),
                "القطعة": p_name,
                "OEM": p_oem,
                "التكلفة($)": round(cost_usd, 2),
                "سعر البيع": round(final_price_yer),
                "الربح": round(final_price_yer - cost_yer)
            }
            st.session_state.inventory.append(new_item)
            st.balloons()
            st.success("تم التشفير والحفظ بنجاح")

    st.divider()
    st.subheader("📄 معاينة عرض السعر للعميل")
    st.markdown(f"""
    <div class="invoice-box">
        <h2 style="color: #1e3a8a; text-align: center;">🛡️ شركة باسل العالمية لقطع الغيار</h2>
        <p style="text-align: center;">فرع الاستيراد المباشر - دبي/اليمن</p>
        <hr>
        <div style="display: flex; justify-content: space-between; direction: rtl;">
            <span><b>الصنف:</b> {p_name}</span>
            <span><b>التاريخ:</b> {datetime.now().strftime('%Y-%m-%d')}</span>
        </div>
        <p><b>رقم القطعة:</b> {p_oem}</p>
        <div style="text-align: center; margin-top: 30px;">
            <h1 style="color: #16a34a; font-size: 50px;">{round(final_price_yer):,} ريال</h1>
            <p style="color: gray;">هذا السعر يشمل الجمارك والشحن وضمان الجودة</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 2. قسم المستودع
with tab_stock:
    st.subheader("🗄️ المستودع المركزي")
    if st.session_state.inventory:
        df_inv = pd.DataFrame(st.session_state.inventory)
        st.dataframe(df_inv, use_container_width=True)
    else:
        st.warning("المستودع خالي حالياً. ابدأ بإضافة بضاعة من قسم التسعير.")

# 3. قسم المبيعات
with tab_sales:
    st.subheader("🛒 صالة البيع والأرشفة")
    if st.session_state.inventory:
        col_s1, col_s2 = st.columns(2)
        inv_list = [f"{i['القطعة']} - {i['OEM']}" for i in st.session_state.inventory]
        selected_p = col_s1.selectbox("اختر القطعة المباعة", inv_list)
        cust_name = col_s2.text_input("اسم الزبون المشتري")
        
        if st.button("💾 إتمام عملية البيع"):
            sale_data = next(item for item in st.session_state.inventory if f"{item['القطعة']} - {item['OEM']}" == selected_p)
            sale_entry = {
                "التاريخ": datetime.now().strftime("%Y-%m-%d"),
                "الزبون": cust_name,
                "القطعة": selected_p,
                "المبلغ": sale_data["سعر البيع"],
                "الربح": sale_data["الربح"]
            }
            st.session_state.sales.append(sale_entry)
            st.success(f"تم تسجيل البيع لـ {cust_name}")
    
    if st.session_state.sales:
        st.divider()
        st.write("📋 **سجل مبيعات اليوم:**")
        st.table(pd.DataFrame(st.session_state.sales))

# 4. قسم ذكاء الأعمال (الفخامة الحقيقية)
with tab_charts:
    st.subheader("📊 تقارير النمو وتحليل الأرباح")
    if st.session_state.sales:
        df_sales = pd.DataFrame(st.session_state.sales)
        
        c_m1, c_m2, c_m3 = st.columns(3)
        c_m1.metric("إجمالي المبيعات", f"{df_sales['المبلغ'].sum():,} YER")
        c_m2.metric("صافي الربح التراكمي", f"{df_sales['الربح'].sum():,} YER", delta="Positive")
        c_m3.metric("كفاءة العمليات", f"{len(df_sales)} بيعة")
        
        st.divider()
        st.write("📈 **منحنى الأرباح البياني:**")
        fig = px.area(df_sales, x="التاريخ", y="الربح", title="نمو الأرباح الصافية", color_discrete_sequence=['#1e3a8a'])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("بانتظار تسجيل أول عملية بيع لتفعيل الرسوم البيانية.")

st.markdown("---")
st.caption("نظام باسل المتكامل v5.0 | تم التصميم ليكون شريكك الذكي في النجاح")
