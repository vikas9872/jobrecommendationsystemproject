# 🧠 AI-Powered Job Recommendation System

Live Demo 👉 [https://jobrecommendationsystemproject.onrender.com](https://jobrecommendationsystemproject.onrender.com)  
GitHub Repo 👉 [https://github.com/vikas9872/jobrecommendationsystemproject](https://github.com/vikas9872/jobrecommendationsystemproject)

---

## 📌 Overview

**Job Recommendation System** is an AI-powered web application that helps users discover the most suitable job roles based on their:

- Skills  
- Experience  
- Communication level  
- Interests  
- Education background  
- Preferred work type  

Built with Django and integrated with a machine learning model (Random Forest), the system uses TF-IDF and other preprocessing techniques to intelligently predict job roles. It offers a clean, responsive user interface and is deployed on Render.

---

## 🖼️ Screenshots

### 🔷 Home Page  
![Home Page](screenshots/home.jpg)

### 🔶 Input Form  
![Form](screenshots/form.jpg)

### ✅ Prediction Result  
![Prediction Result](screenshots/result.jpg)

---

## 🚀 Features

- 🔍 Predicts job roles based on multiple user inputs  
- 🧠 Uses trained ML models with TF-IDF, StandardScaler, and OneHotEncoder  
- ⚡ Fast prediction results integrated with Django backend  
- 🎨 Responsive UI with Tailwind CSS  
- ☁️ Deployed live on Render  

---

## 🏗️ Tech Stack

- **Backend**: Django (Python)  
- **Frontend**: HTML, Tailwind CSS  
- **Machine Learning**: Scikit-learn, pandas, TF-IDF, Random Forest  
- **Deployment**: Render.com  

---

## 🛠️ Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/vikas9872/jobrecommendationsystemproject.git
cd jobrecommendationsystemproject

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Django development server
python manage.py runserver

# 5. Open your browser and visit:
http://127.0.0.1:8000/
