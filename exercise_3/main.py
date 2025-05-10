# ejercicio3/main.py

import argparse
from experimentos import run_experiments
from reporte import analyze_results, export_csv

def main():
    parser = argparse.ArgumentParser(
        description="Ejercicio 3: Comparación de algoritmos de búsqueda en laberintos"
    )
    parser.add_argument('-r', '--rows', type=int, default=45,
                        help='Número de filas del laberinto')
    parser.add_argument('-c', '--cols', type=int, default=55,
                        help='Número de columnas del laberinto')
    parser.add_argument('-k', '--mazes', type=int, default=25,
                        help='Cantidad de laberintos a generar')
    args = parser.parse_args()

    df = run_experiments(args.rows, args.cols, args.mazes)
    summary = analyze_results(df)

    print("=== Resumen promedio ===")
    print(summary)

    export_csv(df, summary)
    print("CSV generados: comparacion_algoritmos.csv y ranking_promedio.csv")

if __name__ == '__main__':
    main()
