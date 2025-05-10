# ejercicio3/reporte.py

import pandas as pd

def analyze_results(df: pd.DataFrame) -> pd.DataFrame:
    """
    Añade la columna 'Place' (ranking por nodos expandidos)
    y devuelve el resumen promedio ordenado por 'Place'.
    """
    df['Place'] = df.groupby('Maze')['Expanded'] \
                   .rank(method='dense', ascending=True).astype(int)
    summary = df.groupby('Algorithm')[['Distance','Expanded','Time_s','Place']] \
                .mean().sort_values('Place')
    return summary

def export_csv(df: pd.DataFrame, summary: pd.DataFrame) -> None:
    """
    Guarda los resultados y el ranking promedio en CSVs.
    """
    df.to_csv("exercise_3/comparacion_algoritmos.csv", index=False)
    summary.to_csv("exercise_3/ranking_promedio.csv")
