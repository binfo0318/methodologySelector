# selector/views.py
from django.shortcuts import render
from .forms import ProjectForm
import joblib

def predict_methodology(data):
    model = joblib.load('selector/model.pkl')
    prediction = model.predict([data])
    methodologies = ['Waterfall', 'Scrum', 'XP', 'Kanban', 'RAD', 'Spiral', 'V-Model', 'RUP/OpenUP/EssUp']
    return methodologies[prediction[0]]

def index(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            data = [
                int(form.cleaned_data['risk_level']),
                int(form.cleaned_data['requirements_change']),
                int(form.cleaned_data['speed_or_quality']),
                int(form.cleaned_data['improvement_needed']),
                int(form.cleaned_data['duration']),
            ]
            methodology = predict_methodology(data)
            return render(request, 'result.html', {'methodology': methodology})
    else:
        form = ProjectForm()
    return render(request, 'index.html', {'form': form})
