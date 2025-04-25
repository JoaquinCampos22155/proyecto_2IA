# proyecto_2IA
# Generador de Laberintos Aleatorios 🌀

Este proyecto en Python permite generar laberintos aleatorios en un grid de tamaño **M x N**, utilizando dos algoritmos:

- **Algoritmo de Kruskal**
- **Algoritmo de Backtracking (DFS iterativo)**

Cada laberinto generado es un **laberinto perfecto**, es decir, tiene una única solución entre el punto de inicio (putno rojo) y el punto final (punto verde).

---

## Disclaimer

En el uso de algoritmo backtracking para la generacion del laberinto se ha creado una pila manual ya que las de python tienen limite de recursion generando entonces un error al intentar hacer laberitnos de 50x50 o mas.