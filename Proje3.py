import sys
import math
import sympy as sp
import mysql.connector
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFormLayout, QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import Qt

# Veritabanına bağlanma
def veritabanina_baglan():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Amiral5276!",
            database="telefon_rehberi"
        )
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS rehber (isim VARCHAR(255), telefon VARCHAR(255))")
        return conn, cursor
    except mysql.connector.Error as err:
        QMessageBox.critical(None, "Veritabanı Hatası", f"Bağlantı hatası: {err}")
        sys.exit()

# Matematik çözümleri işlevleri
def linear_solver(a, b):
    if a != 0:
        return -b / a
    else:
        return "Çözüm yok" if b != 0 else "Sonsuz Çözüm"

def quadratic_solver(a, b, c):
    d = b**2 - 4 * a * c
    if d >= 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return root1, root2
    else:
        return "Karmaşık kökler", None

# Ana uygulama penceresi
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Sekmeli yapı oluştur
        self.setWindowTitle("Matematik ve Telefon Rehberi Uygulaması")
        self.setGeometry(200, 200, 800, 600)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Matematik çözümleri sekmesi
        self.math_tab = QWidget()
        self.rehber_tab = QWidget()
        self.tabs.addTab(self.math_tab, "Matematik Denklem Çözümleri")
        self.tabs.addTab(self.rehber_tab, "Telefon Rehberi")

        self.init_math_tab()
        self.init_rehber_tab()

    # Matematik sekmesi
    def init_math_tab(self):
        layout = QVBoxLayout()

        self.a_input = QLineEdit()
        self.b_input = QLineEdit()
        self.c_input = QLineEdit()
        self.result_label = QLabel("Sonuç: ")

        solve_button = QPushButton("Çöz")
        solve_button.clicked.connect(self.solve_quadratic)

        layout.addWidget(QLabel("a:"))
        layout.addWidget(self.a_input)
        layout.addWidget(QLabel("b:"))
        layout.addWidget(self.b_input)
        layout.addWidget(QLabel("c:"))
        layout.addWidget(self.c_input)
        layout.addWidget(solve_button)
        layout.addWidget(self.result_label)

        self.math_tab.setLayout(layout)

    # Telefon rehberi sekmesi
    def init_rehber_tab(self):
        self.conn, self.cursor = veritabanina_baglan()

        layout = QVBoxLayout()
        self.isim_input = QLineEdit()
        self.telefon_input = QLineEdit()
        ekle_button = QPushButton("Kişi Ekle")
        ekle_button.clicked.connect(self.kisi_ekle)

        listele_button = QPushButton("Kişileri Listele")
        listele_button.clicked.connect(self.kisileri_listele)

        layout.addWidget(QLabel("İsim:"))
        layout.addWidget(self.isim_input)
        layout.addWidget(QLabel("Telefon:"))
        layout.addWidget(self.telefon_input)
        layout.addWidget(ekle_button)
        layout.addWidget(listele_button)

        # Kişi listeleme tablosu
        self.kisiler_table = QTableWidget()
        self.kisiler_table.setColumnCount(2)
        self.kisiler_table.setHorizontalHeaderLabels(["İsim", "Telefon"])
        layout.addWidget(self.kisiler_table)

        self.rehber_tab.setLayout(layout)

    def solve_quadratic(self):
        try:
            a = float(self.a_input.text())
            b = float(self.b_input.text())
            c = float(self.c_input.text())
            result = quadratic_solver(a, b, c)
            self.result_label.setText(f"Sonuç: {result}")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli sayılar girin.")

    def kisi_ekle(self):
        isim = self.isim_input.text()
        telefon = self.telefon_input.text()

        if isim and telefon:
            try:
                self.cursor.execute("INSERT INTO rehber (isim, telefon) VALUES (%s, %s)", (isim, telefon))
                self.conn.commit()
                QMessageBox.information(self, "Başarılı", f"{isim} rehbere eklendi.")
                self.isim_input.clear()
                self.telefon_input.clear()
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Veritabanı Hatası", f"Hata: {err}")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun.")

    def kisileri_listele(self):
        self.cursor.execute("SELECT isim, telefon FROM rehber")
        rows = self.cursor.fetchall()
        self.kisiler_table.setRowCount(len(rows))

        for row_idx, row_data in enumerate(rows):
            self.kisiler_table.setItem(row_idx, 0, QTableWidgetItem(row_data[0]))
            self.kisiler_table.setItem(row_idx, 1, QTableWidgetItem(row_data[1]))

# Giriş ekranı
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Giriş Ekranı")
        self.setGeometry(400, 200, 300, 150)

        layout = QFormLayout()

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addRow("Kullanıcı Adı:", self.username_input)
        layout.addRow("Şifre:", self.password_input)

        login_button = QPushButton("Giriş")
        login_button.clicked.connect(self.check_login)

        layout.addRow(login_button)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "Alper" and password == "5276":
            self.close()
            self.main_app = MyApp()
            self.main_app.show()
        else:
            QMessageBox.warning(self, "Hatalı Giriş", "Kullanıcı adı veya şifre yanlış")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    login = LoginWindow()
    login.show()

    sys.exit(app.exec())