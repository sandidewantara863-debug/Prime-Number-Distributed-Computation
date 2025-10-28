import sympy
import time

def cek_prima_sympy(n):
    """Mengecek bilangan prima menggunakan sympy"""
    return sympy.isprime(n)

def generate_primes_sympy(count):
    """Menghasilkan deret bilangan prima menggunakan sympy"""
    return list(sympy.primerange(1, sympy.prime(count) + 1))

def main_sympy():
    while True:
        print("\n" + "="*50)
        print("PROGRAM BILANGAN PRIMA (Menggunakan SymPy)")
        print("="*50)
        print("1. Cek bilangan prima")
        print("2. Tampilkan deret bilangan prima")
        print("3. Cek bilangan prima dalam range")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2/3/4): ")
        
        if pilihan == '1':
            try:
                angka = int(input("Masukkan bilangan yang ingin dicek: "))
                start_time = time.time()
                if cek_prima_sympy(angka):
                    print(f"✓ {angka} adalah bilangan prima")
                else:
                    print(f"✗ {angka} bukan bilangan prima")
                end_time = time.time()
                print(f"Waktu eksekusi: {end_time - start_time:.6f} detik")
            except ValueError:
                print("Input tidak valid! Harap masukkan bilangan bulat.")
                
        elif pilihan == '2':
            try:
                jumlah = int(input("Berapa banyak bilangan prima yang ingin ditampilkan? "))
                if jumlah <= 0:
                    print("Harap masukkan bilangan positif!")
                else:
                    start_time = time.time()
                    deret_prima = generate_primes_sympy(jumlah)
                    end_time = time.time()
                    
                    print(f"\n{jumlah} bilangan prima pertama:")
                    print(deret_prima)
                    print(f"\nBilangan prima ke-{jumlah}: {deret_prima[-1]}")
                    print(f"Waktu eksekusi: {end_time - start_time:.6f} detik")
            except ValueError:
                print("Input tidak valid! Harap masukkan bilangan bulat.")
                
        elif pilihan == '3':
            try:
                start_range = int(input("Masukkan batas bawah range: "))
                end_range = int(input("Masukkan batas atas range: "))
                
                if start_range < 2:
                    start_range = 2
                
                start_time = time.time()
                primes_in_range = list(sympy.primerange(start_range, end_range + 1))
                end_time = time.time()
                
                print(f"\nBilangan prima antara {start_range} dan {end_range}:")
                print(f"Jumlah: {len(primes_in_range)} bilangan")
                print(f"Daftar: {primes_in_range}")
                print(f"Waktu eksekusi: {end_time - start_time:.6f} detik")
                
            except ValueError:
                print("Input tidak valid! Harap masukkan bilangan bulat.")
                
        elif pilihan == '4':
            print("Program selesai. Terima kasih!")
            break
            
        else:
            print("Pilihan tidak valid! Silakan pilih 1, 2, 3, atau 4.")

if _name_ == "_main_":
    main_sympy()