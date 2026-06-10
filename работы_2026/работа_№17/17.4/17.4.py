def is_password_good(password):
    if len(password) < 8:
        return False
    #проверка наличия разных типов символов
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))