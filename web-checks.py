import requests
import smtplib
import datetime

# Linkleri ve çalışması gereken saatleri bir sözlük içinde saklayın
links = {
    "http://www.exampl2222e.com": (datetime.time(hour=18, minute=0), datetime.time(hour=22, minute=0)),
      # Yukarıdaki link saat 18 ile 22 arasında çalışması gerekiyor. Eğer çalışmıyorsa mail ile bildir.
    "http://www.exampl22222e.com": (datetime.time(hour=5, minute=0), datetime.time(hour=6, minute=0))
      # Yukarıdaki link saat 5 ile 6 arasında çalışması gerekiyor. Eğer çalışmıyorsa mail ile bildir.
}

# Zamanı kontrol edin
current_time = datetime.datetime.now()

# Her bir linki döngü ile gezin
for url, time_range in links.items():
    check_time_start, check_time_end = time_range
    if check_time_start < current_time.time() < check_time_end:
        # HTTP isteği gönderin
        try:
            r = requests.get(url)
            if r.status_code != 200:
                raise Exception("URL is not accessible")
        except:
            # E-posta gönderin
            server = smtplib.SMTP("mail.example.com") 
            server.login("sender@example.com", "oSSgOW0bb2*00i")
            message = "URL is not accessible: " + url
            server.sendmail("sender@example.com", "received@example.net", message)
            server.quit()
