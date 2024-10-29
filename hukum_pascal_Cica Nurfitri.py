def hitung_gaya_pascal(F1, A1, A2):
    """Menghitung gaya F2 menggunakan hukum Pascal"""
    F2 = (F1 * A2) / A1
    return F2

def hitung_gaya_dari_area(F2, A1, A2):
    """Menghitung gaya F1 menggunakan hukum Pascal"""
    F1 = (F2 * A1) / A2
    return F1

def hitung_area_dari_gaya(F1, F2, A1):
    """Menghitung area A2 menggunakan hukum Pascal"""
    A2 = (F2 * A1) / F1
    return A2

def hitung_area_dari_gaya_terbalik(F1, F2, A2):
    """Menghitung area A1 menggunakan hukum Pascal"""
    A1 = (F1 * A2) / F2
    return A1

def menu():
    print("Program untuk menghitung hukum Pascal:")
    print("1. Hitung Gaya F₂ dari Gaya F₁ dan Area")
    print("2. Hitung Gaya F₁ dari Gaya F₂ dan Area")
    print("3. Hitung Area A₂ dari Gaya dan Area")
    print("4. Hitung Area A₁ dari Gaya dan Area")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == '1':
        F1 = float(input("Masukkan gaya F₁ dalam N: "))
        A1 = float(input("Masukkan area A₁ dalam m²: "))
        A2 = float(input("Masukkan area A₂ dalam m²: "))
        F2 = hitung_gaya_pascal(F1, A1, A2)
        print(f"Gaya F₂ adalah: {F2} N")

    elif pilihan == '2':
        F2 = float(input("Masukkan gaya F₂ dalam N: "))
        A1 = float(input("Masukkan area A₁ dalam m²: "))
        A2 = float(input("Masukkan area A₂ dalam m²: "))
        F1 = hitung_gaya_dari_area(F2, A1, A2)
        print(f"Gaya F₁ adalah: {F1} N")

    elif pilihan == '3':
        F1 = float(input("Masukkan gaya F₁ dalam N: "))
        F2 = float(input("Masukkan gaya F₂ dalam N: "))
        A1 = float(input("Masukkan area A₁ dalam m²: "))
        A2 = hitung_area_dari_gaya(F1, F2, A1)
        print(f"Area A₂ adalah: {A2} m²")

    elif pilihan == '4':
        F1 = float(input("Masukkan gaya F₁ dalam N: "))
        F2 = float(input("Masukkan gaya F₂ dalam N: "))
        A2 = float(input("Masukkan area A₂ dalam m²: "))
        A1 = hitung_area_dari_gaya_terbalik(F1, F2, A2)
        print(f"Area A₁ adalah: {A1} m²")

    else:
        print("Pilihan tidak sesuai, silahkan pilih 1/2/3/4")

if __name__ == "__main__":
   menu ()


