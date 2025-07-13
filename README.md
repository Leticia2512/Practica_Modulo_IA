# Asistente Inteligente para Consultas Farmacológicas

*Práctica Módulo de IA · Bootcamp Big Data, Machine Learning & IA – Keepcoding*

---

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un asistente inteligente capaz de responder preguntas específicas sobre medicamentos, utilizando como fuente las fichas técnicas oficiales extraídas de la **Agencia Española de Medicamentos y Productos Sanitarios (AEMPS)**.

El sistema combina técnicas de procesamiento del lenguaje natural como **embeddings semánticos**, **búsqueda vectorial (FAISS)** y **modelos de lenguaje (LLM)** para recuperar información precisa y formular respuestas contextualizadas.

---

## Objetivos

- Convertir fichas técnicas de medicamentos en PDF a texto plano. 
- Dividir y vectorizar los documentos usando embeddings y almacenarlos en un índice semántico con FAISS.
- Permitir consultas en lenguaje natural y devolver respuestas basadas exclusivamente en los textos recuperados (*Retrieval-Augmented Generation, RAG*).

---

## Tecnologías principales
| Herramienta | Uso |
|-------------|-----|
| **LangChain** | Orquestar carga de datos, chunking, embeddings y consulta RAG |
| **OpenAI API** | Generar embeddings y respuestas con `ChatOpenAI` |
| **FAISS (CPU)** | Índice vectorial para búsquedas semánticas |
| **PyMuPDF (fitz)** | Extracción de texto desde PDFs |
| Python 3.10+ | Entorno de ejecución |

---

## Estructura del proyecto

| Ruta / archivo               | Descripción                                                                                        |
|------------------------------|----------------------------------------------------------------------------------------------------|
| `AI_drug_assistant.ipynb`    | Notebook con todo el flujo: preparación de datos, construcción del índice y consultas RAG.        |
| `utils.py`                   | Funciones auxiliares (ej. conversión de PDF a TXT).                                               |
| `data/`                      | PDFs originales y `.txt` generados.                                                               |
| `requirements.txt`           | Dependencias del proyecto.       

---


