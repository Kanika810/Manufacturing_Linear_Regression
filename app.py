import streamlit as st
import requests

# ---------- Page Configuration ----------
st.set_page_config(
    page_title="Manufacturing Equipment Output Prediction",
    page_icon="📦",
    layout="centered"
)

# ---------- Custom Styling ----------
st.markdown("""
    <style>
        .main {
            background-color: #0E1117;
            color: #FFFFFF;
        }
        h1, h2, h3 {
            color: #F5B041;
            text-align: center;
        }
        .stButton>button {
            background-color: #F5B041;
            color: black;
            border-radius: 8px;
            font-weight: bold;
            padding: 0.6em 1.5em;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #F7DC6F;
            color: black;
            transform: scale(1.05);
        }
        .css-1d391kg p {
            color: #D5D8DC;
        }
    </style>
""", unsafe_allow_html=True)


# ---------- App Header ----------
st_lottie(lottie_machine, height=180, key="machine")
st.title("📦 Manufacturing Equipment Output Prediction")
st.write("### Enter Machine Parameters Below")

# ---------- Input Section ----------
with st.form("input_form"):
    st.subheader("Machine Parameters")
    col1, col2 = st.columns(2)

    with col1:
        inj_temp = st.number_input("Injection Temperature (°C)", 0.0, 300.0, 180.0, step=1.0)
        inj_pressure = st.number_input("Injection Pressure (bar)", 0.0, 200.0, 80.0, step=1.0)
        cycle_time = st.number_input("Cycle Time (s)", 0.0, 60.0, 15.0, step=0.5)
        cooling_time = st.number_input("Cooling Time (s)", 0.0, 60.0, 10.0, step=0.5)

    with col2:
        viscosity = st.number_input("Material Viscosity (Pa·s)", 0.0, 500.0, 100.0, step=1.0)
        ambient_temp = st.number_input("Ambient Temperature (°C)", 0.0, 50.0, 18.0, step=1.0)
        machine_age = st.number_input("Machine Age (years)", 0.0, 20.0, 1.0, step=0.5)
        operator_exp = st.number_input("Operator Experience (months)", 0.0, 240.0, 1.0, step=1.0)
        maint_hours = st.number_input("Maintenance Hours Since Last Service", 0.0, 1000.0, 0.0, step=0.5)

    submitted = st.form_submit_button("🔮 Predict Output")

# ---------- Prediction Section ----------
if submitted:
    with st.spinner("Calculating prediction... 🔍"):
        # For now, simulate a fake prediction
        import time
        time.sleep(2)
        predicted_output = round((inj_temp * 0.3 + inj_pressure * 0.4 + operator_exp * 0.2) / 10, 2)
    
    st.success(f"✅ **Predicted Equipment Output:** {predicted_output} units/hour")
    st.balloons()

# ---------- Footer ----------
st.markdown("---")
st.caption("Developed with  using Streamlit by kanika ")
