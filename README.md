# 🤖 AI QA Engineer

AI QA Engineer is a web application that analyzes Python code using AI. It helps developers improve code quality by reviewing code, fixing bugs, explaining logic, generating test cases, and creating PDF reports.

---

## 🚀 Features

- 📊 Code Quality Score
- 📝 AI Code Review
- 🛠 AI Code Fix
- 💡 Code Explanation
- 🧪 Pytest Test Case Generator
- 📄 PDF Report Generation
- 📜 Analysis History
- 📂 Python File Upload Support

---

## 🛠 Tech Stack

### Backend
- FastAPI
- Python
- Groq API

### Frontend
- Streamlit
- Plotly

### Other Libraries
- ReportLab
- Requests
- Pydantic

---

## 📂 Project Structure

```text
AI_QA_Engineer/
│
├── agents/
├── dashboard/
├── models/
├── reports/
├── routers/
├── utils/
│
├── main.py
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd AI_QA_Engineer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

---

## ▶️ Run Backend

```bash
uvicorn main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

---

## ▶️ Run Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard URL:

```
http://localhost:8501
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /quality-score | Analyze code quality |
| POST | /review | AI Code Review |
| POST | /fix-code | Fix Python Code |
| POST | /explain-code | Explain Code |
| POST | /generate-tests | Generate Pytest Cases |
| GET | /history | Analysis History |

---

## 📸 Screenshots

Add screenshots here after project completion.

Example:

- Dashboard
- Quality Score
- AI Review
- Code Fix
- Test Generation

---

## 🔮 Future Improvements

- GitHub Repository Analysis
- Multi-language Support
- Docker Deployment
- Authentication
- CI/CD Integration
- Team Collaboration

---

## 👨‍💻 Author

**Harshvardhan Singh**

B.Tech Data Science

BKBIET, Pilani

---

## 📜 License

This project is developed for educational purposes.