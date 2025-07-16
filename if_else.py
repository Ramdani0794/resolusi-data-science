angka = int(input("masukan angka: ")
if angka > 5:
  print(f"{angka} adalah nilai yang lebih dari 5")
else:
  print(f"{angka} adalah nilai yang kurang dari 5")

# program elif
angka = 5
if angka > 1 and angka <5:
  print(f"{angka} adalah angka yang lebih dari 1 dan kurang dari 5")
elif angka > 5 and angka < 10:
  print(f"{angka} adalah angka yang kurang dari 10 dan lebih dari 5")
else:
  print(f"{angka} adalah angka di luar dari ketentuan")
