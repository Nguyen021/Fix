from sqlalchemy import Column, Integer, Boolean, String, Float, ForeignKey, DateTime
from saleappdemo2 import db, app
from datetime import datetime
from sqlalchemy.orm import relationship


class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    def __str__(self):
        return self.name


class Category(Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'category'

    created_date = Column(DateTime, default=datetime.now())
    products = relationship('Product', backref='category', lazy=True)


class Product(Base):
    __table_args__ = {'extend_existing': True}

    __tablename__ = 'product'

    price = Column(Float, default=0)
    created_date = Column(DateTime, default=datetime.now())
    active = Column(Boolean, default=True)
    description = Column(String(200))
    image = Column(String(150))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == "__main__":
    with app.app_context():
        # db.create_all()
        #
        # c1 = Category(name='Điện thoại')
        # c2 = Category(name='Máy tính bảng')
        # c3 = Category(name='Phụ kiện')
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        p1 = Product(name='Galaxy S22 Pro X2', description='Samsung, 128GB', price=25000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     category_id=1)
        p2 = Product(name='Galaxy Fold 4 Plus', description='Samsung, 128GB', price=38000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg',
                     category_id=1)
        p3 = Product(name='Apple Watch S5G', description='Apple, 32GB', price=18000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     category_id=3)
        p4 = Product(name='Galaxy Tab S8S', description='Samsung, 128GB', price=22000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     category_id=2)
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()
