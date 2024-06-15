# selector/train_model.py
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

def train_model():
    # Пример данных для обучения
    # Параметры: [уровень риска, изменяемость требований, приоритет скорости или качества, необходимость улучшений, длительность проекта]
    X = [
        [1, 1, 0, 1, 30],  # Scrum
        [0, 0, 1, 0, 90],  # Waterfall
        [1, 1, 1, 1, 60],  # XP
        [0, 1, 1, 1, 120], # Kanban
        [1, 0, 0, 0, 45],  # RAD
        [1, 1, 0, 1, 150], # Spiral
        [1, 0, 0, 0, 180], # V-Model
        [0, 1, 1, 0, 90],  # RUP/OpenUP/EssUp
        [0, 1, 0, 1, 30],  # Scrum
        [0, 0, 0, 0, 120], # Waterfall
        [1, 0, 1, 0, 30],  # XP
        [0, 0, 1, 1, 150], # Kanban
        [1, 0, 1, 0, 60],  # RAD
        [1, 1, 0, 0, 90],  # Spiral
        [1, 0, 0, 1, 120], # V-Model
        [0, 0, 1, 1, 45],  # RUP/OpenUP/EssUp

    ]
    y = [1, 0, 2, 3, 4, 5, 6, 7, 1, 0, 2, 3, 4, 5, 6, 7]  # Метки классов, соответствующие методологиям

    # Создание конвейера для масштабирования данных и обучения модели
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=10000))
    model.fit(X, y)
    joblib.dump(model, 'selector/model.pkl')

if __name__ == "__main__":
    train_model()
