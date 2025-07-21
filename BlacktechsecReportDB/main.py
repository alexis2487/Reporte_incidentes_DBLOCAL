from agent import create_agent
from database import init_db, save_query

def main():
    print("\n🤖 Bienvenido a BlackTechSec CLI Agent con soporte de base de datos.")
    print("Escribe tu pregunta o comando (o 'salir' para terminar):")

    # Inicializar la base de datos al ejecutar
    init_db()

    # Crear el agente de lenguaje
    agent = create_agent()

    while True:
        user_input = input("> ")
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("Hasta luego. 👋")
            break

        # Ejecutar el agente con la entrada del usuario
        try:
            response = agent.invoke({"input": user_input})
            print("\nRespuesta del agente:\n", response.content)

            # Guardar la consulta y respuesta en la base de datos
            save_query(user_input, response.content)

        except Exception as e:
            print(f"\n❌ Error procesando tu solicitud: {e}")


if __name__ == "__main__":
    main()