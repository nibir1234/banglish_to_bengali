# coding=utf-8
from bnbphoneticparser import BengaliToBanglish
from bnbphoneticparser import BanglishToBengali

banglish = [
    # "The aristrocrat calls",
    # "Ekhon onek raat tomar kadhe amar niswash",
    # "ami benche achi tomar bhalobasay",
    # "Chuye dile haath",
    # "amar briddho buke tomar matha",
    # "chepe dhore tolchi kemon neshay [x2]",
    # "Ekhan anek rat tomar kandhe amar nissash",
    # "",
    # "Keno je osongkoche ondho ganer koli",
    # "Pakhar bleder tale soja suji kotha boli",
    # "",
    # "Ami vabte parini",
    # "Tumi buker vitor fatcho amar",
    # "Shorir jure tomar premer bij",
    # "Ami thamte parini",
    # "Tomar gaale norom dukkho",
    # "Amay duhat diye muchte dio please..",
    # "",
    # "Tomar gaaner sur",
    # "Amar poket vora sotti mitthe",
    # "rekhe dilam tomar beger nile",
    # "Jani torke bohudur",
    # "Tao amay tumi akre dhoro",
    # "amar vetor barcho tile tile",
    "ami bhalo achi.",
    "tomar khobor ki.",
    "ajke shondha bela tumi ki korcho.",
    "obak bepar holo, ami ekhon bangla likhte pari inglish diye.",
    "aro mojar bepar holo ami dui bhabe likhte pari.",
    "ekTa DairekT arekTa phoneTik.",
    "tomar desh e koto Taka te ek Dolar.",
    "ami ei bhabe abar juk\to bor\no likhte pari.",

]

output = []

# bengali2banglish = BengaliToBanglish()
# bengali_text = "আমি বাংলাদেশি"
# a = bengali2banglish.parse(bengali_text.strip())


banglish2bengali = BanglishToBengali()
for verse in banglish:
    a = banglish2bengali.parse(verse.strip())
    # print(a)
    output.append(a)

for o in output:
    with open("output2.txt", 'ab') as file:
        foo = f"\"{o}\",\n"
        file.write(foo.encode('utf8'))
