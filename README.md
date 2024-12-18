Práctica de Git - Tono Mollá González

Estructura del repositorio:
- main: versión estable del código
- feature/scientific-functions: implementación de funciones científicas
- feature/optimization: optimizaciones y corrección del bug
- bugfix/multiply-negative: corrección específica del bug en multiplicación

Pasos realizados:
1. Creación del proyecto de calculadora
2. Configuración de aliases de git
3. Creación y gestión de múltiples ramas
4. Uso de git bisect para encontrar un bug en la función multiply
5. Configuración de hook pre-commit para verificar sintaxis Python
6. Integración con repositorio remoto en GitHub

Comandos importantes utilizados:
- git bisect: para encontrar el commit que introdujo el bug
- git hook: configurado pre-commit para verificación de código
- git remote: para conectar con GitHub
- git push: para subir todas las ramas al remoto
