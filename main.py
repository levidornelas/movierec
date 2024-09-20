from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

# Simulando um banco de dados simples de filmes organizados por gênero
movies = {
    'action': ['Avengers: Endgame', 'Mad Max: Fury Road', 'John Wick'],
    'comedy': ['The Hangover', 'Step Brothers', 'Superbad'],
    'drama': ['The Shawshank Redemption', 'Forrest Gump', 'The Godfather'],
    'sci-fi': ['Interstellar', 'Inception', 'The Matrix'],
    'romance': ['Pride and Prejudice', 'The Notebook', 'La La Land']
}

def dfs_recommendation(tree, preference, path=None):
    if path is None:
        path = []

    # Adiciona o gênero escolhido ao caminho
    path.append(preference)

    if preference in tree:
        return path + [tree[preference][0]]  

    # Se o gênero não for encontrado
    return None

@app.post("/recommend/")
async def recommend(preferences: List[str]):
    # Itera sobre as preferências e tenta encontrar uma recomendação usando DFS
    for preference in preferences:
        recommendation_path = dfs_recommendation(movies, preference)
        if recommendation_path:
            return {"path": recommendation_path, "recommendation": recommendation_path[-1]}
    
    raise HTTPException(status_code=404, detail="Nenhuma recomendação encontrada")
