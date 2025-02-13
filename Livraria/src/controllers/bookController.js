const { Book } = require('../models');

const getAllBooks = async (req, res) => {
    const books = await Book.findAll();
    res.json(books);
};

const getBookById = async (req, res) => {
    const book = await Book.findByPk(req.params.id);
    book ? res.json(book) : res.status(404).send('Livro não encontrado');
};

const createBook = async (req, res) => {
    const book = await Book.create(req.body);
    res.status(201).json(book);
};

const updateBook = async (req, res) => {
    const book = await Book.findByPk(req.params.id);
    if (book) {
        await book.update(req.body);
        res.json(book);
    } else {
        res.status(404).send('Livro não encontrado');
    }
};

const deleteBook = async (req, res) => {
    const book = await Book.findByPk(req.params.id);
    if (book) {
        await book.destroy();
        res.send('Livro deletado');
    } else {
        res.status(404).send('Livro não encontrado');
    }
};

module.exports = { getAllBooks, getBookById, createBook, updateBook, deleteBook };
