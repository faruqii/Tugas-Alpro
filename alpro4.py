name = input("Enter cars name: ").split()
Japan = ["Honda","Toyota","Suzuki","Nissan"]
Europe = ["BMW","Mercy","Renault","Ferrari","Lamborghini"]
American = ["Ford","Mustang","Jeep","Chevrolet","Tesla"]

if name[0] in Japan:
    print("That is Japanesse cars")
elif name[0] in Europe:
    print("That is European cars")
elif name[0] in American:
    print("That is American cars")
