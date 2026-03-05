import streamlit as st
import pandas as pd
import numpy as np
import time

# Page Config
st.set_page_config(page_title="Flex-Bridge: Solar Sponge", layout="wide")

# --- Header Section ---
st.title("⚡ Flex-Bridge Platform")
st.subheader("Transforming thermal loads into a 'Solar Sponge'")
st.markdown("---")

# --- STAGE 1: Input Dashboard ---
st.sidebar.header("Stage 1: User Setup")
region = st.sidebar.selectbox("Select Region", ["Grand Est", "Île-de-France", "Hauts-de-France"])
forecast_type = st.sidebar.selectbox("Forecast Scenario", ["High Wind + Full Sun", "Moderate Renewables", "Low Yield"])
grid_state = st.sidebar.radio("Grid Condition", ["Saturated Junction", "Normal", "Under-utilised"])

if st.sidebar.button("Run Renewable Surplus Forecast"):
    st.session_state['forecast_run'] = True

# --- STAGE 2 & 3: Process & Output ---
if st.session_state.get('forecast_run'):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Stage 3: Prediction Results")
        # Simulated Forecast Data
        chart_data = pd.DataFrame(
            np.random.randn(24, 1).cumsum(),
            index=pd.date_range("2026-03-05", periods=24, freq="H"),
            columns=["Predicted Surplus (MWh)"]
        )
        st.line_chart(chart_data)
        
    with col2:
        st.metric(label="Total Predicted Surplus", value="1.2 MWh", delta="0.4 MWh vs Avg")
        st.warning("⚠️ Risk Hours Highlighted: 11:00 – 16:00")
        
    st.markdown("---")

    # --- STAGE 4 & 5: Proposed Intervention & Optimization ---
    st.header("Stage 4: 'Solar Sponge' Strategy")
    
    col_interv1, col_interv2 = st.columns(2)
    
    with col_interv1:
        st.info("🔄 **Intervention Logic:** Shifting Residential Hot-Water heating from 'Night-only' to 'Midday-first'.")
        tank_control = st.toggle("Activate Smart Water Tank Control")
        
    if tank_control:
        with col_interv2:
            st.success("✅ Stochastic Load Scheduling Active")
            st.write("Outcome: Staggered scheduling preventing 'Rebound Peak'.")
            
        # --- STAGE 6: Benefit Confirmation ---
        st.markdown("---")
        st.header("Stage 6: Economic Model (MidiFlex Tariff)")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Current Rate", "0.22 €/kWh")
        c2.metric("MidiFlex Rate", "0.08 €/kWh", "-63%")
        c3.metric("User Financial Gain", "+ €14.50", "Estimated Monthly")
        
        st.balloons()