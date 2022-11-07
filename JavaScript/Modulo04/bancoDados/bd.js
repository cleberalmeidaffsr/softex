const Sequelize = require('sequelize')

const sequelize = new Sequelize('cadastro', 'root', '123467', {
    host: 'localhost',
    dialect: 'mysql'
});

sequelize.authenticate()
.then(function(){
    console.log("Sucesso")
}).catch(function(){
    console.log("Não pegou")
})

module.exports = sequelize;