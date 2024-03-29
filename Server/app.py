from flask import make_response, request
from models import Item, Cart, Customer, Store #, checkout
from config import db, app



#CUSTOMERS

#GET
@app.route('/customers', methods=['GET', 'POST'])
def customers():
    customers = Customer.query.all()
    if request.method == 'GET':
        return make_response([customer.to_dict(rules=('-carts', )) for customer in customers], 200)
    
    elif request.method == 'POST':
        form_data = request.get_json()
        try:
            new_customer_obj = Customer(
                name = form_data['name'],
                user_name = form_data['username'],
                password = form_data['password'],
                email = form_data['email'],
                age = form_data['age']
            )
            db.session.add(new_customer_obj)
            db.session.commit()
            resp = make_response(new_customer_obj.to_dict(), 201)
            return resp
        except ValueError:
            resp = make_response({ "errors": ["Validation Errors!"]}, 400)
    return resp



#CUSTOMERS BY ID

#GET, PATCH AND DELETE
@app.route('/customers/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def customer_by_id(id):
    customer = Customer.query.filter_by(id = id).first()
    if customer:
        if request.method == 'GET':
            resp = make_response(customer.to_dict(), 200)
        elif request.method == 'PATCH':
            form_data = request.get_json()
            try:
                for attr in form_data:
                    setattr(customer, attr, form_data.get(attr))
                db.session.commit()
                resp = make_response(customer.to_dict(), 202)
            except ValueError:
                resp = make_response({ "errors": ["Validation Errors"]}, 400)
        elif request.method == 'DELETE':
            db.session.delete(customer)
            db.session.commit()
            resp = make_response({}, 204)

    else:
        resp = make_response({"error" : "No Customer Found!"}, 404)    
    return resp

# ALL STORES

#GET
@app.route('/stores', methods=['GET'])
def stores():
    if request.method == 'GET':
        stores = Store.query.all()
        store_dict = [store.to_dict() for store in stores]
        resp = make_response(store_dict, 200)
    return resp


#STORES BY ID

#GET AND PATCH
@app.route('/stores/<int:id>', methods = ['GET', 'PATCH'])
def store_by_id(id):
    store_by_id = Store.query.filter_by(id = id).first()
    if store_by_id:

        if request.method == 'GET':
            resp = make_response(store_by_id.to_dict(rules = ()), 200)
        elif request.method == 'PATCH':
            form_data = request.get_json()
            try:
                for attr in form_data:
                    setattr(store_by_id, attr, form_data.get(attr))
                db.session.commit()
                resp = make_response(store_by_id.to_dict(), 202)
            except ValueError:
                resp = make_response({ "errors": ["Validation Errors"]}, 400)
    else:
        resp = make_response({"error": "Store not found"}, 404)
    return resp




#CARTS

#GET, POST AND PATCH
@app.route('/carts', methods = ['GET', 'POST', 'PATCH'])
def carts():
    carts = Cart.query.all()
    if carts:

        if request.method == 'GET':
            resp = make_response([cart.to_dict(rules = ('-checkout.store.password','-customer.password', '-checkout.store.items')) for cart in carts], 200)
        elif request.method == 'POST':
            print(request)
            form_data = request.get_json()
            print('Received form data:', form_data)
            try:
                new_cart_obj = Cart(
                    customer_id = form_data['customer_id']
                )
                db.session.add(new_cart_obj)
                db.session.commit()
                resp = make_response(new_cart_obj.to_dict(rules = ('-checkout.store.password','-customer.password', '-checkout.store.items')), 201)
            except ValueError:
                resp = make_response({ "errors": ["Validation Errors"]}, 400)
        elif request.method == 'PATCH':
            form_data = request.get_json()
            try:
                for attr in form_data:
                    setattr(store_by_id, attr, form_data.get(attr))
                db.session.commit()
                resp = make_response(store_by_id.to_dict(), 202)
            except ValueError as e:
                print('Validation error:', e)
                resp = make_response({ "errors": ["Validation Errors"]}, 400)
                
    else:
        resp = make_response({ "error": "No Cart Found!"}, 404)
    return resp



#CARTS BY ID

#GET, POST AND PATCH
@app.route('/carts/<int:id>', methods=['GET', 'POST', 'PATCH'])
def cart_by_id(id):
    cart_by_id = Cart.query.filter_by(id = id).first()
    if cart_by_id:

        if request.method == 'GET':
            resp = make_response(cart_by_id.to_dict(rules = ('-checkout.store.password','-customer.password', '-checkout.store.items')), 200)

        elif request.method == 'POST':
            form_data = request.get_json()
            try:
                new_cart_obj = Cart(
                    customer_id = form_data['customer_id']
                )
                db.session.add(new_cart_obj)
                db.session.commit()
                resp = make_response(new_cart_obj.to_dict(), 201)
            except ValueError:
                resp = make_response({ "errors": ["Validation Errors"]}, 400)

        elif request.method == 'PATCH':
            form_data = request.get_json()
            try:
                for attr in form_data:
                    setattr(store_by_id, attr, form_data.get(attr))
                db.session.commit()
                resp = make_response(store_by_id.to_dict(), 202)
            except ValueError as e:
                print('Validation error:', e)
                resp = make_response({ "errors": ["Validation Errors"]}, 400)
                
    else:
        resp = make_response({ "error": "No Cart Found!"}, 404)
    return resp



# CARTS BY CUSTOMER_ID


#GET, POST AND PATCH
@app.route('/carts/customer_<int:customer_id>', methods=['GET', 'POST', 'PATCH'])
def cart_by_customer_id(customer_id):
    cart_by_customer_id = Cart.query.filter_by(customer_id = customer_id).first()
    if cart_by_customer_id:

        if request.method == 'GET':
            resp = make_response(cart_by_customer_id.to_dict(rules = ('-checkout.store.password','-customer.password', '-checkout.store.items')), 200)
        elif request.method == 'POST':
            form_data = request.get_json()
            try:
                new_cart_obj = Cart(
                    customer_id = form_data['customer_id']
                )
                db.session.add(new_cart_obj)
                db.session.commit()
                resp = make_response(new_cart_obj.to_dict(), 201)
            except ValueError:
                resp = make_response({ "errors": ["Validation Errors"]}, 400)
        elif request.method == 'PATCH':
            form_data = request.get_json()
            try:
                for attr in form_data:
                    setattr(store_by_id, attr, form_data.get(attr))
                db.session.commit()
                resp = make_response(store_by_id.to_dict(), 202)
            except ValueError:
                resp = make_response({ "errors": ["Validation Errors"]}, 400)
                
    else:
        resp = make_response({ "error": "No Cart Found!"}, 404)
    return resp



#ALL ITEMS


#GET
@app.route('/items', methods=['GET'])
def items():
    if request.method == 'GET':
        items = Item.query.all()
    return make_response([item.to_dict(rules=('-store_id', )) for item in items], 200)



@app.route('/checkout', methods=[''])



#ITEMS BY ID


#GET, POST, PATCH AND DELETE
@app.route('/items/<int:id>', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def item_by_id(id):
    item_by_id = Item.query.filter_by(id = id).first()
    if item_by_id:
        if request.method == 'GET':
            resp = make_response(item_by_id.to_dict(), 200)
        elif request.method == 'POST':
            form_data = request.get_json()
            try:
                new_item_obj = Item(
                    name = form_data['name'],
                    type = form_data['type'],
                    description = form_data['description'],
                    quantity = form_data['quantity'],
                    price = form_data['price']
                )
                db.session.add(new_item_obj)
                db.session.commit()
                resp = make_response(new_item_obj.to_dict(), 201)
            except ValueError:
                resp = make_response({ "errors" : ["Validation Errors!"]}, 400)
        elif request.method == 'PATCH':
            form_data = request.get_json()
            try:
                for attr in form_data:
                    setattr(item_by_id, attr, form_data.get(attr))
                db.session.commit()
                resp = make_response(item_by_id.to_dict(), 202)
            except ValueError:
                resp = make_response({ "errors": ["Validation Errors"]}, 400)
        elif request.method == 'DELETE':
            db.session.delete(item_by_id)
            db.session.commit()
            resp = make_response({}, 204)

    else:
        resp = make_response({"error": "No Item found!"})
    return resp

#CART ITEMS

@app.route('/cart_items', methods = ['POST'])
def add_to_cart():
    try:
        data = request.get_json()
        cart_id = data['cart_id']
        item_id = data['item_id']
        return make_response({'message': 'Item added to cart successfully'}, 201)
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    


#REMOVE FROM CART
    
@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    try:
        data = request.get_json()
        cart_id = data['cart_id']
        item_id = data['item_id']
        return make_response({'message': 'Item removed from cart successfully'})
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)