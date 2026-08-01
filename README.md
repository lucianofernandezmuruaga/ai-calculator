🧮 Calculator Agent CLI
Un proyecto en Python que combina una calculadora determinista basada en expresiones regulares con un agente conversacional inteligente potenciado por LangChain y Llama 3 (vía Groq).

🚀 Requisitos Previos
Python 3.10 o superior.

Una API Key gratuita de Groq Cloud.

🛠️ Configuración del Entorno
Clonar el repositorio e instalar dependencias:
```bash
pip install -r requirements.txt
```

Configurar variables de entorno:
Crea un archivo .env en la raíz del proyecto basándote en .env.example:
```env
GROQ_API_KEY=tu_api_key_aqui
```

💻 Modos de Uso
El proyecto cuenta con dos motores de cálculo independientes:

1. Calculadora Clásica (Determinista / Regex)
Procesa operaciones matemáticas básicas leyendo argumentos por línea de comandos o mediante evaluación rápida:

```bash
python src/calculator.py "10 + 15"
```

2. Agente Calculadora con IA (LangChain + Groq)
Un agente conversacional impulsado por llama-3.1-8b-instant capaz de interpretar problemas expresados en lenguaje natural, mantener memoria de la sesión y filtrar consultas ajenas a la matemática.

Modo Prueba de Ejecución Única:
```bash
python src/ai_calculator.py
```

Modo Chat Interactivo (con Memoria de Sesión):
```bash
python src/ai_calculator.py --chat
```

🛠️ Tecnologías Utilizadas
Python 3

LangChain Core & LangChain Groq (Orquestación de LLM e historial de chat)

Llama 3.1 8B Instant (Modelo de Lenguaje en la Nube vía Groq)

python-dotenv (Gestión de variables de entorno)

pytest (Testing unitario)