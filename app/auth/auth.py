import secrets

def generate_auth_key():
    return secrets.token_urlsafe(16)