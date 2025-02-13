const express = require('express');
const { getAllBooks, getBookById, createBook, updateBook, deleteBook } = require('../controllers/bookController');

const router = express.Router();

router.get('/books', getAllBooks);
router.get('/books/:id', getBookById);
router.post('/books', createBook);
router.put('/books/:id', updateBook);
router.delete('/books/:id', deleteBook);

module.exports = router;
