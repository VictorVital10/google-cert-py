# call a variable
device_id_1 = "01234"
device_id_2 = "56789"
print(device_id_2)

# use type function
device_id_3 = "h2b3n4"
data_type = type(device_id_3)
print(data_type) 


# reassing a variable
device_id_5 = "u38me0"
print(device_id_5)
device_id_5 = "h4"
print(device_id_5)

# demonstrate a typer error
device_id_4 = "g6m3o0"
number = 3
try:
    print(device_id_4 + number)
except TypeError as e:
    print("Ocorreu um erro:", e)

# create a conditional
operating_system = "OS 3"
if operating_system == "OS 3":
    print("Updates Needed")
else:
    print("No Updates Needed")

# determinar se atualizações são necessárias
system = "OS 3"
if system == "OS 3":
    print("no update needed")
elif system == "OS 1" or "OS 2":
    print("update needed")     
    
# verificar se o usuário tem acesso ao dispositivo
approved_user1 = "ederson"
approved_user2 = "alisson"
username = "sergio"
if username == approved_user1 or username == approved_user2:
    print("This user has access to this device")
else:
    print("This user does not have access to this device")

# tentavias de login feitas durante o horário comercial
comercial_hours = True
if comercial_hours == False:
    print("Tentativa de login feita durante o horário comercial")
else:
    print("Tentativa de login feita fora do horário comercial")
