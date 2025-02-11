import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def generate_confusion_matrix():
    y_true = np.random.randint(0, 2, 100)  
    y_pred = np.random.randint(0, 2, 100)  
    return confusion_matrix(y_true, y_pred)

def calculate_metrics(cm):
    VP = cm[1, 1]  
    VN = cm[0, 0]  
    FP = cm[0, 1]  
    FN = cm[1, 0]  
    
    N = VP + VN + FP + FN
    
    sensibilidade = VP / (VP + FN) if (VP + FN) > 0 else 0
    especificidade = VN / (FP + VN) if (FP + VN) > 0 else 0
    acurácia = (VP + VN) / N if N > 0 else 0
    precisao = VP / (VP + FP) if (VP + FP) > 0 else 0
    f_score = 2 * (precisao * sensibilidade) / (precisao + sensibilidade) if (precisao + sensibilidade) > 0 else 0
    
    return {
        "Sensibilidade (Recall)": sensibilidade,
        "Especificidade": especificidade,
        "Acurácia": acurácia,
        "Precisão": precisao,
        "F-score": f_score
    }

def plot_confusion_matrix(cm):
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Negativo', 'Positivo'], yticklabels=['Negativo', 'Positivo'])
    plt.xlabel('Previsto')
    plt.ylabel('Real')
    plt.title('Matriz de Confusão')
    plt.show()

def plot_metrics(metrics):
    plt.figure(figsize=(7, 5))
    plt.barh(list(metrics.keys()), list(metrics.values()), color='royalblue')
    plt.xlabel('Valor')
    plt.title('Métricas de Avaliação')
    plt.xlim(0, 1)
    for index, value in enumerate(metrics.values()):
        plt.text(value + 0.02, index, f'{value:.2f}')
    plt.show()

    
cm = generate_confusion_matrix()
metrics = calculate_metrics(cm)
    
plot_confusion_matrix(cm)
plot_metrics(metrics)
