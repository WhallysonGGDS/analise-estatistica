import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import os

# Garante pasta de relatórios
os.makedirs("relatorios", exist_ok=True)

# Carregar dataset
df = pd.read_csv("dados/airbnb_rio_100k.csv")

# Estatísticas básicas do preço
media = df['preco_noite'].mean()
mediana = df['preco_noite'].median()
desvio = df['preco_noite'].std()

print("Média do preço por noite:", media)
print("Mediana do preço por noite:", mediana)
print("Desvio padrão do preço por noite:", desvio)

# Matriz de correlação
colunas_numericas = ['preco_noite', 'quartos', 'avaliacao', 'ocupacao_pct']
corr = df[colunas_numericas].corr()

plt.figure()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Matriz de Correlação — Airbnb Rio")
plt.savefig("relatorios/correlacao_airbnb.png")
plt.close()   # <-- fecha a figura sem abrir janela

# Regressão Linear: preço ~ quartos
X = df[['quartos']]
y = df['preco_noite']

modelo = LinearRegression()
modelo.fit(X, y)

y_pred = modelo.predict(X)

print(f"Coeficiente (inclinação): {modelo.coef_[0]:.2f}")
print(f"Intercepto: {modelo.intercept_:.2f}")

plt.figure()
plt.scatter(df['quartos'], y, alpha=0.3, label="Observado")
plt.plot(df['quartos'], y_pred, label="Regressão Linear", linewidth=2)
plt.xlabel("Quartos")
plt.ylabel("Preço por noite (R$)")
plt.title("Regressão Linear — Preço vs Quartos")
plt.legend()
plt.savefig("relatorios/regressao_preco_quartos.png")
plt.close()   # idem, fecha e não trava
