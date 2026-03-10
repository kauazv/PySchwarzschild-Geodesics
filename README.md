# PySchwarzschild-Geodesics

Simulação numérica de geodésicas no espaço-tempo de Schwarzschild utilizando Python.

Este projeto explora trajetórias de partículas massivas e fótons em torno de um buraco negro não rotante, utilizando integração numérica das equações de geodésica.

## Objetivos

O projeto demonstra numericamente efeitos previstos pela Relatividade Geral:

* órbitas relativísticas
* queda radial em buracos negros
* desvio gravitacional da luz
* órbitas de fótons
* sombra de buraco negro

## Base teórica

A simulação utiliza a métrica de Schwarzschild, solução das equações de campo da Relatividade Geral para um corpo esfericamente simétrico e não rotante.

No plano equatorial (θ = π/2), as equações de movimento podem ser reduzidas utilizando as constantes de movimento:

* energia por unidade de massa (E)
* momento angular por unidade de massa (L)

A equação radial efetiva assume a forma:

(dr/dτ)² + V_eff(r) = E²

onde V_eff(r) é o potencial efetivo relativístico.

Mais detalhes podem ser encontrados em:

theory.md

## Estrutura do projeto

PySchwarzschild-Geodesics

```
schwarzschild.py           # Funções da métrica
geodesics_massive.py       # Geodésicas de partículas massivas
geodesics_photons.py       # Geodésicas de fótons

plots/                     # Visualizações
tests/                     # Testes simples

notebooks/                 # Demonstrações em Jupyter

theory.md                  # Fundamentação teórica
```

## Exemplos de simulações

O projeto inclui scripts para gerar diferentes visualizações físicas:

* queda radial em buraco negro
* órbitas relativísticas
* desvio gravitacional da luz
* feixe de fótons
* sombra de buraco negro

Exemplo de execução:

```
python plots/plot_light_deflection.py
```

## Requisitos

Python 3.10+

Bibliotecas utilizadas:

```
numpy
scipy
matplotlib
```

Instalação:

```
pip install numpy scipy matplotlib
```

## Notebooks

Os notebooks demonstram como utilizar o código para explorar diferentes cenários físicos:

* órbitas relativísticas
* geodésicas de fótons
* visualização de trajetórias

## Motivação

Este projeto foi desenvolvido como estudo de Relatividade Geral e métodos numéricos aplicados à física gravitacional.

## Licença

MIT License
