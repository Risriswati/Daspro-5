# Nomor 1
def hitung_suhu_ruang(suhu):
    if suhu < 20:
        return "Suhu ruangan terlalu dingin!"
    elif suhu >= 20 and suhu <= 25:
        return "Suhu ruangan nyaman."
    else:
        return "Suhu ruangan terlalu panas!"
def main():
    suhu_input=float(input("Masukkan suhu ruangan dalam derajat Celcius: "))
    hasil = hitung_suhu_ruang(suhu_input)
    print(hasil)
if __name__ == "__main__":
    main()
    
# Nomor 2
def sorts(name, chapter):
    print("Nama Saya: ", name)
    print("Saya sedang mengerjakan latihan soal: ", chapter)
def main():
    nama = input("Masukkan Nama: ")
    latihan_ke = input("Masukkan Latihan ke: ")
    sorts(nama, latihan_ke)
if __name__ == "__main__":
    main()
    
#Nomor 3-A
def pembagian(x, y, z=1):
    return x * y / z
print(pembagian(20, 10, 3.190))

#Nomor 3-B
def sorts(*x):
    for arg in x:
        print(arg)
sorts(10, 20)
sorts(50, 70)
sorts(90, 30)