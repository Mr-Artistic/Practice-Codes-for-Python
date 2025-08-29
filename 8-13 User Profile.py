def build_profile(first, last, **user_info):
    """Builds a user information dictionary."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    print(user_info)

build_profile(first = 'John', last = 'Doe', email = 'dummy@mymail.com', age = 18)
