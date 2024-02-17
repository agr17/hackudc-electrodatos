```markdown
# Uso de Electrodatos

Electrodatos es una aplicación que te permite visualizar y analizar tus facturas eléctricas de una manera fácil y eficiente. Sigue estos pasos para comenzar:

## Instalación

1. Clona el repositorio desde GitHub:

```
git clone https://github.com/agr17/hackudc-electrodatos
```

2. Navega al directorio del proyecto:

```
cd hackudc-electrodatos
```

3. Instala las dependencias necesarias:

```
pip install -r requirements.txt
```

## Ejecución

1. Una vez que hayas instalado las dependencias, puedes ejecutar la aplicación Bokeh para visualizar tus datos eléctricos:

```
bokeh serve bokeh-vis --show --args .\data\cups\electrodatos_0.csv 2022
```

2. Sigue las instrucciones en la aplicación para interactuar con los gráficos y métricas de consumo y gasto anual.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir al desarrollo de Electrodatos, consulta el apartado Development del readme

¡Gracias por usar Electrodatos!

```