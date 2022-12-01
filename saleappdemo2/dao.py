import json, os
from saleappdemo2 import app
import models

#
# def read_json(path):
#     path = os.path.join(app.root_path, path)
#     with open(path, encoding='utf8') as f:
#         return json.load(f)
#
#
# def read_category():
#     return read_json("data/category.json")
#
#
# def read_product():
#     path = os.path.join(app.root_path, "data/product.json")
#     return read_json(path)
#

def load_category():
    return models.Category.query.all()


def load_product(category_id=None, kw=None, from_price=None, to_price=None):
    all_products = models.Product.query.filter(models.Product.active.__eq__(True))

    if category_id:
        all_products = all_products.filter(models.Product.category_id.__eq__(category_id))

    if kw:
        all_products = all_products.filter(models.Product.name.contains(kw))

    if from_price:
        all_products = all_products.filter(models.Product.price.__ge__(from_price))

    if to_price:
        all_products = all_products.filter(models.Product.price.__le__(to_price))
    return all_products.all()


def load_product_by_id(id):
    return models.Product.query.get(id)