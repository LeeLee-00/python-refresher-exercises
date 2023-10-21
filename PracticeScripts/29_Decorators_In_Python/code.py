# Great for allowing to easily modify functions

user = {"username": "LeeLee00", "access_level": "guest"}

def get_admin_passwrd():
    return "1234"

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permisions for {user['username']}."
    return secure_function

get_admin_passwrd = make_secure(get_admin_passwrd)

print (get_admin_passwrd())