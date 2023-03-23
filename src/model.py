
class Customer():
    def __init__(self, list) -> None:
        list_name = ["id", "transaction_id", "customer_id", "date", "product", "gender"]
        self.__dict__ = dict(zip(list_name, list[:6]))



