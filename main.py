import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# 1. الإعدادات السيادية (Basil's Identity)
st.set_page_config(page_title="Basil Global ERP", layout="wide", initial_sidebar_state="expanded")

# تصميم UI/UX احترافي (Dark Sapphire & Gold)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .royal-header {
        background: linear-gradient(90deg, #1e3a8a, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center; font-size: 55px; font-weight: 900; padding: 10px; margin-bottom: 0px;
    }
    .sub-text { color: #94a3b8; text-align: center; font-size: 20px; margin-bottom: 30px; }
    [data-testid="stMetric"] {
        background-color: #1a1f2c !important;
        border: 1px solid #3b82f6 !important;
        border-radius: 20px !important;
        padding: 25px !important;
    }
    [data-testid="stMetricValue"] { color: #60a5fa !important; font-size: 35px !important; font-weight: bold !important; }
    [data-testid="stMetricLabel"] { color: #ffffff !important; font-size: 18px !important; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; background-color: #1a1f2c; padding: 10px; border-radius: 15px; }
    .stTabs [data-baseweb="tab"] { color: #94a3b8 !important; font-size: 18px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. نظام حفظ البيانات (الذاكرة المركزية)
if 'inventory' not in st.session_state: st.session_state.inventory = []
if 'sales' not in st.session_state: st.session_state.sales = []

# --- لوحة التحكم الجانبية ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #60a5fa;'>Basil Control</h1>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
    st.divider()
    usd_rate = st.number_input("💵 صرف الدولار (يمني)", value=530)
    sar_rate = st.number_input("🇸🇦 صرف السعودي (يمني)", value=140)
    target_profit = st.slider("🎯 هامش الربح المستهدف (%)", 5, 100, 25)
    st.divider()
    if st.button("🔄 تصفير النظام (للطوارئ)"):
        st.session_state.inventory = []
        st.session_state.sales = []
        st.rerun()

# واجهة النظام الرئيسية
st.markdown('<p class="royal-header">BASIL GLOBAL STRATEGIC ERP</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">المنصة المتكاملة لإدارة الاستيراد، الأصول الاستراتيجية، والذكاء المالي</p>', unsafe_allow_html=True)

# --- التبويبات الرئيسية ---
tabs = st.tabs(["🚀 المشتريات الدولية", "📦 إدارة الأصول", "🛒 مركز المبيعات", "📈 التحليل الاستراتيجي"])

# 1. المشتريات والتسعير
with tabs[0]:
    col_in, col_res = st.columns([1.5, 1])
    with col_in:
        st.subheader("📥 تكويد شحنة جديدة")
        p_name = st.text_input("اسم القطعة (Item Name)")
        p_oem = st.text_input("رقم القطعة (OEM Reference)")
        c1, c2 = st.columns(2)
        price_aed = c1.number_input("سعر دبي (AED)", min_value=0.0)
        shipping_aed = c2.number_input("الشحن (AED)", value=15.0)
        qty = st.number_input("الكمية المستوردة (Qty)", min_value=1, value=1)
        tax = st.number_input("الرسوم الجمركية (%)", value=10)
        
        # معادلات التحليل
        cost_usd = ((price_aed + shipping_aed) / 3.67) * (1 + tax/100)
        cost_yer = cost_usd * usd_rate
        sell_yer = cost_yer * (1 + target_profit/100)

    with col_res:
        st.subheader("💰 التحليل المالي للصفقة")
        st.metric("سعر البيع (يمني)", f"{round(sell_yer):,} YER")
        st.metric("سعر البيع (سعودي)", f"{round(sell_yer/sar_rate):,} SAR")
        st.metric("صافي الربح المتوقع/قطعة", f"{round(sell_yer - cost_yer):,} YER")
        
        if st.button("🚀 تعميد الشحنة وإرسالها للأصول"):
            st.session_state.inventory.append({
                "ID": len(st.session_state.inventory)+1,
                "القطعة": p_name,
                "OEM": p_oem,
                "الكمية": qty,
                "التكلفة_يمني": round(cost_yer),
                "البيع_يمني": round(sell_yer),
                "التاريخ": datetime.now().strftime("%Y-%m-%d")
            })
            st.success(f"تم تسجيل {qty} قطعة في الأصول بنجاح")
            st.balloons()

# 2. إدارة الأصول (المخزن المطور)
with tabs[1]:
    st.subheader("📦 إدارة أصول المستودع الذكي")
    if st.session_state.inventory:
        df_inv = pd.DataFrame(st.session_state.inventory)
        
        # إحصائيات الأصول
        m1, m2 = st.columns(2)
        m1.metric("إجمالي القطع المتوفرة", f"{df_inv['الكمية'].sum()} قطعة")
        m2.metric("القيمة السوقية للمخزون", f"{ (df_inv['البيع_يمني'] * df_inv['الكمية']).sum():,} YER")
        
        # الجدول الاحترافي
        df_display = df_inv.copy()
        df_display['السعر_بالسعودي'] = (df_display['البيع_يمني'] / sar_rate).round(0)
        df_display['الحالة'] = "✅ متوفر"
        df_display = df_display[['ID', 'القطعة', 'OEM', 'الكمية', 'البيع_يمني', 'السعر_بالسعودي', 'الحالة', 'التاريخ']]
        
        st.dataframe(df_display, use_container_width=True)
    else:
        st.info("المستودع خالي حالياً")

# 3. مركز المبيعات
with tabs[2]:
    if st.session_state.inventory:
        st.subheader("🛒 تنفيذ عملية بيع")
        options = [f"{i['القطعة']} | {i['OEM']}" for i in st.session_state.inventory]
        selection = st.selectbox("اختر الصنف من الأصول", options)
        buyer = st.text_input("اسم العميل المشتري")
        
        if st.button("🧾 تأكيد البيع والأرشفة"):
            item_data = next(i for i in st.session_state.inventory if f"{i['القطعة']} | {i['OEM']}" == selection)
            st.session_state.sales.append({
                "التاريخ": datetime.now().strftime("%Y-%m-%d"),
                "العميل": buyer,
                "الصنف": selection,
                "المبلغ": item_data['البيع_يمني'],
                "الربح": item_data['البيع_يمني'] - item_data['التكلفة_يمني']
            })
            st.success("تمت عملية البيع وتحديث السجل المالي")
    else:
        st.warning("المستودع خالي، لا يمكن تنفيذ مبيعات")

# 4. التحليل الاستراتيجي
with tabs[3]:
    st.subheader("📈 تقارير النمو والذكاء المالي")
    if st.session_state.sales:
        df_s = pd.DataFrame(st.session_state.sales)
        c1, c2, c3 = st.columns(3)
        c1.metric("إجمالي الإيرادات", f"{df_s['المبلغ'].sum():,} YER")
        c2.metric("صافي أرباح Basil", f"{df_s['الربح'].sum():,} YER")
        c3.metric("كفاءة العمليات", f"{len(df_s)} بيعة")
        
        st.divider()
        fig = px.area(df_s, x="التاريخ", y="الربح", title="نمو الأرباح الصافية الاستراتيجي", markers=True)
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="white")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("بانتظار تنفيذ صفقات لتفعيل أدوات التحليل الاستراتيجي")

st.markdown("---")
st.caption(f"Basil Strategic Platform v8.0 | Built with Precision Intelligence © {datetime.now().year}")
