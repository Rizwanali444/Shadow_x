![1000255603](https://github.com/user-attachments/assets/9b6dca8e-7230-43f2-a025-ee7c481a28f6)

![1000255601](https://github.com/user-attachments/assets/101aa968-31b6-43e8-ba8d-f45f1e978082)

# Tool Name: Shadow_x
# Author: Rizwan Ali
Shadow_x is a powerful Python script encryption and decryption tool designed to help developers protect their Python code from unauthorized access or tampering. The tool supports multiple encryption techniques including:

Marshal Encryption
Base64 Encryption
Marshal + Zlib + Base64 (Strong Mix)
XOR Encryption (1 Character Key)
Lambda Obfuscation Encryption

# Installation Requirements (For Termux):

rm -rf Shadow_x
git clone https://github.com/Rizwanali444/Shadow_x.git
cd Shadow_x
sed -i '1i#!/data/data/com.termux/files/usr/bin/python' shadow_x.py
chmod +x shadow_x.py
./shadow_x.py

Make sure you have Python and necessary packages installed:

# bash
Copy code
pkg update && pkg upgrade
pkg install python git
pip install requests colorama
