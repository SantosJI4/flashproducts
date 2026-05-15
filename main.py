from flask import Flask, session
from routes.checkout import Checkout
from routes.auth import register, login
from routes.confirm import Confirm
from routes.add_product import AddProducts
from routes.products import Produtos

app = Flask(__name__)

app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(Checkout)
app.register_blueprint(Confirm)
app.register_blueprint(AddProducts)
app.register_blueprint(Produtos)

# @app.route('/', methods=['GET', 'POST'])
# @app.route('/categoria/<categoria_nome>')
# def produtos(categoria_nome=None):
#     if categoria_nome:
#         filtered_products = [p for p in Products if p['category'].lower() == categoria_nome.lower()]
#     else:
#         filtered_products = Products
    
#     return render_template('home.html', products=filtered_products, current_category=categoria_nome)

    
@app.context_processor
def inject_user():
    return {
        'logado': 'usuario_id' in session,
        'email': session.get('usuario_email', ''),
        'name': session.get('usuario_name', '')
    }
    


if __name__ == '__main__':
    app.run(debug=True)
    