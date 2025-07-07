from winotify import Notification, audio
import json
import random
import time
from datetime import datetime

cheatsheet={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',
            13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z',27:'a',
            28:'b',29:'c',30:'d',31:'e'}

fin=open("dictionary.json" ,"r")

cont=json.load(fin)
current_datetime = datetime.now()
day = current_datetime.day
month=current_datetime.month
year=current_datetime.year

letter=cheatsheet[day]
letter_list=[]
for (i,v) in cont.items():
    if i.startswith(letter):
        letter_list.append((i,v))

def send_notification():
    word,meaning=random.choice(letter_list)
    toast=Notification(app_id="WORD OF THE DAY",
                   title=(f"Date:{day}/{month}/{year}\n"
                        f"Letter-'{letter.capitalize()}'\n"),
                   msg=(f"{word.capitalize()}: {meaning}\n"
                       f"  *****Enjoy Learning*****"),
                   duration="long",
                   icon=r"wod.png")
                   
    toast.set_audio(audio.Default, loop=False)
    toast.show()

def main():
    while True:
        send_notification()
        time.sleep(15) 

if __name__ == "__main__":
    main()