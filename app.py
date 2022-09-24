# Tú código va aquí

print("welcom to your horoscope")

def lucky_color(color):
    options = ["Azul","Amarillo","rojo","Lila","Rosa","Morado"]
    option = random.choice(options)
    print("Tu color de la suerte es:", option)
    time.sleep(3)

def read_file(name):
    file_name = "signs/" + name 
    file = open(file_name, "r")
    for line in file:
        print(line)
    time.sleep(3)


def menu():
    print("##############################")
    print("que signo desea consultar")
    print("eligue tu opcion")
    print("1", "aries")
    print("2", "taurus")
    print("3", "cancer")
    print("4", "gemini")
    print("5", "leo")
    print("6", "virgo")
    print("7", "libra")
    print("8", "ecorpio")
    print("9", "sagittarius")
    print("10", "capricornus")
    print("11", "aquarius")
    print("12", "pisces")
    print("exit",)

user_input = ""

while user_input !="exit":
    menu()
    user_input = input()

    if user_input == "1":
        read_file("aries.txt")
    elif user_input =="2":
        read_file("taurus.txt")
    elif user_input =="3":
        read_file("cancer.txt")
    elif user_input == "4":
        read_file("gemini.txt")
    elif user_input == "5":
        read_file("leo.txt")
    elif user_input == "6":
        read_file("virgo.txt")
    elif user_input == "7":
        read_file("libra.txt")
    elif user_input == "8":
        read_file("ecorpio.txt")
    elif user_input == "9":
        read_file("sagittarius")
    elif user_input == "10":
        read_file("capricornus.txt")
    elif user_input == "11":
        read_file("aquarius.txt")
    elif user_input == "12":
        read_file("pisces.txt")
    elif user_input == "13":
        lucky_color()
    elif user_input == "exit":
        print("goodbye")
        exit()
    else:
        print("opciòn incorrecta")
 

