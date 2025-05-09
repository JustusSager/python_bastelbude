"""
Die Bits der Nachricht werden entsprechend dem Schlüssel vertauscht
"""

import random


def gen(length):
    """
    Random bytes
    :param length: Number of bytes
    """
    return random.randbytes(length)


def enc_dec(key: bytes, message: bytes):
    """Verschlüsseln und Entschlüssel passiert auf die selbe Weise, da die Bits getauscht werden"""
    # Die Nachricht zu einem Integer umwandeln, da sonst die Bitoperator nicht funktionieren
    i_key = int.from_bytes(key)
    i_message = int.from_bytes(message)
    # Bitweises XOR zwischen schlüssel und Nachricht
    result = (i_key ^ i_message)
    # Integer zu Bytes umwandeln
    return result.to_bytes(len(message), 'big')


if __name__ == "__main__":
    message: bytes = b"Dies ist eine testnachricht"
    key = gen(len(message))  # Schlüssel generieren mit der selben Länge wie die Nachricht
    cypher = enc_dec(key, message)
    print(f"cypher: {cypher}")
    res_message = enc_dec(key, cypher)
    print(f"result: {res_message}")
