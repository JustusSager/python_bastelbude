"""
Jeder Buchstabe wird um x Stellen (relativ zum Alphabet) verschoben.
"""

def Enc(key, message):
    cypher = ""
    message = message.upper()
    for m_buchst in message:
        if ord(m_buchst) == 32:  # Leerzeichen beibehalten
            cypher += " "
        if 65 <= ord(m_buchst) <= 90:
            c_buchst = chr((((ord(m_buchst) - 65) + key) % 26) + 65)
            cypher += c_buchst
    return cypher


def Dec(k, c):
    message = ""
    c = c.upper()
    for c_buchst in c:
        if ord(c_buchst) == 32:
            message += " "
        elif ord(c_buchst) >= 65 and ord(c_buchst) <= 90:
            m_buchst = chr((((ord(c_buchst) - 65) - k) % 26) + 65)
            message += m_buchst
    return message

def Brute_Force_Message(c):
    for i in range(26):
        print(f"{i}: {Dec(i, c)}")


if __name__ == "__main__":
    # Verschlüsseln einer Nachricht
    message = "Dies ist eine sehr geheime Nachricht"
    cypher = Enc(3, message)
    print(message, " -> ", cypher)

    # Entschlüsseln einer Nachricht
    message = Dec(3, cypher)
    print(cypher, " -> ", message)

    # Brute Force Message
    cypher = "fbrp kyv jvtlizkp fw trvjri tzgyvij gifsrscp yru efkyzex kf uf nzky kyv rjjrjjzerkzfe slk zk drbvj wfi r xffu jkfip"
    Brute_Force_Message(cypher)
