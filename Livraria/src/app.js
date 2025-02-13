const express = require('express');
const bodyParser = require('body-parser');
const bookRoutes = require('./routes/bookRoutes');
const { syncDatabase } = require('./models');

const app = express();
app.use(bodyParser.json());
app.use('/api', bookRoutes);

// Sincronizar banco ao iniciar
syncDatabase();

module.exports = app;
