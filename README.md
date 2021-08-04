# plaka_okuyucu
  plaka_oku is a desktop application that detects and extracts plate number from image. It is designed as a car park system. You can detect the plate number with a button from image or a frame from a video and save it to database with the driver's information and the entering time to the car park. When a customer wants to leave you can click the exit button and save the exit time. Records are listed below main page and can be filtered by date.
  
  Programın çalışabilmesi için requirements-gpu.txt içindeki gereksinimler sağlanmalı ve bilgisayarınızda tesseract yüklü olmalı
  ve core dosyası içindeki functions.py dosyasında belirtilen, tesseract'ın bulunduğu klasörü bilgisayarınızdaki tesseract dosya yolu ile değiştirmelisiniz.
  Son olarak custom-416.tflite dosyasını https://drive.google.com/file/d/1VJHhuBKdZwAvg67M-kurYUevTK1HoF92/view?usp=sharing adresinden indirip checkpoints klasörü içine atmalısınız.
  
  yukarıdaki işlemler tamamlandıktan sonra secUiFunctions.py dosyasını çalıştırarak programı kullanabilirsiniz
  
### Uygulama Açılış Ekranı

  ![Alt Text](https://github.com/akbulutmustafa/plaka_oku-otopark/blob/main/data/hompage.PNG)
  
### Resim Seçme

  ![Alt Text](https://github.com/akbulutmustafa/plaka_oku-otopark/blob/main/data/resimsec.PNG)
  
### Plaka Okuma, Kayıt

  ![Alt Text](https://github.com/akbulutmustafa/plaka_oku-otopark/blob/main/data/kayit.PNG)

### Tarih seç
  ![Alt Text](https://github.com/akbulutmustafa/plaka_oku-otopark/blob/main/data/tarihsec2.PNG)

### Seçilmiş tarih
  ![Alt Text](https://github.com/akbulutmustafa/plaka_oku-otopark/blob/main/data/secilmistarih.PNG)

### Düzenleme
  ![Alt Text](https://github.com/akbulutmustafa/plaka_oku-otopark/blob/main/data/editdialog.PNG)
