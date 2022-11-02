var cliente = {
    nome: 'Cleber',
    cpf: '123.123.123-12',
    senha: '123',
    conta: '1234-1',
    saldo: '123,12',
}

var deposito = function (valor) {
    cliente.saldo = cliente.saldo + valor;
}

var saque = function (valor) {
    cliente.saldo = cliente.saldo - valor;
}

var buscar_saldo = function () {
    console.log('Seu saldo é: ' + cliente.saldo);
}

var numero_conta = function () {
    console.log(cliente.nome + ', O número da sua conta é: ' + cliente.conta)
}