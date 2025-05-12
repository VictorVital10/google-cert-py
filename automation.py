# write a text file
with open("C:/Users/vitas/Desktop/login_attempts.txt", "w") as file: # you can also use "a" to add content to the file
    file_text = file.write("attempt1: user1 - asd567\n")
    file_text = file.write("attempt2: user2 - wxt345\n")
    file_text = file.write("attempt3: admin - senha 123\n")
    file_text = file.write("attempt4: root - pass789\n")

# open a text file
with open("C:/Users/vitas/Desktop/login_attempts.txt", "r") as file:
    file_text = file.read()
    print(file_text)

# creating a simple alghoritm
def update_file(import_file, remove_list):
    with open(import_file, "r") as file:
        ip_addresses = file.read()
    for element in ip_addresses:
        if element in remove_list:
            ip_addresses.remove(element)
    with open(import_file, "w") as file:
        file.write(" ".join(ip_addresses))