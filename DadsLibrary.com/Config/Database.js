// config/database.js
const { Sequelize } = require('sequelize');

// Set up Sequelize to connect to PostgreSQL
const sequelize = new Sequelize('postgres://ubuntu:Grepolis@123@localhost:5432/dads_library_db', {
  dialect: 'postgres',
  logging: false, // Disable SQL query logging
});

module.exports = sequelize;
