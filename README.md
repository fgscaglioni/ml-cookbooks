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
│   └── time-series/       # O teste é o futuro: protocolo temporal, ETS/SARIMAX, lags, fundacional
├── data/                  # Datasets de exemplo ou scripts de download
├── requirements.txt       # Dependências globais do ambiente
├── GLOSSARIO.md           # Os termos em inglês, um por linha
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📓 Notebooks

Cada notebook é autossuficiente: instala o que precisa (com versão fixada, para não quebrar em release futura), carrega os dados e roda o próprio baseline.

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
