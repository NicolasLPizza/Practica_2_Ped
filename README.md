# Practica_2_Ped
Practica 2, TCP y integracion al RumBA 
https://github.com/NicolasLPizza/Practica_2_Ped.git
Este proyecto consiste en la integración de dos módulos principales:

Módulo TCP para comunicación distribuida:

server.py: Un servidor TCP que procesa información (por ejemplo, verifica números primos).

app.py: Un servidor Flask que gestiona el sistema de puntuaciones (recibe puntuaciones y devuelve el ranking).

Juego RoomBA:

Juego_RumbA.py: Un juego desarrollado con Pygame en el que se simula el movimiento de un robot aspirador ("Rumba") en un entorno con zonas, láseres, obstáculos y animaciones.

El juego se integra con el módulo TCP y el servidor Flask para enviar puntuaciones en tiempo real y permitir la verificación de números primos desde la interfaz.

Estructura del Repositorio

Practica_2_Ped/

assets/                  # Carpeta con todos los recursos gráficos (imágenes, sprites, etc.)

__pycache__/             # Archivos compilados de Python

server.py                # Servidor TCP para otras funcionalidades (ejemplo: verificación de números primos)

app.py                   # Servidor Flask para gestionar puntuaciones y ranking

Juego_RumbA.py           # Juego principal RoomBA desarrollado con Pygame

prime_client.py          # Módulo cliente TCP que contiene la función verificar_primo_remoto()

requirements.txt         # Lista de dependencias del proyecto

README.md                # Este archivo: instrucciones y descripción del proyecto

CHANGELOG.md             # (Opcional) Historial de cambios del proyecto
#Requisitos# 
Python 3.8+ (se recomienda usar un entorno virtual)

Dependencias listadas en requirements.txt, que incluye:

pygame

flask

requests

Para instalarlas, puedes usar:

pip install -r requirements.txt
Instrucciones de Ejecución
El proyecto se ejecuta en tres terminales distintas:

Servidor TCP:

Abre una terminal y ejecuta:

python server.py
Esto iniciará el servidor TCP (asegúrate de que esté corriendo en 127.0.0.1:5000 si es que lo requiere el cliente).

Servidor Flask de Puntuaciones:

Abre una segunda terminal y ejecuta:

python app.py
El servidor Flask se levantará en 127.0.0.1:5000 (por defecto) y gestionará las puntuaciones, permitiendo registrar y consultar el ranking.

Juego RoomBA:

Abre una tercera terminal y ejecuta:
python Juego_RumbA.py
Al iniciar el juego, se mostrará el menú principal con las siguientes opciones:

1) Inicio de juego (Manual): En este modo se te pedirá que ingreses tu nombre (a través de la consola) y luego podrás jugar.

2) Modo espectador (Auto): El juego se ejecuta en modo automático y el nombre se asigna automáticamente como "AutoBot".

3) Salir

4) Verificar número primo: Abre una modalidad donde podrás ingresar un número desde la interfaz del juego y se verificará (a través del servidor TCP).

5) Enviar puntuación: Modalidad para enviar una puntuación manualmente al servidor Flask (útil para pruebas).

6) Ver ranking: Modalidad para consultar el ranking almacenado en el servidor Flask.

Cuando el juego termine (por ejemplo, al producirse un Game Over), la puntuación final se enviará automáticamente al servidor Flask y se volverá al menú principal, permitiéndote iniciar otra partida o consultar el ranking.

Funcionamiento Interno
Juego RoomBA:
El juego simula el movimiento de un robot aspirador en un entorno lleno de obstáculos, láseres y tuercas. Utiliza concurrent.futures para acelerar la carga de imágenes y la generación de obstáculos.

Integración TCP y Web:

La función verificar_primo_remoto() del módulo prime_client.py permite conectar con un servidor TCP para verificar números primos.

El servidor Flask (app.py) se encarga de gestionar las puntuaciones enviadas por el juego. Esto permite simular un sistema distribuido donde el juego delega tareas (como el almacenamiento y consulta de puntuaciones) a un servicio web.

Pruebas y Validación
Pruebas Manuales:
Ejecuta cada módulo por separado y verifica su funcionamiento:

Accede a http://127.0.0.1:5000/ranking desde un navegador para ver el ranking.

Usa las opciones del menú en el juego para probar la verificación de números primos y el envío/consulta de puntuaciones.

Casos de Prueba:
Se recomienda probar con entradas válidas e inválidas para asegurarte de que el manejo de errores funciona correctamente (por ejemplo, ingresar cadenas en lugar de números, o puntuaciones que no sean enteros).

Registro de Cambios
Utiliza commits de Git para registrar cada cambio significativo en el proyecto. Puedes incluir un archivo CHANGELOG.md con un resumen de las modificaciones realizadas a lo largo del desarrollo.

Autor
NicolasLPizza
Repositorio en GitHub
