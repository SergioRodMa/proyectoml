# **Scorecard de polizas y deteccion de fraude** 💸

## Contexto 

Una aseguradora ha recopilado información categórica sobre sus clientes y pólizas. Cada fila representa un caso individual, y FraudFound_P indica si el caso fue fraudulento (fraude = 1) o no (fraude = 0). El evento de fraude es de baja frecuencia.

## Objetivo 💢

Diseñar un pipeline completo de procesamiento y modelado de datos que permita detectar posibles fraudes, utilizando técnicas tradicionales de modelado y disponibilizando el modelo final como un servicio de scoring.

## Creacion del ambiente
Para crear el ambiente es necesario utilizar el archivo requeriments.txt junto con la siguiente isntruccion.
```
    virtualenv .venv  # Crea un entorno llamado .venv
    pip install -r requirements.txt
```
Creado por Sergio Maldonado Rodriguez

## 🔗 Link importantes 
1. [Link de la data del proyecto](data/fraud_train.csv)
2. [Notebook del proyecto con el procedimiento detallado](EDA_y_Pipeline.ipynb)
2. [PDF presentación del proyecto y resultados](Presentacion_Modelo_Scorecard.pdf)
4. [Link al API y su documentacion](backend)