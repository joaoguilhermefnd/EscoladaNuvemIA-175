from sklearn.datasets import load_breast_cancer # Conjunto de dados de CA de mama
from sklearn.ensemble import RandomForestClassifier # Algoritmo Random Forest

# Métricas para avaliação do modelo
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

# Funçao para divisão do conjunto de dados
from sklearn.model_selection import train_test_split


# Carregando o dataset de CA de mama
data = load_breast_cancer()


# O conjunto de dados contém características (data.data) e rótulos (data.target).
# data.data: matriz de 30 características
# data.target: vetor 0 (maligno) e vetor 1 (benigno)

# Conjunto de dados de 569 amostras
# Divisão dos dados para treino 70% e para avaliação (teste) 30% (0.3).
# X_train e X_test: características para treino e para teste
# y_train e y_test: rótulos para treino e para teste

# random_state=42: garantir reprodutibilidade


X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=42)

# Inicializar o conjunto Random Forest com os parâmetros
modelo = RandomForestClassifier(random_state=42)

# Treinar o modelo com os dados de treino
modelo.fit(X_train, y_train)

# Fazer as previsões com os dados de teste
y_pred = modelo.predict(X_test) # Previsões de classe (0 ou 1) (maligno ou benigno)
y_pred_proba = modelo.predict_proba(X_test)[:,1] # Probabilidade de classe positiva (1) (benigno)


# Calcular as métricas para avaliação:
precisao = precision_score(y_test, y_pred) # Precisão = TP / (TP + FP)
recall = recall_score(y_test, y_pred) # Recall = TP / (TP + FN)
f1 = f1_score(y_test, y_pred) # F1-score =  2 * [(Precisão * Recall) / (Precisão + Recall)]
auc = roc_auc_score(y_test,y_pred_proba) # Área sob a curva ROC


print(f"Precisão: {precisao:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
print(f"AUC-ROC: {auc:.4f}")