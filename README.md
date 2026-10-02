# ml-cookbooks

Coleção prática, modular e direta ao ponto de notebooks (`.ipynb`) com implementações iniciais e boas práticas para diferentes modelos e paradigmas de Machine Learning.

O foco deste repositório é servir como base reproduzível: cada notebook é autossuficiente, cobrindo da carga de dados à avaliação de baseline.

---

## 📂 Estrutura do Repositório

```text
ml-cookbooks/
├── notebooks/
│   ├── classical/         # Regressão, Classificação, Árvores, SVM
│   ├── ensemble/          # Random Forest, XGBoost, LightGBM, CatBoost
│   ├── deep-learning/     # MLP, CNNs, RNNs (PyTorch)
│   ├── unsupervisioned/   # Clustering (K-Means, DBSCAN), Redução (PCA, t-SNE)
│   ├── metaheuristics/    # Busca e otimização: algoritmos genéticos
│   ├── foundational/      # Modelos fundacionais tabulares (TabPFN, Mitra)
│   ├── time-series/       # Previsão: protocolo temporal, ETS/SARIMAX, lags (em preparação)
│   └── pipeline/          # O fluxo: análise, encoding, features, validação, seleção, desbalanceamento
├── data/                  # Datasets de exemplo ou scripts de download
├── requirements.txt       # Dependências globais do ambiente
├── GLOSSARIO.md           # Os termos em inglês, um por linha
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📓 Notebooks

Cada notebook é autossuficiente: instala o que falta além do que o ambiente já traz (com versão fixada, para não quebrar em release futura), carrega os dados e roda o próprio baseline. Os gráficos usam `seaborn` com a paleta `colorblind`, e o tema está fixado no primeiro bloco de código de cada notebook.

As pastas seguem três eixos. As de **paradigma** (`classical`, `ensemble`, `deep-learning`, `foundational`, `metaheuristics`) ensinam um modelo por vez, com o preparo mínimo embutido, para o notebook se sustentar sozinho. A pasta `pipeline/` é o fluxo da tabela, numerado na ordem em que se faz. A pasta `time-series/` é uma tarefa com protocolo próprio, na qual a ordem importa e o teste é o futuro; `unsupervisioned/` é a outra tarefa, a que não tem rótulo.

**Por onde começar:** o `pipeline/` está numerado na ordem do fluxo, de `01` análise a `06` desbalanceamento; `time-series/01` abre a parte de previsão.

**Onde entra um notebook novo:** ensina um modelo, pasta do paradigma; uma etapa do preparo ou da medição de tabela, `pipeline/`; uma tarefa com protocolo próprio, `time-series/` ou `unsupervisioned/`; uma técnica de busca, `metaheuristics/`. Dois desempates: se no momento da previsão todas as colunas já estão disponíveis, é regressão e fica em `pipeline/`; e o LSTM decide pela tarefa, classificar sequência em `deep-learning/`, prever o próximo valor em `time-series/`.

---

## 🛠️ Ambiente local

```bash
uv venv --python 3.12 --seed .venv
source .venv/bin/activate
uv pip install -r requirements.txt
python -m ipykernel install --user --name ml-cookbooks --display-name "Python (ml-cookbooks)"
```

---

## 📖 Glossário

Os termos em inglês que aparecem nos notebooks, cada um traduzido em uma frase, com um "não confunda" no fim: [`GLOSSARIO.md`](GLOSSARIO.md).
