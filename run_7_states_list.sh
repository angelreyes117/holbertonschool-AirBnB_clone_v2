#!/bin/bash

# Colores
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # Sin color

echo -e "${GREEN}📦 Iniciando entorno para HBNB...${NC}"

# Verificar si el dump existe
if [ ! -f "7-dump.sql" ]; then
    echo -e "${RED}❌ El archivo 7-dump.sql no fue encontrado. Por favor descárgalo primero.${NC}"
    exit 1
fi

# Intentar crear la base de datos (ignora error si ya existe)
echo -e "${GREEN}🛠️  Creando base de datos 'hbnb_dev_db'...${NC}"
mysql -uroot -proot -e "CREATE DATABASE IF NOT EXISTS hbnb_dev_db;" 2>/dev/null

# Cargar el dump
echo -e "${GREEN}⬇️  Cargando dump en la base de datos...${NC}"
cat 7-dump.sql | mysql -uroot -proot hbnb_dev_db

# Exportar variables necesarias
export HBNB_MYSQL_USER=hbnb_dev
export HBNB_MYSQL_PWD=hbnb_dev_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_dev_db
export HBNB_TYPE_STORAGE=db

# Correr el servidor Flask
echo -e "${GREEN}🚀 Ejecutando Flask con DBStorage en 0.0.0.0:5000...${NC}"
python3 -m web_flask.7-states_list

