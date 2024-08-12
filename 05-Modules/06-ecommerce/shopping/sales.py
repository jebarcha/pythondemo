# absolute import - best practice
from ecommerce.customer import contact


# relative import
# from ..customer import contact

print("Sales initialized", __name__)

contact.contact_customer()


def calc_tax():
    pass


def calc_shipping():
    pass


# if we import this module into another module, this code will not be executed because at that point, the name of this module will no longer be main. It will be ecommerce, etc.
if __name__ == "__main__":
    print("Sales started")
    calc_tax()
