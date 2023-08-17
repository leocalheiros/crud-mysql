document.addEventListener("DOMContentLoaded", function () {
    const userList = document.getElementById("user-list");
    const statusMessage = document.querySelector(".message");

    // Função para deletar um usuário
    function deletarUsuario(id) {
        fetch(`/usuario/${id}`, {
            method: "DELETE",
        })
        .then(response => response.json())
        .then(data => {
            if (statusMessage) {
                statusMessage.textContent = data.mensagem;
            }
            removeUsuarioDaLista(id); // Remove o usuário excluído da lista
        })
        .catch(error => {
            console.error("Erro ao deletar usuário:", error);
        });
    }

    // Função para remover o usuário excluído da lista
    function removeUsuarioDaLista(id) {
        const usuarioItem = userList.querySelector(`li[data-id="${id}"]`);
        if (usuarioItem) {
            usuarioItem.remove();
        }
    }

    // Adicionar evento de clique aos botões "Deletar"
    userList.addEventListener("click", function (event) {
        if (event.target.classList.contains("delete-button")) {
            const id = event.target.getAttribute("data-id");
            deletarUsuario(id);
        }
    });

    // Função para atualizar a lista de usuários
    function updateUsers() {
        fetch("/usuarios")
            .then(response => response.json())
            .then(data => {
                const usuarios = data.usuarios;
                const listaUsuarios = usuarios.map(usuario => `<li data-id="${usuario.id}"><span>${usuario.nome} - ${usuario.email}</span><button class="delete-button" data-id="${usuario.id}">Deletar</button></li>`).join("");
                userList.innerHTML = listaUsuarios;
            });
    }

    // Chamar a função para atualizar a lista ao carregar a página
    updateUsers();
});
