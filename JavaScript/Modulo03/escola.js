var readlineSync = require('readline-sync');

var nome = input('Digite o seu nome: ');

console.log(saudacao());

var nota1 = input(questionFloat(nome + ' informe sua nota 1: '));
var nota2 = input(questionFloat(nome + ' informe sua nota 2: '));
var nota3 = input(questionFloat(nome + ' informe sua nota 3: '));

var media = media(nota1, nota2, nota3);

console.log(nome + ' sua média é: ' + media);

var aprovacao = (media) => {
    if (media >= 7.0) return "Aprovado"
    else return "Reprovado"
};

console.log(nome + ' você foi ' + aprovacao(media));

function saudacao() {
    return "Olá " + nome;
}

function media(n1, n2, n3) {
    return (n1 + n2 + n3) / 3;
}