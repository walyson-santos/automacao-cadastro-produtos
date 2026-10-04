# 🤖 Automação de Cadastro de Produtos

Automação desenvolvida em Python para realizar o cadastro de produtos em uma plataforma de treinamento, utilizando dados armazenados em um arquivo CSV.

O projeto foi desenvolvido como prática de **automação de tarefas repetitivas**, manipulação de dados e organização de um projeto Python para portfólio.

---

## 🎯 Objetivo

O objetivo do projeto é automatizar o processo de cadastro de diversos produtos que, manualmente, precisariam ser inseridos um por um.

A automação:

1. Abre o navegador;
2. Acessa a plataforma;
3. Realiza o login;
4. Lê os dados dos produtos a partir de um arquivo CSV;
5. Preenche automaticamente os campos do formulário;
6. Realiza o cadastro dos produtos.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Pandas** — leitura e manipulação dos dados do CSV
- **PyAutoGUI** — automação da interface gráfica
- **Python-dotenv** — gerenciamento das credenciais através de variáveis de ambiente

---

## 📂 Estrutura do projeto

```text
automacao-cadastro-produtos/
│
├── codigo.py
├── auxiliar.py
├── produtos.csv
├── requirements.txt
├── .gitignore
└── README.md