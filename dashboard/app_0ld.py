import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go


API = "http://127.0.0.1:8000"

st.markdown("""
<style>

div[data-testid="metric-container"]{
    background:#1E1E1E;
    border:1px solid #3A3A3A;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.3);
}

div[data-testid="metric-container"] label{
    color:#00E5FF;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="AI QA Engineer",
    page_icon="🤖",
    layout="wide"
)

# ===========================
# Sidebar
# ===========================

st.sidebar.title("🤖 AI QA Engineer")

st.sidebar.success("Backend Connected")
theme = st.sidebar.toggle(
    "🌙 Dark Mode",
    value=True
)

if not theme:
    st.markdown("""
    <style>
    .stApp{
        background:white;
        color:black;
    }
    </style>
    """, unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.markdown("### Features")

st.sidebar.write("📊 Quality Score")
st.sidebar.write("🔍 AI Review")
st.sidebar.write("🛠 Code Fix")
st.sidebar.write("💡 Explain Code")
st.sidebar.write("🧪 Generate Tests")
st.sidebar.write("📄 PDF Report")

st.sidebar.markdown("---")

# ===========================
# History
# ===========================

if st.sidebar.button("📜 Show History", key="history_btn"):

    try:

        response = requests.get(f"{API}/history")

        if response.status_code == 200:

            history = response.json()["history"]

            if history:

                st.sidebar.success(
                    f"{len(history)} analyses found"
                )

                df = pd.DataFrame(history)

                st.subheader("📜 Analysis History")

                st.dataframe(
                    df,
                    use_container_width=True
                )

            else:

                st.info("No history found.")

        else:

            st.error(response.text)

    except Exception as e:

        st.error(e)

# ===========================
# Title
# ===========================

st.title("🤖 AI QA Engineer Dashboard")

st.write(
    "Upload a Python file or paste Python code below."
)

# ===========================
# Upload
# ===========================

uploaded_file = st.file_uploader(
    "Upload Python File",
    type=["py"]
)

code = ""

if uploaded_file is not None:

    code = uploaded_file.read().decode("utf-8")

    st.success(f"Uploaded: {uploaded_file.name}")

    st.code(code, language="python")

else:

    code = st.text_area(
        "Paste Python Code",
        height=350
    )

# ===========================
# Tabs
# ===========================

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "📊 Quality",
        "🔍 Review",
        "🛠 Fix",
        "💡 Explain",
        "🧪 Tests"
    ]
)
with tab1:

    if st.button("📊 Analyze Code", key="analyze_btn"):

        if code.strip() == "":
            st.warning("Please upload or paste Python code.")
        else:

            with st.spinner("Analyzing code..."):

                response = requests.post(
                    f"{API}/quality-score",
                    json={"code": code}
                )

            if response.status_code == 200:

                result = response.json()
                data = result["analysis"]

                st.success("Analysis Completed ✅")

                # Metrics
                col1, col2, col3 = st.columns(3)

                col1.metric("⭐ Quality", data["quality_score"])
                col2.metric("🔒 Security", data["security"])
                col3.metric("⚡ Performance", data["performance"])

                col4, col5 = st.columns(2)

                col4.metric("📖 Readability", data["readability"])
                col5.metric("🛠 Maintainability", data["maintainability"])

                st.markdown("---")

                # Gauge Chart
                gauge = go.Figure(
                    go.Indicator(
                        mode="gauge+number",
                        value=data["quality_score"],
                        title={"text": "Quality Score"},
                        gauge={
                            "axis": {"range": [0, 10]}
                        }
                    )
                )

                st.plotly_chart(
                    gauge,
                    use_container_width=True
                )

                # Bar Chart
                bar = go.Figure()

                bar.add_bar(
                    x=[
                        "Security",
                        "Performance",
                        "Readability",
                        "Maintainability"
                    ],
                    y=[
                        data["security"],
                        data["performance"],
                        data["readability"],
                        data["maintainability"]
                    ]
                )

                st.plotly_chart(
                    bar,
                    use_container_width=True
                )

                st.subheader("📝 AI Summary")

                st.write(data["summary"])

                # PDF Download
                if "pdf_report" in result:

                    pdf_path = result["pdf_report"]

                    try:

                        with open(pdf_path, "rb") as pdf:

                            st.download_button(
                                "📄 Download QA Report",
                                pdf,
                                file_name="QA_Report.pdf",
                                mime="application/pdf"
                            )

                    except Exception:

                        st.warning("PDF report not found.")

            else:

                st.error(response.text)
with tab2:

    if st.button("🔍 Review Code", key="review_btn"):

        if code.strip() == "":
            st.warning("Please upload or paste Python code.")

        else:

            with st.spinner("Reviewing code..."):

                response = requests.post(
                    f"{API}/review",
                    json={"code": code}
                )

            if response.status_code == 200:

                st.success("Review Completed ✅")

                st.markdown(response.json()["review"])

            else:

                st.error(response.text)

with tab3:

    if st.button("🛠 Fix Code", key="fix_btn"):

        if code.strip() == "":
            st.warning("Please upload or paste Python code.")

        else:

            with st.spinner("Fixing code..."):

                response = requests.post(
                    f"{API}/fix-code",
                    json={"code": code}
                )

            if response.status_code == 200:

                data = response.json()

                st.success("Code Fixed Successfully ✅")

                st.metric(
                    "AI Confidence",
                    f"{data['confidence']}%"
                )

                st.code(
                    data["fixed_code"],
                    language="python"
                )

                st.download_button(
                    "⬇ Download Fixed Code",
                    data=data["fixed_code"],
                    file_name="fixed_code.py",
                    mime="text/plain"
                )

            else:

                st.error(response.text)
with tab4:

    if st.button("💡 Explain Code", key="explain_btn"):

        if code.strip() == "":
            st.warning("Please upload or paste Python code.")

        else:

            with st.spinner("Explaining code..."):

                response = requests.post(
                    f"{API}/explain-code",
                    json={"code": code}
                )

            if response.status_code == 200:

                st.success("Explanation Generated")

                st.markdown(response.json()["explanation"])

            else:

                st.error(response.text)
with tab5:

    if st.button("🧪 Generate Tests", key="tests_btn"):

        if code.strip() == "":
            st.warning("Please upload or paste Python code.")

        else:

            with st.spinner("Generating unit tests..."):

                response = requests.post(
                    f"{API}/generate-tests",
                    json={"code": code}
                )

            if response.status_code == 200:

                data = response.json()
                tests = data.get("tests", "")

                st.success("Tests Generated ✅")

                st.json(data)

                st.code(
                    tests,
                    language="python"
                )

                st.download_button(
                    "⬇ Download Tests",
                    data=tests,
                    file_name="test_generated.py",
                    mime="text/plain"
                )

            else:
                st.error(response.text)
