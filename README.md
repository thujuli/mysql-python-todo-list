# TODO LIST

Simple todo list using python and mysql

## Requirements

1. Download and Install MySQL Community Server: [MySQL](https://dev.mysql.com/downloads/mysql/).
    - When you instalation MySQL Server, you can see refrence manual in dev.msql.com: [MySQL](https://dev.mysql.com/doc/refman/8.0/en/installing.html)
2. After finished instalation and configure MySQL Server. Follow this step to:
    1. Login MySQL Server using user root.
        `mysql -u root -p [password]`
    2. Create new Database to follow this tutorial.
        `CREATE DATABASE python_mysql`
    3. Create new user, when you don't have a user to follow this tutorial.
        `CREATE USER 'thujuli'@'localhost' IDENTIFIED BY 'thujuli'`
    4. Give privileges for new user to the new database has be created.
        `GRANT ALL ON python_mysql. * TO 'thuhuli'@'localhost'`
    5. Congrats you can now follow this tutorial.
