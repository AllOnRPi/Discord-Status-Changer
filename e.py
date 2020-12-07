import tkinter as tk
from tkinter import ttk
from tkinter import * 
import os,requests,json
from colorama import Fore, init, Style
init(convert = True)
os.system("title github.com/kieronia Status Changer")

# this is a function which returns the selected combo box item
def change():
	try:
		with open('token.txt', 'r', encoding='UTF-8') as f: token = f.read()
	except:
		print(" > Error accesing token.txt - did u delete the file , did u forget to extract me :(")
	if token == "":
		print(" > Put your discord token in token.txt")
	token = token.replace('"','')
	choice = comboOneTwoPunch.get()
	headers = {'Authorization': token, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*'}
	if "online" in choice.lower():
		os.system("title Changing Status To : [Online]")
		print(f" {Fore.GREEN}>{Fore.WHITE} Changing status to Online")
		ree = requests.patch("https://discord.com/api/v8/users/@me/settings",headers=headers,json={"status":"online"}).status_code
		if ree == 200:
			print(f"{Fore.GREEN} >{Fore.WHITE} Changed status to Online")
			os.system("title Status Changed To : [Online]")
		else:
			print(" > Error Changing Status - Please Check Your Token In token.txt Is VALID")
			os.system("Error")
	if "idle" in choice.lower():
		os.system("title Changing Status To : [Idle]")
		print(f"\u001b[33m > {Fore.WHITE}Changing status to Idle")
		ree = requests.patch("https://discord.com/api/v8/users/@me/settings",headers=headers,json={"status":"idle"}).status_code
		if ree == 200:
			print(f" \u001b[33m>{Fore.WHITE} Changed status to Idle")
			os.system("title Status Changed To : [Idle]")
		else:
			print(" > Error Changing Status - Please Check Your Token In token.txt Is VALID")
			os.system("Error")		
	if "do not disturb" in choice.lower():
		os.system("title Changing Status To : [Do Not Disturb]")
		print(f"{Fore.RED} >{Fore.WHITE} Changing status to Do Not Disturb")
		ree = requests.patch("https://discord.com/api/v8/users/@me/settings",headers=headers,json={"status":"dnd"}).status_code
		if ree == 200:
			print(f" {Fore.RED}>{Fore.WHITE} Changed status to Do Not Disturb")
			os.system("title Status Changed To : [Do Not Disturb]")
		else:
			print(f" > Error Changing Status - Please Check Your Token In token.txt Is VALID")
			os.system("Error")		
	if "invisible" in choice.lower():
		os.system("title Changing Status To : [Invisible]")
		print(f" >{Fore.WHITE} Changing status to Invisible")
		ree = requests.patch("https://discord.com/api/v8/users/@me/settings",headers=headers,json={"status":"invisible"}).status_code
		if ree == 200:
			print(f" >{Fore.WHITE} Changed status to Invisible")
			os.system("title Status Changed To : [Invisible]")
		else:
			print(" > Error Changing Status - Please Check Your Token In token.txt Is VALID")
			os.system("Error")



root = Tk()

root.geometry('661x411')
root.configure(background='#00FFFF')
root.title('Discord Status Changer')


comboOneTwoPunch= ttk.Combobox(root, values=['Online', 'Idle', 'Do Not Disturb', 'Invisible'], font=('arial', 12, 'bold'), width=15)
comboOneTwoPunch.place(x=236, y=150)
comboOneTwoPunch.current(1)


Button(root, text='Change', bg='#7FFFD4', font=('arial', 25, 'bold'), command=change).place(x=238, y=180)


discord= Canvas(root, height=45, width=45)
picture_file = PhotoImage(file = 'discordlogo.gif') 
discord.create_image(50, 0, anchor=NE, image=picture_file)
discord.place(x=298, y=46)


root.mainloop()
