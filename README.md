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
│   ├── metaheuristics/    # Busca e otimização: algoritmos genéticos
│   └── foundational/      # Modelos fundacionais tabulares (TabPFN, Mitra)
│       └── cookbooks/     # Versões completas, com protocolo experimental pareado
├── data/                  # Datasets de exemplo ou scripts de download
├── requirements.txt       # Dependências globais do ambiente
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🛠️ Ambiente local

```bash
uv venv --python 3.12 --seed .venv
source .venv/bin/activate
uv pip install -r requirements.txt
python -m ipykernel install --user --name ml-cookbooks --display-name "Python (ml-cookbooks)"
```

---

## 📓 Notebooks

Cada notebook é autossuficiente: instala o que precisa (com versão fixada, para não quebrar em release futura), carrega os dados e roda o próprio baseline. A ordem da tabela é a leitura sugerida, e os rótulos da coluna `#` são locais de cada pasta.

| # | Notebook | Nível | Modelo | O que faz |
|---|----------|-------|--------|-----------|
| 01 | [`01_tabpfn.ipynb`](notebooks/foundational/01_tabpfn.ipynb) | didático | TabPFN (`tabpfn==9.0.0`) | classificação e regressão contra um RandomForest, com foco no custo de `predict` |
| 02 | [`02_mitra.ipynb`](notebooks/foundational/02_mitra.ipynb) | didático | Mitra via AutoGluon (`autogluon.tabular==1.6.3`) | as mesmas duas tarefas, sobre a mesma divisão de treino e teste |
| C1 | [`cookbooks/01_tabpfn_v2_cookbook.ipynb`](notebooks/foundational/cookbooks/01_tabpfn_v2_cookbook.ipynb) | protocolo completo | TabPFN v2 | impressão digital dos splits, warm-up do checkpoint e resultados em CSV |
| C2 | [`cookbooks/02_mitra_autogluon_cookbook.ipynb`](notebooks/foundational/cookbooks/02_mitra_autogluon_cookbook.ipynb) | protocolo completo | Mitra em modo zero-shot | confere o `splits_fingerprint.json` do C1 e compara na mesma partição |
| M1 | [`metaheuristics/01_genetic_algorithm.ipynb`](notebooks/metaheuristics/01_genetic_algorithm.ipynb) | didático | Algoritmo genético, do zero | função multimodal com vários picos e seleção de atributos no breast cancer |
| CL1 | [`classical/01_classification.ipynb`](notebooks/classical/01_classification.ipynb) | didático | Quatro clássicos de classificação | efeito da escala, validação cruzada e a fronteira de decisão de cada modelo |
| CL2 | [`classical/02_regression.ipynb`](notebooks/classical/02_regression.ipynb) | didático | Regressão linear, Ridge e Lasso | grau do polinômio, underfitting e o que a regularização faz com os coeficientes |
| DL1 | [`deep-learning/01_mlp.ipynb`](notebooks/deep-learning/01_mlp.ipynb) | didático | MLP em PyTorch | fronteira não linear nas meias-luas e a comparação com o modelo linear no dado tabular |
| DL2 | [`deep-learning/02_cnn.ipynb`](notebooks/deep-learning/02_cnn.ipynb) | didático | CNN em PyTorch | kernel compartilhado e pool global contra o padrão que muda de lugar |
| DL3 | [`deep-learning/03_rnn.ipynb`](notebooks/deep-learning/03_rnn.ipynb) | didático | RNN em PyTorch | ordem, comprimento variável, e uma tarefa de memória contra uma de combinação |
| E1 | [`ensemble/01_bagging_and_boosting.ipynb`](notebooks/ensemble/01_bagging_and_boosting.ipynb) | didático | Random Forest, XGBoost, LightGBM e CatBoost | bagging contra boosting na mesma divisão e o efeito do número de árvores |
| E2 | [`ensemble/02_hyperparameters.ipynb`](notebooks/ensemble/02_hyperparameters.ipynb) | didático | XGBoost | taxa de aprendizado contra orçamento, profundidade e parada antecipada |
| U1 | [`unsupervisioned/01_clustering.ipynb`](notebooks/unsupervisioned/01_clustering.ipynb) | didático | K-Means e DBSCAN | o `k` pelo silhouette e o caso em que o formato do grupo decide o vencedor |
| U2 | [`unsupervisioned/02_dimensionality_reduction.ipynb`](notebooks/unsupervisioned/02_dimensionality_reduction.ipynb) | didático | PCA e t-SNE | variância acumulada, vizinhança local e redução como pré-processamento |

Os dois cookbooks formam um par ordenado: rode o C1 primeiro (ele escreve `splits_fingerprint.json`) e o C2 confere a igualdade das partições antes de comparar. Artefatos gerados na execução (`artifacts_*/`, `splits_fingerprint.json` e os diretórios de modelo do AutoGluon) ficam fora do versionamento.
