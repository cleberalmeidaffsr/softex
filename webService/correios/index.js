const {consultarCep} = require('correios-brasil');
const {rastrearEncomendas} = require('correios-brasil');
let codRastreio = ['NA33843825BR'];
const {cep} = '50711120';

consultarCep(cep).then(Response => {
    console.log(Response);

});

consultarCep(cep).then(Response => {
    console.log(Response.bairro);
});

rastrearEncomendas(codRastreio).then(Response => {
    console.log(Response[0].eventos.reverse());
});