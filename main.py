"""
2022/01/15
code:phillychi3
admin:https://blog.csdn.net/qq_17550379/article/details/79006655
"""

import pyautogui 
from mido import MidiFile
import time
import ctypes, sys



c3 = 48 #lower  
c4 = 60
c5 = 72
b5 = 83 #high

# uccu = [ c d e f g a b 
#          c d e f g a b 
#          c d e f g a b ]

key = ["z", "x", "c", "v", "b", "n", "m", #c3~b3
       "a", "s", "d", "f", "g", "h", "j", #c4~b4
       "q", "w", "e", "r", "t", "y", "u"] #c5~b5

idk = {
    "48":"z",
    "49":"z",
    "50":"x",
    "51":"x",
    "52":"c",
    "53":"v",
    "54":"v",
    "55":"b",
    "56":"b",
    "57":"n",
    "58":"n",
    "59":"m",
    "60":"a",
    "61":"a",
    "62":"s",
    "63":"s",
    "64":"d",
    "65":"f",
    "66":"f",
    "67":"g",
    "68":"g",
    "69":"h",
    "70":"h",
    "71":"j",
    "72":"q",
    "73":"q",
    "74":"w",
    "75":"w",
    "76":"e",
    "77":"r",
    "78":"r",
    "79":"t",
    "80":"t",
    "81":"y",
    "82":"y",
    "83":"u"
}

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def main():
    print("我不知道我為甚麼不睡覺寫這東西")
    print("希望寫的出來")
    file = input("請輸入檔案名稱:")
    midi = MidiFile(f"midi_data/{file}")
    print(midi.length)
    print("將會在3秒鐘後開始演奏")
    time.sleep(3)

    for msg in midi.play():
        if msg.type == "note_on" or msg.type == "note_off":
            time.sleep(msg.time)
            note = msg.note 
            if msg.note < 48:
                continue
            if msg.note > 83:
                continue
            note = str(note)
            pyautogui.press(str(idk[note]))
                

if __name__ == '__main__':

    if is_admin():
        main()
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    
