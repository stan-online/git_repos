k=0
a1=3
a2=1
a3=3
a4=4
а5=1
n=input("Как вас зовут?")
print("Здравствуйте",n)
a=int(input("Ваш любимый жанр фильмов? 1- боевики 2-детективы 3-фантастика"))
if (a==a1):
    k=k+1
a=int(input("Ваша любимая музыка? 1- классика 2-рэп 3-поп"))
if (a==a2):
    k=k+1
a=int(input("Ваш любимый цвет? 1- красный 2-желтый 3-зеленый"))
if (a==a3):
    k=k+1
a=int(input("Ваше любимое время года? 1- осень 2-зима 3-весна 4- лето"))
if (a!=a4):
    k=k+1
    print("Почему не лето ваше любимое время года?")
a=int(input("Ваш вид темперамента? 1- холерик 2-флегматик 3-меланхолик 4- сангвиник"))
if (a==a1):
    k=k+1
if (k>=2):
    print(n,"мы с вами подружимся")
if (k<2):
    print(n+" мы с вами очень разные")