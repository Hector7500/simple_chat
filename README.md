# Simple_Chat_RESTful_API
Simple Chat API developed in Python and PostgreSQL 

## Prerequisites 
* To use the API I made a postman collection [Postman Scripts](https://github.com/Hector7500/simple_chat/blob/master/postman/simple_chat.postman_collection.json)
which can just be imported in the postman applicaiton. 
* You will also need to have PostgreSQL version > 9.1 (This is due to UUID) I used PostgreSQL version 11


## Set up
* Most things can be done using the MAKE system for ease 
* If you want to change anything prior to running such as the flask port or db_name you can do so in the [env_vars](https://github.com/Hector7500/simple_chat/blob/master/config/env_vars/dev.sh)

1. run command `make venv`
  - this will install virtualvenv if not already installed and make a virtual env for you to source
  - to source you can run the command `source simple_chat_env/bin/activate` *this assumes you have pyenv* if you dont have pyenv skip sourcing and and jump to pip install
  - once sourced make sure to pip install the requirements
    - pip install -r requirements/prod.txt
    - pip install -r requirements/dev.txt
  - if you run into issues with module names you need to source your pythonpath
2. Start postgres sever
  - create a db with whatever name you want but if not changed it will need to be `simple_chat_db`
3.run command `make db-migrate-up`
  - this will set up your db with the proper schema used for this project
4. run command `make run`
  - this will start the flask server

## API Docs
you can go to the following link `http://localhost:5000/apidocs/#/` to see the API this was maded with flasgger. 
`localhost:5000` will change if you change the env vars in the dev.sh file.

# Notes on API
* You will need to pass the UUID's for the endpoint as the uuid will change for everyone. 
* POST endpoint data is written in the request body. 
* GET endpoint data is written in the request body. 
