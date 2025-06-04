# lingaai/ai_modules.py

from sklearn.tree import DecisionTreeClassifier
import numpy as np

def conseiller_type_sol(humidite, ph, temperature):
    # Ex : données fictives d'entraînement
    X = np.array([[40, 6.5, 25], [30, 5.8, 22], [70, 7.0, 28]])
    y = ["argileux", "sableux", "limoneux"]

    clf = DecisionTreeClassifier()
    clf.fit(X, y)

    prediction = clf.predict([[humidite, ph, temperature]])
    return prediction[0]
