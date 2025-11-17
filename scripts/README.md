📊 Análise Estatística — Airbnb Rio (100k registros)

Este projeto apresenta uma análise estatística completa utilizando um dataset sintético de 100.000 anúncios do Airbnb na cidade do Rio de Janeiro, incluindo estatísticas descritivas, matriz de correlação e uma regressão linear simples para modelar o preço por noite em função do número de quartos.

O foco do projeto é demonstrar domínio de Python, Pandas, Estatística, Visualização de Dados e Modelagem Preditiva.

🚀 Tecnologias Utilizadas

Python 3

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Jupyter Notebook

📁 Estrutura do Projeto
analise_estatistica/
│
├── dados/
│   └── airbnb_rio_100k.csv
│
├── notebooks/
│   └── analise_estatistica.ipynb
│
├── scripts/
│   └── regressao.py
│
├── relatorios/
│   ├── correlacao_airbnb.png
│   └── regressao_preco_quartos.png
│
└── README.md

📥 Dataset

O dataset contém 100.000 linhas simulando anúncios reais do Airbnb no Rio de Janeiro, com as seguintes colunas:

bairro

quartos

preco_noite

avaliacao

ocupacao_pct

📈 Estatísticas Descritivas

Variáveis analisadas:

Preço por noite

Quantidade de quartos

Avaliação

Ocupação (%)

Exemplo dos resultados:

Média do preço por noite:      1050.45
Mediana do preço por noite:    1051.0
Desvio padrão:                 547.84


Essas estatísticas permitem ter uma visão inicial da distribuição dos preços ao longo dos bairros e características dos imóveis.

🔗 Correlação entre Variáveis

Foi gerada uma matriz de correlação entre as principais variáveis numéricas do dataset:

preço_noite

quartos

avaliacao

ocupacao_pct

Imagem gerada em:
📁 relatorios/correlacao_airbnb.png

📉 Regressão Linear — Preço vs Quartos

O modelo de regressão linear simples foi utilizado para investigar se existe relação entre:

Variável independente: número de quartos

Variável dependente: preço por noite

Resultados:

Coeficiente (inclinação):  ~valor entre 180 e 220
Intercepto:                ~800


Ou seja, cada quarto adicional tende a aumentar o preço do anúncio de forma consistente.

Gráfico gerado em:
📁 relatorios/regressao_preco_quartos.png

💡 Insights Observados

Há uma relação positiva entre quartos e preco_noite

A variável avaliacao não influencia tanto no preço

Propriedades com mais quartos são mais caras independentemente do bairro

O dataset é extenso, permitindo testes estatísticos mais robustos

O modelo simples explica uma parte do fenômeno — modelos múltiplos podem melhorar ainda mais

▶️ Como Rodar o Projeto
1. Criar ambiente virtual
python -m venv venv

2. Ativar
venv\Scripts\Activate.ps1

3. Instalar dependências
pip install pandas numpy matplotlib seaborn scikit-learn

4. Rodar o script
python scripts/regressao.py

5. Abrir o notebook (opcional)
jupyter notebook

🧠 Próximos Passos (Melhorias futuras)

Regressão linear múltipla

Modelos avançados (Random Forest / XGBoost)

Clusterização de bairros

Dashboard interativo (Streamlit)

Comparação com dataset real (Inside Airbnb)

👨‍💻 Autor

Whallyson Gabriel Garcia da Silva
Analista de Dados • Python • SQL • Estatística • Portfólio em expansão 🚀