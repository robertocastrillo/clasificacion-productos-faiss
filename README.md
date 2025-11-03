# Clasificación Automática de Productos usando Embeddings y FAISS

Este proyecto presenta una solución profesional para la **clasificación automatizada de productos** mediante técnicas de **Procesamiento de Lenguaje Natural (NLP)** y **búsqueda vectorial con FAISS**, optimizando el tiempo de análisis manual y mejorando la consistencia en bases de datos comerciales.

## Objetivo
Desarrollar un sistema que clasifique descripciones de productos basadas en similitud semántica, utilizando un catálogo previamente clasificado como referencia.

## Tecnologías utilizadas
- Python
- pandas
- SentenceTransformer (MiniLM-L6-v2)
- FAISS
- NumPy
- tqdm
- Excel (openpyxl)

## Estructura del proyecto
```
clasificacion-productos-faiss/
├── main.py
├── utils/
│   ├── limpieza.py
│   └── embeddings.py
├── data/
│   ├── por_clasificar.xlsx
│   ├── catalogo_clasificados.xlsx
│   └── resultados_clasificacion.xlsx
├── requirements.txt
└── README.md
```

## Ejecución
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/robertocastrillo/clasificacion-productos-faiss.git
   cd clasificacion-productos-faiss
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Agregar los archivos Excel en la carpeta `/data/`:
   - `por_clasificar.xlsx` → productos sin clasificar
   - `catalogo_clasificados.xlsx` → catálogo base

4. Ejecutar el script principal:
   ```bash
   python main.py
   ```

## Resultados esperados
- Coincidencias automáticas con similitud ≥ 0.80
- Clasificación de marca, subcategoría y proveedor
- Reducción significativa del tiempo de análisis manual

## Licencia
Proyecto de carácter académico y demostrativo. No incluye datos reales ni confidenciales.
