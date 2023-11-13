function selecao () {
    const form = document.querySelector(".form");

    function recebimento(evento) {
        evento.preventDefault()

    }
    form.addEventListener("submit", recebimento)

    
  }