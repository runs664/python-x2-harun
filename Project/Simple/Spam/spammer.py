import pyautogui, time
time.sleep(7) # selama durasi sleep ini, persiapkan kursor ketik '|' ke media yang diinginkan, misal WhatsApp, Telegram, dan lain-lain
f = open("Project/Simple/Spam/text.txt", 'r') # teks untuk bahan spam (spam akan berisi ini semua), jika ada 35 baris, maka terbuat 35 pesan
for word in f:
    pyautogui.typewrite(word) # eksekusi penyalinan file spam ke media spam
    pyautogui.press("enter") # eksekusi enter (mengirimkan pesan)
print("Spam selesaiiii Mweheheheheeee")
input() # pause console