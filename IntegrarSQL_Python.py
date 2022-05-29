import pyodbc

dados_conexao = (
    "Driver={SQL Server};"# instalado automaticante junto com o sql
    "Server=DESKTOP-TS58G3G\SQLEXPRESS;"
    "Database=PythonSQL;"
)
#necessario criar a variavel
conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()

#insert no banco de dados
id = input("qual foi a venda")
cliente = input("nome do cliente")
produto = input("qual o produto")
data = input("emissao")
preco = input("valor da venda")
quantidade = input("quantidade vendida")

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()