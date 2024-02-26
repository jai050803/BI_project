class User:
    def __init__(self, user_id, username, password, email, auth_key=None):
        self.user_id = user_id
        self.username = username
        self.password = password  # Note: This should be a hashed password
        self.email = email
        self.auth_key = auth_key  # Optional, based on your schema and use case

    def __repr__(self):
        return f"User(user_id={self.user_id}, username='{self.username}', email='{self.email}', auth_key='{self.auth_key}')"
