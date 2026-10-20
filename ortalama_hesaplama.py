import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

print("=== Ortalama Hesaplama (2 Sayi) ===\n")

sayilar = []

for i in range(1, 3):
    while True:
        girdi = input(f"  {i}. Sayi: ").strip().replace(",", ".")
        try:
            sayilar.append(float(girdi))
            break
        except ValueError:
            print("  Gecersiz deger, lutfen sayi girin.")

ortalama = sum(sayilar) / len(sayilar)
print(f"\nGirilen sayilar : {sayilar[0]} ve {sayilar[1]}")
print(f"Ortalama        : {ortalama:.4f}")
