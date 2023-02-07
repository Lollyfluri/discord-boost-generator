import time,sys,random,string,requests
from colorama import Fore

main = "https://discord.gift/"
def slowtype(text):
  for i in text:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.09)


def generator16():
    final_str1 =''.join(random.choice(string.ascii_letters) for i in range (16))
    return final_str1

def generator24():
  final_str2 = ''.join(random.choice(string.ascii_letters)for i in range (24))
  return final_str2

slowtype("Bienvenido al generador de codigos de discord nitro de ⱠØⱠⱠɎ₣ⱠɄⱤł :)\n")
print("*****************************************************************")
slowtype("Primero comentame que discord quieres?\n")
el = int(input("1) Discord nitro normal (16 caracteres) 2)nitro boost (24 caracteres): "))
linknum = int(input("Cuantos codigos quieres generar? "))

  
if el == 1 :
  for i in range(linknum):
    web_url = "https://discord.gift/"+ generator16()
    r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{generator16()}?with_application=false&with_subscription_plan=true")
    if r.status_code == 200: 
      print(Fore.GREEN+"VALID: " + web_url)
      break
    elif r.status_code != 200:
      print(Fore.RED+"INVALID: " + web_url)
    i += 1
elif el == 2:
  for i in range(linknum):
    web_url = generator24()
    r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{web_url}?with_application=false&with_subscription_plan=true")
    if r.status_code == 200: 
      print(Fore.GREEN+"VALID: "+ "https://discord.gift/" + web_url)
      break
    elif r.status_code != 200:
      print(Fore.RED+"INVALID: "+"https://discord.gift/" + web_url)
    i += 1
else:
  print("Lo siento pero esa opcion no esta disponible por ahora")

