"hubungkan modul"
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
    QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout, QButtonGroup)


from random import shuffle, randint



"buat aplikasi dan jendelanya"
APP = QApplication([])
JENDELA = QWidget()
JENDELA.setWindowTitle("APLIKASI QUIZ")
JENDELA.setFixedSize(200, 200) ## ukuran jendelanya


"menambahkan widget"
pertanyaan = QLabel("ini untuk pertanyaannya")
tombol = QPushButton("JAWAB")
radio1 = QRadioButton("pilihan 1")
radio2 = QRadioButton("pilihan 2")
radio3 = QRadioButton("pilihan 3")
radio4 = QRadioButton("pilihan 4")
radioGrup = QGroupBox("Pilihan Jawaban")
"tambahkan widget untuk grup jawaban"
hasil = QLabel("BENAR / SALAH")
jawaban = QLabel("INI JAWABANNYA LOOO")
jawabanGrup = QGroupBox("Hasilnya adalah")


"tambahkan button grup"
RadioButtonGrup = QButtonGroup()
RadioButtonGrup.addButton(radio1)
RadioButtonGrup.addButton(radio2)
RadioButtonGrup.addButton(radio3)
RadioButtonGrup.addButton(radio4)


"menambahkan layout untuk grup radio"
v1Grup = QVBoxLayout()
v1Grup.addWidget(radio1)
v1Grup.addWidget(radio2)
v2Grup = QVBoxLayout()
v2Grup.addWidget(radio3)
v2Grup.addWidget(radio4)
hGrup = QHBoxLayout()
hGrup.addLayout(v1Grup)
hGrup.addLayout(v2Grup)
radioGrup.setLayout(hGrup)
"menambahkan layout untuk grup jawaban"
vGrupJawaban = QVBoxLayout()
vGrupJawaban.addWidget(hasil)
vGrupJawaban.addWidget(jawaban)
jawabanGrup.setLayout(vGrupJawaban)


radioGrup.show()
jawabanGrup.hide()


"menambahkan layout untuk tampilan utama"
v_utama = QVBoxLayout()
v_utama.addWidget(pertanyaan)
v_utama.addWidget(radioGrup)
v_utama.addWidget(jawabanGrup) ## tambahkan jawaban grup
v_utama.addWidget(tombol)
JENDELA.setLayout(v_utama)




"kumpulan fungsi fungsi"
def check_answer():
    if list_pilihan[0].isChecked():
        hasil.setText("Benar")
        JENDELA.nilai += 1
    else:
        hasil.setText("Salah")
    print("-------------------------------")
    print("total pertanyaan:", JENDELA.total)
    print("total benar:", JENDELA.nilai)
    print("Statistik:", (JENDELA.nilai / JENDELA.total)*100, "%")
    show_result()

def show_result():
    radioGrup.hide() ## sembunyikan pilihan jawaban
    jawabanGrup.show() ## tampilkan hasil
    tombol.setText("SOAL BERIKUTNYA")


def show_question():
    jawabanGrup.hide()
    radioGrup.show()
    tombol.setText("JAWAB")
    ## reset semua pilihan
    RadioButtonGrup.setExclusive(False)    
    radio1.setChecked(False)
    radio2.setChecked(False)
    radio3.setChecked(False)
    radio4.setChecked(False)
    RadioButtonGrup.setExclusive(True)    

list_pertanyaan = list()


"tambahkan kelas"
class Question():
    def __init__(self, soal, benar, salah1, salah2, salah3):
        self.soal = soal
        self.benar = benar
        self.salah1 = salah1
        self.salah2 = salah2
        self.salah3 = salah3

"objek dari class Question"
soal1 = Question("sudah makan?", "belum", "sudah 1 kali", "sudahh", "hmm")
soal2 = Question("sudah mandi?", "belum", "sudah 1 kali", "sudahh", "hmm")


list_pertanyaan.append(soal1)
list_pertanyaan.append(soal2)

"kumpulan fungsi-fungsi"
list_pilihan = [radio1, radio2, radio3, radio4]
def ask(tanya):
    shuffle(list_pilihan)
    list_pilihan[0].setText(tanya.benar)
    list_pilihan[1].setText(tanya.salah1)
    list_pilihan[2].setText(tanya.salah2)
    list_pilihan[3].setText(tanya.salah3)
    pertanyaan.setText(tanya.soal)
    jawaban.setText(tanya.benar)
    show_question()

"kumpulan fungsi-fungsi"
JENDELA.soal_sekarang = -1
JENDELA.nilai = 0
JENDELA.total = 0
def next_question():
    JENDELA.soal_sekarang += 1
    if JENDELA.soal_sekarang >= len(list_pertanyaan):
        JENDELA.soal_sekarang = 0
    ask(list_pertanyaan[JENDELA.soal_sekarang])
    JENDELA.total += 1
    indeksAcak = randint(0, len(list_pertanyaan)-1)
    ask(list_pertanyaan[indeksAcak])

def ujicoba():
    if tombol.text() == "JAWAB":
        check_answer()
    else:
        next_question()

next_question()





"kumpulan event handler"
tombol.clicked.connect(ujicoba)



"munculkan jendela dan jalankan aplikasinya"
JENDELA.show()
APP.exec_()




