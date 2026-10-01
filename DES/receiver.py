import socket
from des_algo import dekripsi_teks

secretkey = "INIKUNCI"

host = '127.0.0.1'
port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print("-------------------")
print(f"Receiver berjalan di {host}:{port}")
print("Menunggu ada pengiriman dari Sender...")
print("-------------------")

conn, alamat = server_socket.accept()
print(f"Terhubung dengan sender dari alamat : {alamat}")

# ciphertext
data = conn.recv(1024)
ciphertext = data.decode('latin-1')

print("\n+++ PESAN MASUK +++")
print(f"Ciphertext : {repr(ciphertext)}")

plaintext = dekripsi_teks(ciphertext, secretkey)
print(f"Plaintext  : {plaintext}")

conn.close()
server_socket.close()
print("\nKoneksi diputus. Program selesai.")
