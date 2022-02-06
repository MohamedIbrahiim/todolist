# todolist

### Run Using Docker:

``` sh
# Note we need to add .env first at base direcotry 
# .env file will hold those data: 
SECRET_KEY=#YourStrongSecretKey
MYSQL_ROOT_PASSWORD=StrongPassword
MYSQL_DATABASE=ToDoListDB
MYSQL_USER=UserName
MYSQL_PASSWORD=StrongPassword
MYSQL_ENGINE=django.db.backends.mysql
MYSQL_HOST=db
MYSQL_PORT=3306
MODE_FILE=todolist.settings.development
```

```` sh
# run in terminal
- docker-compose up
````
To view API documentation swagger interface can be used:
```sh
http://127.0.0.1:8000/api/docs/
```
this link will only be available after running docker

## for admin portal use:
```
http://127.0.0.1:8000/admin/

using username: test@mail.com
      password: 12345678
```

### Note:

If .env file does not exist, the default values will be used
which will lead to the use of sqlite instead of MySql
