#SCIKIT-LEARN
"""
O scikit-learn é uma biblioteca muito versátil que abrange diversas tarefas relacionadas
a aprendizado de máquina, incluindo regressão, classificação e clusterização, entre outras.
Ele fornece ferramentas para criar, treinar e avaliar modelos em várias áreas de aprendizado
de máquina. Vou explicar brevemente como o scikit-learn pode ser usado em cada uma dessas tarefas:
Aprendizado de Máquina: O scikit-learn oferece muitas funcionalidades para criar e treinar
modelos de aprendizado de máquina. Você pode criar modelos que se ajustam a dados e fazem
previsões ou classificações com base nesses dados. Ele fornece uma ampla gama de algoritmos e técnicas para isso.
Regressão: Para problemas de regressão, como prever um valor numérico (por exemplo, prever
o preço de uma casa com base em suas características), o scikit-learn possui implementações
de vários algoritmos de regressão, como regressão linear, regressão polinomial e mais.
Classificação: Para problemas de classificação, em que você quer categorizar dados em classes
(por exemplo, classificar e-mails como spam ou não spam), o scikit-learn oferece algoritmos como
máquinas de suporte vetorial (SVM), árvores de decisão, k-vizinhos mais próximos (k-NN), entre outros.
Clusterização: O scikit-learn também permite realizar tarefas de clusterização, 
onde você agrupa dados sem rótulos em clusters com base em suas similaridades.
O algoritmo K-Means é um exemplo popular para isso, mas existem outros algoritmos de 
clusterização disponíveis.

EXEMPLO CHATGPT ;-)

REGRESSÃO
Imagine que você é um detetive que gosta muito de resolver mistérios.
Hoje, você tem uma lista de casas com tamanhos diferentes e seus respectivos preços de venda.
Você quer descobrir se existe um jeito de prever o preço de uma casa com base no seu tamanho.
Para resolver esse mistério, você vai usar uma "máquina de adivinhar" especial chamada "scikit-learn".
Essa máquina vai olhar para todos os tamanhos de casas que você tem e os preços delas.
Depois de olhar para muitos exemplos, a máquina vai aprender uma regra mágica que vai ajudar
a prever o preço de qualquer casa só olhando para o tamanho dela.
A regra mágica que a máquina vai aprender é uma linha que ajuda a conectar os pontos.
Cada ponto é como uma dica para a máquina. Ela vai tentar traçar uma linha que esteja perto dos
pontos para fazer suas previsões.
Agora, você pega uma casa nova, mede o tamanho dela e coloca esse número na máquina.
A máquina usa a regra mágica para "adivinhar" o preço da casa com base no tamanho.
E voilà! Você tem uma previsão do preço da casa.
Mas como saber se a máquina é boa em adivinhar?
É aí que entra a parte legal. Você tem algumas casas que não mostrou para a máquina antes,
como uma surpresa. Você pede para a máquina adivinhar o preço delas e compara com o preço real.
Se a máquina acertar muitas vezes, é um sinal de que ela está fazendo um bom trabalho!
E isso, criança, é como o scikit-learn ajuda a resolver mistérios de previsão.
Ele é como um detetive mágico que aprende com exemplos e faz adivinhações usando regras especiais.
Legal, né? Agora você tem uma ideia de como usar o scikit-learn para fazer previsões de preços
de casas com base em seus tamanhos!
"""

# Primeiro, precisamos importar a biblioteca mágica chamada scikit-learn
from sklearn.linear_model import LinearRegression

# Agora, vamos criar nossa lista de tamanhos de casas (características) e os preços delas (alvos)
tamanhos = [[80], [100], [120], [150], [200]]  # Tamanhos das casas (em metros quadrados)
precos = [150000, 200000, 230000, 280000, 350000]  # Preços das casas (em moedas mágicas)

# A próxima coisa é ensinar nossa máquina mágica (scikit-learn) sobre essas casas
maquina = LinearRegression()  # Criamos nossa máquina de regressão mágica

# Agora, mostramos para a máquina os tamanhos das casas e os preços delas, como se fossem pistas
maquina.fit(tamanhos, precos)

# Nossa máquina agora aprendeu uma regra mágica que conecta tamanhos e preços!

# Ok, agora temos uma casa nova, e queremos saber o preço dela.
tamanho_nova_casa = [[130]]  # Tamanho da casa nova (também em metros quadrados)

# Vamos pedir para a máquina adivinhar o preço da casa nova com base na regra mágica que ela aprendeu
preco_adivinhado = maquina.predict(tamanho_nova_casa)

# Uau! A máquina fez uma adivinhação do preço da casa nova! Vamos ver o que ela acha...
print(f"A máquina adivinha que o preço da casa é aproximadamente {preco_adivinhado[0]:.2f} moedas mágicas!")

# Agora, a parte divertida: vamos testar se a máquina é boa em adivinhar. Temos uma casa surpresa!
tamanhos_surpresa = [[180]]  # Tamanho da casa surpresa

# Pedimos para a máquina adivinhar o preço da casa surpresa
precos_adivinhados_surpresa = maquina.predict(tamanhos_surpresa)

# Agora, nós, os detetives, comparamos a adivinhação da máquina com o preço real da casa surpresa
preco_real_surpresa = 320000  # Preço real da casa surpresa (em moedas mágicas)
erro = preco_real_surpresa - precos_adivinhados_surpresa[0]  # Calculamos o erro mágico

# Vamos ver o que aconteceu!
print(f"A máquina adivinhou um preço de {precos_adivinhados_surpresa[0]:.2f} moedas mágicas para a casa surpresa.")
print(f"O preço real da casa surpresa é {preco_real_surpresa:.2f} moedas mágicas.")
print(f"A diferença entre a adivinhação da máquina e o preço real é {erro:.2f} moedas mágicas.")

"""
#CLASSIFICAÇÃO
Era uma vez um jardim mágico cheio de flores incríveis e misteriosas. 
Nesse jardim, viviam três tipos diferentes de flores: as flores Setosas,
as flores Versicolor e as flores Virginicas. Um grupo de cientistas,
apaixonados pela magia da natureza, queria ensinar uma máquina especial a
reconhecer cada tipo de flor só olhando para elas.
Primeiro, eles trouxeram uma ferramenta mágica chamada "scikit-learn" do seu baú de tesouros.
Essa ferramenta tinha um feitiço muito poderoso que podia ensinar uma máquina a
fazer previsões mágicas. Eles também tinham um conjunto mágico de flores chamado "Iris"
que continha informações sobre o tamanho das pétalas e sépalas de cada flor, além do seu tipo.
Os cientistas pegaram as informações sobre os tamanhos das pétalas e sépalas das flores
e usaram como pistas para treinar a máquina. Eles separaram algumas flores para treiná-la
e outras para testar suas habilidades mágicas.
A máquina mágica, chamada de "K-Nearest Neighbors" (Vizinhos Mais Próximos),
ficou muito curiosa para aprender sobre as flores. Ela olhou atentamente para
as pistas mágicas e aprendeu a diferenciar as características das flores de cada tipo.
Ela ficou tão boa que conseguia olhar para uma flor nova e dizer qual tipo de flor era,
só de olhar para o tamanho das pétalas e sépalas.
Um dia, um pesquisador trouxe uma flor que nunca tinha sido vista antes. 
Era uma flor desconhecida, com tamanhos mágicos de pétalas e sépalas. Ele pediu à máquina para
adivinhar o tipo da flor, e a máquina, confiante em seus conhecimentos mágicos, fez uma previsão.
Ela disse: "A flor é do tipo X!" E todos ficaram admirados com a precisão da máquina.
Mas os cientistas adoravam desafios e decidiram testar a máquina com flores surpresa.
Eles trouxeram duas flores surpresa com tamanhos mágicos e pediram à máquina para adivinhar seus tipos.
A máquina fez suas adivinhações, e os cientistas compararam suas previsões com os tipos reais das
flores surpresa. A máquina acertou a maioria das vezes!
Os cientistas ficaram maravilhados com a precisão da máquina. Eles usaram uma mágica especial
chamada "Acurácia" para medir o quão boa a máquina estava em adivinhar. Eles viram que a
máquina tinha uma precisão mágica de aproximadamente 83%, ou seja, ela acertou 83% das vezes!
E assim, a máquina mágica do "scikit-learn" mostrou que podia aprender com pistas mágicas e
fazer previsões mágicas sobre os tipos das flores. Os cientistas ficaram encantados com essa mágica moderna,
que podia ajudá-los a entender melhor o mundo mágico das flores.
E assim, a história da máquina mágica de classificação chegou ao fim,
mas suas habilidades continuaram a deslumbrar os cientistas em muitas outras aventuras mágicas.
"""

# Primeiro, importamos a biblioteca mágica chamada scikit-learn
from sklearn.datasets import load_iris  # Vamos usar um conjunto de dados mágico do scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Carregamos o conjunto de dados mágico chamado "Iris"
dados_iris = load_iris()

# As características das flores são como pistas para a máquina mágica (scikit-learn)
caracteristicas = dados_iris.data  # Tamanho da pétala e sépala das flores
alvos = dados_iris.target  # Tipo de flor (0, 1 ou 2)

# Dividimos os dados em conjuntos de treinamento e teste
caracteristicas_treino, caracteristicas_teste, alvos_treino, alvos_teste = train_test_split(caracteristicas, alvos,test_size=0.2, random_state=42)

# Criamos nossa máquina de classificação mágica (K-Nearest Neighbors)
maquina_classificacao = KNeighborsClassifier(n_neighbors=3)  # K = 3, que é o número de vizinhos mágicos

# Ensinamos nossa máquina mágica sobre as flores e seus tipos
maquina_classificacao.fit(caracteristicas_treino, alvos_treino)

# Agora, nossa máquina sabe como diferenciar tipos de flores!

# Pegamos uma flor nova e queremos saber qual é o tipo dela.
flor_desconhecida = [[5.1, 3.5, 1.4, 0.2]]  # Características da flor nova (tamanho da pétala e sépala)

# Pedimos para a máquina adivinhar o tipo da flor nova com base no que ela aprendeu
tipo_adivinhado = maquina_classificacao.predict(flor_desconhecida)

# Uau! A máquina fez uma adivinhação do tipo da flor nova! Vamos ver o que ela acha...
print(f"A máquina adivinha que o tipo da flor é {tipo_adivinhado[0]}!")

# Agora, a parte divertida: vamos testar se a máquina é boa em adivinhar. Temos flores surpresa!
flores_surpresa = [
    [6.3, 2.9, 5.6, 1.8],
    [5.7, 2.8, 4.5, 1.3]
]

# Pedimos para a máquina adivinhar o tipo das flores surpresa
tipos_adivinhados_surpresa = maquina_classificacao.predict(flores_surpresa)

# Agora, nós, os detetives, comparamos as adivinhações da máquina com os tipos reais das flores surpresa
tipos_reais_surpresa = [2, 1]  # Tipos reais das flores surpresa
acuracia = accuracy_score(tipos_reais_surpresa, tipos_adivinhados_surpresa)  # Calculamos a precisão mágica

# Vamos ver o que aconteceu!
print(f"A máquina adivinhou os tipos das flores surpresa: {tipos_adivinhados_surpresa}!")
print(f"Os tipos reais das flores surpresa são: {tipos_reais_surpresa}.")
print(f"A precisão da máquina em adivinhar é aproximadamente {acuracia:.2f} moedas mágicas!")

"""
# CLUSTERIZAÇÃO
Havia uma terra encantada onde viviam criaturas mágicas chamadas "Pontos".
Esses Pontos tinham características mágicas, como brilho e cor. No entanto,
esses Pontos eram muito curiosos e queriam estar perto de outros Pontos que
fossem semelhantes a eles.
Um dia, um grupo de cientistas mágicos decidiu explorar essa terra e entender
como os Pontos gostavam de se agrupar. Para isso, eles trouxeram uma ferramenta mágica chamada
"scikit-learn" que tinha um feitiço especial chamado K-Means. Esse feitiço permitia que eles
ensinassem a máquina a criar grupos mágicos de Pontos com base em suas características.
Os cientistas começaram a criar Pontos mágicos usando uma fórmula secreta,
formando grupos de Pontos brilhantes em diferentes partes da terra. 
Eles criaram quatro grupos mágicos de Pontos, cada um com um brilho e uma cor únicos.
A máquina mágica de K-Means ficou empolgada em aprender sobre os Pontos e como eles
gostavam de se juntar. Os cientistas ensinaram a máquina a reconhecer as características
dos Pontos e a formar grupos mágicos com base na proximidade entre eles. 
A máquina estudou os Pontos com muita atenção e aprendeu a criar grupos que fossem parecidos uns com os outros.
Depois de um tempo, a máquina mágica de K-Means ficou muito sábia e disse aos cientistas
que tinha aprendido a formar quatro grupos mágicos de Pontos com base em suas características.
Os cientistas ficaram animados e pediram à máquina para mostrar como os grupos foram formados.

                                                                                            