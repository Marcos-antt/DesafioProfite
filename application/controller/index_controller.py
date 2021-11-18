from application import app
from application.model.dao.produtoDAO import ProdutoDAO
from flask import Flask, render_template, redirect, url_for, jsonify

ProdutoDAO = ProdutoDAO()
produto_list = ProdutoDAO.produto_list()


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produto_list = produto_list[0:4])

@app.route("/produtos2")
def produtos2():
    return render_template("produtos.html", produto_list = produto_list[4:7])