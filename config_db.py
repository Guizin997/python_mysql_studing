import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "python_crud"
)

cursor = db.cursor()

# Criação do database:
# sql = "CREATE DATABASE python_crud"

# Criação da table:
# sql ="CREATE TABLE teste (id INT AUTO_INCREMENT PRIMARY KEY, produto VARCHAR(100) NOT NULL, preco FLOAT NOT NULL)"

# Drop database e table:
# sql = "DROP DATABASE python_crud"
# sql = "DROP TABLE teste"

# Insert:
# sql = "INSERT INTO teste (produto, preco) VALUES (%s, %s)"
# val = ("cereal", "12.25") -> essa variavel tem que ser colocada no "cursor.execute()" também
# obs -> o insert precisa que o método "mydb.commit()" seja colocado depois do excute para inserir o "val" no "sql"

# Select:
# sql = "SELECT * FROM teste"
# result = cursor.fetchall() -> precisa ser colocado depois do "cursor.execute()" caso queira pegar/armazenar os valores
# obs -> para exibir usa-se um laço de repetição, ex: "for"

cursor.execute(sql)
