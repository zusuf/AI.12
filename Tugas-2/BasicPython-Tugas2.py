#Data
nama = ["Fawwaz", "John"]
no_telepon = ["08123456789", "08987654321"]


#Menu
def main_menu():
    while(True):
        print("------------------------")
        print("          MENU          ")
        print("------------------------")
        print("1. Lihat Daftar Kontak")
        print("2. Tambah Kontak")
        print("3. Keluar")
        print("------------------------")
        print("\n")

        menu = int(input("Pilih Menu (1/2/3) : "))

        if menu == 1:
            for x in range(len(nama)):
                for y in range(len(no_telepon)):
                    if x == y:
                        print("")   
                        print("  Nama: " + nama[x])
                        print("  No Telepon: " + no_telepon[y])  
        elif menu == 2:
            nama.append(str(input("  Nama : ")))
            no_telepon.append(str(input("  No Telepon : ")))
        elif menu == 3:
            print("Terima kasih!")
            print("") 
            exit()
        else:
            print('Maaf, nomor menu yang dipilih tidak tersedia!') 
            print("") 

main_menu()



