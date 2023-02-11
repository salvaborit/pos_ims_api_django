-- creates a django db 'todo_dev_db' with utf8 charset
-- creates superuser 'todo_dev' + grants

CREATE DATABASE IF NOT EXISTS pos_ims_db CHARACTER SET utf8;

CREATE USER IF NOT EXISTS 'pos_ims_dev'@'localhost' IDENTIFIED BY 'dev_pwd';
GRANT ALL PRIVILEGES ON pos_ims_db.* TO 'pos_ims_dev'@'localhost';
FLUSH PRIVILEGES;
