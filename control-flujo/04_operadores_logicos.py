# and or, not

gas = False
encendido = True
edad = 18

# if gas and encendido:
#     print("Puedes avanzar")

# if gas or encendido:
#     print("Puedes avanzar")

# if not gas or encendido:
#     print("Puedes avanzar")

# if gas and encendido and edad > 17:
#     print("Puedes avanzar")

# if gas and (encendido or edad > 17):
#     print("Puedes avanzar")

if not gas and (encendido or edad > 17):
    print("Puedes avanzar")

    