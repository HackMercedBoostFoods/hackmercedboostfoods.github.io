const express = require('express')
const app = express();
const port = process.env.PORT || 8080;

app.use(express.static('UI'));
app.use('/css', express.static(__dirname + "UI/CSS"));
app.use('/html', express.static(__dirname + "UI/HTML"));
app.use('/img', express.static(__dirname + "UI/images"));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/UI/HTML/index.html');
});

app.post('/', (req, res) => {
    
});

app.get('/map.html', (req, res) => {
    res.sendFile(__dirname + '/UI/HTML/map.html');
});

app.post('/map.html', (req, res) => {
    
});

app.get('/analytics.html', (req, res) => {
    res.sendFile(__dirname + '/UI/HTML/analytics.html');
});

app.post('/analytics.html', (req, res) => {

});

app.get('/settings.html', (req, res) => {
    res.sendFile(__dirname + '/UI/HTML/settings.html');
});

app.post('/settings.html', (req, res) => {

});

app.get('/sign-in.html', (req, res) => {
    res.sendFile(__dirname + '/UI/HTML/sign-in.html');
});

app.post('/sign-in.html', (req, res) => {

});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});