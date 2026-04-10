import bcrypt

class PasswordHelper:

    def generate_password_hash(self, password: str):
        hash_password = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
        return hash_password

    def verify_password_hash(self, entered_password, hashed_password):
        password_check = bcrypt.checkpw(entered_password.encode(),hashed_password)
        if password_check:
            return True
        else:
            return False