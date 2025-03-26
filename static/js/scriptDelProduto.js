// Script simplificado para manipular a seleção e exibir o modal
document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('.product-checkbox');
    const deleteBtn = document.getElementById('deleteSelectedBtn');
    const modal = document.getElementById('confirmModal');
    const cancelBtn = document.getElementById('cancelDelete');
    const form = document.getElementById('deleteForm');
    
    // Atualizar estado do botão de exclusão
    function updateDeleteButton() {
        const hasSelected = Array.from(checkboxes).some(cb => cb.checked);
        deleteBtn.disabled = !hasSelected;
    }
    
    // Adicionar listeners para os checkboxes
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', updateDeleteButton);
        checkbox.addEventListener('change', function() {
            // Destacar visualmente os cards selecionados
            const card = this.closest('.product-card');
            if (this.checked) {
                card.classList.add('selected');
            } else {
                card.classList.remove('selected');
            }
        });
    });
    
    // Abrir modal de confirmação ao clicar no botão de exclusão
    deleteBtn.addEventListener('click', function() {
        if (!deleteBtn.disabled) {
            modal.style.display = 'flex';
        }
    });
    
    // Fechar modal ao cancelar
    cancelBtn.addEventListener('click', function() {
        modal.style.display = 'none';
    });
    
    // Fechar modal ao clicar fora
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
    
    // Esconder mensagens flash após alguns segundos
    setTimeout(function() {
        const flashMessages = document.querySelector('.flash-messages');
        if (flashMessages) {
            flashMessages.style.opacity = '0';
            setTimeout(function() {
                flashMessages.remove();
            }, 500);
        }
    }, 5000);
});