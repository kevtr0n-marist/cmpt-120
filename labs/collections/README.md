# Lab 8 - Collections

In this lab we are going to create a simple inventory management system.

## Step 1 - Setup

First create a new folder inside our `cmpt-120/labs` folder called `collections` and inside that folder create a file called `product.py`. Copy the contents of my `product.py` file on Github into yours. Create a file called `test_collections.py` and copy the contents of my `test_collections.py` file on Github into yours. Finally, create a file called `inventory.py`.

## Step 2 - Defining the Inventory class/constructor.

The next piece of code we are going to define is a class to represent the inventory of a business that sells products. Define the `Inventory` class, it has a single property called `products` which is a __dict__ (dictionary). However, I want the constructor method to take __a single list argument__ which is a __list__. The goal of the constructor method is to build up the `products` dictionary where the product name is the __key__ and the __value__ is the list of products.

In the constructor you should you be iterating through the list of products passed into the constructor and raising a `TypeError` if anything other than a `Product` is passed in.

You can check if a key exists like so:

```py
if "mykey" in my_dictionary.keys():
    pass
```

If the key exists, append the product to the list in the key. If it doesn't exists, set the key to a list containing the product. You can index the value of a dictionary like so:

```py
my_dictionary["mykey"] = [some_list_item]
```

> __Note__: If a list of 3 Products is passed into the constructor that all share the same name, then there should be a single key mapping to a list of 3 products.

## Step 3 - Define methods

1. Define a method called `add` in the `Inventory` class that takes a single argument called `product`. This method should add the product to the existing list inside the `products` dictionary or a create a new key-to-list-value pair if it doesn't exist.

2. Define a method called `remove` in the `Inventory` class that takes two arguments called `product_name` and `product_id`. This method removes a `Product` from a the `products` dictionary that has a matching `uuid`. This method should raise a `ValueError` if there is no key equal to `product_name` or if there is no product with a matching `uuid`.

3. Define a method called `get_products` which takes no arguments and just returns `self.products`.

4. Define a method called `get_products_by_name` which takes a single argument `product_name` and returns the list of products associated with the product name. If there is no key present equalling `product_name` simply return an empty list.

5. Define a method called `get_stock` which takes no arguments and returns the total number of __all__ products in `self.products`.

6. Define a method called `get_stock_by_name` which takes a single argument `product_name` and returns the total number of products associated with that key.

7. Define a method called `get_total_cost` which takes no arguments and returns the summed dollar amount of all products in `self.products`.

8. Define a method called `get_total_cost_by_name` which takes a single argument `product_name` and returns the summed dollar amount of all products associated with that key.

9. Define a method called `in_stock` which takes a single argument `product_name` and returns `True` if there is at least 1 in stock; return `False` otherwise.

## Step 4 - Debugging

Create a file called `main.py`. At the top of the file be sure to import your two classes like so:

```py
from product import Product
from inventory import Inventory
```

Create an instance of `Inventory`, add some `Products` to it, invoke some methods and see if it working as you are intending. Pytest is also a good measure to show you if it is working as I expect it to.

## Step 5 - Unit test

Run pytest and when all your tests are passing, take a screenshot of the output and submit it on Brightspace.
