#secure klasöründe isminde users bulunan tüm dosyaların githuba yüklenmesi gitignore eklenerek engellenmiştir.
#spotify bot için
#secure klasörüde spotify_users.py oluşturulmalıdır aşağıdaki şekilde bir kod ile kullanıcı listesi tutulabilir.
from data.user import User
users = [User(name="abc@gmail.com", password="aaaa"),
    User(name="acd@hotmail.com", password="dddd")]