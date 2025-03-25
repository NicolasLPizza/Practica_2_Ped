import socket

def verificar_primo_remoto(numero, host='127.0.0.1', port=8809):
    """
    Envía 'numero' al servidor TCP que escucha en (host, port) para verificar si es primo.
    Retorna la respuesta como cadena.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            client_socket.send(str(numero).encode())
            respuesta = client_socket.recv(1024).decode()
            return respuesta
    except Exception as e:
        return f"Error en la conexión: {e}"

# Si lo deseas, puedes conservar la función de consola para pruebas:
def iniciar_cliente():
    host = '127.0.0.1'
    port = 8809
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        numero = input("Introduce un número entero: ").strip()
        client_socket.send(numero.encode())
        respuesta = client_socket.recv(1024).decode()
        print("Respuesta del servidor:", respuesta)
    except Exception as e:
        print(f"Error en la conexión: {e}")
    finally:
        client_socket.close()
