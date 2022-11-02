const express = require('express');
const app = express()

app.get('/', (req, res) => {
    res.send('primeira rota')
})
app.get('/segunda', (req, res) => {
    res.send('segunda rota')
})

app.listen(3333)