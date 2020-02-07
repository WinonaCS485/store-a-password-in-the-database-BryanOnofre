import pymysql.cursors
import hashlib
import uuid

# Salt Creation
salt = str(uuid.uuid4())

# New User Creation Input
user_Name = input("Enter new UserName: ")
password = input("Enter Password: ")

# Hash the password
hashed_Password = hashlib.sha256((password + salt).encode())

# print the hashed password
# print("the hashed pw is: ", hashed_Password)


# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='pi8643bb',
                             password='sailboat128',
                             db='pi8643bb_Passwords',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


try:
    with connection.cursor() as cursor:
        # Insert New User Into Passwords table using input
        setPW = "INSERT INTO `UserInfo` (`UniqueID`, `UserName`, `Salt`, `HashedPassword`) VALUES (NULL,%s,%s,%s)"

        # execute the SQL command
        cursor.execute(setPW, (user_Name, salt, hashed_Password.hexdigest()))

        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes.
        connection.commit()

    with connection.cursor() as cursor:
        # get credentials from UserInfo table using input
        getCredentials = "SELECT * FROM `UserInfo` WHERE UserName = %s"

        # execute the SQL command
        cursor.execute(getCredentials, user_Name)

        # get the results
        for row in cursor:
            SaltFromDataB = row['Salt']
            HashedPasswordFromDataB = row['HashedPassword']
finally:
    connection.close()

# ask user to reenter their password
reEnteredPassword = input("Enter your password again to recheck: ")

# rehash the reEntered password with salt retrieved from DB
reHashedPassword = hashlib.sha256((
    reEnteredPassword + SaltFromDataB).encode())

# test if hash from DB and hash from reEntered passwords match
if HashedPasswordFromDataB == reHashedPassword.hexdigest():
    print("Congradulations, your passwords matched! Want a cookie?")
else:
    print("Your passwords didn't match, get lost loser")
