from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from base64 import b64decode


def Gen(bits=1024):
    keypair = RSA.generate(bits, e=65537)
    public_key = keypair.public_key().exportKey("PEM")
    private__key = keypair.exportKey("PEM")
    return public_key, private__key


def Enc(public_key, message):
    pk = RSA.importKey(public_key)
    rsa_oaep_es = PKCS1_OAEP.new(pk)
    ciphertext = rsa_oaep_es.encrypt(message)
    return ciphertext


def Dec(private_key, ciphertext):
    sk = RSA.importKey(private_key)
    rsa_oaep_es = PKCS1_OAEP.new(sk)
    message = rsa_oaep_es.decrypt(ciphertext)
    return message


if __name__ == "__main__":
    (public_key, private_key) = Gen()
    cypher = Enc(public_key, b"TestText123")
    decypher = Dec(private_key, cypher)
    print(decypher)
