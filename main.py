import streamlit as st

st.set_page_config(page_title="نظام تجارة قطع الغيار", layout="centered")
st.title("📦 نظام التسعير الذكي (دبي - اليمن)")

# محرك الحسابات المبسط
aed_price = st.number_input("سعر القطعة في دبي (درهم)", value=100.0)
yer_rate = st.number_input("سعر صرف الدولار في اليمن", value=1600)

# الحسبة: سعر دبي + 10% جمارك + 15 درهم شحن بري / 3.67 (تحويل لدولار) * الصرف * 1.25 (ربحك)
final_price = ((aed_price * 1.1 + 15) / 3.67) * yer_rate * 1.25

if st.button("اعرض السعر النهائي للزبون"):
    st.header(f"{round(final_price):,} ريال يمني")
    st.success("تم حساب السعر بنجاح")
