# Escalonamento de Ônibus Universitários

Projeto desenvolvido para a disciplina de Programação Matemática, com o objetivo de modelar e resolver o problema de escalonamento dos ônibus entre os campi da USP São Carlos.

## Descrição

O problema consiste em determinar a quantidade de ônibus que deve realizar viagens entre os dois campi ao longo do dia, buscando minimizar o número total de viagens realizadas e, ao mesmo tempo, atender toda a demanda de passageiros.

O modelo considera:

* Capacidade máxima dos ônibus;
* Quantidade total de veículos disponíveis;
* Demanda de passageiros em cada horário;
* Conservação da frota entre os campi;
* Limite máximo de viagens diárias.

## Métodos Utilizados

Foram implementadas três abordagens distintas:

* **Gurobi** (solver comercial);
* **SCIP/PySCIPOpt** (solver gratuito);
* **Heurística gulosa** desenvolvida em Python.

Os modelos de otimização foram formulados como problemas de Programação Inteira.

## Estrutura do Projeto

```text
solver_comercial.py   -> Implementação utilizando Gurobi
solver_gratuito.py    -> Implementação utilizando SCIP
heuristica.py         -> Algoritmo guloso
relatorio.pdf         -> Relatório do projeto
```

## Requisitos

### Gurobi

```bash
pip install gurobipy
```

É necessária uma licença acadêmica ou comercial do Gurobi.

### SCIP

```bash
pip install pyscipopt
```

## Execução

Para executar os programas:

```bash
python solver_comercial.py
```

```bash
python solver_gratuito.py
```

```bash
python heuristica.py
```

## Resultados

Os experimentos mostraram que:

* Ambos os solvers encontraram soluções ótimas.
* O gap de otimalidade foi igual a 0%.
* Os tempos de processamento ficaram na ordem de milissegundos.
* A heurística encontrou as mesmas soluções dos solvers nos casos de teste avaliados, apresentando menor tempo de execução.

## Autores

* Eduardo A. Paiva
* Henrique R. de Figueiredo
* João Pedro B. Faga
* Pedro C. Gonzaga

## Disciplina

Programação Matemática
Engenharia de Computação – USP São Carlos
