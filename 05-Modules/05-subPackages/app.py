# from ecommerce.sales

# ecommerce.sales.calc_tax()


# much better approach with from statement:
# from ecommerce.sales import calc_tax, calc_shipping

# calc_tax()


# import sales as a module
from ecommerce.shopping import sales

# use the dot to access all the members of the module
sales.calc_tax()
