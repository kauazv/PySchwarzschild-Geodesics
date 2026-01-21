# Teoria: Órbitas em Schwarzschild

## 1. Métrica de Schwarzschild

A métrica de Schwarzschild descreve a geometria do espaço-tempo ao redor de um objeto esfericamente simétrico e estático (como um buraco negro não rotante). Em coordenadas de Schwarzschild (t, r, θ, φ), a métrica expressa como o intervalo espaço-temporal se relaciona com as coordenadas.

Parâmetros importantes:
    - M é a massa do buraco negro (em unidades geométricas onde o G = c = 1)
    - r é a coordenada radial
    - O horizonte de eventos está localizado em r_s = 2M (raio de Schwarzschild)
    
A métrica possui duas superfícies importantes:
    - Horizonte de eventos (r = 2M):superfície de não-retorno
    - Singularidade (r = 0): onde a curvatura diverge

A métrica de Schwarzschild é dada por

ds² = -(1 - 2M/r) dt² + (1 - 2M/r)⁻¹ dr²
      + r² (dθ² + sin²θ dφ²)


## 2. Plano Equatorial

Por simetria esférica, podemos restringir o movimento de partículas ao plano equatorial sem perda de generalidade. Fazemos = θ = pi/2 e a derivada temporal de θ igual a zero.

Isso simplifica drasticamente as equações de movimento. No plano equatorial, a métrica reduz-se a apenas três coordenadas relevantes: tempo t, raio r, e ângulo azimutal

Esta simplificação é valida porque:
    - A métrica é esfericamente simétrica
    - Qualquer órbita pode ser rotacionada para coincidir com o plano equatorial
    - Reduz o problema de 4D para 3D efetivamente

## 3. Constantes de Movimento

As simetrias da métrica de Schwarzschild levam a constantes de movimento através do teorema de Noether:

-- Energia por unidade de massa

Por independência temporal (a métrica não depende explicitamente do tempo coordenado t), existe uma quantidade conservada E relacionada à componente temporal da quadrivelocidade.

-- Momento Angular por unidade de massa

Por simetria azimutal (a métrica não depende do ângulo φ), existe uma quantidade conservada L relacionada à componente angular da quadrivelocidade.

-- Condição de Normalização 

Para partículas massivas, a quadrivelocidade satisfaz uma condição de normalização que relaciona todas as componentes da velocidade.
Combinando essas três equações no plano equatorial, obtemos a equação radial efetiva: a derivada do raio em relação ao tempo próprio ao quadrado, mais um potencial efetivo V_eff(r), é igual a E ao quadrado.
O potencial efetivo V_eff(r) depende tanto da massa M quanto do momento angular L, e descreve como a geometria do espaço-tempo afeta o movimento radial.
Esta equação descreve o movimento radial como se fosse uma partícula em um potencial unidimensional, facilitando enormemente a análise das órbitas.

# Observações importantes:

Partículas com E < 1 têm órbitas ligadas
Órbitas circulares ocorrem em extremos de V_eff(r)
A última órbita circular estável (ISCO) está em r = 6M para partículas massivas
Fótons (m = 0) têm órbitas circulares instáveis em r = 3M (esfera de fótons)