import matplotlib.pyplot as plt
import os

# Crear carpeta para almacenar gráficos
output_dir = "graficos_mentoria"
os.makedirs(output_dir, exist_ok=True)

# Proyección de Atención y Análisis de Viabilidad

# 1. Capacidad de Atención con Recursos Actuales
mentores = 9
horas_por_dia = 8
dias_laborables = 22

# Capacidad de atención
usuarios_individual = 4  # 2 horas por usuario
usuarios_grupal = 40  # 10 usuarios por sesión de 2 horas

# Cálculo mensual de atenciones
atenciones_individual = mentores * usuarios_individual * dias_laborables
atenciones_grupal = mentores * usuarios_grupal * dias_laborables

# Meta mensual
meta_min = 1260
meta_max = 2709

# 2. Viabilidad de Migrar a Mentoría Individual
usuarios_anuales = 24300
horas_requeridas = usuarios_anuales * 2
horas_disponibles = mentores * horas_por_dia * dias_laborables * 12
cobertura = horas_disponibles / horas_requeridas * 100

# 3. Necesidad de Mentores Adicionales
horas_faltantes = horas_requeridas - horas_disponibles
horas_contratista_anual = horas_por_dia * dias_laborables * 12
mentores_necesarios = horas_faltantes / horas_contratista_anual

# Costo de contratistas
salario_diario = 424921
costo_anual_por_mentor = salario_diario * dias_laborables * 12
costo_total = mentores_necesarios * costo_anual_por_mentor
presupuesto_disponible = 1.9e9  # 1.9 mil millones
viabilidad = costo_total <= presupuesto_disponible

# 4. Estrategias para Optimizar Recursos
porcentaje_grupal = 0.6
personas_grupal = int(usuarios_anuales * porcentaje_grupal)
sesiones_grupales = personas_grupal / 10
costo_sesion_grupal = 81100
costo_total_grupal = sesiones_grupales * costo_sesion_grupal

personas_individual = usuarios_anuales - personas_grupal
costo_atencion_individual = 140000
costo_total_individual = personas_individual * costo_atencion_individual

costo_total_mixto = costo_total_grupal + costo_total_individual
ahorro = presupuesto_disponible - costo_total_mixto


#resultados
# Resultados
print("Capacidad Mensual:")
print(f"Mentoría individual: {atenciones_individual} atenciones/mes")
print(f"Mentoría grupal: {atenciones_grupal} atenciones/mes")
print(f"Meta mensual: {meta_min} - {meta_max} personas")
print("\nViabilidad de Mentoría Individual:")
print(f"Cobertura: {cobertura:.2f}%")
print("\nMentores Adicionales Necesarios:")
print(f"Mentores requeridos: {mentores_necesarios:.0f}")
print(f"Costo total: ${costo_total:,.0f}")
print(f"Viabilidad: {'Sí' if viabilidad else 'No'}")
print("\nEstrategia Mixta:")
print(f"Personas en mentoría grupal: {personas_grupal}")
print(f"Costo mentoría grupal: ${costo_total_grupal:,.0f}")
print(f"Personas en mentoría individual: {personas_individual}")
print(f"Costo mentoría individual: ${costo_total_individual:,.0f}")
print(f"Costo total mixto: ${costo_total_mixto:,.0f}")
print(f"Ahorro: ${ahorro:,.0f}")

# Función para guardar gráficos
def guardar_grafico(fig, nombre):
    ruta = os.path.join(output_dir, nombre)
    fig.savefig(ruta, bbox_inches='tight')

# Capacidad de atención mensual
fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.bar(["Mentoría Individual", "Mentoría Grupal"], [atenciones_individual, atenciones_grupal], color=['blue', 'green'])
ax.set_title("Capacidad de Atención Mensual")
ax.set_ylabel("Número de Atenciones")

# Agregar etiquetas en las barras
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2, altura, f'{altura:,}', ha='center', va='bottom')

guardar_grafico(fig, "grafico_capacidad_atencion.png")
plt.close(fig)


# Cobertura de mentoría individual
fig, ax = plt.subplots(figsize=(8, 5))
ax.pie([horas_disponibles, horas_faltantes], labels=["Cobertura Actual", "Falta por Cubrir"], autopct='%1.1f%%', colors=['blue', 'red'])
ax.set_title("Cobertura de Mentoría Individual")
guardar_grafico(fig, "grafico_cobertura_mentoria.png")
plt.close(fig)

# Comparación de costos de mentoría
fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.bar(["Mentoría Individual", "Mentoría Grupal"], [costo_total_individual, costo_total_grupal], color=['red', 'green'])
ax.set_title("Comparación de Costos de Mentoría")
ax.set_ylabel("Costo en millones de $")

# Agregar etiquetas en las barras
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2, altura, f'${altura/1e6:,.1f}M', ha='center', va='bottom')

guardar_grafico(fig, "grafico_comparacion_costos.png")
plt.close(fig)

# Distribución de mentoría (mixto)
fig, ax = plt.subplots(figsize=(8, 5))
ax.pie([personas_individual, personas_grupal], labels=["Mentoría Individual", "Mentoría Grupal"], autopct='%1.1f%%', colors=['red', 'green'])
ax.set_title("Distribución de Mentoría Mixta")
guardar_grafico(fig, "grafico_distribucion_mentoria.png")
plt.close(fig)

# Ahorro logrado con mentoría mixta
fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.bar(["Presupuesto Disponible", "Costo Total Mixto"], [presupuesto_disponible, costo_total_mixto], color=['blue', 'orange'])
ax.set_title("Ahorro con Estrategia Mixta")
ax.set_ylabel("Costo en millones de $")

# Agregar etiquetas en las barras
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2, altura, f'${altura/1e6:,.1f}M', ha='center', va='bottom')

guardar_grafico(fig, "grafico_ahorro_mixto.png")
plt.close(fig)


# Crear carpeta para almacenar gráficos
output_dir = "graficos_mentoria"
os.makedirs(output_dir, exist_ok=True)

# Datos de capacidad de atención
mentoria_individual = 792
mentoria_grupal = 7920
meta_min = 1260
meta_max = 2709

# Función para crear tarjetas
def crear_tarjeta(valor, titulo, nombre_archivo, color):
    fig, ax = plt.subplots(figsize=(4, 2))
    ax.set_facecolor(color)
    ax.text(0.5, 0.6, f"{valor:,}", fontsize=18, fontweight="bold", ha="center", color="white")
    ax.text(0.5, 0.2, titulo, fontsize=12, ha="center", color="white")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    
    # Guardar tarjeta
    ruta = os.path.join(output_dir, nombre_archivo)
    fig.savefig(ruta, bbox_inches="tight", facecolor=color)
    plt.close(fig)

# Crear tarjetas
crear_tarjeta(mentoria_individual, "Mentoría Individual\n(atenciones/mes)", "tarjeta_mentoria_individual.png", "blue")
crear_tarjeta(mentoria_grupal, "Mentoría Grupal\n(atenciones/mes)", "tarjeta_mentoria_grupal.png", "green")

print("Tarjetas guardadas en la carpeta 'graficos_mentoria'")
print("Gráficos guardados en la carpeta 'graficos_mentoria'")

# Gráfico: Cantidad de Mentores Necesarios
fig, ax = plt.subplots(figsize=(6, 4))
barra = ax.bar(["Mentores Actuales", "Mentores Necesarios"], [9, mentores_necesarios], color=['blue', 'red'])
ax.set_title("Cantidad de Mentores Necesarios")
ax.set_ylabel("Número de Mentores")

# Etiquetas en las barras
for b in barra:
    altura = b.get_height()
    ax.text(b.get_x() + b.get_width()/2, altura, f'{int(altura)}', ha='center', va='bottom')

guardar_grafico(fig, "grafico_mentores_necesarios.png")
plt.close(fig)

# Gráfico: Comparación de Costo Total vs. Presupuesto
fig, ax = plt.subplots(figsize=(6, 4))
barras = ax.bar(["Presupuesto Disponible", "Costo Total Necesario"], [presupuesto_disponible, costo_total], color=['green', 'red'])
ax.set_title("Costo de Mentores Adicionales")
ax.set_ylabel("Costo en millones de $")

# Etiquetas en las barras
for b in barras:
    altura = b.get_height()
    ax.text(b.get_x() + b.get_width()/2, altura, f'${altura/1e6:,.1f}M', ha='center', va='bottom')

guardar_grafico(fig, "grafico_costo_vs_presupuesto.png")
plt.close(fig)

# Gráfico: Viabilidad de Contratación
fig, ax = plt.subplots(figsize=(6, 4))

# Definir colores correctamente
colores = ["red", "green"] if not viabilidad else ["green", "lightgreen"]

ax.pie(
    [costo_total, presupuesto_disponible - costo_total], 
    labels=["Costo Total", "Presupuesto Restante"], 
    autopct='%1.1f%%', 
    colors=colores
)
ax.set_title("Viabilidad de Contratación")

guardar_grafico(fig, "grafico_viabilidad_contratacion.png")
plt.close(fig)

print("Gráficos de necesidad de mentores adicionales guardados en 'graficos_mentoria'")

# Crear carpeta para almacenar tarjetas
output_dir = "graficos_mentoria"
os.makedirs(output_dir, exist_ok=True)

# Datos
horas_faltantes = horas_requeridas - horas_disponibles
horas_contratista_anual = horas_por_dia * dias_laborables * 12
mentores_necesarios = horas_faltantes / horas_contratista_anual

salario_diario = 424921
costo_anual_por_mentor = salario_diario * dias_laborables * 12
costo_total = mentores_necesarios * costo_anual_por_mentor
presupuesto_disponible = 1.9e9
viabilidad = "Sí" if costo_total <= presupuesto_disponible else "No"

# Formatear valores como texto
horas_faltantes_str = f"{horas_faltantes:,.0f}"
mentores_necesarios_str = f"{mentores_necesarios:.0f}"
costo_total_str = f"${costo_total:,.0f}"

# Función para crear tarjetas
def crear_tarjeta(valor, titulo, nombre_archivo, color):
    fig, ax = plt.subplots(figsize=(4, 2))
    ax.set_facecolor(color)
    ax.text(0.5, 0.6, valor, fontsize=18, fontweight="bold", ha="center", color="white")  # Aquí eliminamos el formato adicional
    ax.text(0.5, 0.2, titulo, fontsize=12, ha="center", color="white")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    
    # Guardar tarjeta
    ruta = os.path.join(output_dir, nombre_archivo)
    fig.savefig(ruta, bbox_inches="tight", facecolor=color)
    plt.close(fig)

# Crear tarjetas
crear_tarjeta(horas_faltantes_str, "Horas Faltantes", "tarjeta_horas_faltantes.png", "red")
crear_tarjeta(mentores_necesarios_str, "Mentores Necesarios", "tarjeta_mentores_necesarios.png", "blue")
crear_tarjeta(costo_total_str, "Costo Total de Mentores", "tarjeta_costo_total.png", "purple")
crear_tarjeta(viabilidad, "Viabilidad", "tarjeta_viabilidad.png", "green" if viabilidad == "Sí" else "red")

print("Tarjetas guardadas en la carpeta 'graficos_mentoria'")