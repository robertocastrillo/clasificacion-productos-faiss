"""
Clasificación Automática de Productos usando Embeddings y FAISS
Autor: Roberto Castrillo
Descripción:
Este script aplica procesamiento de lenguaje natural (NLP) para clasificar descripciones
de productos mediante embeddings semánticos y búsqueda vectorial con FAISS.
"""

import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from tqdm import tqdm

archivo_original = "data/por_clasificar.xlsx"
archivo_clasificados = "data/catalogo_clasificados.xlsx"
output_excel = "data/resultados_clasificacion.xlsx"
umbral_similitud = 0.80

df_original = pd.read_excel(archivo_original)
df_clasificados = pd.read_excel(archivo_clasificados)

df_original.columns = df_original.columns.str.strip().str.lower()
df_clasificados.columns = df_clasificados.columns.str.strip().str.lower()

df_original = df_original.drop_duplicates(subset=["codigo_barra"])
df_original["descripcion"] = df_original["descripcion"].astype(str).str.strip()
df_clasificados["descripcion"] = df_clasificados["descripcion"].astype(str).str.strip()

df_original = df_original[df_original["descripcion"].str.contains(r'[a-zA-Z]', na=False)]
df_clasificados = df_clasificados[df_clasificados["descripcion"].str.contains(r'[a-zA-Z]', na=False)]

modelo = SentenceTransformer("paraphrase-MiniLM-L6-v2")

print("🧠 Generando embeddings para el catálogo clasificado...")
embeddings_clasificados = modelo.encode(df_clasificados["descripcion"].tolist(), show_progress_bar=True)

dim = embeddings_clasificados.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(np.array(embeddings_clasificados))

print("🔍 Generando embeddings para los productos por clasificar...")
embeddings_original = modelo.encode(df_original["descripcion"].tolist(), show_progress_bar=True)

print("🔎 Buscando coincidencias más similares...")
D, I = index.search(np.array(embeddings_original), 1)

resultados = []

for i, (distancia, indice_clasificado) in enumerate(zip(D, I)):
    similitud = 1 - distancia[0] / 4
    if similitud >= umbral_similitud:
        fila_original = df_original.iloc[i]
        fila_clasificada = df_clasificados.iloc[indice_clasificado[0]]

        resultados.append({
            "codigo_barra": fila_original["codigo_barra"],
            "descripcion": fila_original["descripcion"],
            "marca": fila_clasificada.get("marca", ""),
            "segmento": fila_clasificada.get("segmento", ""),
            "submarca": fila_clasificada.get("submarca", ""),
            "categoria": fila_clasificada.get("categoria", ""),
            "proveedor": fila_clasificada.get("proveedor", ""),
            "similitud": round(similitud, 4)
        })

df_resultado = pd.DataFrame(resultados)
df_resultado.to_excel(output_excel, index=False)
print(f"✅ Clasificación completada. Resultados guardados en {output_excel}")
