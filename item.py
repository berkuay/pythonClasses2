import csv


class Item:
    pay_Rate = 0.8  # The pay rate after discount
    all = []  # itemler için oluşturulan boş liste

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"price is under zero: {price}"
        assert quantity >= 0, f"quantity is under zero: {quantity}"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)  # all listesine Item clasındaki her instanceı eklemek için oluşturuldu

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_Rate
        # Item.pay_Rate -> sadece class leveldeki değeri alır. Eğer self.pay_Rate kullanılırsa
        # spesifik olarak atanan değeri alır, herhangi bir değer belirtilmezse class levelda olan
        # rate kullanılır.

    def apply_increment(self, increment_value):
        self.__price = self.price + self.__price * increment_value

    @property
    def name(self):
        return self.__name

    # setter olmazsa property sadece okumaya izin vericek private class gibi
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("too long")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):  # objeleri consola yazdırdığında kontrol edebilmek için
        return f"{self.__class__.__name__}('{self.name}','{self.__price}','{self.quantity}')"

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times.
        Regards, berkuay
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()
