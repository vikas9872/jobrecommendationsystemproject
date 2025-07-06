from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
import pandas as pd
from scipy.sparse import hstack, csr_matrix
from django.apps import apps
from django.core.files.storage import FileSystemStorage
import os
import pdfplumber
import docx
from .utils import extract_skills_from_resume
import requests

def home_view(request):
    return render(request, 'home/homepage.html')

def about_view(request):
    return render(request, 'home/aboutpage.html')

def services_view(request):
    return render(request, 'home/ourservicespage.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'home/registerpage.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('options_page')
    else:
        form = AuthenticationForm()
    return render(request, 'home/loginpage.html', {'form': form})

def options_view(request):
    return render(request,'home/optionspage.html')

def enter_details(request):
    return render(request, 'home/enterdetailspage.html')

def predict_category(skills, experience, interest, education, work_type, communication):
    input_data = pd.DataFrame([{
        'skills': skills,
        'experience': float(experience),
        'interest': interest,
        'education': education,
        'work_type': work_type,
        'communication': float(communication)
    }])

def predict_view(request):
    if request.method == 'POST':
        skills = request.POST.get('skills', '')
        experience = float(request.POST.get('experience', 0))
        communication = float(request.POST.get('communication', 0))
        interest = request.POST.get('interest', '')
        education = request.POST.get('education', '')
        work_type = request.POST.get('work_type', '')
        app_config = apps.get_app_config('jobrecommendationsystemapp')
        tfidf_vectorizer = getattr(app_config, 'tfidf_vectorizer', None)
        scaler = getattr(app_config, 'scaler', None)
        onehot_encoder = getattr(app_config, 'onehot_encoder', None)
        classifier = getattr(app_config, 'rf_classifier', None)
        predicted_role = None
        job_link = None
        remotive_jobs = []
        try:
            if all([tfidf_vectorizer, scaler, onehot_encoder, classifier]):
                input_df = pd.DataFrame([{
                    'skills': skills,
                    'experience': experience,
                    'communication': communication,
                    'interest': interest,
                    'education': education,
                    'work_type': work_type
                }])
                input_text = tfidf_vectorizer.transform(input_df['skills'])
                input_numerical = csr_matrix(scaler.transform(input_df[['experience', 'communication']]))
                input_categorical = onehot_encoder.transform(input_df[['interest', 'education', 'work_type']])
                input_combined = hstack([input_text, input_numerical, input_categorical])
                predicted_role = classifier.predict(input_combined)[0]
                role_query = str(predicted_role).strip().replace(" ", "+")
                # API CALLED
                remotive_url = f"https://remotive.com/api/remote-jobs?search={role_query}"
                response = requests.get(remotive_url)
                if response.status_code == 200:
                    jobs_data = response.json()
                    for idx, job in enumerate(jobs_data.get("jobs", [])):
                        job_data = {
                            "title": job.get("title"),
                            "company": job.get("company_name"),
                            "location": job.get("candidate_required_location"),
                            "url": job.get("url"),
                            "salary": job.get("salary"),
                            "job_type": job.get("job_type"),
                            "category": job.get("category"),
                            "publication_date": job.get("publication_date"),
                        }
                        remotive_jobs.append(job_data)
                        if idx == 0 and not job_link:
                            job_link = job_data["url"]
                else:
                    print("Failed to fetch jobs from Remotive")

            else:
                print("Model components not available.")

        except Exception as e:
            print("Prediction error:", e)

        return render(request, 'home/result.html', {
            'predicted_role': predicted_role,
            'job_link': job_link
        })
    return render(request, 'home/enterdetailspage.html')

def upload_resume(request):
    error_message = ""
    predicted_role = None
    job_link = None
    remotive_jobs = []
    if request.method == 'POST' and request.FILES.get('resume'):
        resume_file = request.FILES['resume']
        fs = FileSystemStorage()
        filename = fs.save(resume_file.name, resume_file)
        file_path = fs.path(filename)
        resume_text = ""
        try:
            if filename.lower().endswith('.pdf'):
                with pdfplumber.open(file_path) as pdf:
                    for page in pdf.pages:
                        resume_text += page.extract_text() or ""
            elif filename.lower().endswith('.docx'):
                doc = docx.Document(file_path)
                for para in doc.paragraphs:
                    resume_text += para.text + "\n"
            else:
                error_message = "Unsupported file type. Please upload a PDF or DOCX file."
            if resume_text:
                extracted_skills = extract_skills_from_resume(resume_text)
                print("Extracted skills:", extracted_skills)
                if extracted_skills:
                    app_config = apps.get_app_config('jobrecommendationsystemapp')
                    tfidf_vectorizer = getattr(app_config, 'tfidf_vectorizer_resume', None)
                    rf_classifier = getattr(app_config, 'rf_classifier_resume', None)

                    if tfidf_vectorizer and rf_classifier:
                        try:
                            input_tfidf = tfidf_vectorizer.transform([extracted_skills])
                            prediction = rf_classifier.predict(input_tfidf)
                            predicted_role = prediction[0]
                            role_query = str(predicted_role).strip().replace(" ", "+")
                            #API CALLED
                            url = f"https://remotive.com/api/remote-jobs?search={role_query}"
                            response = requests.get(url)
                            if response.status_code == 200:
                                jobs = response.json().get("jobs", [])
                                for idx, job in enumerate(jobs):
                                    job_info = {
                                        "title": job.get("title"),
                                        "company": job.get("company_name"),
                                        "location": job.get("candidate_required_location"),
                                        "url": job.get("url"),
                                        "salary": job.get("salary"),
                                        "job_type": job.get("job_type"),
                                        "category": job.get("category"),
                                        "publication_date": job.get("publication_date"),
                                    }
                                    remotive_jobs.append(job_info)
                                    if idx == 0 and not job_link:
                                        job_link = job_info["url"]
                            else:
                                error_message = "Could not fetch jobs from Remotive."
                        except Exception as e:
                            error_message = f"Error predicting job role: {e}"
                    else:
                        error_message = "Prediction model is not available."
                else:
                    error_message = "No skills extracted from resume."
            else:
                error_message = "Could not extract text from the uploaded resume."
        except Exception as e:
            error_message = f"Error processing resume: {e}"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
    if predicted_role or error_message:
        return render(request, 'home/result.html', {
            'predicted_role': predicted_role,
            'job_link': job_link,
            'remotive_jobs': remotive_jobs,
            'error_message': error_message
        })
    return render(request, 'home/uploadresumepage.html', {
        'error_message': error_message
    })

def result_view(request):
    return render(request,'home/result.html')

def logout_view(request):
    auth_logout(request)
    return redirect('home')