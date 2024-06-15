# selector/forms.py
from django import forms

class ProjectForm(forms.Form):
    risk_level = forms.ChoiceField(choices=[(0, 'Низкий'), (1, 'Высокий')], label='Уровень риска')
    requirements_change = forms.ChoiceField(choices=[(0, 'Нет'), (1, 'Да')], label='Изменение требований')
    speed_or_quality = forms.ChoiceField(choices=[(0, 'Скорость'), (1, 'Качество')], label='Скорость или качество')
    improvement_needed = forms.ChoiceField(choices=[(0, 'Нет'), (1, 'Да')], label='Необходимы улучшения')
    duration = forms.IntegerField(label='Длительность проекта (в днях)')

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
                int(form.cleaned_data['duration_important']),
            ]
            methodology = predict_methodology(data)
            return render(request, 'result.html', {'methodology': methodology})
    else:
        form = ProjectForm()
    return render(request, 'index.html', {'form': form})
