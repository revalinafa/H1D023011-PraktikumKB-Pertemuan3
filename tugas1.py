import random
import time

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    percobaan = 0
    riwayat_tebakan = []
    
    print("\n===== Game Tebak Angka =====")
    print("Saya telah memilih angka antara 1 hingga 100. Coba tebak!")
    
    while True:
        try:
            tebakan = int(input("Masukkan tebakanmu: "))
            riwayat_tebakan.append(tebakan)
            percobaan += 1
            
            if tebakan < angka_rahasia:
                print("Terlalu kecil! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu besar! Coba lagi.")
            else:
                print(f"Selamat! Kamu berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan.")
                print("Riwayat tebakanmu:", riwayat_tebakan)
                break
            
            time.sleep(0.5)  
        except ValueError:
            print("Masukkan angka yang valid!")

def main():
    while True:
        print("\n===== Menu =====")
        print("1. Main Tebak Angka")
        print("2. Keluar")
        
        choice = input("Pilih menu (1-2): ")
        
        if choice == "1":
            tebak_angka()
        elif choice == "2":
            print("Terima kasih telah bermain!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
