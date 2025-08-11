# Backend del scorecard 💰
Este es la carpeta que tiene el proceso de despligue del Backend de la aplicacion 
esta se monto sobre GCP en App Engine mediante los siguientes pasos:

Previo a estos pasos se debe tener la carpeta de la aplicacion aislada con su propio ambiente, para esto vamos a generar un archivo llamado **requirements.txt** donde almacenaremos los paquetes necesarios para la aplicacion. Adicionalmente necesitaremos un archivo con el runtime para el inicio de esta. 

Este archivo sera nombrado como **app** y tendra una estructura como la siguiente:
```
runtime: python39
entrypoint: uvicorn main:app --host 0.0.0.0 --port 8080
```
Posteriormente a tener todos los archivos y dependencias necesaerias para la aplicacion seguiremos los siguientes pasos:

1. Instalar el SDK de Google Cloud de este [enlance](https://cloud.google.com/sdk/docs/how-to)
2. Correr ```gcloud init``` en la terminal para logearte con tu cuenta
3. Configurar el Nombre del proyecto y carpeta  ```gcloud config set project [project_id]```
4. Finalmente seleccionar la aplicacion que queremos desplegar
```gcloud app deploy```

La direccion de nuestra API es la siguiente 
**https://fastapimlcf.ue.r.appspot.com/info**


Si se quiere probar en un ambiente local basta con clonar la carpeta y correr lo siguiente:
```
uvicorn main:app --reload
```

## Intrucciones de uso

La API esta conformada de un endpoint llamado score el cual por medio de una peticion post se le debe enviar en forma unica los datos para realizar la prediccion.


Estos son las siguientes variables con los valores posibles a enviar:

- 'Fault'-> 'Policy Holder', 'Third Party',
- 'PolicyType'-> 'Sedan - All Perils', 'Sedan - Collision','Sport - Liability','Sport - Collision','Utility - All Perils','Utility - Collision','Utility - Liability','Sport - All Perils'
- 'VehicleCategory' -> 'Sedan', 'Sport' 'Utility'
- 'Month' -> 'Aug', 'Dec', 'Feb', 'Jun', 'Jan', 'Nov', 'Jul', 'May', 'Oct', 'Sep', 'Mar', 'Apr'
- 'VehiclePrice' -> '30000 to 39000', '20000 to 29000', 'less than 20000', 'more than 69000', '40000 to 59000'm '60000 to 69000'
- 'Make' -> 'Honda','Chevrolet', 'Pontiac', 'Toyota', 'Mazda', 'Ford', 'Accura', 'Mercury','VW', 'Saturn', 'Dodge', 'Saab', 'BMW', 'Nisson', 'Porche','Ferrari','Jaguar','Mecedes'
- 'DayOfWeek' -> 'Friday', 'Tuesday', 'Sunday', 'Monday', 'Thursday', 'Wednesday', 'Saturday'
- 'AgeOfVehicle' -> '7 years', '5 years', '6 years', '3 years', 'more than 7', 'new', '2 years', '4 years'
- 'Deductible' -> 400, 500, 700, 300
- 'Sex' -> 'Male', 'Female'
- 'AccidentArea' -> 'Urban', 'Rural'
- 'AgentType' -> 'External', 'Internal'
- 'WeekOfMonthClaimed' -> 5, 3, 4, 2, 1

Como ejemplo al utilizar los siguientes valores 
```
# request.py
import requests

url = "http://127.0.0.1:8000/score"
payload = {
 'Fault':'Policy Holder',
 'PolicyType':'Sedan - All Perils',
 'VehicleCategory':'Sedan',
 'Month':'May',
 'VehiclePrice':'20000 to 29000',
 'Make':'BMW',
 'DayOfWeek':'Monday',
 'AgeOfVehicle':'6 years',
 'Deductible':'500',
 'Sex':'Female',
 'AccidentArea':'Urban',
 'AgentType':'External',
 'WeekOfMonthClaimed':'3'
    
}
response = requests.post(url, json=payload)

print(response.json())
```

Obteniendo la siguiente respuesta del 

```
{'fraud_probability': 0.7147, 'score': 338}
```