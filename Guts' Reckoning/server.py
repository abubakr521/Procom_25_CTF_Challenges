import socket
import json
import threading

# Updated flag
FLAG = "AxP25{Why_d0_I_S33_th1ng5_..._4ft3r_th3y_4r3_d0n3_4nd_g0n3}"

def get_flash_response(readlen):
    jedec_id = [0xEF, 0x40, 0x18]  # Manufacturer ID, Memory Type, Capacity ID
    flag_bytes = [ord(c) for c in FLAG]  # Convert flag to ASCII values

    # If readlen <= 3, return only the JEDEC ID
    if readlen <= 3:
        return jedec_id[:readlen]

    # Otherwise, return JEDEC ID + flag data
    return jedec_id + flag_bytes[:readlen - 3]

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    try:
        data = conn.recv(1024).decode('utf-8')
        command = json.loads(data)

        readlen = command.get("readlen", 0)
        response_data = get_flash_response(readlen)

        conn.sendall(json.dumps(response_data).encode('utf-8'))
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")

def start_server():
    host = "0.0.0.0"  # Listen on all network interfaces
    port = 5001       # Choose an open port

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)  # Allows up to 5 clients in the queue before rejecting new ones
    print(f"[LISTENING] Server is listening on {host}:{port}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")  # Minus 1 for the main thread

if __name__ == "__main__":
    start_server()

