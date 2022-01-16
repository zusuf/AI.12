nilai_teori = float(input("Masukkan nilai Ujian Teori : "))
nilai_praktek = float(input("Masukkan nilai Ujian Praktek : "))

if nilai_teori >= 70:
    if nilai_praktek >= 70:
        print("Selamat, Anda LULUS!")

    else:
        print("Anda harus mengulang Ujian Praktek.")

else:
    if nilai_praktek >= 70:
        print("Anda harus mengulang Ujian Teori.")

    else:
        print("Anda harus mengulang Ujian Teori dan Praktek.")    