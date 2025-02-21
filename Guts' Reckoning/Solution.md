# Solution 
This file was basically a client server architecture where the server was running in the docker and the players had the client file.  
The description had a very big hint: **a very popular NOR flash memory chip manufactured by, the adversary, Winbond**. 
A simple google search for popular NOR flash memory chip manufactered by Winbond reveals that it is a chip 
commonly used in various electronic devices for storing firmware, configuration data, and other types of non-volatile memory. The client basically asks for some command which is 
visible in the last line of the code  
``jedec_id = exchange([0x9F], 0)``  
``print(jedec_id)``  
You should have noticed that when you run the client it gives you this response: ``[]``. That's because of the ``0`` in the exchange command, once you start incresing that number you start getting the flag.  
With a little trial and error you will get to number 68, now you just have to put the decimals in cyberchef and convert it into ASCII to get the complete flag.  
``jedec_id = exchange([0x9F], 68)``    

***If you wish to further understand the working of the chip head over to this write up by Abdul Issa, [https://infosecwriteups.com/htb-cyber-apocalypse-ctf-2024-hardware-a45ddedae49b](url), which was the inspiration for this challenge.
Here he has explained the working of the chip in quite great detail.***
#
```diff
AxP25{Why_d0_I_S33_th1ng5_..._4ft3r_th3y_4r3_d0n3_4nd_g0n3}
```
