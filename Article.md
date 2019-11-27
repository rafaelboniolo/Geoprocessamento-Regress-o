# Introdução

O trabalho aborda o uso do algoritmo *K Nearest Neighbors*, com o objetivo de predizer coordenadas não disponíveis no conjunto de dados com base em características previamente normalizadas.

# Material e Métodos

## Classificação

Optou-se por utilizar a técnica de classificação *K Nearest Neighbors* (KNN). A implementação tradicional do algoritmo KNN, propõe que, ao plotar um elemento com seu conjunto de caracteristicas sobre um hiperplano, existem k elementos próximos dele, a classe prevalecente no espaço k, será a classe do elemento a ser predito.

Neste caso, a implementação tradicional não resolve o problema por completo, pois o KNN atribui uma classe para o elemento a ser predito, no melhor dos casos, o argoritmo atribuiria ao elemento predito o valor de outro elemento da base, causando a sobreposição de pontos no mapa.

Para resolver o problema será utilizado uma variação do KNN, cujo foi modificado para realizar regressão multivalorada (KNN-R), no que consiste em calcular os k-vizinhos mais próximos e calcular valores de saída com base na inteporlação dos k-vizinhos. De tal maneira, será possível obter a latitude e a longitude de cada ponto e posteriormente adicioná-los ao mapa.

Para calcular a taxa de erro da predição será utilizado o `erro quadrático`, permitindo calcular o erro em metros baseado no cálculo da escala do mapa.

## Dataset

A base de dados foi extraída dos livros:

* Levantamento semidetalhado de solos do Município de Londrina
* Levantamento semidetalhado de solos e diagnóstico dos remanescentes florestais do município de Cambé - PR
* Levantamento semidetalhado de solos do município de Bela Vista do Paraíso - PR

### Digitalização dos Dados

Com os determinados livros em mãos, foi utilizado o aplicativo *mobile* Google Lens. O Google Lens permite realizar uma varredura e tradução de textos em tempo real por meio da câmera do *smartphone* (GOOGLE LENS, 2019). Com o uso do Google Lens, o processo de digitalização dos dados foi agilizado e então os dados foram persistidos na base dados, que em seguida, foi disponibilizada no Google Drive, um serviço de armazenamento da Google.

### A Base de Dados Pré-Normalização

A base, sem sofrer o processo de normalização de dados, está utilizando os seguintes atributos:

- Identificação da observação: `numero_campo`
- Coordenada X (Leste): `coord_x`
- Coordenada Y (Norte): `coord_y`
- Classificação Taxonômica (SiBCS)
  - Por ordem: `taxon_sibcs_ordem`
  - Por subordem: `taxon_sibcs_subordem`
  - Por grupos: `taxon_sibcs_grupos`
  - Por subgrupos: `taxon_sibcs_subgrupos`
  - Por horizonte: `taxon_sibcs_horizonte`
  - Por agrupamento textural: `taxon_sibcs_horizonte`
- Altitude: `relevo_elevacao`
- Classe do Relevo Local: `relevo_local`

### Normalização da Base

Algumas informações tiveram que ser normalizadas enquanto outras foram removidas devido a falta de atributos. O KNN-R utiliza de valores númericos ou binários para o processamento do algoritmo. 
Dito isso, foi necessário readequar a base, realizando a transformação de atributos categóricos para atributos binários. De tal maneira, cada categoria do atributo, virou um novo atributo binário.


<!-- # Resultados Esperados

Espera-se predizer, com acurácia, os pontos da base de teste -->

# Referências

GOOGLE LENS. Search What You See. Disponível em <<https://lens.google.com/>>. Acesso em 8 Nov 2019.