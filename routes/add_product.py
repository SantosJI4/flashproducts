from flask import Blueprint, request, flash, redirect, url_for, render_template
from routes.products import carregar_produtos, salvar_produtos

AddProducts = Blueprint('AddProducts', __name__)


@AddProducts.route('/admin/add-product', methods=['GET', 'POST'])
def add_product():
    
    produtos = carregar_produtos()
    
    if request.method == 'POST':
        # 1. Captura os dados do formulário
        
        name = request.form.get('name')
        category = request.form.get('category')
        image_url = request.form.get('image_url')
        description = request.form.get('description')
        price = request.form.get('price')
        # 2. Lógica de inserção (Exemplo com print, substitua pelo seu Banco de Dados)
        try:
            new_product = {
            'id': len(produtos) + 1, # Gera um ID simples
            'name': name,
            'category': category,
            'image_url': image_url,
            'description': description,
            'price': float(price)
        }
            
            produtos.append(new_product)
            salvar_produtos(produtos)  # Salva no JSON
            
        
            flash('Produto cadastrado com sucesso!', 'success')
            return redirect(url_for('AddProducts.add_product'))
            
        except Exception as e:
            flash(f'Erro ao cadastrar: {str(e)}', 'error')
            return redirect(url_for('AddProducts.add_product'))

    return render_template('add_product.html')