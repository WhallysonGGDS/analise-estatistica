# 📊 **Airbnb Rio — Análise Estatística & Regressão Linear**

Um projeto de análise exploratória e modelagem simples utilizando um dataset de 100k entradas de imóveis do Airbnb na cidade do Rio de Janeiro.  
Aqui você encontra **correlações, estatísticas descritivas e uma regressão linear** para entender se o número de quartos influencia no preço das diárias.

---

## 🚀 **Tecnologias Utilizadas**
- Python 3.x  
- Pandas  
- NumPy  
- Seaborn  
- Matplotlib  
- Scikit-learn  
- Jupyter Notebook / Scripts `.py`

---

## 📁 **Estrutura do Projeto**
```
│── dados/
│   └── airbnb_rio_100k.csv
│
│── relatorios/
│   ├── correlacao_airbnb.png
│   └── regressao_preco_quartos.png
│
│── analise_estatistica.ipynb
│── regressao.py
│── README.md
```

---

## 📈 **1. Estatísticas Básicas do Dataset**

O script calcula:

- **Média do preço por noite**
- **Mediana**
- **Desvio padrão**

Isso já dá um panorama da distribuição geral dos valores do Airbnb no Rio.

---

## 🔥 **2. Matriz de Correlação**

A correlação foi analisada entre:

- `preco_noite`  
- `quartos`  
- `avaliacao`  
- `ocupacao_pct`  

A matriz deixa claro que **nenhuma variável numérica possui correlação forte com o preço**, mostrando que os valores são altamente dispersos.

---

## 📉 **3. Regressão Linear — Preço vs Quartos**

Rodamos um modelo simples:

```
preco_noite ~ quartos
```

Resultado?  
**Praticamente nenhuma relação.**  
O coeficiente é praticamente zero — ou seja, aumentar quartos **não altera significativamente o preço** no dataset analisado.

---

## ▶️ **Como rodar o projeto**

### 1️⃣ Instalar dependências  
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 2️⃣ Rodar a análise completa  
```bash
python regressao.py
```

### 3️⃣ Abrir o notebook  
```bash
jupyter notebook analise_estatistica.ipynb
```

---

## 📝 **Autor**
**Whallyson Gabriel Garcia da Silva**  
Analista de Dados  
GitHub: https://github.com/WhallysonGGDS
