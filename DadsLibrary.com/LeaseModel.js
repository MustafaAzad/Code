// models/lease.js
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = require('../config/database'); // Database connection
const User = require('./user');
const Book = require('./book');

const Lease = sequelize.define('Lease', {
  leaseCount: {
    type: DataTypes.INTEGER,
    defaultValue: 0,
  },
  maxLeases: {
    type: DataTypes.INTEGER,
    defaultValue: 3,
  },
}, {
  tableName: 'leases',
  timestamps: true,
});

// Define relationships
Lease.belongsTo(User, { foreignKey: 'borrowerId' });
Lease.belongsTo(User, { foreignKey: 'ownerId' });
Lease.belongsTo(Book, { foreignKey: 'bookId' });

module.exports = Lease;
