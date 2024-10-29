# ------------------------
# Script para automatizar tareas de configuración y ejecución en PowerShell
# ------------------------

# 1. Activar el entorno virtual
Write-Host "Activando el entorno virtual..."
# Asegúrate de que la ruta sea correcta para tu entorno virtual
& .\env\Scripts\Activate

# 2. Instalar dependencias necesarias desde requirements.txt
Write-Host "Instalando dependencias..."
pip install -r requirements.txt

# 3. Ejecutar la aplicación con parámetros predeterminados
# Asegúrate de reemplazar 'weather.py' con el nombre de tu archivo de aplicación principal
Write-Host "Ejecutando la aplicación..."
python weather.py "Asuncion, Paraguay" --unidad "metric"

# 4. Ejecutar pruebas automatizadas
# Asegúrate de tener pruebas definidas, por ejemplo, en una carpeta llamada 'tests'
Write-Host "Ejecutando pruebas automatizadas..."
pytest tests/

# 5. Desactivar el entorno virtual
Write-Host "Desactivando el entorno virtual..."
deactivate

Write-Host "Script ejecutado con éxito."

# Fin del script
