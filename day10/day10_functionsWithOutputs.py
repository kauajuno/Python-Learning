def format_name(first_name, last_name):
    first_name = first_name.title()
    last_name = last_name.title()
    return f"{first_name} {last_name}"


name = format_name('KauA', 'JuNiO')
print(name.split())
