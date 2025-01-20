"Program Perhitungan BMI"

print("PERHITUNGAN BMI (BODY MASS INDEX)")
print("----------------------------------")

berat_badan = float(input("Masukkan berat badan anda (kilogram) : "))
tinggi_badan = float(input("Masukkan tinggi badan anda (meter) : "))

bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*(tinggi_badan**2)
berat_badan_ideal['atas'] = 25*(tinggi_badan**2)

if bmi < 18.5:
    kategori = "Anda kekurangan Berat Badan"
elif bmi < 25:
    kategori = "Nilai BMI anda adalah normal"
elif bmi < 30:
    kategori = "Anda kelebihan Berat Badan"
else:
    kategori = "Anda mengalami obesitas"

print("\nHasil Kalkulator BMI anda adalah")
print("----------------------------------")
print(f"Nilai BMI anda adalah {bmi:.2f} kg/m^2")
print(kategori)
print("Nilai BMI normal adalah 18.5 kg/m^2 - 25 kg/m^2")
print("")
print(f"Berat Badan Ideal anda adalah dalam rentang "
f"{berat_badan_ideal['bawah']:.2f} kg- {berat_badan_ideal['atas']:.2f}  kg")
print("")
print("terima kasih")

