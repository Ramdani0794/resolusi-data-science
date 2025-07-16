angka1 = int(input("masukan angka pertama: ")
angka2 = int(input("masukan angka kedua: ")
hasil = angka1 + angka2
if hasil > 5:
  print(f"{hasil} adalah nilai yang lebih dari 5")
else:
  print(f"{hasil} adalah nilai yang kurang dari 5")


# program elif
angka1 = int(input("masukan angka pertama: ")
angka2 = int(input("masukan angka kedua: ")
hasil = angka1 + angka2
if angka > 1 and angka <5:
  print(f"{hasil} adalah angka yang lebih dari 1 dan kurang dari 5")
elif angka > 5 and angka < 10:
  print(f"{hasil} adalah angka yang kurang dari 10 dan lebih dari 5")
else:
  print(f"{hasil} adalah angka di luar dari ketentuan")
