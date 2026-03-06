import streamlit as st
import pandas as pd
import numpy as np
import time

# Page Config
st.set_page_config(page_title="Flex-Bridge: Heat Sponge", layout="wide")


# Injecting Custom CSS for a Green Energy Theme
st.markdown("""
    <style>

        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #d0ddb5;
        }
        [data-testid="stSidebar"] .stMarkdown p {
            color: #e0f2e9;
        }
        
    </style>
    """, unsafe_allow_html=True)


# --- Header Section ---
st.title("Flex-Bridge Platform")
st.subheader("Transforming thermal loads into a 'Heat Sponge'")
st.markdown("---")

# --- STAGE 1: Input Dashboard ---
st.sidebar.header("Stage 1: Setup")
region = st.sidebar.selectbox("Select Region", ["Grand Est", "Île-de-France", "Hauts-de-France"])
forecast_type = st.sidebar.selectbox("Forecast Scenario", ["High Wind + Full Sun", "Moderate Renewables", "Low Yield"])
grid_state = st.sidebar.radio("Grid Condition", ["Saturated Junction", "Normal", "Under-utilised"])

if st.sidebar.button("Run Renewable Surplus Forecast"):
    st.session_state['forecast_run'] = True

# --- STAGE 2 & 3: Process & Output ---
if st.session_state.get('forecast_run'):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Stage 2: Prediction Results")
        # Simulated Forecast Data
        hours = np.arange(24)
        fixed_surplus = [
        2.0,  2.1,  2.1,  2.1,  3.2,  5.0,  
        4.8,  4.5,  4.0,  4.2,  5.0, 6.2,  
        7.0, 8.0, 7.8, 7.4,  6.0,  4.0, 
        3.5, 2.0, 2.5,  2.8,  3.2,  2.8  
        ]
        chart_df = pd.DataFrame({
            "Hour of Day": hours,
            "Predicted Surplus (MWh)": fixed_surplus
        }).set_index("Hour of Day")
        st.line_chart(chart_df)

        
    with col2:
        st.header("Stage 3: Predicted Surplus")
        st.metric(label="Total Predicted Surplus", value="1.2 MWh", delta="0.4 MWh vs Avg")
        st.warning("⚠️ Risk Hours Highlighted: 11:00 – 16:00")
        
    st.markdown("---")

    # --- STAGE 4 & 5: Proposed Intervention & Optimization ---
    st.header("Stage 4: 'Heat Sponge' Strategy")
    
    col_interv1, col_interv2 = st.columns(2)
    
    with col_interv1:
        st.info("🔄 **Intervention Logic:** Shifting Residential Hot-Water heating from 'Night-only' to 'Midday-first'.")
        tank_control = st.toggle("Activate Smart Water Tank Control")
        
    if tank_control:
        with col_interv2:
            st.header("Stage 5: Load Scheduling")
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
