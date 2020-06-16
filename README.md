# PasswordGenerator

I created a password generator that creates a scrambled password consisting of letters, numbers, and symbols. Then using cryptography.fernet, I encrypted the password, and stored the encrypted password and decryption key in a file. 

This application can be accessed in the command line, where you are asked whether you want to store a password or access an already stored password. If chosen to store a new password, the user is asked to enter an account that will be linked to the password. The program then creates a password, encrypts it, and stores the account, encrypted password, and decryption key in a storage file. If chosen to access a password, all accounts within the storage are display and the user is asked to pick which account password they would like to access. When the account is picked, the encrypted password and key are selected from the file and put into the program, where the decrypted password will be displayed.
