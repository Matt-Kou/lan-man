import socket
import pickle


def register():
    HOST = ""
    PORT = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # AF_INET: IPv4, SOCK_STREAM: TCP
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()  # blocks
        with conn:
            print(f"Connection established with {addr}")
            data = conn.recv(4096)
            if not data:
                raise Exception("connection closed by client.")
            data_type, content = pickle.loads(data)  # content is left empty for future usage
            if data_type != "registration_req":
                raise Exception("must be a registration request.")
            reg_ack = ("registration_ack", {"Hostname": socket.gethostname()})
            conn.sendall(pickle.dumps(reg_ack))
            print("Sent registration acknowledgement.")

def connect():
    HOST = ""
    PORT = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # AF_INET: IPv4, SOCK_STREAM: TCP
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()  # blocks
        with conn:
            print(f"Connection established with {addr}")
            while data := conn.recv(4096):
                data_type, content = pickle.loads(data)
                match data_type:
                    case "connection_test":
                        continue
                    # case
