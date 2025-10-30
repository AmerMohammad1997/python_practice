def require_admin(func):
    def delete_database_wrapper(user):
        if user != "admin":
            print("Access denied")
        else:
            return func(user)
    return delete_database_wrapper

@require_admin
def delete_database(user):
    print("database deleted", user)

delete_database("amer")
delete_database("admin")