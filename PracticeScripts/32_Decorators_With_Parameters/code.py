# Great for allowing to easily modify functions
import functools


user = {"username": "LeeLee00", "access_level": "guest"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func) #Keeps name and documentaiton fo get_admin_password
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permisions for {user['username']}."
            
        return secure_function

    return decorator

@make_secure("admin")
def get_admin_password():
    return "user: set_password"


@make_secure("user")
def get_dashboard_password():
    return "user: userpassword"

user = {"username": "LJN", "access_level": "admin"}

print(get_admin_password())
print(get_dashboard_password())