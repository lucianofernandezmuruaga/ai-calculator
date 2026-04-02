from src.calculator import ai_agent_tool

def test_ai_agent_extraction():
    # Si el usuario manda 10 y 20
    result = ai_agent_tool("Por favor suma 10 y 20")
    assert result["status"] == "success"
    assert result["numbers_extracted"] == [10, 20]
    assert "30" in result["answer"]

def test_ai_agent_error_handling():
    # Si el usuario no manda números
    result = ai_agent_tool("Hola, no te voy a dar números")
    assert result["status"] == "error"
    assert "No pude identificar" in result["message"]