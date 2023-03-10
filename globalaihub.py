#Hatice Kartal
# LinkedIn: https://www.linkedin.com/in/hatice-kartal/
# Github: https://github.com/haticekartal
# e-posta: haticenaz_2001@hotmail.com

#Enis Semerci
# LinkedIn: https://www.linkedin.com/in/enis-semerci-569762244/
# Github: https://github.com/Enisemerci
#e-posta: enissemerci2@gmail.com


#gerekli kitaplıkları içe aktarma
import csv
import datetime


#menu.txt dosyasını oluşturma
def read_menu_list():
    with open('Menu.txt', 'r') as menu_file:
        print(menu_file.read())


#menu_list'in okunması
def main():
    read_menu_list()


#Pizza Üst Sınıfı oluşturduk
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    # Pizza açıklamasının okunması
    def get_description(self):
        return self.description

    # Pizza fiyatının okunması
    def get_cost(self):
        return self.cost


# Pizza türleri, Pizza alt sınıfları
class KlasikPizza(Pizza):

    # pizza açıklaması ve fiyatı
    def __init__(self):
        super().__init__('Klasik Pizza', 45.0)


class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__('Margarita Pizza', 50.0)


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__('Türk Pizza', 60.0)


class SadePizza(Pizza):
    def __init__(self):
        super().__init__('Sade Pizza', 40.0)


# decorator sınıfı oluşturduk,sosların süper sınıfı, Pizza'nın alt sınıfı
class Decorator(Pizza):
    def __init__(self, component, description, cost):
        super().__init__(description, cost)
        self.component = component

    # seçilen pizza ve sosun fiyarlarının toplanıp geri döndürülmesi
    def get_cost(self):
        return self.component.get_cost() + super().get_cost()

    # seçilen pizza ve sosun açıklamalarının geri döndürülmesi
    def get_description(self):
        return super().get_description() + ' ' + self.component.get_description()


# sos çeşitleri, Decorator'un alt sınıfı
class Zeytin(Decorator):
    # sos açıklaması ve fiyatı
    def __init__(self, component):
        super().__init__(component, 'Zeytinli', 5.0)


class Mantar(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Mantarlı', 7.0)


class KeciPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Keçi peynirli', 10.0)


class Et(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Etli', 15.0)


class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Soğanlı', 6.0)


class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Mısırlı', 7.0)


def TC_control(value):
    value = str(value)

    # Tc Kimlik No 11 hanelidir.
    if not len(value) == 11:
        return False

    # Sadece rakamlardan olusur.
    if not value.isdigit():
        return False
    return True

def CC_control(value):
    value = str(value)

    # 16 hanelidir.
    if not len(value) == 16:
        return False

    # Sadece rakamlardan olusur.
    if not value.isdigit():
        return False
    return True


def CC_pass_control(value):
    value = str(value)

    # 4 hanelidir.
    if not len(value) == 4:
        return False

    # Sadece rakamlardan olusur.
    if not value.isdigit():
        return False

    return True


# şuanın tarihini al ve formata uygun hale getir
def Time():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


# main foksiyonu çağırılması (menünün yazılması)
if __name__ == '__main__':
    main()

# pizza seçimi koşulu sağlamıyorsa tekrar sor
while True:

    pizza_choice = int(input('Pizza seçiniz (1-4): '))

    # gelen veriye göre pizza seç
    if pizza_choice == 1:
        pizza = KlasikPizza()
        break
    elif pizza_choice == 2:
        pizza = MargaritaPizza()
        break
    elif pizza_choice == 3:
        pizza = TurkPizza()
        break
    elif pizza_choice == 4:
        pizza = SadePizza()
        break
    else:
        print('Geçersiz pizza kodu.\n')

# sos seçimi koşulu sağlamıyorsa tekrar sor
while True:

    sauce_choice = int(input('Sos seçiniz (11-16): '))

    if sauce_choice == 11:
        sauce = Zeytin(pizza)
        break
    elif sauce_choice == 12:
        sauce = Mantar(pizza)
        break
    elif sauce_choice == 13:
        sauce = KeciPeyniri(pizza)
        break
    elif sauce_choice == 14:
        sauce = Et(pizza)
        break
    elif sauce_choice == 15:
        sauce = Sogan(pizza)
        break
    elif sauce_choice == 16:
        sauce = Misir(pizza)
        break
    else:
        print('Geçersiz sos kodu.\n')

total_cost = sauce.get_cost()

# pizza, sos seçimini ve toplam fiyatı yazdır
print(f'\nSeçiminiz : {sauce.get_description()}\nToplam tutar: {total_cost:.2f} TL\n')

# sipariş onayı kontrol
while True:
    # sipariş onayı iste
    aprvl = input('Siparişi Onayla (e/h)').lower()

    # onay verilir ise gir
    if aprvl == 'e':

        name = input('\nLütfen isminizi giriniz: ')

        # TC No kontrol
        while True:
            id_num = input('Lütfen TC kimlik numaranızı giriniz: ')
            if TC_control(id_num) is True:
                break
            else:
                print('Hatalı TC NO\n')

        # CC No kontrol
        while True:
            cc_num = input('Lütfen kredi kartı numaranızı giriniz: ')
            if CC_control(cc_num) is True:
                break
            else:
                print('Kart numarası 16 haneli ve rakamlardan oluşmalıdır\n')

        # CC password kontrol
        while True:
            cc_password = input('Lütfen kredi kartı şifrenizi giriniz: ')
            if CC_pass_control(cc_password) is True:
                break
            else:
                print('Kart şifresi 4 haneli ve rakamlardan oluşmalıdır\n')

        dt_string = Time()

        # csv dosyasını aç eğer yok ise oluştur ve kullanıcı bilgilerini, siparişi, tutarı ve zamanı yaz
        with open('Orders_Database.csv', 'a') as db_file:
            db_writer = csv.writer(db_file)
            db_writer.writerow([name, id_num, sauce.get_description(), total_cost, cc_num, cc_password, dt_string])

        print(f'\nTeşekkürler {name}! {sauce.get_description()} siparişiniz alınmıştır.')
        print(f'Toplam tutar: {total_cost:.2f} TL')
        break

    # onay verilmez ise iptal et ve çık
    elif aprvl == 'h':
        print('Seçiminiz iptal edildi')
        break

    # yanlış tuşlanırsa tekrar sor (while a geri dön)
    else:
        print('\nHatalı giriş\nLütfen tekrar giriniz.\n')

