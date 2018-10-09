
# Notes:
# 1. Python 2.7
# 2. pycrypto OR pycryptodome installed (as they clash)
# 3. to switch between install and uninstall like so (and visa-versa):
#
#    A. c:\Python2.7.14\python.exe -m pip uninstall pycrypto
#
#    B1. c:\Python2.7.14\python.exe -m pip install pycryptodome
#    B2. c:\Python2.7.14\python.exe -m pip install pycryptodomex

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

import base64

BEGIN_RSA_PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----\n"
END_RSA_PRIVATE_KEY = "\n-----END RSA PRIVATE KEY-----"


def decrypt_message(encoded_encrypted_msg, public_key_str):

    key = BEGIN_RSA_PRIVATE_KEY + public_key_str + END_RSA_PRIVATE_KEY
    #print "joint key:\n%s" % key

    rsakey = RSA.importKey(key)

    # padding
    rsakey = PKCS1_OAEP. new(rsakey, SHA256)

    decoded_64b_msg = base64.b64decode(encoded_encrypted_msg)

    # Use the private key to decrypt
    decrypted_msg = rsakey.decrypt(decoded_64b_msg)

    return decrypted_msg
