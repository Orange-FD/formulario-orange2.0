#!/bin/bash

echo "🚀 Iniciando aplicación Flask Orange..."
echo "📁 Activando entorno virtual..."

# Activar el entorno virtual
source venv/bin/activate

echo "✅ Entorno virtual activado"
echo "🌐 Ejecutando aplicación en http://localhost:5000"
echo "⏹️  Presiona Ctrl+C para detener la aplicación"
echo ""

# Ejecutar la aplicación
python3 app.py