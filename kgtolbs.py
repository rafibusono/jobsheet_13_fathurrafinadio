def weight_conversion() :
    berat = float(input("Masukkan berat badan anda : "))
    satuan = input("Pilih satuan [kg]/[lbs] : ")

    kg = berat * 2.20462
    lbs = berat * 0.453592

    if (satuan == "kg") :
        print(f"Berat badan anda {lbs:.2f} Lbs")
    elif (satuan == "lbs") :
        print(f"Berat badan anda {kg:.2f} Kg")
    else :
        print("satuan tidak valid")