import sys

class Node:
    def __init__(self, nama, umur, penyakit):
        self.nama = nama
        self.umur = umur
        self.penyakit = penyakit
        self.next = None

class DataPasien:
    def __init__(self):
        self.head = None
    
    def tambah_pasien(self, nama, umur, penyakit):
        new_node = Node(nama, umur, penyakit)

        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node


    def print_pasien(self):
        # cur_node = self.head

        # while cur_node:
        #     print(f"nama : {cur_node.nama}\numur: {cur_node.umur}\npenyakit: {cur_node.penyakit}")
        #     cur_node = cur_node.next
        #     print("#" * 40)

        seen = set()
        cur_node = self.head
        while cur_node:
            if (cur_node.nama, cur_node.umur, cur_node.penyakit) not in seen:
                print(f"nama : {cur_node.nama}\numur: {cur_node.umur}\npenyakit: {cur_node.penyakit}")
                seen.add((cur_node.nama, cur_node.umur, cur_node.penyakit))
                # Only print the separator if there's a next node
                if cur_node.next:
                    print("#" * 40)
        cur_node = cur_node.next
        
    def hapus_pasien(self, key):
        # self explanotory
        cur_node = self.head

        if cur_node and cur_node.nama == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.nama != key:
            prev = cur_node
            cur_node = cur_node.next
        
        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def cari_pasien(self, key):
        cur_node = self.head

        while cur_node:
            if cur_node.nama == key:
                print(f"nama : {cur_node.nama}\numur: {cur_node.umur}\npenyakit: {cur_node.penyakit}")
                print("\n")
                return 

            cur_node = cur_node.next

        return False

    def cari_penyakit_pasien(self, key):
        cur_node = self.head

        while cur_node:
            if cur_node.penyakit == key:
                print(cur_node.nama)
                return

            cur_node = cur_node.next

        return False

    

def main():
    list = DataPasien()

    while True:
        opsi = int(input(f"1. Tambah Pasien\n2. Hapus Pasien\n3. Cari Pasien\n4. Tampilkan Semua Pasienn\n5. Pasien dengan peyakit tertentu\n"))
        list.tambah_pasien("Anto", "17", "kista")

        match opsi:
            case 1:
                nama = input("Nama: ")
                umur = input("Umur: ")
                penyakit = input("Penyakit: ")
                list.tambah_pasien(nama, umur, penyakit)
            case 2:
                nama = input("Nama pasien yang akan dihapus: ")
                list.hapus_pasien(nama)
            case 3:
                nama = input("Nama pasien: ")
                list.cari_pasien(nama)
            case 4:
                print(list.print_pasien())
            case 5:
                penyakit = input("Nama penyaki: ")
                list.cari_penyakit_pasien(penyakit)
            case _:
                sys.exit()




if __name__ == "__main__":
    main()