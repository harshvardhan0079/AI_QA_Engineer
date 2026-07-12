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

### Dashboard

![Dashboard](/Users/harshwardhansingh/Desktop/Screenshot 2026-07-12 at 4.57.48 PM.png
/Users/harshwardhansingh/Desktop/Screenshot 2026-07-12 at 4.58.11 PM.png)

### Quality Score

![Quality Score](/Users/harshwardhansingh/Desktop/Screenshot 2026-07-12 at 5.00.29 PM.png)

### AI Review

![AI Review](/Users/harshwardhansingh/Desktop/Screenshot 2026-07-12 at 5.00.46 PM.png)

### Fix Code

![Fix Code](/Users/harshwardhansingh/Desktop/Screenshot 2026-07-12 at 5.00.59 PM.png)

### Explain Code

![Explain Code](/Users/harshwardhansingh/Desktop/Screenshot 2026-07-12 at 5.01.17 PM.png)

### Generate Tests

![Generate Tests](/Users/harshwardhansingh/Desktop/Screenshot 2026-07-12 at 5.01.29 PM.png)

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