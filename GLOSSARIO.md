# Glossário

Os termos em inglês que aparecem nos notebooks, cada um traduzido em uma frase.

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

## Ajuste e avaliação

| Termo | Em uma frase |
|-------|--------------|
| parâmetro | O que o treino ajusta sozinho: os pesos, os coeficientes. |
| hiperparâmetro | O que você escolhe antes do treino (profundidade da árvore, taxa de aprendizado, o `k` do K-Means); o modelo não descobre sozinho. |
| ajuste de hiperparâmetros (tuning) | Procurar a combinação de hiperparâmetros que rende mais numa métrica de validação. |
| semente (seed) | O número que fixa os sorteios; com a mesma semente o mesmo código dá o mesmo resultado, quando o método é determinístico. |
| validação cruzada (k-fold) | Dividir o treino em k partes e treinar k vezes, cada vez com uma parte de fora; devolve média e desvio, que uma divisão só não dá. |
| KFold | Divide a tabela em k partes iguais; embaralhar é obrigatório quando a tabela veio ordenada, senão um fold pode ficar sem nenhuma classe positiva. |
| StratifiedKFold | O mesmo, mantendo a proporção das classes em cada parte; é o padrão em classificação. |
| GroupKFold | Mantém o grupo inteiro (pessoa, cliente, sensor) de um lado só; evita que o modelo reconheça quem respondeu. |
| TimeSeriesSplit | Treina sempre no passado e testa no futuro; é a única divisão honesta quando existe ordem. |
| grupo (groups=) | A coluna que diz a que unidade a linha pertence, quando uma unidade responde mais de uma linha. |
| vazamento por grupo | Nota alta porque linhas da mesma unidade aparecem no treino e no teste; não gera aviso e depende do modelo aparecer. |
| validação aninhada | Um laço externo mede e um interno escolhe, para o número que serviu para escolher não ser o número que você reporta. |
| origem deslizante (backtesting) | Reavaliar o modelo avançando a origem do treino e testando sempre o bloco seguinte. |
| validação | O pedaço usado para decidir (escolher hiperparâmetro, parar o treino). Não é o teste. |
| teste | O pedaço que só se olha no fim, para medir de verdade; decidir olhando o teste é a forma mais fácil de publicar número otimista. |
| baseline | O resultado simples que qualquer proposta precisa superar para valer a pena. |
| overfitting (decorar) | Acertar no treino e errar no que não viu, porque o modelo aprendeu o ruído. |
| underfitting | Modelo simples demais: erra no treino e no teste. |
| viés e variância | Os dois lados do trade-off; pouco viés com muita variância decora, o contrário não representa. |
| regularização | Somar à perda uma penalidade pelo tamanho dos coeficientes, para o modelo só usar o que se paga. |
| padronização (standardization) | Deixar cada coluna com média 0 e desvio 1; obrigatório quando o modelo mede distância (kNN, SVM, rede) e irrelevante para árvore. |

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

## Redução de dimensão

| Termo | Em uma frase |
|-------|--------------|
| PCA | Procura as direções de maior variância e projeta os dados nelas; é linear, e as componentes são combinações das colunas originais. |
| componente | Uma dessas direções; a primeira explica mais variância que a segunda, e assim por diante. |
| variância explicada | Quanto da variação total cada componente carrega; a soma acumulada decide quantas guardar. |
| t-SNE | Posiciona os pontos em duas dimensões tentando manter cada um perto dos seus vizinhos; serve para ver, não para medir. |
| perplexity | No t-SNE, o tamanho aproximado da vizinhança que cada ponto tenta respeitar. |

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

## Seleção de features

| Termo | Em uma frase |
|-------|--------------|
| seleção de features | Escolher quais colunas entram no modelo, entre as que já existem. |
| filtro | Mede cada coluna sozinha, sem treinar modelo: barato, e cego para redundância. |
| wrapper | Treina o modelo muitas vezes, tirando e pondo colunas, e escolhe pelo que o modelo usa. |
| embutido | A importância sai do próprio modelo treinado (`L1`, importância de árvore). |
| RFE | Remove a coluna menos importante de cada vez, até sobrar o número pedido. |
| RFECV | O `RFE` que decide sozinho quantas colunas ficam, por validação cruzada. |
| permutation importance | Mede o estrago na nota ao embaralhar uma coluna de cada vez. |
| Boruta | Procura todas as colunas que carregam informação, comparando cada uma com uma cópia embaralhada. |
| features sombra | As cópias embaralhadas que o Boruta usa como régua do que é ruído. |
| all-relevant | A pergunta do Boruta: tudo o que carrega informação, em vez do mínimo que basta. |
| minimal-optimal | A pergunta do filtro, do wrapper e do embutido: o menor conjunto que mantém a nota. |
| SHAP | Reparte a contribuição de cada coluna em cada previsão do modelo treinado. |
| valor de Shapley | A contribuição média de uma coluna considerando todas as combinações possíveis de colunas. |
| redundância | A coluna que repete informação de outra; é correlação alta entre colunas, não com o alvo. |

## Engenharia de features

| Termo | Em uma frase |
|-------|--------------|
| engenharia de features | Criar coluna nova a partir das que existem, com hipótese declarada e medição. |
| interação | Efeito que só aparece quando duas colunas são olhadas juntas, como o produto delas. |
| agregação por grupo | Trocar a linha pelo comportamento médio do grupo dela: contexto, não resposta. |
| transformação de distribuição | Mudar a escala de uma coluna (`log`, quantil) para o modelo lidar melhor com ela. |
| faixas (binning) | Trocar uma coluna numérica por faixas ordenadas. |
| data expandida | Extrair mês, dia da semana e fim de semana de uma coluna de data. |
| palavra-chave (indicador de texto) | Coluna que diz se o texto menciona algo que importa. |
| vazamento temporal | Coluna que só existe depois do desfecho; usá-la é prever o passado com a resposta na mão. |
| hipótese | A aposta que justifica a coluna nova. Sem hipótese, criar feature é tentativa. |

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
| análise exploratória (EDA) | Olhar a tabela antes de modelar: distribuição, faltante, cardinalidade, duplicata e vazamento. |
| distribuição | Como os valores de uma coluna se espalham, e onde ficam o centro e as caudas. |
| assimetria (skew) | O quanto a coluna tem cauda de um lado; 0 é simétrica, acima de 1 é cauda longa. |
| valor faltante (missing) | Ausência de medição, que não é zero nem categoria. |
| imputação | Preencher o faltante com uma estimativa, dentro do pipeline, para a estatística do teste não entrar no treino. |
| cardinalidade | Quantos valores distintos uma coluna de texto tem; é o que decide o custo do encoding. |
| duplicata | A mesma linha aparecendo mais de uma vez na base. |
| correlação de Pearson | Mede relação em linha reta entre duas colunas numéricas. |
| correlação de Spearman | Mede relação de ordem, sem exigir que seja reta. |
| vazamento (leakage) | Coluna que só existe depois do desfecho, ou informação do teste que entra no treino. |
| classe majoritária | A classe mais frequente; chutar sempre ela é o baseline que a acurácia esconde. |
| encoding (codificação) | Transformar coluna de texto em número, para o modelo poder usá-la. |
| coluna ordinal | Categórica em que a ordem existe (`baixo` < `medio` < `alto`). |
| coluna nominal | Categórica sem ordem (`plano`, `cidade`). |
| cardinalidade alta | Coluna com muitas categorias distintas; é o que decide entre one-hot e codificação pelo alvo. |
| one-hot | Uma coluna por categoria, com 1 na categoria da linha e 0 nas outras. |
| categorias raras | As que têm poucas linhas; juntá-las num rótulo só é decisão que não usa o alvo. |
| codificação pelo alvo (target encoding) | Trocar a categoria pela média do alvo naquela categoria. |
| suavização (smoothing) | Puxar a média da categoria na direção da média geral, quando há poucas linhas nela. |
| codificação com validação cruzada interna | O codificador calcula a média de cada fold, para não usar a própria linha que está codificando. |
| handle_unknown | O que o codificador faz quando aparece categoria nova na hora de prever: errar ou ignorar. |
| ColumnTransformer | Objeto que aplica um tratamento diferente a cada grupo de colunas. |
| Pipeline | Objeto que encadeia tratamentos e modelo, e garante que o tratamento aprenda só no treino. |

## Não confunda

- **parâmetro × hiperparâmetro**: o primeiro o treino ajusta, o segundo você escolhe antes de treinar.
- **validação × teste**: a validação serve para decidir, o teste só para medir no fim.
- **época × iteração**: uma época é uma passada por todo o treino; uma iteração é um passo (um lote).
- **padronização × normalização**: padronizar é deixar média 0 e desvio 1; normalizar costuma ser reescalar para um intervalo.
- **importância × causa**: nenhum notebook aqui mede causa, e acurácia não é explicação.
- **correlação × causa**: duas colunas andando juntas não dizem que uma causa a outra, e uma coluna vazada anda junto porque é o alvo disfarçado.
- **faltante × zero**: zero é um valor medido, faltante é ausência; tratar os dois igual inventa dado.
- **one-hot × codificação pelo alvo**: o primeiro não usa o alvo e pode ser calculado antes da divisão; o segundo usa, e por isso tem de acontecer dentro do pipeline.
- **transformar × criar**: transformar reescreve a coluna que existe (encoding, `log`, faixas); criar acrescenta coluna que não existia (interação, agregação, calendário, palavra-chave).
- **métrica indefinida × métrica perfeita**: um fold sem nenhuma linha da classe positiva não dá nota 1, dá nota que não existe; a média que ignora esses folds mente.
- **relevante × redundante**: relevante é carregar informação; redundante é repetir informação que outra coluna já carrega, e o Boruta mede uso, não novidade.
