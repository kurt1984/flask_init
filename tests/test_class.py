from src.model import Customer

def test_class_init():
    customer = Customer(list = [1, "40170","1348959766","14/11/2013","Hair Band","Female"])
    assert customer.__dict__ == {"id":1, "transaction_id":"40170",
    "customer_id": "1348959766","date":"14/11/2013","product":"Hair Band","gender":"Female"}