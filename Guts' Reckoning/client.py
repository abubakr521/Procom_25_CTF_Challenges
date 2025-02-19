import socket
import json

def exchange(hex_list, value=3):
    host = '127.0.0.1'  
    port = 5001 

    command_data = {
        "data_out": [hex(x) for x in hex_list],
        "readlen": value
    } 

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(json.dumps(command_data).encode('utf-8'))
        
        data = b''
        while True:
            data += s.recv(1024)
            if data.endswith(b']'):
                break    

        response = json.loads(data.decode('utf-8'))

    return response

jedec_id = exchange([0x9F], 0)
print(jedec_id)