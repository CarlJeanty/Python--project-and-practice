def format_name(f_name,l_name):
    """ takes first and last name and format it by first title function."""
    if f_name =="" or l_name== "":
        return
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return (f"{formated_f_name} {formated_l_name}")

print(format_name("curious",'george'))
format_name(input('Whatn is your first name'), input("What is your last name"))