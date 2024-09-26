# INPUT
inputUserName = input("Masukkan Nama\t: ")
nasiGoreng = int(input("Jumlah Nasgor\t: "))
mieKuah = int(input("Jumlah Mie Kuah\t: "))

# Output
# Bagian 1
print("\nSelamat Datang di Warung ENAK")
print("-" * 29)
print(f"Nama Pelanggan\t: {inputUserName}")

# Bagian 2
print("Nasi Goreng")
print(f"\t[{nasiGoreng}] x Rp 15.000 = Rp {nasiGoreng * 15000:,}".replace(",", "."))

# Bagian 3
print("Mie Kuah")
print(f"\t[{mieKuah}] x Rp 12.000 = Rp {mieKuah * 12000:,}".replace(",", "."))

# Bagian 4
subTotal = (nasiGoreng * 15000) + (mieKuah * 12000)
ppn = int(subTotal * (11/100))
PajakService = 5000

print(f"Subtotal\t\t= Rp {subTotal:,}".replace(",", "."))
print(f"Pajak 11%\t\t= Rp {ppn:,}".replace(",", "."))

# Bagian 5
print(f"Pajak Service\t\t= Rp 5.000")
print(f"Total\t\t\t= Rp {int(subTotal + ppn + PajakService):,}".replace(",", "."))
