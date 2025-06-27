-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Crear el usuario si no existe
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Otorgar todos los privilegios en hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Otorgar privilegio SELECT en performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Aplicar los privilegios
FLUSH PRIVILEGES;
