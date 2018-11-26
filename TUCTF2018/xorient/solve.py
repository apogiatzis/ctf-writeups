import string

def xor(msg, key):
    o = ''
    for i in range(len(msg)):
        o += chr(ord(msg[i]) ^ ord(key[i % len(key)]))
    return o

with open('encrypted', 'r') as f:
    msg = ''.join(f.readlines())


# Phase 1 - Find part of key
# part_of_msg = 'TUCTF{'

#for i in range(len(msg)):
#    candidate = xor(msg[i:i+len(part_of_msg)], part_of_msg)
#    if candidate.isalnum():
#        print(candidate)



# Phase 2
partial_key = 'XORISC'

# I guess that key is XORISCOOL

key = 'XORISCOOL'

print(xor(msg,key))
