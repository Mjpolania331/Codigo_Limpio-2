import pandas as pd
import ace_tools as tools

# Estructura para los tipos de pruebas por funcionalidad
funcionalidades = [
"Crear nota", "Editar nota", "Eliminar nota",
"Iniciar sesión", "Crear cuenta", "Cambiar contraseña"
]

tipos = ["Normal", "Error", "Extremo"]
casos = []

for funcionalidad in funcionalidades:
    for tipo in tipos:
        for i in range(1, 4):
            casos.append({
                "Funcionalidad": funcionalidad,
                "Tipo de Prueba": tipo,
                "Caso": f"{funcionalidad} - {tipo.lower()} {i}",
                "Resultado Esperado": "Pasa"
            })

df = pd.DataFrame(casos)
tools.display_dataframe_to_user(name="Resumen de Casos de Prueba", dataframe=df)
