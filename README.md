CyberReport CLI: Agente para reportes y consultas de seguridad

Un agente inteligente que:

* Recibe reportes de posibles incidentes de seguridad.

* esponde preguntas sobre ciberseguridad.

* Guarda cada reporte con fecha, usuario, descripción e ID.

* Permite consultar el historial de incidentes registrados.

Todo funciona desde la terminal, guardando y consultando los datos desde una base de datos local SQLite. No necesita internet.

## Technologias que se usaron:

python - lenguaje principal
ollama + llama3 - llm local responde las preguntas
SQlite - es una base datos local integrada con python
Langchain - para conectar el llm con los prompts
dotenv - configuracion privada para el nombre del modelo a usar

----------------------------------------------------------------------

## Iniciamos creado el directorio raiz con sus respectivas carpetas

cyberreport_cli/
│
├── agent.py           # Agente LLM con prompt especializado
├── db.py              # Manejo de base de datos SQLite
├── main.py            # Punto de entrada, menú por terminal
├── .env               # Configuración del modelo
├── requirements.txt   # Lista de librerías necesarias
├── README.md          # Guía técnica y explicación detallada
├── check_db.py        # funcion que visaliza las interacciones
├── export_db_to_cvs.py #exporta base de datos en formato .cvs
└── consultas_export_20250720_175230.cvs #Archivo exportado por la funcion

## Requisitos
- Tener Python 3.10 o superior
- Tener instalado `ollama` y haber hecho pull del modelo: `ollama pull llama3`

## Instalación

python -m venv venv
venv\Scripts\activate       # En PowerShell o terminal VS Code
pip install -r requirements.txt


## Uso

bash
ollama run llama3            # En una terminal separada
python main.py               # Para iniciar el agente
