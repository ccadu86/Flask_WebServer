from flask import Flask, render_template, redirect, flash, request, url_for
import os

app = Flask(__name__)

app.secret_key = os.urandom(24).hex()

context = {}
context["logo"] = "img/logo_senai.png"

produtos = {}
produtos[1] = {
    "nome": "Arroz",
    "preco": 19.90,
    "descricao": "Arroz branco tipo 1, pacote de 5kg. Grãos selecionados de alta qualidade.",
    "imagem": "img/arroz.png"
}
produtos[2] = {
    "nome": "Café",
    "preco": 12.50,
    "descricao": "Café torrado e moído, pacote de 500g. Sabor intenso e aroma irresistível.",
    "imagem": "img/cafe.png"
}
produtos[3] = {
    "nome": "Azeite",
    "preco": 24.90,
    "descricao": "Azeite de oliva extra virgem, garrafa de 500ml. Acidez máxima de 0,5%.",
    "imagem": "img/azeite.png"
}


@app.route('/')
def homepage():    
    
    context["img"] = "img/img_home.png"
    context["Titulo"] = "VENDINHA DA C13"
    context["Texto"] = '''
    'Seja bem-vindo à Vendinha da C13, seu novo espaço favorito para encontrar produtos de qualidade com preços acessíveis. Aqui você encontra desde itens essenciais do dia a dia até produtos exclusivos selecionados especialmente para nossos clientes.
    Nosso compromisso é oferecer uma experiência de compra agradável, com atendimento personalizado e produtos que fazem a diferença no seu dia a dia. Navegue pelo nosso catálogo e descubra porque a Vendinha da C13 se tornou a escolha preferida da comunidade.'''

    return render_template("homepage.html", **context)

@app.route('/add_produto')
def add_produto():
       
    context["produtos"] = produtos

    return render_template("add_produto.html", **context)

@app.route('/del_produto')
def del_produto():

    context["produtos"] = produtos
    return render_template("del_produto.html", **context)

@app.route('/excluir_produtos', methods=['POST'])
def excluir_produtos():

    produtos_ids = request.form.getlist('produtos_ids')
    
    if not produtos_ids:
        flash('Nenhum produto selecionado para exclusão.', 'warning')
        return redirect(url_for('del_produto'))
    
    try:
        produtos_ids = [int(id) for id in produtos_ids]
        
        count = 0
        
        for id in produtos_ids:
            if id in produtos:
                produtos.pop(id)
                count += 1
        
        if count > 0:
            flash(f'{count} produto(s) excluído(s) com sucesso!', 'success')
        else:
            flash('Nenhum dos produtos selecionados foi encontrado.', 'info')
            
    except Exception as e:
        flash(f'Erro ao excluir produtos: {str(e)}', 'error')
    
    return redirect(url_for('del_produto'))

@app.route('/up_produto')
def up_produto():
    
    return render_template("up_produto.html", **context)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")