# Great for allowing to easily modify functions
import functools


user = {"username": "LeeLee00", "access_level": "admin"}



def make_secure(func):
    @functools.wraps(func) #Keeps name and documentaiton fo get_admin_password
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permisions for {user['username']}."
    return secure_function

@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


print (get_password("billing"))