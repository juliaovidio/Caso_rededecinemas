# Levantamento de Requisitos e Regras de Negócio

## Requisitos Funcionais

### RF01 — Cadastrar Filme
O administrador poderá cadastrar filmes informando título, duração, gênero, diretor e elenco.

### RF02 — Cadastrar Cinema
O administrador poderá cadastrar cinemas informando nome, endereço, cidade, estado e capacidade máxima de público.

### RF03 — Cadastrar Sessão
O administrador poderá cadastrar sessões vinculando um filme a um cinema, definindo data e horário da exibição.

### RF04 — Registrar Público da Sessão
O funcionário poderá registrar a quantidade de espectadores presentes em cada sessão.

---

## Requisitos Não Funcionais

### RNF01 — Persistência de Dados
O sistema deverá armazenar os dados utilizando o banco de dados SQLite.

### RNF02 — Arquitetura do Sistema
O sistema deverá seguir a arquitetura MVC utilizando as camadas View, Controller, Service e Repository.

### RNF03 — Facilidade de Uso
O sistema deverá possuir interface simples e de fácil utilização para os funcionários.

### RNF04 — Organização do Código
O código-fonte deverá ser organizado em módulos e pastas separadas conforme a responsabilidade de cada camada.

---

## Regras de Negócio

### RN01 — Vínculo da Sessão
Toda sessão deve estar vinculada obrigatoriamente a um único filme e a um único cinema.

### RN02 — Limite de Público
A quantidade de espectadores registrada em uma sessão não pode ultrapassar a capacidade máxima do cinema.

### RN03 — Intervalo Entre Sessões
Deve existir um intervalo mínimo entre sessões realizadas no mesmo cinema.

### RN04 — Validação de Horário
Não será permitido cadastrar sessões com data ou horário inválidos.
