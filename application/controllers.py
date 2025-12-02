from flask import Flask,redirect,render_template,request
from flask import current_app as app
from .models import *


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username = username).first()
        if user:
            if user.password == password:
                if user.role == 'seller':
                    return redirect('/admin-dashboard')
                else:
                    return redirect(f'/user-dashboard/{user.id}')
            else:
                return render_template('invalid_pass.html')
        else:
            return render_template('user-not-found.html')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        role = request.form.get('role')
        password = request.form.get('password')
        name_user = User.query.filter_by(username=username).first()
        if name_user:
            return "Username already exists"
        email_user = User.query.filter_by(email=email).first()
        if email_user:
            return "Email already registered"
        new_user = User(username=username, email=email, role=role, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')


@app.route('/admin-dashboard')
def manager():
    admin_user = User.query.filter_by(role = 'seller').first()
    all_products = Products.query.all()
    return render_template('admin-dashboard.html' , admin_user = admin_user, all_products = all_products)


@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        quantity = request.form.get('quantity')
        amount = request.form.get('amount')
        new_product = Products(name=name, category=category, quantity=quantity, amount=amount, status="available")
        db.session.add(new_product)
        db.session.commit()
        return redirect('/admin-dashboard')
    return render_template('add.html')


@app.route('/update/<int:product_id>',methods=['GET', 'POST'])
def update_product(product_id):
    product = Products.query.get(product_id)
    if request.method == 'POST':
        product.category = request.form.get('category')
        product.quantity = request.form.get('quantity')
        product.amount = request.form.get('amount')
        db.session.commit()
        return redirect('/admin-dashboard')
    return render_template('update.html', product=product)


@app.route('/admin-request')
def admin_request():
    this_user = User.query.filter_by(role='seller').first()
    all_requests = Requests.query.all()
    return render_template('admin-request.html', all_requests=all_requests, user=this_user)


@app.route('/user-dashboard/<int:user_id>')
def user_dashboard(user_id):
    this_user = User.query.filter_by(id=user_id).first()
    all_products = Products.query.all()
    return render_template('user-dashboard.html', all_products=all_products, user=this_user)

@app.route('/create_new_request/<int:user_id>/<int:product_id>',methods=['GET','POST'])
def create_new_request(user_id,product_id):
    # load the user and product objects so the template can access their attributes
    user = User.query.get(user_id)
    product = Products.query.get(product_id)

    if request.method == 'POST':
        quantity = request.form.get('quantity')
        new_request = Requests(user_id=user_id,product_id=product_id,status='requested',requests=quantity)
        db.session.add(new_request)
        db.session.commit()
        return redirect(f'/user-dashboard/{user_id}')

    return render_template('create_new_request.html', user=user, product=product)
@app.route('/user-request/<int:user_id>')
def user_request(user_id):
    this_user = User.query.filter_by(id=user_id).first()
    user_requests = Requests.query.filter_by(user_id=user_id).all()
    return render_template('user-request.html', user=this_user, user_requests=user_requests)

@app.route('/request-status/<int:request_id>/<string:action>', methods=['POST'])
def request_status(request_id, action):
    req = Requests.query.get(request_id)
    if action == 'approve':
        req.status = 'approved'
    elif action == 'deny':
        req.status = 'denied'
    db.session.commit()
    return redirect('/admin-request')
