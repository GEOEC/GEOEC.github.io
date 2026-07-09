"""
Punto de entrada WSGI para servidores de producción (gunicorn).

Uso:
    gunicorn wsgi:app
"""
import os
import sys

# En producción: si la base de datos no existe, la crea con datos demo
_db_path = os.path.join(os.path.dirname(__file__), "cyberrisk360.db")
if not os.path.exists(_db_path):
    print("⚙️  Base de datos no encontrada. Ejecutando seed...")
    from seed import seed
    seed()
    print("✅ Base de datos inicializada con datos de demostración.")

from app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
