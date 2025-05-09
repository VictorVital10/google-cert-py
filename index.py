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

# create a while loop
max_devices = 5
i = 1

while i < max_devices:
    print("User can still connect to aditional devices")
    i = i + 1
print("User has reached maximum number of connected devices")

# repeat a specific action
connection_attempts = 5
for i in range(connection_attempts):
    print("Connection could not be established")

# define a function
def greet_employee():
    print("Welcome! You're logged in.")
# call a function
greet_employee()

# greet employees by name and last name
def greet_employee(first_name, last_name):
    print("Welcome! You're logged in", first_name, last_name)
greet_employee("Kiara", "Carter")

# explore input and output of print
print("This is a String, but", 75, "is a number")

# explore input and output of type
print(type("security"))
print(type(73.2))

# explore max
a = 1
b = 2
c = 3
print(max(a,b,c))

# use the sorted function
usernames = ["elarson", "bmoreno", "tshah", "gilmore", "eraab", "alek"]
print(sorted(usernames))

# convert an integer into a string
new_string = str(123)
print(type(new_string))

# print the length of a string "Hello"
print(len("Hello "))

# concatenate two strings
print("Hello " + "Python")

# apply upper method to "Hello"
print("Hello".upper())

# apply lower method to "Hello"
print("Hello".lower())

# extract a slice from a string
print("HELLO"[1:4])

# use the index string method
print("HELLO".index("E"))

print("Ubuntu".index("U"))

# extract from a list
my_list = ["DEV","OPS","ENGINEER"]
print(my_list[1])

# concatenate two lists
my_list = ["A", "B", "C", "D", "E"]
number_list = [1, 2, 3, 4, 5]
print(my_list + number_list)

# extract the first three characters from a list of IP addresses
IP = ["198.xxx.yyy.zz", "199.xxx.yyy.zz", "197.xxx.yyy.zz", "196.xxx.yyy.zz"]
networks = []
for address in IP:
    networks.append(address[0:3])
print(networks)

# list of approved users and devices
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]
username = "sgilmore"
device_id = "4n482ts"
if username in approved_users:
    print("The user", username, "is approved to connect the system.")
else:
    print("The user", username, "is not approved to connect the system.")

ind = approved_users.index(username)
print(ind)

if username in approved_users and device_id in approved_devices:
    print("The username", username, "is approved to access the system")
    print(device_id, "is the assigned device for", username)

# expressões regulares
import re
texto = ("Segurança da Informação é essencial")
resultado = re.search("essencial", texto) # search procura o padrão em qualquer parte da string.
print(resultado.group())        
