import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# ==========================================
# 1- الهندسة البصرية والوسائط (Visual Identity)
# ==========================================
st.set_page_config(page_title="Basil Global Quantum HQ", layout="wide", page_icon="👑")

# تصميم احترافي بلمسة سينمائية
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #05070a 0%, #0d1117 100%); color: #ffffff; }
    
    /* تنسيق الكروت المالية العملاقة */
    [data-testid="stMetric"] {
        background: rgba(22, 27, 34, 0.8);
        border: 2px solid #30363d;
        border-radius: 25px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        transition: transform 0.3s;
    }
    [data-testid="stMetric"]:hover { transform: translateY(-10px); border-color: #58a6ff; }
    
    /* نصوص ناصعة وواضحة */
    [data-testid="stMetricValue"] { color: #ffffff !important; font-size: 40px !important; font-weight: 900; }
    [data-testid="stMetricLabel"] { color: #58a6ff !important; font-size: 18px !important; }
    
    /* الأزرار التفاعلية */
    .stButton>button {
        width: 100%; border-radius: 15px; height: 3.5em;
        background: linear-gradient(90deg, #1f6feb, #58a6ff);
        color: white; border: none; font-weight: bold;
        box-shadow: 0 4px 15px rgba(31, 111, 235, 0.4);
    }
    
    .main-title { 
        font-size: 60px; font-weight: 900; text-align: center; 
        background: linear-gradient(90deg, #58a6ff, #bc8cff);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2- القائمة الجانبية (مركز قيادة باسل - الإدارة والأمان)
# ==========================================
with st.sidebar:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
    st.markdown("<h2 style='color: #58a6ff;'>BASIL ADMIN</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.divider()
    st.subheader("🎵 الوسائط الصوتية")
    # إضافة صوت تفاعلي للمشروع
    st.audio("https://www.soundjay.com/buttons/sounds/button-10.mp3") 
    
    st.divider()
    st.subheader("💰 إعدادات السوق")
    ex_rate = st.number_input("سعر صرف الدرهم/يمني اليوم", value=145.0)
    
    st.divider()
    st.subheader("🛡️ بروتوكول الأمان")
    st.code("SSL: ACTIVE\nENCRYPTION: RSA-4096\nSTATUS: SECURED")
    
    if st.button("🔄 تحديث النظام بالكامل"):
        st.balloons()
        st.rerun()

# ==========================================
# 3- المحتوى الرئيسي (مشروع الوسائط المتكامل)
# ==========================================
st.markdown('<p class="main-title">BASIL GLOBAL QUANTUM</p>', unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #8b949e;'>مشروع الوسائط المتعددة: إدارة سلاسل الإمداد الذكية (دبي - اليمن)</h3>", unsafe_allow_html=True)
st.divider()

# التبويبات العملاقة
tab_dashboard, tab_multimedia, tab_logistics, tab_finance, tab_interactive = st.tabs([
    "📊 لوحة التحكم العملاقة", "🎬 معرض الوسائط", "🚢 المسار اللوجستي", "💰 المحرك المالي", "🎮 مركز التفاعل"
])

# --- التبويب 1: لوحة التحكم (الذكاء الاصطناعي) ---
with tab_dashboard:
    st.subheader("📈 رؤى الأداء الاستراتيجي")
    m1, m2, m3 = st.columns(3)
    m1.metric("إجمالي قيمة الأصول", "1,840,000 AED", "+4.2%")
    m2.metric("كفاءة العمليات", "96%", "تحسن مستمر")
    m3.metric("صافي الأرباح المتوقع", "145,000,000 YER")
    
    # رسم بياني تفاعلي عملاق
    df_chart = pd.DataFrame({'الشهر': ['يناير', 'فبراير', 'مارس', 'أبريل'], 'الواردات': [120, 250, 180, 320]})
    fig = px.area(df_chart, x='الشهر', y='الواردات', title="منحنى تدفق البضائع الدولي", color_discrete_sequence=['#58a6ff'])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig, use_container_width=True)

# --- التبويب 2: معرض الوسائط (صور وفيديو) ---
with tab_multimedia:
    st.subheader("📽️ العرض البصري للمشروع")
    c_vid, c_img = st.columns([2, 1])
    with c_vid:
        st.markdown("#### فيديو تشغيلي: من دبي إلى صنعاء")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # رابط افتراضي
    with c_img:
        st.markdown("#### صور المخزون")
        st.image("https://img.freepik.com/free-photo/car-engine-parts_23-2148970367.jpg", caption="قطع أصلية 100%")
        st.image("https://img.freepik.com/free-photo/logistics-transportation-container-cargo-ship_335224-659.jpg", caption="شحن دولي آمن")

# --- التبويب 3: اللوجستيات (تتبع حي) ---
with tab_logistics:
    st.subheader("🚛 مصفوفة اللوجستيات الدولية")
    col_t1, col_t2 = st.columns([2, 1])
    with col_t1:
        st.info("📍 تتبع حي: الشحنة #BSL-2026")
        st.progress(85)
        st.markdown("**الموقع الحالي:** ميناء جبل علي ⬅️ منفذ شحن (اليمن) ➡️ المستودع المركزي")
    with col_t2:
        st.subheader("📜 المستندات القانونية")
        st.success("✅ بوليصة الشحن")
        st.success("✅ الفواتير التجارية")
        st.warning("⏳ فسح الجمارك النهائي")

# --- التبويب 4: المحرك المالي (أتمتة الحسابات) ---
with tab_finance:
    st.subheader("💰 الحاسبة المالية التفاعلية")
    f1, f2 = st.columns(2)
    with f1:
        cost_aed = st.number_input("سعر الشراء (درهم إماراتي)", value=15000)
        tax_pct = st.selectbox("نسبة الجمارك والضرائب", [0.05, 0.15, 0.25], format_func=lambda x: f"{int(x*100)}%")
    with f2:
        final_aed = cost_aed * (1 + tax_pct)
        final_yer = final_aed * ex_rate
        st.metric("التكلفة النهائية (ريال يمني)", f"{final_yer:,.0f} YER")
        st.info(f"إجمالي التكلفة بالدرهم: {final_aed:,.0f} AED")

# --- التبويب 5: مركز التفاعل (أزرار ومؤثرات) ---
with tab_interactive:
    st.subheader("🎮 تفاعل مع النظام")
    st.write("اضغط على الأزرار لتفعيل المؤثرات التفاعلية للمشروع:")
    ib1, ib2, ib3 = st.columns(3)
    
    if ib1.button("🎉 تفعيل احتفال النجاح"):
        st.balloons()
        st.snow()
        st.toast("تهانينا يا باسل! النظام يعمل بكفاءة قصوى.")
        
    if ib2.button("📢 إرسال إشعار صوتي"):
        st.write("🔊 جاري تشغيل تنبيه المستودع...")
        st.audio("https://www.soundjay.com/buttons/sounds/button-09.mp3")
        
    if ib3.button("📊 توليد تقرير شامل"):
        st.success("تم إعداد التقرير التفاعلي بنجاح!")
        st.download_button("تحميل التقرير (PDF)", data="تقرير باسل العالمي", file_name="Basil_Report.pdf")

# ==========================================
# 4- التذييل (Footer)
# ==========================================
st.divider()
st.markdown(f"<p style='text-align: center; color: #8b949e;'>Basil Quantum Enterprise | v23.0 Master Multimedia | {datetime.now().year}</p>", unsafe_allow_html=True)
