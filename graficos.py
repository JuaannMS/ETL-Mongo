import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('profesionales.csv')
df1 = pd.read_csv('salarios.csv')

fig, ax = plt.subplots()


bars = ax.bar(df['tipo_cargo_generalizado'], df['cantidad'], color='skyblue')

for bar in bars:
    yval = bar.get_height()  
    ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom', fontsize=8)

ax.set_xlabel('Tipo de Cargo Generalizado')
ax.set_ylabel('Cantidad')
ax.set_title('Cantidad de Cargos por Tipo Generalizado')


fig, ax = plt.subplots()

# Graficar los datos
ax.bar(df1['_id'], df1['promedio_salario'], color='skyblue')

# Añadir etiquetas y título
ax.set_xlabel('Nivel de Experiencia')
ax.set_ylabel('Promedio de Salario')
ax.set_title('Promedio de Salario por Nivel de Experiencia')

for bar, salario in zip(bars, df1['promedio_salario']):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{salario:.2f}', ha='center', va='bottom')

# Mostrar el gráfico
plt.tight_layout()
plt.show()


# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
