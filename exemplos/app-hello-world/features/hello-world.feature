Funcionalidade: Hello World na API

Cenário: Mensagem "Hello World"
Dado a api no endereço: http://localhost:5000
Quando eu realizo um GET no endpoint: /
Então devo receber status code igual a 200
Então devo receber content-type igual a application/json
Então devo receber um body com {"message":"Hello World"}

