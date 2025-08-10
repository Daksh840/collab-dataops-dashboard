# 🚀 Collaborative Data-Ops Dashboard

A visually stunning, real-time dashboard for managing, tracking, and interacting with Data Pipelines using a full-stack architecture (React + FastAPI + PostgreSQL).

> ✨ Designed for DevOps, Data Engineers, ML engineers, and anyone working with ETL or CI/CD pipelines.

---

## 📸 Preview

![App Screenshot](./screenshot.png) <!-- Replace with your actual screenshot path -->

---

## 🧩 Features

- 🔄 **Real-time Pipeline Updates** (Auto-refresh every 10s)
- ➕ **Add New Pipelines**
- 📝 **Edit Existing Pipelines** via modal
- ❌ **Delete Pipelines** with confirmation
- 🔍 **Search and Filter Pipelines** by name/status
- 💡 **Status-Based Animations**
  - ✅ Green pulse for Running
  - ⏸️ Yellow pulse for Paused
  - ❌ Red pulse for Error
- ✨ **Advanced UI Effects**
  - Particle glows
  - Mouse spotlight tracking
  - Ripple click effects
  - Border glow animations

---

## 🛠️ Tech Stack

### Frontend
- **React.js** (with Hooks)
- **Tailwind CSS**
- **GSAP** (GreenSock Animation Platform)
- Custom components: `MagicBento`, `ParticleCard`, `Hyperspeed`

### Backend
- **FastAPI** (Python)
- **PostgreSQL** (relational database)
- **SQLAlchemy** for ORM

---

## 🗂️ Project Structure

```bash
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── AddPipelineForm.jsx
│   │   │   ├── EditPipelineModal.jsx
│   │   │   ├── MagicBento.jsx
│   │   │   └── Hyperspeed.jsx
│   │   ├── api/
│   │   │   └── index.js
│   │   └── App.js
│   └── public/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── crud.py
````

---

## ⚙️ Getting Started

### 🔧 Prerequisites

* Node.js v18+
* Python 3.10+
* PostgreSQL

---

### 🖥️ Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

### 🐍 Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
uvicorn main:app --reload
```

> Ensure PostgreSQL is running and credentials are correctly set in `database.py`.

---

## 📦 API Endpoints

| Method | Endpoint        | Description         |
| ------ | --------------- | ------------------- |
| GET    | /pipelines      | Fetch all pipelines |
| POST   | /pipelines      | Add a new pipeline  |
| PUT    | /pipelines/{id} | Update a pipeline   |
| DELETE | /pipelines/{id} | Delete a pipeline   |

---

## 🌈 UI/UX Highlights

* Responsive card grid layout
* Glow effects based on pipeline status
* Real-time spotlight & tilt effects
* Smooth animations using GSAP

---

## 💡 Future Enhancements

* 🧩 Pipeline logs/metrics integration
* 📈 Dashboard analytics (pipeline run stats)
* 🔐 Auth + Role-based access
* 📁 Export pipeline configs (YAML/JSON)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

```bash
# Format with Prettier
npm run format
```

---

## 📄 License

[MIT](./LICENSE)

---

## 🙌 Acknowledgments

* [GSAP](https://greensock.com/gsap/)
* [Tailwind CSS](https://tailwindcss.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
* Inspired by magic UI concepts from [reactbits.dev](https://reactbits.dev)

---

> Built with ❤️ by [Daksh Kumar Nahar](https://github.com/daksh840)

```

---

### ✅ Next Steps:

- 📸 Add a screenshot to `frontend/public/screenshot.png`
- 📝 Replace `"Your Name"` and GitHub links
- 🧪 Add `requirements.txt` (if not done) for backend dependencies
- 🧑‍💻 Push to GitHub and ensure all paths (like `/LICENSE`, `/screenshot.png`) resolve correctly  
```

