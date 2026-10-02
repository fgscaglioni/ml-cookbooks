# Glossário

Os termos em inglês que aparecem nos notebooks, cada um traduzido em uma frase. No fim de cada seção, onde aquilo aparece no repositório.

## Treino e otimização

| Termo | Em uma frase |
|-------|--------------|
| função de perda (loss) | A nota de erro que o treino tenta baixar; ela define o que "aprender" significa naquele problema. |
| descida de gradiente | Ajustar os parâmetros na direção que mais reduz a perda, em passos pequenos e repetidos. |
| taxa de aprendizado (learning rate) | O tamanho de cada passo dessa descida: baixa demora e converge melhor, alta chega rápido e pode passar do ponto. |
| momento (momentum) | Guardar parte da direção do passo anterior, para atravessar vales estreitos sem zigue-zaguear. |
| Adam | Otimizador que junta momento com passo adaptativo por parâmetro; é o padrão em rede neural e o usado aqui. |
| época (epoch) | Uma passada completa do modelo sobre todo o conjunto de treino. |
| lote (batch) | Quantos exemplos entram em cada passo do treino; o lote completo usa todos de uma vez. |
| backpropagation | A regra da cadeia aplicada camada por camada, que calcula quanto cada peso contribuiu para o erro. |
| convergir | Quando a perda para de cair; daí em diante treinar mais só gasta tempo, ou começa a decorar. |
| gradiente que desvanece (vanishing gradient) | O gradiente que chega às primeiras camadas vira produto de fatores pequenos e some; é o que limita a RNN simples. |
| corte de gradiente (clipping) | Limitar o tamanho do gradiente para ele não explodir num passo só. |

Onde: `deep-learning/01_mlp`, `deep-learning/03_rnn`, `ensemble/02_hyperparameters`.

## Ajuste e avaliação

| Termo | Em uma frase |
|-------|--------------|
| parâmetro | O que o treino ajusta sozinho: os pesos, os coeficientes. |
| hiperparâmetro | O que você escolhe antes do treino (profundidade da árvore, taxa de aprendizado, o `k` do K-Means); o modelo não descobre sozinho. |
| ajuste de hiperparâmetros (tuning) | Procurar a combinação de hiperparâmetros que rende mais numa métrica de validação. |
| semente (seed) | O número que fixa os sorteios; com a mesma semente o mesmo código dá o mesmo resultado, quando o método é determinístico. |
| validação cruzada (k-fold) | Dividir o treino em k partes e treinar k vezes, cada vez com uma parte de fora; devolve média e desvio, que uma divisão só não dá. |
| validação | O pedaço usado para decidir (escolher hiperparâmetro, parar o treino). Não é o teste. |
| teste | O pedaço que só se olha no fim, para medir de verdade; decidir olhando o teste é a forma mais fácil de publicar número otimista. |
| baseline | O resultado simples que qualquer proposta precisa superar para valer a pena. |
| overfitting (decorar) | Acertar no treino e errar no que não viu, porque o modelo aprendeu o ruído. |
| underfitting | Modelo simples demais: erra no treino e no teste. |
| viés e variância | Os dois lados do trade-off; pouco viés com muita variância decora, o contrário não representa. |
| regularização | Somar à perda uma penalidade pelo tamanho dos coeficientes, para o modelo só usar o que se paga. |
| padronização (standardization) | Deixar cada coluna com média 0 e desvio 1; obrigatório quando o modelo mede distância (kNN, SVM, rede) e irrelevante para árvore. |

Onde: todos os notebooks; a discussão de validação cruzada está em `classical/01_classification`.

## Métricas

| Termo | Em uma frase |
|-------|--------------|
| acurácia | A fração de acertos; engana quando uma classe é muito mais comum que a outra. |
| ROC-AUC | Mede se o modelo ordena bem por probabilidade, sem depender do limiar de decisão. |
| F1-macro | Mistura precisão e revocação sem favorecer a classe mais comum. |
| RMSE e MAE | Erros de regressão na unidade do alvo; o RMSE pune erro grande mais que o MAE. |
| R² | Fração da variação do alvo que o modelo explica; 0 equivale a chutar a média. |
| matriz de confusão | Tabela de acertos e erros por classe, que mostra onde o modelo confunde. |
| silhouette | Nota de -1 a 1 de uma partição, comparando a distância dentro do grupo com a distância ao grupo vizinho. |
| inércia | Soma das distâncias ao centro do grupo no K-Means; sempre melhora quando se aumenta o número de grupos, então não decide o `k` sozinha. |
| ARI | Compara dois agrupamentos (o seu e a verdade escondida), de 0 (acaso) a 1 (idênticos). |

Onde: `classical/01_classification`, `classical/02_regression` e `unsupervisioned/01_clustering`.

## Famílias de modelos

| Termo | Em uma frase |
|-------|--------------|
| modelo pré-treinado (foundation model) | Já foi treinado em milhões de tabelas por outra pessoa e, aqui, não aprende com o seu dado: lê o seu treino como contexto. |
| in-context learning | Responder usando os exemplos que chegaram na entrada, sem mexer nos pesos. |
| zero-shot | Usar o modelo pré-treinado sem nenhum ajuste no seu dado. |
| fine-tuning | Ajustar os pesos do modelo pré-treinado no seu dado, em vez de só usá-lo como contexto. |
| checkpoint | O arquivo com os pesos treinados de um modelo; carregar o checkpoint é ler esse arquivo. |
| support set (contexto) | As linhas de treino que o modelo pré-treinado lê na hora de prever. |
| prior | No Mitra, o tipo de tabela sintética usada no treino dele; escolher a mistura de priors é o que o paper investiga. |
| árvore de decisão | Modelo de regras do tipo se... então; sozinha decora com facilidade, e é a peça de que o ensemble é feito. |
| profundidade (max_depth) | Quantas perguntas a árvore pode encadear; é o botão de capacidade dela. |
| ensemble | Combinação de vários modelos; bagging e boosting são as duas formas. |
| bagging | Treinar modelos independentes em amostras do dado e votar (o Random Forest é isso com árvores). |
| boosting | Treinar modelos em sequência, cada um corrigindo o erro que sobrou do anterior (XGBoost, LightGBM, CatBoost). |

Onde: `foundational/01_tabpfn` e `foundational/02_mitra` (os seis primeiros), `ensemble/01_bagging_and_boosting` (os três últimos).

## Redes neurais

| Termo | Em uma frase |
|-------|--------------|
| rede densa (MLP) | Camadas em que cada neurônio vê todas as saídas da camada anterior. |
| neurônio | Multiplica cada entrada por um peso, soma tudo e passa o resultado por uma ativação. |
| camada escondida | A camada do meio que cria colunas novas a partir das originais; é ela que dá não linearidade ao modelo. |
| ativação | A função não linear aplicada na saída do neurônio; sem ela, empilhar camadas equivale a uma única transformação linear. |
| ReLU | A ativação mais simples: devolve o valor se for positivo e zero se for negativo. |
| logit | A saída crua do modelo, antes de virar probabilidade; a sigmoide é a curva que faz essa conversão. |
| convolução | Aplicar o mesmo kernel deslizando pela imagem; é o que compartilha pesos e dá tolerância a deslocamento. |
| kernel (filtro) | A pequena matriz que a convolução desliza para detectar um padrão. |
| canal | Um mapa de respostas; cada canal aprende um detector. |
| pooling | Resumir uma região do mapa num só valor (em geral o máximo), reduzindo a resolução. |
| pool global | Resumir o mapa inteiro, o que tira a posição da conta e dá invariância a deslocamento. |
| RNN | Rede que percorre a sequência passo a passo carregando um estado; aceita comprimento variável com os mesmos pesos em todos os passos. |
| estado escondido | A memória da RNN, reescrita a cada passo. |
| LSTM e GRU | Células recorrentes com portas, que decidem o que guardar e o que esquecer; existem porque a RNN simples falha em tarefas que combinam a sequência inteira. |

Onde: `deep-learning/01_mlp`, `deep-learning/02_cnn` e `deep-learning/03_rnn`.

## Redução de dimensão

| Termo | Em uma frase |
|-------|--------------|
| PCA | Procura as direções de maior variância e projeta os dados nelas; é linear, e as componentes são combinações das colunas originais. |
| componente | Uma dessas direções; a primeira explica mais variância que a segunda, e assim por diante. |
| variância explicada | Quanto da variação total cada componente carrega; a soma acumulada decide quantas guardar. |
| t-SNE | Posiciona os pontos em duas dimensões tentando manter cada um perto dos seus vizinhos; serve para ver, não para medir. |
| perplexity | No t-SNE, o tamanho aproximado da vizinhança que cada ponto tenta respeitar. |

Onde: `unsupervisioned/02_dimensionality_reduction`.

## Busca sem derivada

| Termo | Em uma frase |
|-------|--------------|
| metaheurística | Método de busca que não usa derivada da função objetivo; o algoritmo genético daqui é um. |
| indivíduo | Uma solução candidata. |
| cromossomo | O indivíduo escrito como sequência de valores (os genes). |
| gene | Cada posição do cromossomo. |
| população | O conjunto de indivíduos mantido geração após geração. |
| fitness | A nota de um indivíduo, calculada pela função que você escreve. |
| seleção por torneio | Sortear alguns indivíduos e escolher o de melhor nota como pai. |
| crossover | Misturar o cromossomo de dois pais para gerar filhos. |
| mutação | Mudar um gene ao acaso, para a busca não travar num ponto. |
| elitismo | Garantir que o melhor indivíduo de cada geração sobreviva à seguinte. |
| geração | Uma rodada completa de avaliar, selecionar, cruzar e mutar. |

Onde: `metaheuristics/01_genetic_algorithm`.

## Dados e vocabulário comum

| Termo | Em uma frase |
|-------|--------------|
| atributo (feature, coluna) | Uma informação sobre o exemplo. |
| alvo (target) | A coluna que se quer prever. |
| rótulo (label) | O valor do alvo, quando já conhecido; em classificação, a classe. |
| instância (linha, exemplo) | Um caso da tabela. |
| classe positiva | A classe que a métrica trata como "o evento" (aqui, em câncer de mama, o tumor maligno). |
| divisão estratificada | Manter a proporção das classes em treino e teste, o que importa em dado desbalanceado. |
| dataset de brinquedo | Dado pequeno e sintético usado para ensinar, como as meias-luas e os blobs. |
| custo (fit_s, predict_s) | Tempo de treino e de previsão; em produção costuma ser o que decide qual modelo vai. |

Onde: todos os notebooks.

## Não confunda

- **parâmetro × hiperparâmetro**: o primeiro o treino ajusta, o segundo você escolhe antes de treinar.
- **validação × teste**: a validação serve para decidir, o teste só para medir no fim.
- **época × iteração**: uma época é uma passada por todo o treino; uma iteração é um passo (um lote).
- **padronização × normalização**: padronizar é deixar média 0 e desvio 1; normalizar costuma ser reescalar para um intervalo.
- **importância × causa**: nenhum notebook aqui mede causa, e acurácia não é explicação.
