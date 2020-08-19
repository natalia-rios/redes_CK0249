TAREFA 1 - SERVIDOR HTTP

Nesta tarefa, você desenvolverá um servidor Web simples em Python ou Java, capaz de
processar apenas uma requisição. Seu servidor Web:

● criará um socket de conexão quando contatado por um cliente (navegador);
● receberá a requisição HTTP dessa conexão;
● analisará a requisição para determinar o arquivo específico sendo requisitado;
● obterá o arquivo requisitado do sistema de arquivo do servidor;
● criará uma mensagem de resposta HTTP consistindo no arquivo requisitado
precedido por linhas de cabeçalho; e
● enviará a resposta pela conexão TCP ao navegador requisitante. Se um navegador
requisitar um arquivo que não está presente no seu servidor, seu servidor deverá
retornar uma mensagem de erro “404 Not Found”.
