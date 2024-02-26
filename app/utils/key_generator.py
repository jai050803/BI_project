import secrets
import string

def generate_auth_key(length=16):
    """Generate a secure, random 16-character alphanumeric key."""
    alphabet = string.ascii_letters + string.digits
    key = ''.join(secrets.choice(alphabet) for i in range(length))
    return key

# Example usage
if __name__ == "__main__":
    print(generate_auth_key())
    # Outputs a secure, random 16-character alphanumeric key
