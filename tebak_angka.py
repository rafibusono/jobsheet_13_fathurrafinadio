def tebak_angka() :
    import random
    r_number = random.randint(1,10)
    g = 0
    gchance = 2
    glimit = 3
    print("Angka ditemukan!")

    while g < 3:
        tebakan = input("Tebak angka mulai dari 1 sampai 10 : ")
        if int(tebakan) > 10:
            print("Sampai 10 bang")
        elif int(tebakan) < 1:
            print("Dari 1 bang")
        elif int(tebakan) == r_number:
            print("Selamat Tebakan anda benar")
            break
        elif int(tebakan) > r_number:
            print(f"Angka anda terlalu besar, sisa kesempatan anda {gchance}")
            g += 1
            gchance -= 1
        else:
            int(tebakan) < r_number
            print(f"Angka anda terlalu kecil, sisa kesempatan anda {gchance}")
            g += 1
            gchance -= 1

    else:    
        g == glimit
        print(f"Kesempatan anda habis, angka yang benar adalah {r_number}")