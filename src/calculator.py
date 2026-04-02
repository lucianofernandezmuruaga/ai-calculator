import re

def add_numbers(a, b):
    """Esta es la función técnica que ejecuta la acción."""
    return a + b

def ai_agent_tool(user_message):
    """
    Simula la 'Capa de Inteligencia' (LLM). 
    Interpreta el lenguaje natural y decide qué parámetros enviar a la función.
    """
    print(f" Agente procesando mensaje: '{user_message}'")
    
    # Simulación de extracción de entidades (lo que haría un LLM)
    numbers = [int(n) for n in re.findall(r'\d+', user_message)]
    
    if len(numbers) == 2:
        res = add_numbers(numbers[0], numbers[1])
        return {
            "status": "success",
            "numbers_extracted": numbers,
            "answer": f"Interpreté tu pedido. La suma de {numbers[0]} y {numbers[1]} es {res}."
        }
    
    return {
        "status": "error",
        "message": "No pude identificar dos números claros en tu mensaje. ¿Podrías ser más específico?"
    }

if __name__ == "__main__":
    # Caso de éxito
    print(ai_agent_tool("Hola! Por favor sumá 120 y 80"))
    print("-" * 30)
    # Caso de error
    print(ai_agent_tool("Hola, quiero sumar pero no te digo qué números"))