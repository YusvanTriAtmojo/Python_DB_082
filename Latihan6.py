import tkinter as tk
import sqlite3
from tkinter import messagebox

##Membuat fungsi untuk memasukkan data ke dalam database SQL##
def simpan_keSql(nama_siswa, biologi, fisika, inggris, prediksi_fakultas):
    ##Menunjuk ke dalam database yang dituju##
    conn = sqlite3.connect("SQL1.db")
    ##Mengubah database##
    cursor = conn.cursor()

    ##Membuat tabel di dalam database jika belum dibuat##
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama_siswa TEXT,
                    biologi INTEGER,
                    fisika INTEGER,
                    inggris INTEGER,
                    prediksi_fakultas TEXT)''')
    
    ##Memasukkan nilai berdasarkan parameter ke dalam kolom yang ada pada database##
    cursor.execute ('''INSERT INTO nilai_siswa (nama_siswa, 
                    biologi, fisika, inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)''',
    (nama_siswa, biologi, fisika, inggris, prediksi_fakultas))

    ##Melakukan commit atau simpan dan menutup##
    conn.commit()
    conn.close()

##Membuat GUI dengan judul Pemograman Kelas B dan ukuran 500x500 tanpa resize##
top = tk.Tk()
top.title("Pemograman Kelas B")
top.geometry("500x500")
top.resizable(False,False)

##Membuat pengaturan frame pada GUI##
inputframe = tk.Frame(top)
inputframe.pack(padx=10,pady=10,fill="x", expand=True)

##Membuat fungsi prediksi fakultas dengan pengkondisian##
def PrediksiFakultas(Nilai1, Nilai2, Nilai3):
    if Nilai1 > Nilai2 and Nilai1 > Nilai3:
        return "Kedokteran"
    elif Nilai2 > Nilai1 and Nilai2 > Nilai3:
        return "Teknik"
    elif Nilai3 > Nilai1 and Nilai3 > Nilai2:
        return "Bahasa"
    else:
        return

##Membuat fungsi show untuk menampilkan hasil inputan dan prediksi pada GUI##
def show():
    ##Untuk mengambil nilai dari setiap input E1 sampai E4 dan di masukkan ke dalam setiap variabel##
    Namamhs =E1.get()
    Nilai1 =E2.get()
    Nilai2 =E3.get()
    Nilai3 =E4.get()
    
    ##Memasukkan fungsi prediksi ke dalam variabel prediksi##
    prediksi = PrediksiFakultas(Nilai1, Nilai2, Nilai3)
    ##Untuk menampilkan output hasil##
    hasilmhs = f"Nama Mahasiswa: {Namamhs}"
    Hasil1 = f"Nilai Biologi: {Nilai1}"
    Hasil2 = f"Nilai Fisika: {Nilai2}"
    Hasil3 = f"Nilai Inggris: {Nilai3}"
    HasilPrediksi = f"Hasil Fakultas: {prediksi}"

    ##Memasukkan input ke dalam lebel hasil##
    label_hasilmhs.config(text=hasilmhs)
    label_Hasil1.config(text=Hasil1)
    label_Hasil2.config(text=Hasil2)
    label_Hasil3.config(text=Hasil3)
    label_HasilPrediksi.config(text=HasilPrediksi)

    ##Pengkondisian jika bukan sesuai parameter  atau variabel maka tidak masuk ke database##
    if not Nilai1 and not Nilai2 and not Nilai3 and not Namamhs:
        frameHasil.pack_forget()
    else:
        frameHasil.pack()
        simpan_keSql(Namamhs, Nilai1, Nilai2, Nilai3, prediksi)
        messagebox.showinfo("Info", "Data Tersimpan")

##Membuat Label untuk judul##
Var = tk.Label(inputframe, text="Aplikasi Prediksi Fakultas Pilihan", font=("Times",14,"bold"))
Var.pack()

##Membuat Label dan Input Nama##
Input1=tk.Label(inputframe, text="Masukan Nama Anda: ", font = ("Times",11))
Input1.pack(padx=10,pady=5, fill="x", expand=True)
E1=tk.Entry(inputframe)
E1.pack(padx=10,pady=5, fill="x", expand=True)

##Membuat Label untuk cara memasukkan Nilai##
Var2 = tk.Label(inputframe, text="Masukkan Nilai dengan 3 digit !", font=("Times",12,"bold"))
Var2.pack()

##Membuat label dan input Nilai matakuliah##
Input2=tk.Label(inputframe, text="Masukan Nilai Biologi: ", font = ("Times",11))
Input2.pack(padx=10,pady=5, fill="x", expand=True)
E2=tk.Entry(inputframe)
E2.pack(padx=10,pady=5, fill="x", expand=True)

Input3=tk.Label(inputframe, text="Masukan Nilai Fisika: ", font = ("Times",11))
Input3.pack(padx=10,pady=5, fill="x", expand=True)
E3=tk.Entry(inputframe)
E3.pack(padx=10,pady=5, fill="x", expand=True)

Input4=tk.Label(inputframe, text="Masukan Nilai Inggris: ", font = ("Times",11))
Input4.pack(padx=10,pady=5, fill="x", expand=True)
E4=tk.Entry(inputframe)
E4.pack(padx=10,pady=5, fill="x", expand=True)

##Membuat Tombol Hasil yang akan terhubung dengan fungsi show##
tombol=tk.Button(top, text="Sumbit", command= show)
tombol.pack(padx=10,pady=5,fill="x", expand=True)

##Membuat Frame atau bingkai untuk menampilkan hasil input jika frameHasil.pack_forget() atau tidak tersimpan##
frameHasil = tk.LabelFrame(top, labelanchor="n", padx= 0, pady= 0)
frameHasil.pack_forget()

##Membuat Label Hasil##
label_hasilmhs = tk.Label(frameHasil, text="",font=("Times", 9))
label_hasilmhs.pack()

label_Hasil1 = tk.Label(frameHasil, text="",font=("Times", 9))
label_Hasil1.pack()

label_Hasil2 = tk.Label(frameHasil, text="",font=("Times", 9))
label_Hasil2.pack()

label_Hasil3 = tk.Label(frameHasil, text="",font=("Times", 9))
label_Hasil3.pack()

label_Hasil4 = tk.Label(frameHasil, text="",font=("Times", 9))
label_Hasil4.pack()

label_HasilPrediksi = tk.Label(frameHasil, text="", font=("Times", 9,"bold"))
label_HasilPrediksi.pack()

##Menjalankan program##
top.mainloop()
