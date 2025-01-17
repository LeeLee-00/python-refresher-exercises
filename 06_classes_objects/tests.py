from unittest import TestCase


class Evaluate(TestCase):
    def test_store_creation(self):
        try:
            from student import Store
        except ImportError:
            self.assertTrue(False,
                            "The class Store doesn't exist or could not be imported. Make sure to have a class called Store, and that it is not inside another block.")

        store = Store("JL")
        self.assertEqual(store.name, "JL",
                         "Tried initialising a Store('JL'), but then self.name was not equal to 'JL'. Instead, it was {}.".format(
                             store.name))
        self.assertEqual(store.items, [],
                         "Tried initialising a Store('JL'), but then self.items was not equal to []. Instead, it was {}.".format(
                             store.items))

    def test_add_item(self):
        try:
            from student import Store
        except ImportError:
            self.assertTrue(False,
                            "The class Store doesn't exist or could not be imported. Make sure to have a class called Store, and that it is not inside another block.")

        store = Store("JL")
        self.assertEqual(store.items, [],
                         "Tried initialising a Store('JL'), but then self.items was not equal to []. Instead, it was {}.".format(
                             store.items))

        with self.assertRaises(TypeError,
                               msg="Tried adding an item without providing a price, and an error was not raised. Make sure your add_item method is accepting two arguments: one for the name and one for the price of the item."):
            store.add_item("test")

        store.add_item("test", 25.00)
        self.assertEqual(store.items, [{'name': 'test', 'price': 25.00}],
                         "Added an item with name 'test' and price 25.00, but the store.items was equal to {} instead of the expected ".format(
                             store.items) + " [{'name': 'test', 'price': 25.00}].")

    def test_stock_price(self):
        try:
            from student import Store
        except ImportError:
            self.assertTrue(False,
                            "The class Store doesn't exist or could not be imported. Make sure to have a class called Store, and that it is not inside another block.")

        store = Store("JL")

        store.add_item("test", 25.00)
        store.add_item("test2", 15.00)
        store.add_item("test3", 55.00)

        self.assertEqual(store.stock_price(), 95.00,
                         "Added three items with a combined value of 95.00, but the store.stock_price() method returned {} instead of the expected 95.00. Make sure the method is correctly adding all item prices in the store together and returning that value.".format(
                             store.stock_price()))
