const sequelize = require('../../config/database');
const Book = require('./book');

const syncDatabase = async () => {
    await sequelize.sync();
    console.log('📚 Banco de dados sincronizado');
};

module.exports = { sequelize, Book, syncDatabase };
