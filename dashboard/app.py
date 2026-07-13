import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go

API = "http://127.0.0.1:8000"

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI QA Engineer",
    page_icon="🤖",
    layout="wide"
)
# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🤖 AI QA Engineer")

    st.markdown("---")

    st.success("🟢 Backend Connected")

    st.write("### Features")

    st.write("📊 Quality Score")
    st.write("📝 AI Review")
    st.write("🛠 Fix Code")
    st.write("💡 Explain Code")
    st.write("🧪 Generate Tests")
    st.write("🐞 Bug Detector" )
    st.markdown("---")

    st.info(
        """
Powered by

• FastAPI

• Streamlit

• Groq LLM
"""
    )

    st.markdown("---")

    st.caption("Version 2.0")
# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main{
    padding-top:20px;
}

div[data-testid="metric-container"]{
    background:#1f1f1f;
    border-radius:15px;
    padding:15px;
    border:1px solid #444;
    box-shadow:0px 3px 10px rgba(0,0,0,.25);
}

div[data-testid="metric-container"] label{
    color:#00D9FF;
    font-weight:bold;
}

.stButton>button{
    width:100%;
    border-radius:10px;
}
/* Tabs */

button[data-baseweb="tab"]{
    font-size:16px;
    font-weight:600;
    border-radius:12px;
    padding:12px 20px;
    margin-right:8px;
}

button[data-baseweb="tab"]:hover{
    background:#2563eb;
    color:white;
}

button[aria-selected="true"]{
    background:#2563eb !important;
    color:white !important;
}

/* Expander */

.streamlit-expanderHeader{
    font-size:18px;
    font-weight:bold;
}

/* Code Block */

pre{
    border-radius:12px !important;
}

/* Download Button */

.stDownloadButton>button{
    width:100%;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HISTORY
# --------------------------------------------------

if st.sidebar.button("📜 Show History", key="history_btn"):

    try:

        response = requests.get(f"{API}/history")

        if response.status_code == 200:

            history = response.json()["history"]

            if history:

                df = pd.DataFrame(history)

                st.subheader("📜 Previous Analysis")

                if "quality_score" in df.columns:

                    minimum = st.slider(
                        "Minimum Quality Score",
                        0,
                        10,
                        0
                    )

                    df = df[df["quality_score"] >= minimum]

                st.dataframe(
                    df,
                    use_container_width=True
                )

            else:

                st.info("No history available.")

        else:

            st.error(response.text)

    except Exception as e:

        st.error(e)
 # --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown("""
<div style="
background: linear-gradient(90deg,#0f172a,#1e3a8a,#2563eb);
padding:30px;
border-radius:20px;
text-align:center;
margin-bottom:25px;
box-shadow:0 8px 20px rgba(0,0,0,0.35);
">

<h1 style="color:white;font-size:42px;margin-bottom:10px;">
🤖 AI QA Engineer
</h1>

<p style="color:#dbeafe;font-size:20px;margin:0;">
Analyze • Review • Fix • Explain • Generate Tests
</p>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DASHBOARD STATS
# --------------------------------------------------

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "🤖 AI Modules",
        "6",
        delta="Active"
    )

with col2:
    st.metric(
        "⚡ API",
        "Groq",
        delta="Online"
    )

with col3:
    st.metric(
        "📄 Reports",
        "PDF",
        delta="Enabled"
    )

with col4:
    st.metric(
        "🟢 Status",
        "Healthy",
        delta="100%"
    )

st.info(
    "🚀 Upload a Python file or paste your code below. The AI can analyze quality, detect bugs, review code, fix issues, explain logic, and generate pytest test cases."
)
# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------
import ast
st.markdown("## 📂 Upload Your Python Project")
uploaded_file = st.file_uploader(
    "📁 Drag & Drop your Python file here",
    type=["py"],
    help="Supported format: .py"
)

code = ""
col1, col2 = st.columns(2)

with col1:

    if st.button("📄 Load Sample Code"):

        code = """
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(add(10, 20))
"""

with col2:

    if st.button("🗑 Clear Editor"):

        code = ""
if uploaded_file:

    code = uploaded_file.read().decode("utf-8")

    st.success(f"✅ File Uploaded Successfully: {uploaded_file.name}")
    st.subheader("📄 Uploaded Source Code")

    st.code(
        code,
        language="python"
    )

else:

   code = st.text_area(
    "Paste Python Code",
    value=code,
    height=300
)
    # -------------------------
# Smart File Analysis
# -------------------------

if uploaded_file:

    try:
        tree = ast.parse(code)

        functions = sum(
            isinstance(node, ast.FunctionDef)
            for node in ast.walk(tree)
        )

        classes = sum(
            isinstance(node, ast.ClassDef)
            for node in ast.walk(tree)
        )

        imports = sum(
            isinstance(node, (ast.Import, ast.ImportFrom))
            for node in ast.walk(tree)
        )

        lines = len(code.splitlines())

        st.subheader("📂 File Analysis")

        c1, c2, c3 = st.columns(3)

        c1.metric("📄 File", uploaded_file.name)
        c2.metric("📦 Size", f"{uploaded_file.size/1024:.2f} KB")
        c3.metric("📏 Lines", lines)

        c4, c5, c6 = st.columns(3)

        c4.metric("🧩 Functions", functions)
        c5.metric("🏛 Classes", classes)
        c6.metric("📚 Imports", imports)

    except Exception as e:
        st.error(f"Analysis Error: {e}")
if code.strip():

    lines = len(code.splitlines())
    words = len(code.split())
    chars = len(code)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📄 Lines", lines)

    with col2:
        st.metric("🔤 Words", words)

    with col3:
        st.metric("⌨ Characters", chars)

     # -------------------------
# Code Complexity Meter
# -------------------------

if code.strip():

    lines = len(code.splitlines())

    if lines < 30:
        level = "🟢 Beginner"
        progress = 0.30

    elif lines < 100:
        level = "🟡 Intermediate"
        progress = 0.65

    else:
        level = "🔴 Advanced"
        progress = 1.0

    st.subheader("🧠 Code Complexity")

    st.progress(progress)

    st.success(f"Complexity Level : {level}")   

if code.strip():

    with st.expander("👀 Preview Code"):

        st.code(code, language="python")
# --------------------------------------------------
# TABS
# --------------------------------------------------
st.markdown("## 🚀 AI Tools")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Quality Score",
    "📝 AI Review",
    "🛠 Fix Code",
    "💡 Explain",
    "🧪 Tests",
    "🐞 Bug Detector"
])

with tab1:

    if st.button("🚀 Analyze Code", key="analyze"):

        if code.strip() == "":
            st.warning("Please upload or paste Python code.")

        else:

            with st.spinner("🤖 AI is analyzing your code..."):

                try:
                    response = requests.post(
                        f"{API}/quality-score",
                        json={"code": code},
                        timeout=30
                    )
                except requests.exceptions.ConnectionError:
                    st.error("❌ Cannot connect to FastAPI backend. Make sure uvicorn is running.")
                    st.stop()
                except requests.exceptions.Timeout:
                    st.error("⏱ Backend request timed out.")
                    st.stop() 

            if response.status_code == 200:

                response_json = response.json()
                st.json(response_json)
                if "analysis" not in response_json:
                    st.error("Backend Error")
                    st.stop()

                data = response_json["analysis"]

                st.success("Analysis Complete ✅")

                score = data["quality_score"]
                st.write(type(score))
                st.write(score)
                # -------------------------
                # Overall Grade
                # -------------------------

                if score >= 9:
                    grade = "A+"
                    recommendation = "✅ Production Ready"

                elif score >= 8:
                    grade = "A"
                    recommendation = "👍 Very Good Code"

                elif score >= 7:
                    grade = "B"
                    recommendation = "⚠ Needs Minor Improvements"

                elif score >= 6:
                    grade = "C"
                    recommendation = "⚠ Improve Code Quality"

                else:
                    grade = "D"
                    recommendation = "❌ Major Refactoring Needed"

                col1, col2 = st.columns(2)

                with col1:

                    fig = go.Figure(go.Indicator(
                        mode="gauge+number",
                        value=score,
                        title={"text": "Quality Score"},
                        gauge={
                            "axis": {"range": [0,10]},
                            "bar": {"color":"green"}
                        }
                    ))

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

                with col2:

                    st.metric(
                        "🏆 Overall Grade",
                        grade
                    )

                    st.metric(
                        "⭐ Quality Score",
                        f"{score}/10"
                    )

                    st.success(recommendation)

                st.divider()

                # -------------------------
                # Bar Chart
                # -------------------------

                scores = {
                    "Security": data["security"],
                    "Performance": data["performance"],
                    "Readability": data["readability"],
                    "Maintainability": data["maintainability"]
                }

                fig = go.Figure()

                fig.add_trace(
                    go.Bar(
                        x=list(scores.keys()),
                        y=list(scores.values())
                    )
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

                # -------------------------
                # Radar Chart
                # -------------------------

                categories = list(scores.keys())

                values = list(scores.values())

                radar = go.Figure()

                radar.add_trace(
                    go.Scatterpolar(
                        r=values+[values[0]],
                        theta=categories+[categories[0]],
                        fill="toself"
                    )
                )

                radar.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            visible=True,
                            range=[0,10]
                        )
                    ),
                    showlegend=False
                )

                st.plotly_chart(
                    radar,
                    use_container_width=True
                )

                # -------------------------
                # Pie Chart
                # -------------------------

                pie = go.Figure(
                    data=[
                        go.Pie(
                            labels=categories,
                            values=values,
                            hole=0.45
                        )
                    ]
                )

                st.plotly_chart(
                    pie,
                    use_container_width=True
                )

                st.divider()

                # -------------------------
                # Progress Bars
                # -------------------------

                st.subheader("📈 Metrics")

                st.write("Security")
                st.progress(data["security"]/10)

                st.write("Performance")
                st.progress(data["performance"]/10)

                st.write("Readability")
                st.progress(data["readability"]/10)

                st.write("Maintainability")
                st.progress(data["maintainability"]/10)

                st.divider()

                st.subheader("📝 AI Summary")

                st.write(data["summary"])

                if "pdf_report" in response_json:

                    pdf_path = response_json["pdf_report"]

                    try:

                        with open(pdf_path,"rb") as pdf:

                            st.download_button(
                                "📄 Download QA Report",
                                data=pdf,
                                file_name="QA_Report.pdf",
                                mime="application/pdf"
                            )

                    except Exception as e:

                        st.warning(e)

            else:

                st.error(response.text)

with tab2:

    if st.button("🔍 AI Review", key="review"):

        if code.strip() == "":
            st.warning("Please upload or paste Python code.")

        else:

            with st.spinner("🤖 Reviewing your code..."):

                response = requests.post(
                    f"{API}/review",
                    json={"code": code}
                )
                st.write("Status Code:", response.status_code)

                response_json = response.json()

                st.json(response_json)
                


            if response.status_code == 200:

                data = response.json()

                # Agar backend error bheje
                if "error" in data:
                    st.error(data["error"])
                    st.stop()

                review = data["review"]

                st.success("✅ Review Completed")

                with st.container(border=True):

                    st.markdown("## 📝 AI Review Report")

                    st.markdown(review)

            else:

                st.error(response.text)
                data = response.json()

                if "error" in data:
                    st.error(data["error"])
                    st.stop()

                review = data["review"]

with tab3:

    if st.button("🛠 Fix Code", key="fix"):

        if code.strip() == "":
            st.warning("Please upload or paste code.")

        else:

            with st.spinner("🔧 AI is fixing your code..."):

                response = requests.post(
                    f"{API}/fix-code",
                    json={"code": code}
                )

            

            if response.status_code == 200:

                data = response.json()

                # Backend error check
                if "error" in data:
                    st.error(data["error"])
                    st.stop()

                st.success("✅ Code Fixed Successfully")

                st.metric(
                    "🤖 AI Confidence",
                    f"{data['confidence']}%"
                )

                with st.container(border=True):

                    st.markdown("## 🛠 Fixed Python Code")

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

    if st.button("💡 Explain Code", key="explain"):

        if code.strip() == "":
            st.warning("Please upload or paste code.")

        else:

            with st.spinner("📖 AI is explaining your code..."):

                response = requests.post(
                    f"{API}/explain-code",
                    json={"code": code}
                )

            if response.status_code == 200:

                data = response.json()

                # Backend error check
                if "error" in data:
                    st.error(data["error"])
                    st.stop()

                st.success("📖 Explanation Ready")

                with st.container(border=True):

                    st.markdown("## 💡 Code Explanation")

                    st.markdown(data["explanation"])

            else:

                st.error(response.text)

with tab5:

    if st.button("🧪 Generate Tests", key="tests"):

        if code.strip() == "":
            st.warning("Please upload or paste code.")

        else:

            with st.spinner("🧪 AI is generating tests..."):

                response = requests.post(
                    f"{API}/generate-tests",
                    json={"code": code}
                )

            if response.status_code == 200:

                data = response.json()

                # Backend error check
                if "error" in data:
                    st.error(data["error"])
                    st.stop()

                tests = data["tests"]

                st.success("🧪 Test Cases Generated Successfully")

                with st.container(border=True):

                    st.markdown("## 🧪 Generated Pytest Test Cases")

                    st.code(
                        tests,
                        language="python"
                    )

                st.download_button(
                    "⬇ Download Test Cases",
                    data=tests,
                    file_name="test_code.py",
                    mime="text/plain"
                )

            else:

                st.error(response.text) 
with tab6:

    st.subheader("🐞 Bug Detector")

    if st.button("🔍 Scan Bugs"):

        response = requests.post(
            f"{API}/scan-bugs",
            json={"prompt": code}
        )

        if response.status_code == 200:

            data = response.json()

            if "error" not in data:

                st.metric("🐞 Bugs Found", data["total"])

                c1, c2, c3 = st.columns(3)

                c1.metric("🔴 Critical", data["critical"])
                c2.metric("🟠 Medium", data["medium"])
                c3.metric("🟢 Minor", data["minor"])

                st.session_state["bugs_scanned"] = True

            else:

                st.error(data["error"])

    if st.session_state.get("bugs_scanned"):

        if st.button("🔧 Fix All Bugs"):

            response = requests.post(
                f"{API}/fix-code",
                json={"code": code}
            )

            if response.status_code == 200:

                fixed = response.json()

                st.success("✅ Bugs Fixed Successfully")

                st.code(
                    fixed["fixed_code"],
                    language="python"
                )

                st.download_button(
                    "⬇ Download Fixed Code",
                    fixed["fixed_code"],
                    file_name="fixed_code.py"
                )                 

st.markdown("---")

st.markdown(
    """
    <div style="
    text-align:center;
    padding:20px;
    color:#94a3b8;
    ">

    <h4>🤖 AI QA Engineer</h4>

    <p>
    Built with ❤️ by harshvardhan Singh(raju)
    </p>

    <p>
    © 2026 Harshvardhan Singh
    </p>

    </div>
    """,
    unsafe_allow_html=True
)                                                   