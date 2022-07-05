
    $( document ).ready(function() {
        buscaProdutos()
    });
    function buscaProdutos() {
        axios.get('produto/') // 4
        .then(res => {
            res.data.produtos.forEach(function(dados, key) {
                const foto =  axios.get('produto/foto/', {
                    params: {
                        id: dados.id
                    }
                }) // 4
                .then(res => {
                     var urlFoto = res.data.foto
                     $("#col_produto").append(
                        "<div class='col-md form-group'>"+
                            "<div class='card py-2 px-2 todosProdutos' style='border-radius:10px' id='produto"+dados.id+"' onmouseover='inserir(this)'>"+
                                "<img class='card-img-top' src='media/"+urlFoto+"' height='250px'>"+
                                "<div class='card-body px-2>"+
                                    "<p class='card-text'><strong>"+
                                        dados.nome+
                                    "</strong></p>"+
                                    "<p class='card-text'><label style='font-size:10pt'>Preço:</label><strong> R$ 1280,00</strong></p>"+
                                    "<caption>"+
                                        "ou até 10 x R$ 128,85"+
                                    "</caption>"+
                                "</div>"+
                            "</div>"+
                        "</div>"
                    )
                     
                }) // 5
                .catch(errors => console.log(errors))
                
                // console.log(foto)
            });
        }) // 5
        .catch(errors => console.log(errors))
    }
    function inserir(event) {
        const el = event
        $('.todosProdutos').removeClass('cardProdutos')
        $("#"+el.id).addClass('cardProdutos')
    }
