# before

"""
این اصل میگوید هر کلاس فقط و فقط باید یک مسیولیت داشته باشد
در مثال بد زیر کلاس آشپز هم مسیولیت آشپزی دارد هم مسیولیت تحویل غذا
"""


class Chef:
    def cook_food(self): ...
    def deliver_food(self): ...


# after
class Chef2:
    def cook_food(self): ...


class DeliveryService:
    def deliver_food(self): ...
