import matplotlib.pyplot as plt

def lcm(pengkali, penambah, modulus, seed, sample): #function untuk menjalankan LCM
    hasilx = [] #Array untuk menampung hasil pseudo random dari distribusi uniform (0 s/d 1)
    hasily = [] #Array untuk menampung hasil pseudo random dari nomor acak (0 s/d modulus-1)
    for i in range(sample): #loop LCM dengan maskimal total sample yang akan diambil
        x = pengkali*seed+penambah #perhitungan dari a*c*m nomor acak LCM
        print(i+1,"|",pengkali,"*",seed,"+",penambah,"=",x,"|",x,"mod",modulus ,"=", end=' ') #menampilkan hasil a*c*m
        seed = x % modulus # perhitungan dari hasil nomor acak LCM
        hasily.append(seed) #memasukan hasil perhitungan nomor acak ke dalam array
        print(seed,end=' | ') #menampilkan hasil nomor acak
        u = seed/modulus #mnjumlahkan distribusi uniform 
        print('{:.4f}'.format(u)) #menampilkan distribusi uniform
        hasilx.append(u) #memasukan hasil distribusi uniform kedalam array
    print(hasilx) #menampilkan hasil array distribusi uniform
    print(hasily) #menampilkan hasil array nomor acak
    plt.scatter(hasilx,range(0, sample)) #mendeklarasikan matplotlib x dan y menggunakan hasil array distribusi uniform dan hasil array nomor acak
    plt.show() #memanggil matplotlib

pengkali = 21 #pengkali = a
penambah = 3 #penambah = c
modulus = 16 #modulus = m
seed = 12 #seed = Z0
sample = 2 #sample = total sample yang akan diambil, sample < modulus
lcm(pengkali , penambah, modulus, seed, sample) #memanggil fungsi
#rumus LCM | Zi = (a.Z(i) + c) mod m











