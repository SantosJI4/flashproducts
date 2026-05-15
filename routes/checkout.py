from flask import Blueprint, render_template, request, redirect, url_for
from database.produts import Products

Checkout = Blueprint('checkout', __name__)

@Checkout.route('/checkout', methods=['GET', 'POST'])
def checkout_page():
    if request.method == 'POST':
        pix = request.form.get('pix')
        card = request.form.get('card')
        boleto = request.form.get('boleto')
        return render_template('confirm_pay.html', pix=pix, card=card, boleto=boleto)
    
    return render_template('checkout.html')

@Checkout.route('/checkout/<int:product_id>')
def checkout(product_id):
    # Procura o produto pelo ID na lista
    product = next((p for p in Products if p['id'] == product_id), None)
    
    if product:
        # Em vez de redirect, usamos render_template para MOSTRAR os dados
        return render_template('checkout.html', product=product)
    
    # Se o ID não existir, volta para a página inicial
    return redirect(url_for('produtos'))

@Checkout.route('/confirmar-pagamento/')
def Confirmar():
    return render_template('confirm_pay.html')
