def encode(s):
    encoded = ''
    for x in s:
        encoded += code[x] + ' '
    print("Encoded message: " + encoded)


def decode(msg):
    decoded = ''
    for y in msg.split(' '):
        key_list = list(code.keys())
        val_list = list(code.values())
        print(key_list[val_list.index(y)], end='')


alphabets = [' ']
alpha = 'a'
for i in range(0, 26):
    alphabets.append(alpha)
    alpha = chr(ord(alpha) + 1)
cypher = ['__', '_|', '|_|', '|_', ']', '[]', '[', '`|', '|`|', '|`', '._|', '|_._|', '|_.', '.]', '[.]',
          '[.', '.`|', '|`.`|', '|`.', '>', 'V', '<', '^', '.>', 'V.', '<.', '^.']

code = dict(zip(alphabets, cypher))
print(code)

message = input("Enter message: ")
encode(message.strip())
decode_message = input("Enter encoded text: ")
decode(decode_message.strip())



