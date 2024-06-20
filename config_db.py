import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "python_crud"
)

# Teste da conexão
# print(mydb)

cursor = mydb.cursor()

# Criação do database:
# sql = "CREATE DATABASE python_crud"

# Criação da table:
# sql ="CREATE TABLE teste (id INT AUTO_INCREMENT PRIMARY KEY, produto VARCHAR(100) NOT NULL, preco FLOAT NOT NULL)"

# Drop database e table:
# sql = "DROP DATABASE python_crud"
# sql = "DROP TABLE teste"

# Insert:
# sql = "INSERT INTO teste (produto, preco) VALUES (%s, %s)"
# val = ("cereal", 12.25)# -> essa variavel tem que ser colocada no "cursor.execute()" também
# obs -> o insert precisa que o método "mydb.commit()" seja colocado depois do excute para inserir o "val" no "sql"

# Select:
# sql = "SELECT * FROM teste"
# result = cursor.fetchall() -> precisa ser colocado depois do "cursor.execute()" caso queira pegar/armazenar os valores
# obs 1 -> para exibir usa-se um laço de repetição, ex: "for"
# obs 2 -> para selecionar uma unica linha/informação utiliza-se o metodo "fetchone()"

# Delete:
# sql = "DELETE FROM teste WHERE id=%s"
# val = (1)
# obs -> assim como o insert também necessita do uso do "mydb.commit()" após o "cursor.execute()"

# Update:
# sql = "UPDATE teste SET produto = %s WHERE id = %s"
# val = ("sabão", 1)
# obs -> te a mesma obrigatoriedade que o insert e o delete quanto ao "mydb.commit()"

cursor.execute(sql)