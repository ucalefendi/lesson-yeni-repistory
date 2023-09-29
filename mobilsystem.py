# CameraSystem classinin each_camera_price adinda hidden bir propertysi olsun. Deyeri 50 verin
class CameraSystem:
    __each_camera_price = 50
    def get_camera_price(self):
        return self.__each_camera_price * self.count

    def set_camara_count(self, count):
        self.count = count

# MemorySystem classinin each_gb_price adinda hidden bir propertysi olsun. Deyeri 10 verin
class MemorySystem:
    __each_gb_price = 10
    def set_memory_amount(self, amount):
        self.amount = amount

    def get_memory_price(self):
        return self.amount * self.__each_gb_price


class SmartDevice(CameraSystem, MemorySystem):
    def __init__(self, camera_count, memory_amount):
        self.set_memory_amount(memory_amount)
        self.set_camara_count(camera_count)

class Phone(SmartDevice):
    def get_total_price(self):
        return self.get_camera_price() + self.get_memory_price()


class PremiumPhone(SmartDevice):
    def __init__(self, charger_price, camera_count, memory_amount):
        self.charger_price = charger_price
        super().__init__(camera_count,memory_amount)

    def get_total_price(self):
        return super().get_total_price() + self.charger_price

class Laptop(SmartDevice):
    def get_total_price(self):
        return self.get_camera_price() + self.get_memory_price() + 150

class Tablet(SmartDevice):
    def get_total_price(self):
        return self.get_camera_price() + self.get_memory_price() + 300


samsung = Phone(4, 256)
iphone = PremiumPhone(70, 3, 128)
dell = Laptop(1, 512)
huawei = Tablet(2, 256)

# print(samsung.get_camera_price())
# print(samsung.get_memory_price())
# print(iphone.get_memory_price())
# print(iphone.get_memory_price()))

def calculate_product_prices(*args):
    price = 0
    for d in args :
        price += d.get_total_price()
    return price

print(calculate_product_prices(samsung, iphone, dell, huawei))