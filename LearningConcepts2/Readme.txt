Requires pycryptodome and python 3 use pip install pycryptodome

Part 1: AESen.py and AESde.py, AESKey.txt
Run AESen first to encrypt and send data to ctext.txt then AESde to decrypt ctext. AESKey.txt is the secret key. Do not modify.

Part 2: RSAen.py, RSAde.py, RSAkeyPair.pem, RSAublicKey.pem 
Run RSAen first to encrypt and send data to ctext.txt then RSAde to decrypt ctext. RSAkeyPair.pem is the private key, RSApublicKey.pem is the public key. Do not modify them.

Part 3: AESTimed.py, RSATimed.py
These files generate their own keys every test case since they are not required to read it from a file and having 6 keys (one for each test case) is impractical. 
Select the key size by inputting 1, 2, or 3. Then input the message to be encrypted/decrypted. The program must be rerun per each testcase.
