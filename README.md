# Estimativa de geolocalização utilizando uma variação do algoritmo KNN

## Sobre o trabalho

O trabalho a ser realizado consiste em determinar a localização aproximada (coordenadas: latitude e longitude) de pontos de uma base de dados. Para realizar esse trabalho, será feita uma classificação dos pontos que não possuem coordenadas a partir dos pontos que possuem. O algoritmo escolhido para realizar o trabalho é o KNN, modificado para realizar regressão linear.

O alvo é previsto pela interpolação local dos alvos associados aos vizinhos mais próximos no conjunto de treinamento. Assim, ele nos permite determinar a Latitude e a Longitude de cada ponto.

Por fim, com os pontos encontrados, será utilizado o PostGIS para plotar os dados em um mapa a fim de verificar se a interpolação faz sentido.

# Dados

## Fonte

As observações do solo com as quais o projeto da disciplina será desenvolvido pertencem a três relatórios de levantamento pedológico realizados em municípios do estado do Paraná. 

São eles:

- [ctb0022](http://coral.ufsm.br/febr/catalog/ctb0022.html): `Bognola, I. A.; Curcio, G. R.; Gomes, J. B. V.; Caviglione, J. H.; Uhlmann, A.; Cardoso, A.; Carvalho, A. P. Levantamento semidetalhado de solos do Município de Londrina. IAPAR : Londrina, 2011. 100p. `

- [ctb0047](https://docs.google.com/spreadsheets/d/1HlFLNRDzRqD42lJ1GF3Pv00xHBMJ2w9Yj4Z2U1OR5_Q/edit?usp=sharing): `Curcio, G. R.; Gomes, J. B. V.; Bognola, I. A.; Caviglione, J. H.; Uhlmann, A.; Cardoso, A.; Carvalho, A. P. de. Levantamento semidetalhado de solos e diagnóstico dos remanescentes florestais do município de Cambé - PR. IAPAR : Londrina, 2011. 147p.`

- [ctb0048](https://docs.google.com/spreadsheets/d/1LMa_n5E2xGnZqKFuhf_8hAG83sdoNm30PgeTVfs25FM/edit?usp=sharing): `Gomes, J. B. V.; Bognola, I. A.; Curcio, G. R.; Caviglione, J. H.; Uhlmann, A.; Cardoso, A.; Carvalho, A. P. de. Levantamento semidetalhado de solos do município de Bela Vista do Paraíso - PR. IAPAR : Londrina, 2011. 68p.`


## Processo de Normalização dos Dados

Algumas colunas serão removidas, por falta de informações. Enquanto outras serão normalizadas para informações númericas, a fim de entrar no processo e ajudar na regressão.

Mais informações, iremos atualizando o repositório.




### Colaboradores

- Rafael Boniolo
- Jonathan Galdino
- Mikael Pereira Messias
- Richard Peccin

:: Com a ilustre orientação do [Prof. Dr. Alessandro Samuel-Rosa](http://lattes.cnpq.br/1609751519717461)

