from flask import Blueprint, render_template, redirect
import os, json

Produtos = Blueprint('produtos', __name__)
produtos_db = 'products.json'


def carregar_produtos():
    if not os.path.exists(produtos_db):
        with open(produtos_db, 'w', encoding='utf-8') as f:
            json.dump([], f)
        return []

    with open(produtos_db, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
        
def salvar_produtos(dados):
    with open(produtos_db, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

Products = carregar_produtos()

@Produtos.route('/produtos', methods=['GET'])
def listar_produtos():
    pass

@Produtos.route('/', methods=['GET', 'POST'])
@Produtos.route('/categoria/<categoria_nome>')
def produto(categoria_nome=None):
    
    if categoria_nome:
        filtered_products = [p for p in Products if p['category'].lower() == categoria_nome.lower()]
    else:
        filtered_products = Products
        
    return render_template('home.html', products=filtered_products, current_category=categoria_nome, produtos=Products)

@Produtos.route('/ir_para/<int:product_id>')

def ir_para(product_id):
    product = next((p for p in Products if p['id'] == product_id), None)
    if product:
        return redirect(product['link'])
    return redirect('/')