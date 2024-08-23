from sqlalchemy import engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#conexion a la base de datos
#nombre BD
dataBaseName = "gestiobd"
#Uuario BD
userName = "root"
#contraseña BD
userPassword = ""
#PUERTO DE CONEXION
conexionPort = "3306"
#localhost
servidor =  "localhost"

#creando la conexion
connectionToDatabase = f"mysql+mysqlconnector://{userName}:{userPassword}@{servidor}:{conexionPort}/{dataBaseName}"

print(connectionToDatabase)

engine = create_engine(connectionToDatabase)
sessionLocal = sessionmaker(autocommit = False,autoFlush = False,bind=engine)
