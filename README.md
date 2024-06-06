Com o intuito de facilitar o cálculo na análise de circuitos de 1° e 2° ordem, este repositório oferece funções para criar, combinar e associar fasores, tanto na sua forma polar como retangular.
Para utiliza-lo deve primeiro calcular as impedâncias do circuito, da seguinte forma:

RESISTOR
Zr = R, onde Zr é a impedância do resistor e R a sua resistência.

CAPACITOR
Zc = - jwC, onde Zc é a impedância do capacitor, j é o número complexo, w é a frequência angular e C a capacitância.

INDUTOR
Zl = jwL, onde Zl é a impedância do indutor, j é o número complexo, w é a frequência angular e L a indutância.

Em seguinda deve-se criar os fasores com a classe "Fasores" que recebe a parte real, a parte imaginária e a forma do fasor como parâmetros. Por exemplo, 

Para o fasor 60∠90° (Forma Polar)

No código:
Fasor = (60, 90, "Polar")
