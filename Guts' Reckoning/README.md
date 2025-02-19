# Category
Hardware

# Description
Lost in the depths of an ancient stronghold, Guts and his comrades stumble upon a sealed chamber, its entrance bound by an old but functional security system. Among the remnants of forgotten technology, a very popular NOR flash memory chip manufactured by, the adversary, Winbond  catches their attention.

``nc 159.223.46.39 5001``

## Docker Setup Commands
The Client.py file is the challenge file. To play the challenge keep the Dockerfile and the server.py file in the same directory.  
``sudo docker build -t hrdwr2 .``  
``docker run -dit --name hrdwr2 -p 5001:5001 hrdwr2``
