import streamlit as st

st.set_page_config(page_title="Earned Value Analysis", page_icon="📊", layout="centered")

st.title("📊 Earned Value Analysis Tool")
st.markdown("Enter your project values below to get an instant health check.")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    PV = st.number_input("Planned Value (PV) $", min_value=0.0, format="%.2f")
with col2:
    AC = st.number_input("Actual Cost (AC) $", min_value=0.0, format="%.2f")
with col3:
    EV = st.number_input("Earned Value (EV) $", min_value=0.0, format="%.2f")

st.divider()

if st.button("🔍 Analyse Project", use_container_width=True):

    if AC == 0 or PV == 0:
        st.error("⚠️ PV and AC cannot be zero.")
    else:
        CV  = EV - AC
        SV  = EV - PV
        CPI = EV / AC
        SPI = EV / PV

        st.subheader("📈 Results")

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Cost Variance (CV)",     f"${CV:.2f}")
        m2.metric("Schedule Variance (SV)", f"${SV:.2f}")
        m3.metric("CPI", f"{CPI:.2f}")
        m4.metric("SPI", f"{SPI:.2f}")

        st.divider()

        st.subheader("🩺 Project Health")

        # CV Check
        if CV == 0:
            st.success("✅ Cost: Project is exactly on budget")
        elif CV > 0:
            st.success("✅ Cost: Project is under budget")
        else:
            st.error("❌ Cost: Project is over budget")

        # SV Check
        if SV == 0:
            st.success("✅ Schedule: Project is exactly on schedule")
        elif SV > 0:
            st.success("✅ Schedule: Project is ahead of schedule")
        else:
            st.error("❌ Schedule: Project is behind schedule")

        # CPI Check
        if CPI == 1:
            st.info("ℹ️ CPI: Cost efficiency is perfect (1.0)")
        elif CPI > 1:
            st.success(f"✅ CPI {CPI:.2f}: Getting more value than spent")
        else:
            st.warning(f"⚠️ CPI {CPI:.2f}: Spending more than planned")

        # SPI Check
        if SPI == 1:
            st.info("ℹ️ SPI: Schedule efficiency is perfect (1.0)")
        elif SPI > 1:
            st.success(f"✅ SPI {SPI:.2f}: Ahead of schedule")
        else:
            st.warning(f"⚠️ SPI {SPI:.2f}: Behind schedule")

st.divider()
st.caption("Built with Python & Streamlit · Earned Value Analysis Tool")
