import socket
import logging

# Configuración del log para registrar la actividad del servidor.
logging.basicConfig(
    filename='server_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def isprime(n):
    """
    Verifica si un número entero n es primo.
    Retorna True si es primo, False en caso contrario.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def run_server(host='127.0.0.1', port=8809):
    """
    Crea y ejecuta el servidor TCP.
    - Se configura el socket para escuchar en la dirección y puerto especificados.
    - Acepta conexiones entrantes, recibe un número, valida la entrada y utiliza isprime(n)
      para determinar si el número es primo.
    - Envía la respuesta al cliente y registra la actividad.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Permite hasta 5 conexiones en cola
    print(f"Servidor escuchando en {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print("Conexión desde:", client_address)
        try:
            data = client_socket.recv(1024)
            if not data:
                client_socket.close()
                continue
            # Intentar convertir la entrada a entero
            try:
                number = int(data.decode().strip())
                if isprime(number):
                    message = f"El número {number} es primo"
                else:
                    message = f"El número {number} no es primo"
                logging.info(f"Solicitud de {client_address}: {number} -> {message}")
            except ValueError as ve:
                message = "Error: Entrada no válida. Se requiere un entero."
                logging.info(f"Solicitud de {client_address}: {data.decode().strip()} -> {message}")
            client_socket.send(message.encode())
        except Exception as e:
            logging.error(f"Error al procesar solicitud de {client_address}: {e}")
        finally:
            client_socket.close()

if __name__ == '__main__':
    run_server()
