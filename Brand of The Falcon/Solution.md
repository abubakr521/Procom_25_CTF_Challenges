# Solution
**Disclaimer: **  
This was my first attempt at getting my hands dirty in the hardware category. This was a good learning experience for me and I enjoyed it, hope you like the challenges.
This challenge was inspired by a hardware challenge that I played in the HTB Tryout CTF.
#
The schematic.png basically shows the complete layout of the device/ circuit. .vhdl(VHSIC(Very High Speed Integrated Circuit Program) Hardware Description Language) files describe how electronic circuits function at a logical level.
VHDL is used for designing and simulating digital circuits.  
In hardware and embedded systems, ``.tpm`` usually refers to TPM(Trusted Platform Module), which is a hardware-based security chip used for cryptographic operations, secure storage, and system integrity. It is commonly found in motherboards, 
embedded systems, and IoT devices.  
As you start the challenge you are asked for a 16 bit binary input. Here's how the whole logic works:  
Key (ckey):  
The key is a constant 16-bit value: ``1011010110101100 ``  
Encryption (encryption):  
The encryption process XORs the input data ``D`` with the key ``K``. Additionally, it flips specific bits in the output:  
Bit 2: ``E(2) <= NOT K(2)``  
Bit 7: ``E(7) <= NOT K(7)``  
Bit 12: ``E(12) <= NOT K(12)``  
Backdoor (backdoor):  
The backdoor checks if the input matches a specific pattern: ``0110101110011011``. 
If the input matches the pattern, the backdoor signal B is set to ``1``; otherwise, it is ``0``.  
Output Logic (tpm):  
If the backdoor signal B is ``1``, the output is the key. Otherwise, the output is the encrypted data.  

So keeping all this in mind the correct answer is ``0110101100111001``. This would give you the flag.
#
```diff
AxP25{N0t_th4t_h4rd_w4r3}
```
