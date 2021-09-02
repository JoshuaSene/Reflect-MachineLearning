# Reflect-MachineLearning

I. Técnologias Utilizadas
Python
Maria DB

II. DESCRIÇÃO DO PROBLEMA:
Desenvolver um sistema de recomendação simples, utilizando a abordagem de agentes racionais reflexivos / reflexivos baseados em modelos. Esse sistema deve atender aos seguintes requisitos e restrições:

III. REQUISITOS:
Quando um consumidor indicar a intenção de comprar um produto A, frequentemente comprado com um produto B, o sistema de recomendação sugerirá ao cliente a compra do produto B;
Quando um consumidor indicar a intenção de compra dos produtos A e B, frequentemente comprados com o produto C, o sistema de recomendação sugerirá ao cliente a compra do produto C;
O sistema deve permitir o cadastro, a exclusão e a visualização das regras armazenadas em um banco de dados relacional;
A interface poderá ser totalmente textual, via prompt de comando.

IV. RESTRIÇÕES:
Ser desenvolvido em linguagem de programação Python 3+;
Utilizar uma base de regras que seja armazenada em banco de dados relacional (utilizar o MariaDB);
Disponibilizar todo o código via repositório do GitHub (não esquecer de gerar o arquivo requirements.txt com as dependências de projeto) .
Primeiros Passos

1. Criação do ambiente virutal.
1.1. Instalar a virtualenv

pip install virtualenv
1.2. Criar virtualenv

virtualenv nome_da_virtualenv