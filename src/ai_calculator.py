import sys
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.chat_history import InMemoryChatMessageHistory

# 1. Cargar variables del archivo .env
load_dotenv()

# 2. Inicializar el modelo con LangChain
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0
)

# 3. Definir las instrucciones del sistema (System Prompt)
SYSTEM_PROMPT = """
Sos un Agente Calculadora especializado. 
Tu trabajo es interpretar los pedidos matemáticos del usuario y resolver los cálculos de forma clara y precisa.

Reglas de salida:
1. Si el usuario te pide un cálculo (ej: "sumá 45 y 15" o "tengo diez manzanas y me regalan quince"), identificá la operación y devolvé la respuesta expresando los números SIEMPRE en formato de dígitos (ej: "10 + 15 = 25" o "El total es 25").
2. Si el texto del usuario no contiene ningún pedido matemático ni números para operar, indicá de forma amable que solo podés resolver operaciones matemáticas.
3. Sé conciso y directo al responder.
"""

def run_ai_agent_with_history(history: InMemoryChatMessageHistory, new_user_input: str):
    """
    Ejecuta el agente manteniendo el historial completo de la sesión.
    """
    # 1. Agregamos el nuevo mensaje del usuario al historial
    history.add_user_message(new_user_input)
    
    # 2. Preparamos el paquete completo: System Prompt + Todo el historial acumulado
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + history.messages
    
    # 3. Invocamos al LLM con la conversación completa
    response = llm.invoke(messages)
    
    # 4. Guardamos la respuesta de la IA en el historial para la próxima vuelta
    history.add_ai_message(response.content)
    
    return response.content

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--chat":
        print("🤖 --- AGENTE CALCULADORA CON MEMORIA (Modo Chat) ---")
        print("Escribí tu consulta o 'salir' para terminar.\n")
        
        # Crearmos el objeto de memoria local para esta sesión
        session_history = InMemoryChatMessageHistory()
        
        while True:
            user_input = input("Vos: ")
            if user_input.lower().strip() in ["salir", "exit", "quit"]:
                print("¡Nos vemos!")
                break
            
            if not user_input.strip():
                continue
                
            respuesta = run_ai_agent_with_history(session_history, user_input)
            print(f"IA: {respuesta}\n")
    else:
        print("--- Agente Calculadora (Modo Prueba) ---")
        # Prueba directa sin memoria
        temp_history = InMemoryChatMessageHistory()
        prueba = "Tengo diez peras y regalo siete a mi amigo, ¿cuántas tengo en total?"
        print(f"\nConsulta: {prueba}")
        print(f"Respuesta:\n{run_ai_agent_with_history(temp_history, prueba)}")