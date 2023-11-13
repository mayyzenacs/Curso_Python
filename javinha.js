function selecao () {
    const form = document.querySelector(".form");

    form.onsubmit = function (evento) {
        evento.preventDefault()
        alert(1)
        console.log("enviado")

    };
    form.addEventListener("submit", recebimento)

    
  }