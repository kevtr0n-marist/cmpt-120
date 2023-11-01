import pytest

from product import Product
from inventory import Inventory

@pytest.fixture(autouse=True)
def setup_and_teardown():
    global inventory
    inventory = Inventory()
    yield
    # teardown

class TestClass:
    
    def test_00(self):
        '''
        Assert constructor works properly.
        '''
        product = Product("Raspberry Pi", "A single board IoT device.", 89.99)
        assert product.name == "Raspberry Pi"
        assert product.uuid != None
        assert product.cost == 89.99

    def test_01(self):
        '''
        Assert that the underlying collection is a dictionary.
        '''
        assert type(inventory.get_products()) == dict

    def test_02(self):
        '''
        Assert products are unique in a set.
        '''
        product_set = set()
        product_set.add(Product("Raspberry Pi", "A single board IoT device.", 89.99))
        product_set.add(Product("Raspberry Pi", "A single board IoT device.", 79.99))
        assert len(product_set) == 1
        assert product_set.pop().cost == 89.99

    def test_03(self):
        '''
        Assert constructor rejects non list arguments.
        '''
        with pytest.raises(TypeError):
            Inventory(1)

    def test_04(self):
        '''
        Assert constructor rejects lists of non-Products.
        '''
        products = [1, 2, 3]
        with pytest.raises(TypeError):
            Inventory(products)

    def test_05(self):
        '''
        Assert constructor works.
        '''
        products = [
            Product("Raspberry Pi", "A single board IoT device.", 89.99),
            Product("Raspberry Pi", "A single board IoT device.", 89.99),
            Product("Raspberry Pi", "A single board IoT device.", 89.99),
            Product("Raspberry Pi", "A single board IoT device.", 89.99),
            Product("Raspberry Pi", "A single board IoT device.", 89.99),
        ]
        inventory = Inventory(products)
        assert inventory.get_stock_by_name("Raspberry Pi") == 5

    def test_06(self):
        '''
        Assert the add method works.
        '''
        inventory.add(Product("Raspberry Pi", "A single board IoT device.", 89.99))
        assert inventory.get_stock_by_name("Raspberry Pi") == 1

    def test_07(self):
        '''
        Assert we can't add non-Products to inventory.
        '''
        with pytest.raises(TypeError):
            inventory.add(1)

    def test_08(self):
        '''
        Assert the remove method works.
        '''
        product = Product("Raspberry Pi", "A single board IoT device.", 89.99)
        inventory.add(product)
        inventory.remove(product.name, product.uuid)
        assert inventory.get_stock_by_name("Raspberry Pi") == 0
    
    def test_09(self):
        '''
        Assert removing an unknown item type errors out.
        '''
        with pytest.raises(ValueError):
            inventory.remove("slkasdlkaj", "laksjdlakjsd")

    def test_10(self):
        '''
        Assert attempting remove a known item that is not in stock errors out.
        '''
        product = Product("Raspberry Pi", "A single board IoT device.", 89.99)
        inventory.add(product)
        with pytest.raises(ValueError):
            inventory.remove(product.name, "slkdjhaksd")


    def test_11(self):
        '''
        Assert that we can accurately determine cost of our stock.
        '''
        products = [
            Product("Raspberry Pi", "A single board IoT device.", 89.99),
            Product("Cheap gum", "A stick of gross gum", 0.01)
        ]
        inventory = Inventory(products)
        assert inventory.get_total_cost() == 90.00

    def test_12(self):
        '''
        Assert that we can accurately determine cost of our stock of a specific item.
        '''
        products = [
            Product("Raspberry Pi", "A single board IoT device.", 89.99),
            Product("Raspberry Pi", "A single board IoT device.", 89.99),
            Product("Cheap gum", "A stick of gross gum", 0.01)
        ]
        inventory = Inventory(products)
        assert inventory.get_total_cost_by_name("Raspberry Pi") == 179.98

    def test_13(self):
        '''
        Assert checking cost of unknown item returns $0.0.
        '''
        assert inventory.get_total_cost_by_name("sldkajsldkajsd") == 0.0

    def test_14(self):
        '''
        Assert that the in_stock method correctly reports if an item is in stock.
        '''
        products = [
            Product("Raspberry Pi", "A single board IoT device.", 89.99),
            Product("Raspberry Pi", "A single board IoT device.", 89.99),
            Product("Cheap gum", "A stick of gross gum", 0.01)
        ]
        inventory = Inventory(products)
        assert inventory.in_stock("Cheap gum")

    def test_15(self):
        '''
        Assert that the in_stock method doesn't error out when checking unknown type.
        '''
        assert not inventory.in_stock("ASkHASDKJABHSKDBASDMN")

