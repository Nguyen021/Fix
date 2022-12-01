from saleappdemo2 import app, models, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin(app=app, name="E-commerce Administrator", template_mode="bootstrap4")


admin.add_view(ModelView(models.Category, db.session, name='Danh mục'))
admin.add_view(ModelView(models.Product, db.session, name='San Pham'))
