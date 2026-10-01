import socket
from des_algo import enkripsi_teks

secretkey = "INIKUNCI"

host = '127.0.0.1'
port = 5000

print("-------------------")
print("SENDER PROGRAM")
print("-------------------")

plaintext = input("Masukkan pesan : ")

ciphertext = enkripsi_teks(plaintext, secretkey)

print(f"\nProses Enkripsi Selesai!")
print(f"Ciphertext yang akan dikirim: {repr(ciphertext)}")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((host, port))
    print("\nBerhasil terhubung ke Receiver.")
    
    client_socket.send(ciphertext.encode('latin-1'))
    print("Pesan ciphertext berhasil dikirim!")
    
except Exception as e:
    print(f"\nGagal terhubung! Error: {e}")
    print("Pastikan receiver.py sudah dijalankan lebih dulu.")

client_socket.close()
