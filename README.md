# Proje3
Masaüstü Uygulaması (proje1 ve proje2 kodlarını ve Veritabanı bağlantısını kullanır.)

## PyQt6 Matematik Denklem Çözümleri ve Telefon Rehberi Uygulaması

Bu proje, PyQt6 ile geliştirilmiş iki sekmeli bir masaüstü uygulamasıdır. İlk sekmede matematiksel denklem çözümleri yapılabilirken, ikinci sekmede bir telefon rehberi yönetilebilir. Telefon rehberi bilgileri bir MySQL veritabanına kaydedilmektedir.

## Özellikler

- **Matematik Denklem Çözümleri Sekmesi**: Kullanıcı, ikinci dereceden denklemleri çözmek için `a`, `b`, `c` katsayılarını girebilir ve sonucu görüntüleyebilir.
- **Telefon Rehberi Sekmesi**: Kullanıcı, isim ve telefon numarası ekleyebilir, rehberdeki kişileri listeleyebilir ve veritabanına kaydedebilir.
- **Giriş Ekranı**: Uygulama başlarken kullanıcı adı ve şifre sorulmaktadır. Doğru giriş yapıldığında uygulamaya erişim sağlanır.

### Giriş Bilgileri

- **Kullanıcı Adı**: `Alper`
- **Şifre**: `5276`

### Ekran Görüntüleri

#### 1. Giriş Ekranı
![Giriş Ekranı](screenshots/login_screen.png)

#### 2. Matematik Denklem Çözümleri Sekmesi
![Matematik Sekmesi](screenshots/math_tab.png)

#### 3. Telefon Rehberi Sekmesi
![Telefon Rehberi Sekmesi](screenshots/rehber_tab.png)

## Kurulum

### Gereksinimler

- Python 3.8 veya üzeri
- Aşağıdaki Python kütüphanelerinin yüklenmesi gerekmektedir:
  - PyQt6
  - mysql-connector-python
- MySQL Server

### Python Paketlerinin Kurulumu

Gerekli kütüphaneleri aşağıdaki komutlarla kurabilirsiniz:

```bash
pip install PyQt6 mysql-connector-python
