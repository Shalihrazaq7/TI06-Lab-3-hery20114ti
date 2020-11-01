# DDP LAB-3

# SOAL 1 - Gunting-Batu-Kertas
# Tuliskan program untuk Soal 1 di bawah ini
""""
player1=input("Masukkan Pilihan Player-1 : ")
player2=input("Masukkan Pilihan Player-2 : ")
print(end='\n')

if player1 == "kertas" and player2 == "kertas" :
  print ("Permainan Seri")
elif player1 == "kertas" and player2 == "batu" :
  print ("Player-1 Win!!")
elif player1 == "kertas" and player2 == "gunting" :
  print ("Player-2 Win!!")
elif player1 == "gunting" and player2 == "gunting" :
  print ("Permainan Seri")
elif player1 == "gunting" and player2 == "batu" :
  print ("Player-2 Win!!")
elif player1 == "gunting" and player2 == "kertas" :
  print ("Player-1 Win!!")
elif player1 == "batu" and player2 == "batu" :
  print ("Permainan Seri")
elif player1 == "batu" and player2 == "kertas" :
  print ("Player-2 Win!!")
elif player1 == "batu" and player2 == "gunting" :
  print ("Player-1 Win!!")
else :
  print("Maaf inputan Anda salah!")
  
"""



# SOAL 2 - Toko Buku Bekas
# Tuliskan program untuk Soal 2 di bawah ini
"""
buku=eval(input("Masukkan total buku yang dibeli : "))
print(end='\n')

if buku <= 0  :
  total=buku*0
  print ("Total yang harus Anda Bayar : ", total)
elif buku < 11 :
  total=buku*20000
  print ("Total yang harus Anda Bayar : ", total)
elif buku < 26 :
  total=buku*18000
  print ("Total yang harus Anda Bayar : ", total)
elif buku < 51 :
  total=buku*15000
  print ("Total yang harus Anda Bayar : ", total)
elif buku > 50 :
  total=buku*10000
  print ("Total yang harus Anda Bayar : ", total)
else :
  print("Anda tidak masukan jumlah buku")
"""


# SOAL 3 - Mencetak Persegi
# Tuliskan program untuk Soal 3 di bawah ini
""""
Angka = eval(input("Masukan angka : "))
print(end='\n')
for i in range(Angka):
  if i %2 == 0 :
    print("#######")
  else :
    print("$$$$$$$")
print(end='\n')
kotak = int(input("Masukkan sebuah bilangan bulat : "))
"""

kotak = int(input("Masukan angka : "))
for i in range(1, kotak):
  if(i % 2):
    print('# '*kotak)
  elif(i % 3):
    print('$ '*kotak)






