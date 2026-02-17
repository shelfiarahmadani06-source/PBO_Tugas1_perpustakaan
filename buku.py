class buku:
    def __init__(self, judul, penulis, stok):
        self.judul = judul
        self.penulis = penulis
        self.stok = stok
        self.status = "tersedia"

    def tampilkan_info(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis:{self.penulis}")
        print(f"stok: {self.stok}")
        print(f"status: {self.status}")
        print("-" * 25)

class anggota:
    def __init__(self, nama, NIM, Semester):
        self.nama = nama
        self.NIM = NIM
        self.Semester = Semester
        self.buku_dipinjam = None

    def pinjam_buku(self, buku):
        if buku.status == "tersedia":
            buku.status = "dipinjam"
            self.buku_dipinjam = buku
            print(f"{self.nama} berhasil meminjam {buku.judul}")
        else:
            print(f"Maaf, {buku.judul} sedang dipinjam oleh orang lain.")

    def kembalikan_buku(self):
        if self.buku_dipinjam:
            self.buku_dipinjam.status = "tersedia"
            print(f"{self.nama} berhasil mengembalikan {self.buku_dipinjam.judul}")
            self.buku_dipinjam = None
        else:
            print("Anda tidak meminjam buku apapun.")
        

class perpustakaan:
    def __init__(self, nama_pustaka):
        self.nama_pustaka = nama_pustaka
        self.daftar_buku = []
    
    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_semua_buku(self):
        print("nama perpustakaan :", self.nama_pustaka)
        print("=" * 30)
        for buku in self.daftar_buku: buku.tampilkan_info()
