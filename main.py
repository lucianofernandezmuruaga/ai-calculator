import sys
import subprocess

def menu():
    print("\n" + "="*40)
    print("   🧮 CALCULATOR AGENT CLI - MENÚ")
    print("="*40)
    print("1. Calculadora Clásica (Expresiones Regex)")
    print("2. Agente IA - Consulta Rápida (Ejecución única)")
    print("3. Agente IA - Chat Interactivo (Con memoria)")
    print("4. Salir")
    print("="*40)

def run_classic_calculator():
    expr = input("\n[Clásica] Ingresa la expresión matemática (ej: 10 + 15): ")
    if expr.strip():
        subprocess.run([sys.executable, "src/calculator.py", expr])

def main():
    while True:
        menu()
        choice = input("Selecciona una opción (1-4): ").strip()
        
        if choice == "1":
            run_classic_calculator()
        elif choice == "2":
            print("\n[Agente IA] Iniciando prueba de ejecución única...\n")
            subprocess.run([sys.executable, "src/ai_calculator.py"])
        elif choice == "3":
            print("\n[Agente IA] Iniciando modo chat interactivo...\n")
            subprocess.run([sys.executable, "src/ai_calculator.py", "--chat"])
        elif choice == "4":
            print("\n¡Hasta luego! 👋\n")
            break
        else:
            print("\n❌ Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()