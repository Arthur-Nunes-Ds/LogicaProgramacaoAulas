# CLASSIFICAÇÃO DE FRUTAS COM KNN E RANDOM FOREST


# 1. Importação de bibliotecas
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use("TkAgg")   # ou "QtAgg" se tiver PyQt5/PySide6
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# 2. Geração de dataset fictício com list comprehension

''' np.random.seed(42)
Define a semente aleatória para garantir que os mesmos números sejam gerados toda vez.
Isso é útil para reprodutibilidade: todos os alunos terão os mesmos dados.
'''
np.random.seed(42)

def gerar_frutas(nome, peso_range, textura_range, cor_range, docura_range, quantidade):
    return [
        {
            "peso": np.random.uniform(*peso_range),
            "textura": np.random.uniform(*textura_range),
            "cor": np.random.uniform(*cor_range),
            "docura": np.random.uniform(*docura_range),
            "fruta": nome
        }
        for _ in range(quantidade)
    ]

# Gerando dados para 3 tipos de frutas
banana = gerar_frutas("Banana", peso_range=(100, 130), textura_range=(0.6, 0.9), cor_range=(0.7, 1.0), docura_range=(5.5, 7.0), quantidade=20)
maca   = gerar_frutas("Maçã", peso_range=(110, 140), textura_range=(0.4, 0.7), cor_range=(0.3, 0.6), docura_range=(5.0, 6.5), quantidade=20)
melancia = gerar_frutas("Melancia", peso_range=(2200, 2800), textura_range=(0.1, 0.4), cor_range=(0.8, 1.0), docura_range=(5.5, 6.8), quantidade=20)
hibrida = gerar_frutas("Híbrida", peso_range=(1000, 1500), textura_range=(0.3, 0.6), cor_range=(0.4, 0.7), docura_range=(5.2, 6.8), quantidade=20)

dados = banana + maca + melancia + hibrida
df = pd.DataFrame(dados)

print(df.head())

sns.pairplot(df, hue="fruta")
plt.suptitle("Dispersão entre variáveis", y=1.02)
plt.show()