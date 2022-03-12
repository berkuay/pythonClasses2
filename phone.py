from item import Item

class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        #Call to super funct to have acces to all attributes/methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments

        assert broken_phones >= 0, f"broken phones is under zero: {broken_phones}"

        # Assign to self object

        self.broken_phones = broken_phones

        # Actions to execute