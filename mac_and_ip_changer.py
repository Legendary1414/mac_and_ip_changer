import os
import random
import time
import subprocess

while True:
	try:
		os.system("apt-get install figlet")
		os.system("clear")
		os.system("figlet Mac and ip changer")

		print("""

	 ____________________________________
	|Producer : Hasan Alali              |
	|Age : 14                            |
	|From : Turkey                       |
	|For support : hasansupprt.gmail.com |
	|instagram : cyber_lord_hasan        |
	|____________________________________|



1) constantly change ip address
2) constantly change mac address
3) constantly change ip and mac address
4) show mac address
5) show ip address
6) enter mac address
7) enter ip address
8) show random ip and mac address
9) Revert to orginal mac address
10) Meaningful mac change
11) help
			""")

		add1 = str(input("choose an option: "))

		def change_ip_address(interface, ip):
					os.system(f"sudo ifconfig {interface} {ip}")


		def change_mac_address(interface, mac_mac):
					os.system(f"sudo ifconfig {interface} down")
					os.system(f"sudo ifconfig {interface} hw ether {mac_mac}")
					os.system(f"sudo ifconfig {interface} up")


		def change_ip_mac_address(ip, interface, mac_mac):
					os.system(f"sudo ifconfig eth0 {ip}")

					os.system(f"sudo ifconfig {interface} down")
					os.system(f"sudo ifconfig {interface} hw ether {mac_mac}")
					os.system(f"sudo ifconfig {interface} up")


		def get_mac_address(interface):
			output_mac = subprocess.check_output(["ifconfig", interface])
			output_mac = output_mac.decode("utf-8")
			mac_index = output_mac.find("ether ")
			if mac_index != -1:
				mac = output_mac[mac_index+6:].split()[0]
				return mac
			else:
				return None


		def get_ip_address(interface):
			output_ip = subprocess.check_output(["ifconfig", interface])
			output_ip = output_ip.decode("utf-8")
			ip_index = output_ip.find("inet ")
			if ip_index != -1:
				ip = output_ip[ip_index+4:].split()[0]
				return ip
			else:
				return None


		if add1 == "1":
			interface = input("interface: ")
			add2 = float(input("Every few seconds change: "))
			count1 = 1

			while True:
				ip = ".".join(str(random.randint(0, 255)) for _ in range(4))

				change_ip_address(interface, ip)

				print(f"{count1}. ip address is changed.")
				count1 += 1

				time.sleep(add2)

		elif add1 == "2":
			interface = input("interface: ")
			add3 = float(input("Every few seconds change: "))
			count2 = 1

			while True:
				mac = [random.randint(0x00, 0xff) for _ in range(6)]
				mac_mac = ":".join(map(lambda x: "%02x" % x,mac))

				change_mac_address(interface, mac_mac)

				print(f"{count2}. mac address is changed.")
				count2 += 1

				time.sleep(add3)

		elif add1 == "3":
			interface = input("interface: ")
			add4 = float(input("Every few seconds change: "))
			count3 = 1
			while True:
				ip = ".".join(str(random.randint(0, 255)) for _ in range(4))

				mac = [random.randint(0x00, 0xff) for _ in range(6)]
				mac_mac = ":".join(map(lambda x: "%02x" % x,mac))

				change_ip_mac_address(ip, interface, mac_mac)

				print(f"{count3}. ip and mac address is changed.")
				count3 += 1

				time.sleep(add4)

		elif add1 == "4":
			while True:
				interface = input("interface: ")
				mac_address = get_mac_address(interface)

				print("Your mac address:", mac_address)

				ques = input("Do you want to continue y/n : ")

				if ques == "y":
					break
				elif ques == "n":
					exit()
				else:
					print("This option is not found!!!")
					exit()

		elif add1 == "5":
			while True:
				interface = input("interface: ")
				ip_address = get_ip_address(interface)

				print("Your ip address:", ip_address)

				ques1 = input("Do you want to continue y/n : ")

				if ques1 == "y":
					break
				elif ques1 == "n":
					exit()
				else:
					print("This option is not found!!!")
					exit()

		elif add1 == "6":
			interface = input("interface: ")
			mac = input("Enter the mac address you want: ")

			change_mac_address(interface, mac)

		elif add1 == "7":
			interface = input("interface: ")
			ip = input("enter the ip address you want: ")

			change_ip_address(interface, ip)

		elif add1 == "8":
			while True:
				ip = ".".join(str(random.randint(0, 255)) for _ in range(4))

				mac = [random.randint(0x00, 0xff) for _ in range(6)]
				mac_mac = ":".join(map(lambda x: "%02x" % x,mac))

				print("\nRandom ip:", ip)
				print("\nRandom mac:", mac_mac)

				ques = input("\nDo you want to repeat the process y/n : ")

				if ques == "y":
					continue
				elif ques == "n":
					break
				else:
					print("This option is not found!!!")
					exit()
			
		elif add1 == "9":
			os.system(f"sudo macchanger {interface} -p")
			
			print("Reverted to original mac address.")

		elif add1 == "10":
			interface = input("interface: ")
			add5 = float(input("Every few seconds change: "))
			count4 = 1

			while True:
				os.system(f"macchanger {interface} -a")

				print(f"{count1}. mac address is changed.")
				count4 += 1

				time.sleep(add5)

		elif add1 == "11":
			language = input("Your language Turkish or English : ")

			while True:
				if language == "Turkish":
					print("""
__________________________________________________________________________________________________________________________________________________________
					
1 = raskele ip adresleri olusturur ve mevcut ip adresi ile belirlediginiz araliklarla degistirir.


2 = raskele mac adresleri olusturur ve mevcut mac adresi ile belirlediginiz araliklarla degistirir.(bu mac adres ile internete yani firefox ve google gibi yerlere giremezsiniz.)


3 = raskele ip ve mac adresleri olusturur ve mevcut ip ve mac adresleri ile belirli araliklarla degistirir.


4 = mevcut mac adresinizi gosterir.


5 = mevcut ip adresinizi gosterir.


6 = size istediginiz mac adresini mevcut mac adresiniz ile degistirir.


7 = size istediginiz ip adresini mevcut ip adresiniz ile degistirir.


8 = size raskele ip ve mac adresi verir.


9 = size guvenli ve gercek mac adresleri olusturur ve mevcut mac adresi ile belirlediginiz araliklarla degistirir.(bu mac adres ile internete yani firefox ve google gibi yerlere girmenizi saglar.)


10 = mevcut mac adresinizi orjinal mac adresiniz ile degistirir.


							""")
					ques2 = input("Do you want to continue y/n : ")

					if ques2 == "y":
						break
					elif ques2 == "n":
						exit()
					else:
						print("This option is not found!!!")
						exit()

				elif language == "English":
					while True:
						print("""
__________________________________________________________________________________________________________________________________________________________
						
1 = Creates fast ip addresses and switches between the available ip addresses and the intervals you specify.


2 = random mac addresses are created and the current mac address is selected with the ranges you specify. (You cannot access the internet with this mac address, that is, places such as firefox and google.)


3 = Generates random ip and mac addresses and matches available ip and mac addresses at regular intervals.


4 = will show your current mac address.


5 = will show your current ip address.


6 = replaces the mac address you want with your current mac address.


7 = It replaces the ip address you want with your current ip address.


8 = gives you a random ip and mac address.


9 = It creates secure and real mac addresses for you and changes them at intervals that you specify with the current mac address. (With this mac address, it allows you to access the internet, that is, places such as firefox and google.)


10 = Replaces your current mac address with your original mac address.


								""")

						ques3 = input("Do you want to continue y/n : ")

						if ques3 == "y":
							break
						elif ques3 == "n":
							exit()
						else:
							print("This option is not found!!!")
							exit()

				else:
					print("This language is not found!!!")
					exit()
		else:
			print("This option is not found!!!")

	except KeyboardInterrupt:
		while True:
			choice = input("\nDo you want to reactivate the tool? y/n :")

			if choice == "y":
				break

			elif choice == "n":
				exit()
