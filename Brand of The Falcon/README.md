# Category
Hardware

# Description
As Guts traverses the treacherous wastelands in search of answers, he stumbles upon the ruins of an ancient stronghold, rumored to have once belonged to the Falcon Order. Among the wreckage, he finds a mysterious relic—a long-forgotten encryption device, seemingly untouched by time. The markings on the device resemble those of the God Hand, hinting at a dark secret hidden within its circuits.

Through careful examination, you determine that the device uses an advanced crypto-processor, one that encrypts all outgoing transmissions. However, there are whispers of an ancient backdoor, known only to the chosen. If you can find the right sequence to break the encryption, you may unveil the lost secrets of the Eclipse.

## Docker Setup Commands
The .vhdl files and the schematic.png are the challenge files. To complete the challenge, setup the Dockerfile and the hrdwr1.py file in the same directory.  
``sudo docker build -t hrdwr1 .``  
``sudo docker run -dit --name hrdwr1 -p 31337:31337 hrdwr1``
