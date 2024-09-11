import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFormLayout, QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import Qt
from sympy import Symbol, solve, sqrt
from math import factorial, log, gcd, exp, sin, cos, tan, radians

# Ana Uygulama Penceresi
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matematik İşlemleri ve Telefon Rehberi Uygulaması")
        self.initUI()

    # Pencere genişliği ve sekmelerin ayarlanması
    def initUI(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Ana Sekmeler
        self.math_tab = QWidget()  # Matematik Denklem Çözümleri için ana menü
        self.rehber_tab = QWidget()  # Telefon Rehberi için ana menü
        self.tabs.addTab(self.math_tab, "Matematik Denklem Çözümleri")
        self.tabs.addTab(self.rehber_tab, "Telefon Rehberi")

        self.init_math_tab()
        self.init_rehber_tab()

        # Pencere genişliği otomatik ayarlanacak
        self.adjustSize()

    # Matematik Denklem Çözümleri için ana menü
    def init_math_tab(self):
        layout = QVBoxLayout()

        # Her bir işlem için butonlar oluşturuluyor
        layout.addWidget(QLabel("Matematik Denklem Çözümleri"))
        buttons = [
            ("Birinci Dereceden Denklem Çöz", self.show_linear_solver),
            ("İkinci Dereceden Denklem Çöz", self.show_quadratic_solver),
            ("Üçüncü Dereceden Denklem Çöz", self.show_cubic_solver),
            ("Faktöriyel Hesapla", self.show_factorial),
            ("Seri Toplamı Hesaplama (Faulhaber Formülü ile)", self.show_faulhaber),
            ("Permütasyon Hesapla", self.show_permutation),
            ("Kombinasyon Hesapla", self.show_combination),
            ("Fibonacci Sayısı Hesapla", self.show_fibonacci),
            ("Asal Sayı Kontrolü", self.show_prime_check),
            ("EBOB Hesapla", self.show_gcd),
            ("EKOK Hesapla", self.show_lcm),
            ("Logaritma Hesapla", self.show_logarithm),
            ("Üstel Fonksiyon Hesapla", self.show_exponential),
            ("Trigonometrik Fonksiyon Hesapla", self.show_trigonometry)
        ]

        for btn_text, method in buttons:
            btn = QPushButton(btn_text)
            btn.clicked.connect(method)
            layout.addWidget(btn)

        self.math_tab.setLayout(layout)

    # Her bir matematik işlemi için sekme fonksiyonları
    def show_linear_solver(self):
        self.open_math_solver_tab("Birinci Dereceden Denklem Çöz", self.init_linear_tab)

    def show_quadratic_solver(self):
        self.open_math_solver_tab("İkinci Dereceden Denklem Çöz", self.init_quadratic_tab)

    def show_cubic_solver(self):
        self.open_math_solver_tab("Üçüncü Dereceden Denklem Çöz", self.init_cubic_tab)

    def show_factorial(self):
        self.open_math_solver_tab("Faktöriyel Hesapla", self.init_factorial_tab)

    def show_faulhaber(self):
        self.open_math_solver_tab("Seri Toplamı Hesaplama (Faulhaber Formülü ile)", self.init_faulhaber_tab)

    def show_permutation(self):
        self.open_math_solver_tab("Permütasyon Hesapla", self.init_permutation_tab)

    def show_combination(self):
        self.open_math_solver_tab("Kombinasyon Hesapla", self.init_combination_tab)

    def show_fibonacci(self):
        self.open_math_solver_tab("Fibonacci Hesapla", self.init_fibonacci_tab)

    def show_prime_check(self):
        self.open_math_solver_tab("Asal Sayı Kontrolü", self.init_prime_check_tab)

    def show_gcd(self):
        self.open_math_solver_tab("EBOB Hesapla", self.init_gcd_tab)

    def show_lcm(self):
        self.open_math_solver_tab("EKOK Hesapla", self.init_lcm_tab)

    def show_logarithm(self):
        self.open_math_solver_tab("Logaritma Hesapla", self.init_logarithm_tab)

    def show_exponential(self):
        self.open_math_solver_tab("Üstel Fonksiyon Hesapla", self.init_exponential_tab)

    def show_trigonometry(self):
        self.open_math_solver_tab("Trigonometrik Fonksiyon Hesapla", self.init_trigonometry_tab)

    # Seçilen matematik işlemi için yeni bir sekme aç
    def open_math_solver_tab(self, title, init_function):
        new_tab = QWidget()
        self.tabs.addTab(new_tab, title)
        init_function(new_tab)
        self.tabs.setCurrentWidget(new_tab)

    # Örnek olarak birinci dereceden denklem sekmesi başlatma fonksiyonu
    def init_linear_tab(self, tab):
        layout = QFormLayout()
        self.linear_a_input = QLineEdit()
        self.linear_b_input = QLineEdit()
        self.linear_result = QLabel("Sonuç: ")
        self.linear_formula = QLabel("Denklem: ax + b = 0")  # Formül ekrana yazdırılıyor

        solve_button = QPushButton("Çöz")
        solve_button.clicked.connect(self.solve_linear)

        layout.addRow(QLabel("Birinci Dereceden Denklem: ax + b = 0"))
        layout.addRow("a (katsayı):", self.linear_a_input)
        layout.addRow("b (sabit terim):", self.linear_b_input)
        layout.addRow(solve_button)
        layout.addRow(self.linear_formula)  # Girilen değerlere göre formül burada gösterilecek
        layout.addRow(self.linear_result)
        tab.setLayout(layout)

    def solve_linear(self):
        try:
            a = float(self.linear_a_input.text())
            b = float(self.linear_b_input.text())
            if a != 0:
                result = -b / a
                self.linear_formula.setText(f"Denklem: {a}x + {b} = 0")  # Girilen değerlerle formül yazdırılıyor
                self.linear_result.setText(f"Sonuç: x = {result}")
            else:
                self.linear_result.setText("Sonsuz veya geçersiz çözüm.")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli sayılar girin.")

    # İkinci Dereceden Denklem (Karmaşık köklerle birlikte)
    def init_quadratic_tab(self, tab):
        layout = QFormLayout()
        self.quadratic_a_input = QLineEdit()
        self.quadratic_b_input = QLineEdit()
        self.quadratic_c_input = QLineEdit()
        self.quadratic_result = QLabel("Sonuç: ")
        self.quadratic_formula = QLabel("Denklem: ax^2 + bx + c = 0")  # Formül ekrana yazdırılıyor

        solve_button = QPushButton("Çöz")
        solve_button.clicked.connect(self.solve_quadratic)

        layout.addRow(QLabel("İkinci Dereceden Denklem: ax^2 + bx + c = 0"))
        layout.addRow("a (katsayı):", self.quadratic_a_input)
        layout.addRow("b (katsayı):", self.quadratic_b_input)
        layout.addRow("c (sabit terim):", self.quadratic_c_input)
        layout.addRow(solve_button)
        layout.addRow(self.quadratic_formula)  # Girilen değerlere göre formül burada gösterilecek
        layout.addRow(self.quadratic_result)
        tab.setLayout(layout)

    def solve_quadratic(self):
        try:
            a = float(self.quadratic_a_input.text())
            b = float(self.quadratic_b_input.text())
            c = float(self.quadratic_c_input.text())
            d = b**2 - 4*a*c
            self.quadratic_formula.setText(f"Denklem: {a}x^2 + {b}x + {c} = 0")  # Girilen değerlerle formül yazdırılıyor
            if d >= 0:
                root1 = (-b + sqrt(d)) / (2 * a)
                root2 = (-b - sqrt(d)) / (2 * a)
                self.quadratic_result.setText(f"Kökler: {root1}, {root2}")
            else:
                root1 = (-b + sqrt(d)) / (2 * a)
                root2 = (-b - sqrt(d)) / (2 * a)
                self.quadratic_result.setText(f"Karmaşık Kökler: {root1}, {root2}")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli sayılar girin.")

    # Üçüncü Dereceden Denklem
    def init_cubic_tab(self, tab):
        layout = QFormLayout()
        self.cubic_a_input = QLineEdit()
        self.cubic_b_input = QLineEdit()
        self.cubic_c_input = QLineEdit()
        self.cubic_d_input = QLineEdit()
        self.cubic_result = QLabel("Sonuç: ")
        self.cubic_formula = QLabel("Denklem: ax^3 + bx^2 + cx + d = 0")  # Formül ekrana yazdırılıyor

        solve_button = QPushButton("Çöz")
        solve_button.clicked.connect(self.solve_cubic)

        layout.addRow(QLabel("Üçüncü Dereceden Denklem: ax^3 + bx^2 + cx + d = 0"))
        layout.addRow("a (katsayı):", self.cubic_a_input)
        layout.addRow("b (katsayı):", self.cubic_b_input)
        layout.addRow("c (katsayı):", self.cubic_c_input)
        layout.addRow("d (sabit terim):", self.cubic_d_input)
        layout.addRow(solve_button)
        layout.addRow(self.cubic_formula)  # Girilen değerlere göre formül burada gösterilecek
        layout.addRow(self.cubic_result)
        tab.setLayout(layout)

    def solve_cubic(self):
        try:
            a = float(self.cubic_a_input.text())
            b = float(self.cubic_b_input.text())
            c = float(self.cubic_c_input.text())
            d = float(self.cubic_d_input.text())
            x = Symbol('x')
            roots = solve(a*x**3 + b*x**2 + c*x + d, x)
            self.cubic_formula.setText(f"Denklem: {a}x^3 + {b}x^2 + {c}x + {d} = 0")  # Girilen değerlerle formül yazdırılıyor
            self.cubic_result.setText(f"Kökler: {roots}")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli sayılar girin.")

    # Faktöriyel Hesaplama
    def init_factorial_tab(self, tab):
        layout = QFormLayout()
        self.factorial_input = QLineEdit()
        self.factorial_result = QLabel("Sonuç: ")

        calc_button = QPushButton("Hesapla")
        calc_button.clicked.connect(self.calculate_factorial)

        layout.addRow(QLabel("Faktöriyel Hesaplama"))
        layout.addRow("n (sayı):", self.factorial_input)
        layout.addRow(calc_button)
        layout.addRow(self.factorial_result)
        tab.setLayout(layout)

    def calculate_factorial(self):
        try:
            n = int(self.factorial_input.text())
            if n >= 0:
                result = factorial(n)
                self.factorial_result.setText(f"Sonuç: {result}")
            else:
                self.factorial_result.setText("Pozitif bir sayı giriniz.")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli bir sayı girin.")

    # Seri Toplamı Hesaplama (Faulhaber Formülü ile)
    def init_faulhaber_tab(self, tab):
        layout = QFormLayout()
        self.faulhaber_n_input = QLineEdit()
        self.faulhaber_p_input = QLineEdit()
        self.faulhaber_result = QLabel("Sonuç: ")
        self.faulhaber_formula = QLabel("Seri: 1^p + 2^p + ... + n^p")  # Seriyi göster

        calc_button = QPushButton("Hesapla")
        calc_button.clicked.connect(self.calculate_faulhaber)

        layout.addRow(QLabel("Seri Toplamı Hesaplama (Faulhaber Formülü ile): 1^p + 2^p + ... + n^p"))
        layout.addRow("n (terim sayısı):", self.faulhaber_n_input)
        layout.addRow("p (kuvvet):", self.faulhaber_p_input)
        layout.addRow(calc_button)
        layout.addRow(self.faulhaber_formula)
        layout.addRow(self.faulhaber_result)
        tab.setLayout(layout)

    def calculate_faulhaber(self):
        try:
            n = int(self.faulhaber_n_input.text())
            p = int(self.faulhaber_p_input.text())
            series = [f"{i}^{p}" for i in range(1, n+1)]
            # İlk 3 ve Son 3 terim
            if len(series) > 6:
                series_display = ' + '.join(series[:3]) + " + ... + " + ' + '.join(series[-3:])
            else:
                series_display = ' + '.join(series)
            result = sum(k**p for k in range(1, n+1))  # Seri hesaplanıyor
            self.faulhaber_formula.setText(f"Seri: {series_display}")
            self.faulhaber_result.setText(f"Sonuç: {result}")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli sayılar girin.")

    # Permütasyon Hesaplama
    def init_permutation_tab(self, tab):
        layout = QFormLayout()
        self.permutation_n_input = QLineEdit()
        self.permutation_r_input = QLineEdit()
        self.permutation_result = QLabel("Sonuç: ")

        calc_button = QPushButton("Hesapla")
        calc_button.clicked.connect(self.calculate_permutation)

        layout.addRow(QLabel("Permütasyon Hesaplama: P(n, r)"))
        layout.addRow("n:", self.permutation_n_input)
        layout.addRow("r:", self.permutation_r_input)
        layout.addRow(calc_button)
        layout.addRow(self.permutation_result)
        tab.setLayout(layout)

    def calculate_permutation(self):
        try:
            n = int(self.permutation_n_input.text())
            r = int(self.permutation_r_input.text())
            result = factorial(n) // factorial(n - r)
            self.permutation_result.setText(f"Sonuç: {result}")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli sayılar girin.")

    # Kombinasyon Hesaplama
    def init_combination_tab(self, tab):
        layout = QFormLayout()
        self.combination_n_input = QLineEdit()
        self.combination_r_input = QLineEdit()
        self.combination_result = QLabel("Sonuç: ")

        calc_button = QPushButton("Hesapla")
        calc_button.clicked.connect(self.calculate_combination)

        layout.addRow(QLabel("Kombinasyon Hesaplama: C(n, r)"))
        layout.addRow("n:", self.combination_n_input)
        layout.addRow("r:", self.combination_r_input)
        layout.addRow(calc_button)
        layout.addRow(self.combination_result)
        tab.setLayout(layout)

    def calculate_combination(self):
        try:
            n = int(self.combination_n_input.text())
            r = int(self.combination_r_input.text())
            result = factorial(n) // (factorial(r) * factorial(n - r))
            self.combination_result.setText(f"Sonuç: {result}")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli sayılar girin.")

    # Fibonacci Hesaplama
    def init_fibonacci_tab(self, tab):
        layout = QFormLayout()
        self.fibonacci_input = QLineEdit()
        self.fibonacci_result = QLabel("Sonuç: ")

        calc_button = QPushButton("Hesapla")
        calc_button.clicked.connect(self.calculate_fibonacci)

        layout.addRow(QLabel("Fibonacci Sayısı Hesaplama"))
        layout.addRow("n (sayı):", self.fibonacci_input)
        layout.addRow(calc_button)
        layout.addRow(self.fibonacci_result)
        tab.setLayout(layout)

    def calculate_fibonacci(self):
        try:
            n = int(self.fibonacci_input.text())
            if n >= 0:
                a, b = 0, 1
                for _ in range(n):
                    a, b = b, a + b
                self.fibonacci_result.setText(f"Sonuç: {n}. Fibonacci sayısı budur: {a}")
            else:
                self.fibonacci_result.setText("Pozitif bir sayı giriniz.")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli bir sayı girin.")

    # Asal Sayı Kontrolü
    def init_prime_check_tab(self, tab):
        layout = QFormLayout()
        self.prime_input = QLineEdit()
        self.prime_result = QLabel("Sonuç: ")

        check_button = QPushButton("Kontrol Et")
        check_button.clicked.connect(self.check_prime)

        layout.addRow(QLabel("Asal Sayı Kontrolü"))
        layout.addRow("n (sayı):", self.prime_input)
        layout.addRow(check_button)
        layout.addRow(self.prime_result)
        tab.setLayout(layout)

    def check_prime(self):
        try:
            n = int(self.prime_input.text())
            if n < 2:
                self.prime_result.setText(f"{n} asal değil.")
            else:
                for i in range(2, int(n**0.5) + 1):
                    if n % i == 0:
                        self.prime_result.setText(f"{n} asal değil.")
                        return
                self.prime_result.setText(f"{n} asal bir sayıdır.")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli bir sayı girin.")

    # EBOB Hesaplama
    def init_gcd_tab(self, tab):
        layout = QFormLayout()
        self.gcd_a_input = QLineEdit()
        self.gcd_b_input = QLineEdit()
        self.gcd_result = QLabel("Sonuç: ")

        calc_button = QPushButton("EBOB Hesapla")
        calc_button.clicked.connect(self.calculate_gcd)

        layout.addRow(QLabel("EBOB Hesaplama"))
        layout.addRow("a:", self.gcd_a_input)
        layout.addRow("b:", self.gcd_b_input)
        layout.addRow(calc_button)
        layout.addRow(self.gcd_result)
        tab.setLayout(layout)

    def calculate_gcd(self):
        try:
            a = int(self.gcd_a_input.text())
            b = int(self.gcd_b_input.text())
            result = gcd(a, b)
            self.gcd_result.setText(f"EBOB: {result}")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli sayılar girin.")

    # EKOK Hesaplama
    def init_lcm_tab(self, tab):
        layout = QFormLayout()
        self.lcm_a_input = QLineEdit()
        self.lcm_b_input = QLineEdit()
        self.lcm_result = QLabel("Sonuç: ")

        calc_button = QPushButton("EKOK Hesapla")
        calc_button.clicked.connect(self.calculate_lcm)

        layout.addRow(QLabel("EKOK Hesaplama"))
        layout.addRow("a:", self.lcm_a_input)
        layout.addRow("b:", self.lcm_b_input)
        layout.addRow(calc_button)
        layout.addRow(self.lcm_result)
        tab.setLayout(layout)

    def calculate_lcm(self):
        try:
            a = int(self.lcm_a_input.text())
            b = int(self.lcm_b_input.text())
            result = abs(a * b) // gcd(a, b)
            self.lcm_result.setText(f"EKOK: {result}")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli sayılar girin.")

    # Logaritma Hesaplama
    def init_logarithm_tab(self, tab):
        layout = QFormLayout()
        self.log_x_input = QLineEdit()
        self.log_base_input = QLineEdit()
        self.log_result = QLabel("Sonuç: ")

        calc_button = QPushButton("Logaritma Hesapla")
        calc_button.clicked.connect(self.calculate_logarithm)

        layout.addRow(QLabel("Logaritma Hesaplama: log_b(x)"))
        layout.addRow("x:", self.log_x_input)
        layout.addRow("Taban (b):", self.log_base_input)
        layout.addRow(calc_button)
        layout.addRow(self.log_result)
        tab.setLayout(layout)

    def calculate_logarithm(self):
        try:
            x = float(self.log_x_input.text())
            base = float(self.log_base_input.text())
            result = log(x, base)
            self.log_result.setText(f"Sonuç: {result}")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli sayılar girin.")

    # Üstel Fonksiyon Hesaplama
    def init_exponential_tab(self, tab):
        layout = QFormLayout()
        self.exp_input = QLineEdit()
        self.exp_result = QLabel("Sonuç: ")

        calc_button = QPushButton("Üstel Fonksiyon Hesapla")
        calc_button.clicked.connect(self.calculate_exponential)

        layout.addRow(QLabel("Üstel Fonksiyon Hesaplama: e^x"))
        layout.addRow("x:", self.exp_input)
        layout.addRow(calc_button)
        layout.addRow(self.exp_result)
        tab.setLayout(layout)

    def calculate_exponential(self):
        try:
            x = float(self.exp_input.text())
            result = exp(x)
            self.exp_result.setText(f"Sonuç: {result}")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli bir sayı girin.")

    # Trigonometrik Fonksiyon Hesaplama
    def init_trigonometry_tab(self, tab):
        layout = QFormLayout()
        self.angle_input = QLineEdit()
        self.trig_func_input = QLineEdit()
        self.trig_result = QLabel("Sonuç: ")

        calc_button = QPushButton("Hesapla")
        calc_button.clicked.connect(self.calculate_trig)

        layout.addRow(QLabel("Trigonometrik Fonksiyon Hesaplama (sin, cos, tan)"))
        layout.addRow("Açı (derece):", self.angle_input)
        layout.addRow("Fonksiyon (sin, cos, tan):", self.trig_func_input)
        layout.addRow(calc_button)
        layout.addRow(self.trig_result)
        tab.setLayout(layout)

    def calculate_trig(self):
        try:
            angle = float(self.angle_input.text())
            func = self.trig_func_input.text().lower()

            if func == 'sin':
                result = sin(radians(angle))
            elif func == 'cos':
                result = cos(radians(angle))
            elif func == 'tan':
                result = tan(radians(angle))
            else:
                self.trig_result.setText("Geçersiz fonksiyon. (sin, cos, tan)")
                return

            self.trig_result.setText(f"Sonuç: {result}")
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli sayılar girin.")

    # Telefon Rehberi için ana menü
    def init_rehber_tab(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Telefon Rehberi İşlemleri"))
        buttons = [
            ("Kişi Ekle", self.show_add_contact),
            ("Kişileri Listele", self.show_list_contacts),
            ("Kişi Ara", self.show_search_contact),
            ("Kişiyi Düzelt", self.show_edit_contact),
            ("Kişiyi Sil", self.show_delete_contact)
        ]

        for btn_text, method in buttons:
            btn = QPushButton(btn_text)
            btn.clicked.connect(method)
            layout.addWidget(btn)

        self.rehber_tab.setLayout(layout)

        # Rehber verileri
        self.contacts = {}  # Verileri burada tutalım

    # Telefon Rehberi için her işlem fonksiyonları
    def show_add_contact(self):
        self.open_contact_tab("Kişi Ekle", self.init_add_contact_tab)

    def show_list_contacts(self):
        self.open_contact_tab("Kişileri Listele", self.init_list_contacts_tab)

    def show_search_contact(self):
        self.open_contact_tab("Kişi Ara", self.init_search_contact_tab)

    def show_edit_contact(self):
        self.open_contact_tab("Kişiyi Düzelt", self.init_edit_contact_tab)

    def show_delete_contact(self):
        self.open_contact_tab("Kişiyi Sil", self.init_delete_contact_tab)

    # Kişi ekleme işlemi
    def init_add_contact_tab(self, tab):
        layout = QFormLayout()
        self.contact_name_input = QLineEdit()
        self.contact_phone_input = QLineEdit()
        self.add_contact_result = QLabel("Sonuç: ")

        add_button = QPushButton("Ekle")
        add_button.clicked.connect(self.add_contact)

        layout.addRow("İsim:", self.contact_name_input)
        layout.addRow("Telefon:", self.contact_phone_input)
        layout.addRow(add_button)
        layout.addRow(self.add_contact_result)
        tab.setLayout(layout)

    def add_contact(self):
        name = self.contact_name_input.text()
        phone = self.contact_phone_input.text()
        if name and phone:
            self.contacts[name] = phone  # Verileri sözlüğe ekle
            self.add_contact_result.setText(f"Kişi Eklendi: {name}, {phone}")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun.")

    # Kişileri Listele
    def init_list_contacts_tab(self, tab):
        layout = QVBoxLayout()
        self.contacts_table = QTableWidget()
        self.contacts_table.setColumnCount(2)
        self.contacts_table.setHorizontalHeaderLabels(["İsim", "Telefon"])
        self.contacts_table.setRowCount(len(self.contacts))

        for row, (name, phone) in enumerate(self.contacts.items()):
            self.contacts_table.setItem(row, 0, QTableWidgetItem(name))
            self.contacts_table.setItem(row, 1, QTableWidgetItem(phone))

        layout.addWidget(self.contacts_table)
        tab.setLayout(layout)

    # Kişi arama işlemi
    def init_search_contact_tab(self, tab):
        layout = QFormLayout()
        self.contact_search_input = QLineEdit()
        self.search_contact_result = QLabel("Sonuç: ")

        search_button = QPushButton("Ara")
        search_button.clicked.connect(self.search_contact)

        layout.addRow("Aramak istediğiniz kişinin ismi:", self.contact_search_input)
        layout.addRow(search_button)
        layout.addRow(self.search_contact_result)
        tab.setLayout(layout)

    def search_contact(self):
        name = self.contact_search_input.text()
        if name:
            # Büyük küçük harf duyarlılığını kaldırıyoruz ve ismi arıyoruz
            found = False
            for stored_name, phone in self.contacts.items():
                if stored_name.lower() == name.lower():
                    self.search_contact_result.setText(f"Kişi Bulundu: {stored_name}, Telefon: {phone}")
                    found = True
                    break
            if not found:
                self.search_contact_result.setText(f"{name} rehberde bulunamadı.")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen bir isim girin.")

    # Kişi düzenleme işlemi
    def init_edit_contact_tab(self, tab):
        layout = QFormLayout()
        self.contact_search_input = QLineEdit()
        self.new_phone_input = QLineEdit()
        self.edit_contact_result = QLabel("Sonuç: ")

        search_button = QPushButton("Düzenle")
        search_button.clicked.connect(self.edit_contact)

        layout.addRow("Düzenlemek istediğiniz kişinin ismi:", self.contact_search_input)
        layout.addRow("Yeni telefon numarası:", self.new_phone_input)
        layout.addRow(search_button)
        layout.addRow(self.edit_contact_result)
        tab.setLayout(layout)

    def edit_contact(self):
        name = self.contact_search_input.text()
        new_phone = self.new_phone_input.text()
        if name in self.contacts and new_phone:
            self.contacts[name] = new_phone  # Telefon numarasını güncelle
            self.edit_contact_result.setText(f"{name} kişisinin yeni telefon numarası: {new_phone}")
        else:
            QMessageBox.warning(self, "Hata", "Kişi bulunamadı veya geçersiz telefon numarası.")

    # Kişi Silme
    def init_delete_contact_tab(self, tab):
        layout = QFormLayout()
        self.contact_delete_input = QLineEdit()
        self.delete_contact_result = QLabel("Sonuç: ")

        delete_button = QPushButton("Sil")
        delete_button.clicked.connect(self.delete_contact)

        layout.addRow("Silmek istediğiniz kişinin ismi:", self.contact_delete_input)
        layout.addRow(delete_button)
        layout.addRow(self.delete_contact_result)
        tab.setLayout(layout)

    def delete_contact(self):
        name = self.contact_delete_input.text()
        if name in self.contacts:
            del self.contacts[name]  # Kişiyi sil
            self.delete_contact_result.setText(f"{name} rehberden silindi.")
        else:
            QMessageBox.warning(self, "Hata", "Kişi bulunamadı.")

    # Seçilen kişi işlemi için yeni sekme aç
    def open_contact_tab(self, title, init_function):
        new_tab = QWidget()
        self.tabs.addTab(new_tab, title)
        init_function(new_tab)
        self.tabs.setCurrentWidget(new_tab)

# Giriş Ekranı
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Giriş Ekranı")
        self.setGeometry(400, 200, 300, 150)

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(QLabel("Kullanıcı Adı:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Şifre:"))
        layout.addWidget(self.password_input)

        login_button = QPushButton("Giriş")
        login_button.clicked.connect(self.check_login)

        layout.addWidget(login_button)
        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Şifre "1234" olarak ayarlandı
        if username == "Alper" and password == "1234":
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