# Great for allowing to easily modify functions
import functools


user = {"username": "LeeLee00", "access_level": "admin"}



def make_secure(func):
    @functools.wraps(func) #Keeps name and documentaiton fo get_admin_password
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permisions for {user['username']}."
    return secure_function

@make_secure
def get_admin_passwrd():
    return "1234"

get_admin_passwrd = make_secure(get_admin_passwrd)

print (get_admin_passwrd())