function openEditModal(id, nome, preco, descricao, imagem) {
    document.getElementById('editProdutoId').value = id;
    document.getElementById('editNome').value = nome;
    document.getElementById('editPreco').value = preco;
    document.getElementById('editDescricao').value = descricao;
    
    const modal = document.getElementById('editProdutoModal');
    modal.style.display = 'block';
}

function closeEditModal() {
    const modal = document.getElementById('editProdutoModal');
    modal.style.display = 'none';
}

// Fechar modal ao clicar fora
window.onclick = function(event) {
    const modal = document.getElementById('editProdutoModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}