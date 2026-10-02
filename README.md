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
│   ├── deep-learning/     # MLP, CNNs, RNNs (PyTorch / TensorFlow)
│   ├── unsupervisioned/   # Clustering (K-Means, DBSCAN), Redução (PCA, t-SNE)
│   └── foundational/      # Modelos fundacionais tabulares (TabPFN, Mitra)
│       └── cookbooks/     # Versões completas, com protocolo experimental pareado
├── data/                  # Datasets de exemplo ou scripts de download
├── requirements.txt       # Dependências globais do ambiente
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📓 Notebooks

Cada notebook é autossuficiente: instala o que precisa (com versão fixada, para não quebrar em release futura), carrega os dados e roda o próprio baseline. A numeração indica a **ordem de leitura sugerida**, não dependência de execução.

| # | Notebook | Nível | Modelo | O que faz |
|---|----------|-------|--------|-----------|
| 01 | [`01_tabpfn.ipynb`](notebooks/foundational/01_tabpfn.ipynb) | didático | TabPFN (`tabpfn==9.0.0`) | classificação e regressão contra um RandomForest, com foco no custo de `predict` |
| 02 | [`02_mitra.ipynb`](notebooks/foundational/02_mitra.ipynb) | didático | Mitra via AutoGluon (`autogluon.tabular==1.6.3`) | as mesmas duas tarefas, sobre a mesma divisão de treino e teste |
| C1 | [`cookbooks/01_tabpfn_v2_cookbook.ipynb`](notebooks/foundational/cookbooks/01_tabpfn_v2_cookbook.ipynb) | protocolo completo | TabPFN v2 | impressão digital dos splits, warm-up do checkpoint e resultados em CSV |
| C2 | [`cookbooks/02_mitra_autogluon_cookbook.ipynb`](notebooks/foundational/cookbooks/02_mitra_autogluon_cookbook.ipynb) | protocolo completo | Mitra em modo zero-shot | confere o `splits_fingerprint.json` do C1 e compara na mesma partição |

Os dois cookbooks formam um par ordenado: rode o C1 primeiro (ele escreve `splits_fingerprint.json`) e o C2 confere a igualdade das partições antes de comparar. Artefatos gerados na execução (`artifacts_*/`, `splits_fingerprint.json` e os diretórios de modelo do AutoGluon) ficam fora do versionamento.

---

## 🛠️ Ambiente local

```bash
uv venv --python 3.12 --seed .venv
source .venv/bin/activate
uv pip install tabpfn==9.0.0 "autogluon.tabular[mitra]==1.6.3" ipykernel==7.4.0
python -m ipykernel install --user --name ml-cookbooks --display-name "Python (ml-cookbooks)"
```
