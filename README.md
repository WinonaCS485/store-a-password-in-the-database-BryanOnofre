# Store a Password

Your assignment is to create a program in any language that does the following:
* Asks the user to store a password
* Stores the password in your database, salted and hashed
* Asks the user to enter it again
* Tells them whether they got it right or not

https://crackstation.net/hashing-security.htm 



My program will ask the user for a User Name and Password

Adds salt to the Password, then hashes the password

strores the salt and hash in my Passwords database

retrieves salt and hash from the DB

asks the user to reEnter their password

hashes their reEntered password with the salt returned from the database

checks if rehashed password is equal to the hash returned from the DB
