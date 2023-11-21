from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
import re

from config import db

cart_items = db.Table(
    'cart_items',
    db.Column('cart_id', db.Integer, db.ForeignKey('carts.id'), primary_key=True),
    db.Column('item_id', db.Integer, db.ForeignKey('items.id'), primary_key=True)
)



#ITEMS (1)



class Item(db.Model, SerializerMixin):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    position = db.Column(db.String)
    team = db.Column(db.String)
    avg_points = db.Column(db.Integer)
    pos_rank = db.Column(db.Integer)
    price = db.Column(db.Float)
    img = db.Column(db.String)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    store = db.relationship('Store', back_populates = 'items')

    serialize_rules = ('-store.items', )

    @validates('name')
    def validates_name(self, key, name):
        if name:
            return name
        else:
            raise ValueError('Name must be between 3 and 100 characters incusive!')
    
    @validates('position')
    def validates_type(self, key, position):
        if position:
            return position
        else:
            raise ValueError('')
    
    @validates('price')
    def validates_price(self, key, price):
        if price:
            return price
        else:
            raise ValueError('')

    def __repr__(self):
        return f''



#CART (2)



class Cart(db.Model, SerializerMixin):
    __tablename__ = 'carts'


    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    customer = db.relationship('Customer', back_populates = 'carts')

    checkout = db.relationship('Checkout', back_populates = 'cart', cascade ='all, delete-orphan')

    serialize_rules = ('-customer.carts', '-items.cart', '-checkout.cart')
    

    def __repr__(self):
        return f''




#CUSTOMER (3)



class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    user_name = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    age = db.Column(db.Integer)
    membership = db.Column(db.Boolean, default = False)

    carts = db.relationship('Cart', back_populates = 'customer', cascade = 'all, delete-orphan')

    items = association_proxy('Cart', 'items')

    serialize_rules = ('-carts.customer', )


    @validates('name')
    def validates_name(self, key, name):
        if 3 <= len(name):
            return name
        else:
            raise ValueError('Name must be between 3 and 20 characters incusive!')
        
    @validates('password')
    def validates_password(self, key, password):
        if len(password) < 6:
            raise ValueError("Password must have at lest 6 letters!")
        elif re.search('[0-9]',password) is None:
            raise ValueError("Password must have a number in it!")
        elif re.search('[A-Z]',password) is None: 
            raise ValueError("Password must have a capital letter in it!")
        else:
            return password
    @validates('email')
    def validates_email(self, key, email):
        if 3 <= len(email):
            return email
        else:
            raise ValueError('Email must be between 3 and 20 characters incusive!')
        
    @validates('age')
    def validates_age(self, key, age):
        if 13 <= age <= 100:
            return age
        else:
            raise ValueError('Age must be between 13 and 100 incusive!')
    

    def __repr__(self):
        return f''




#STORE (4)



class Store(db.Model, SerializerMixin):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    location = db.Column(db.String)
    hours = db.Column(db.Integer)

    items = db.relationship('Item', back_populates = 'store', cascade ='all, delete-orphan')
    checkouts = db.relationship('Checkout', back_populates = 'store', cascade ='all, delete-orphan')

    serialize_rules = ('-items.store', '-checkouts.store')

    @validates('name')
    def validates_name(self, key, name):
        if 3 <= len(name) :
            return name
        else:
            raise ValueError('Name must be between 3 and 20 characters inclusive!')

    @validates('password')
    def validates_password(self, key, password):
        if len(password) < 6:
            raise ValueError("Password must have at lest 6 letters!")
        elif re.search('[0-9]',password) is None:
            raise ValueError("Password must have a number in it!")
        elif re.search('[A-Z]',password) is None: 
            raise ValueError("Password must have a capital letter in it!")
        else:
            return password
    
    @validates('email')
    def validates_email(self, key, email):
        if 3 <= len(email):
            return email
        else:
            raise ValueError('Email must be between 3 and 15 characters inclusive!')


    def __repr__(self):
        return f''

class Checkout(db.Model, SerializerMixin):
    __tablename__ = 'checkouts'

    id = db.Column(db.Integer, primary_key = True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    cart = db.relationship('Cart', back_populates = 'checkout')
    store = db.relationship('Store', back_populates = 'checkouts')

    customer = association_proxy('Cart', 'customer')
    items = association_proxy('Cart', 'items')

    serialize_rules = ('-cart.checkout', '-store.checkouts')


    def __repr__(self):
        return f''
        