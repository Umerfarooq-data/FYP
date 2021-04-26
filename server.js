// including third party modules
const express = require('express');
const path = require('path')
const bodyParser = require('body-parser')

// Including Routes
const zoonoticRouter = require('./routes/zoonoticModel')
    // modules initalization
const app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/views/'));
// app.use(bodyParser.urlencoded({ extended: false }))
app.use(express.json({ limit: '1mb' }))

app.use(express.static(__dirname + '/public'));

// Home Route
app.use('/zoonoticModel', zoonoticRouter);
app.get('/', (req, res) => {
    res.render('index');
});
app.get('/test', (req, res) => {
    res.render('test');
});
app.get('/about', (req, res) => {
    res.render('about');
})
app.get('/report', (req, res) => {
    res.render('report')
})

app.listen(3000, () => {
    console.log('It is running on port 3000');
})