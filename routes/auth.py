from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import os
import json

arquivo_db = 'users.json'
 
def carregar_dados():
    # 1. Verifica se o arquivo NÃO existe
    if not os.path.exists(arquivo_db):
        # Cria o arquivo com uma lista vazia inicial
        with open(arquivo_db, 'w', encoding='utf-8') as f:
            json.dump([], f)
        return []

    # 2. Se existe, lê os dados
    with open(arquivo_db, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return [] # Retorna lista vazia se o JSON estiver corrompido

def salvar_dados(dados):
    with open(arquivo_db, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


login = Blueprint('login', __name__)
@login.route('/login', methods=['GET', 'POST'])
def login_page():
    logado = False
    email = None
    name = None
    
    if request.method == 'POST':
        
        email = request.form.get('email')
        password = request.form.get('password')
        
        usuarios = carregar_dados()
        
        # Procura o usuário
        user = next((u for u in usuarios if u['email'] == email and u['password'] == password), None)
        
        if user:
            # Login com sucesso
            logado = True
            print(logado)
            session['usuario_id'] = user['id']
            session['usuario_email'] = user['email']
            session['usuario_name'] = user['username']
            return redirect(url_for('produtos'))
            
        else:
            # Erro de login
            flash('E-mail ou senha incorretos!', 'error')
            return redirect(url_for('login.login_page'))
            
    return render_template('login.html', logado=logado, email=email, name=name)

register = Blueprint('register', __name__)
@register.route('/register', methods=['POST'])
def register_page():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    print(f"Dados recebidos: {name}, {email}, {password}")
 
    # Verifica se o e-mail já existe
    usuarios = carregar_dados()
    if any(u['email'] == email for u in usuarios):
        flash('Este e-mail já está cadastrado!', 'error')
        return redirect(url_for('login.login_page'))
    
    new_user = {
        "id": len(usuarios) + 1,
        "username": name,
        "email": email,
        "password": password
    }
    usuarios.append(new_user)
    salvar_dados(usuarios)
    flash('Conta criada com sucesso! Faça login.', 'success')
    return redirect(url_for('login.login_page'))

@login.context_processor
def inject_user():
    return {
        'logado': 'usuario_id' in session,
        'email': session.get('usuario_email', '')
    }
    
@login.route('/logout')
def logout():
    session.clear() # Limpa tudo (desloga)
    return redirect(url_for('login.login_page'))