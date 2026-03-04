import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

model = joblib.load("best_model.pkl")

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="Medical Cost Intelligence System",
    page_icon="🏥",
    layout="wide"
)

# ==========================================================
# PREMIUM GLASSMORPHIC DESIGN (WITH ANIMATION)
# ==========================================================
st.markdown("""
<style>

/* Animated Gradient Background */
.stApp {
    background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #1e3c72);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    color: white;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Glass Container */
.block-container {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(15px);
    padding: 2rem 3rem;
    border-radius: 25px;
}

/* Header */
.main-header {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 10px;
}

.sub-header {
    text-align: center;
    font-size: 18px;
    opacity: 0.8;
    margin-bottom: 40px;
}

/* KPI Card */
.kpi-card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    backdrop-filter: blur(10px);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
    transition: 0.4s;
}

.kpi-card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 12px 35px rgba(0,0,0,0.4);
}

/* Section Title */
.section-title {
    font-size: 28px;
    font-weight: 600;
    margin-top: 50px;
    margin-bottom: 20px;
    border-left: 6px solid #00c6ff;
    padding-left: 12px;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    font-size: 18px;
    border-radius: 12px;
    border: none;
    height: 3em;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #0072ff, #00c6ff);
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# LOAD DATA
# ==========================================================
df = pd.read_csv("insurance.csv")

# ==========================================================
# HEADER
# ==========================================================
st.markdown('<div class="main-header">🏥 Medical Cost Intelligence System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Premium Healthcare Analytics & Risk Prediction Platform</div>', unsafe_allow_html=True)

# ==========================================================
# NAVIGATION
# ==========================================================
menu = st.radio("", ["📊 Analytics Dashboard", "💰 Prediction Engine"], horizontal=True)

# ==========================================================
# ANALYTICS DASHBOARD
# ==========================================================
if menu == "📊 Analytics Dashboard":

    st.markdown('<div class="section-title">📌 Key Metrics Overview</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    c1.markdown(f'<div class="kpi-card"><h4>Total Records</h4><h2>{df.shape[0]}</h2></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="kpi-card"><h4>Average Age</h4><h2>{round(df.age.mean(),1)}</h2></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="kpi-card"><h4>Average BMI</h4><h2>{round(df.bmi.mean(),1)}</h2></div>', unsafe_allow_html=True)
    c4.markdown(f'<div class="kpi-card"><h4>Average Charges</h4><h2>${round(df.charges.mean(),2)}</h2></div>', unsafe_allow_html=True)

    # ---------------- UNIVARIATE ----------------
    st.markdown('<div class="section-title">📊 Univariate Analysis</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.histogram(df, x="age", color_discrete_sequence=["#00c6ff"])
        fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.histogram(df, x="charges", color_discrete_sequence=["#ff4b4b"])
        fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig2, use_container_width=True)

    # ---------------- BIVARIATE ----------------
    st.markdown('<div class="section-title">📈 Bivariate Analysis</div>', unsafe_allow_html=True)

    fig3 = px.box(df, x="smoker", y="charges",
                  color="smoker",
                  color_discrete_sequence=["#00ff87","#ff416c"])
    fig3.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig3, use_container_width=True)

    # ---------------- MULTIVARIATE ----------------
    st.markdown('<div class="section-title">🔬 Multivariate Correlation</div>', unsafe_allow_html=True)

    corr = df.select_dtypes(include=["number"]).corr()
    fig5 = px.imshow(corr, text_auto=True, color_continuous_scale="RdBu_r")
    fig5.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig5, use_container_width=True)

# ==========================================================
# PREDICTION ENGINE
# ==========================================================
if menu == "💰 Prediction Engine":

    st.markdown('<div class="section-title">💰 Medical Cost Estimator</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age", 18, 65, 30)
        bmi = st.slider("BMI", 10.0, 50.0, 25.0)
        children = st.slider("Children", 0, 5, 0)

    with col2:
        sex = st.selectbox("Gender", ["male", "female"])
        smoker = st.selectbox("Smoker", ["yes", "no"])
        region = st.selectbox("Region", df.region.unique())

    st.markdown("---")

    if st.button("Generate Prediction"):

        input_data = pd.DataFrame({
            "age": [age],
            "sex": [sex],
            "bmi": [bmi],
            "children": [children],
            "smoker": [smoker],
            "region": [region]
        })

        prediction = model.predict(input_data)

        st.success(f"Estimated Medical Cost: ${round(prediction[0],2)}")