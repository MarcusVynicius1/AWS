const { Sequelize } = require('sequelize');

const sequelize = new Sequelize('bookstore', 'user', 'password', {
    host: 'db',
    dialect: 'postgres'
});

module.exports = sequelize;
