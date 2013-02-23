import urllib2
import sys

def query(q):
        target = 'http://crypto-class.appspot.com/po?er=' + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:
            if e.code == 404:
                return True # good padding
            return False # bad padding

ct = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'

def int2hex(i):
    return hex(i)[2:] if len(hex(i)[2:]) == 2 else '0' + hex(i)[2:]

def exor_pad(i):
    assert(i > 0)
    assert(i<=16)
    return  '00' * (16 -i) + int2hex(i) * i

def exor_g(g,pos):
    assert(pos>=0)
    assert(pos<16)
    return '00' * (15-pos) + int2hex(g) + '00' * pos

def rellenar_zero(s):
    return '0' * (32 - len(s)) + s

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def hexexor(s1,s2):
    return strxor(s1.decode("hex"),s2.decode("hex")).encode("hex")


blocks = ()
while ct:
    blocks = blocks + (ct[:32],)
    ct = ct[32:]

mensaje = ()

probable_range = [ord(' '),] +  range(ord('a'),ord('z')) + range(ord('A'),ord('Z')) + range(17)

for b in range(1,len(blocks)):
    iv = blocks[b-1]
    block = blocks[b]
    msg = ""
    for pos in range(1,17):
        pad = exor_pad(pos)
        lastmsg = rellenar_zero(msg.encode("hex"))
        getletter = 0
        for g in probable_range:
            gpad = exor_g(g,pos-1)
            print "probando " + int2hex(g)
            if query("".join(blocks[:(b-1)]) + hexexor(lastmsg,hexexor(iv,hexexor(gpad,pad))) + block):
                getletter = 1
                break
        if getletter:
            msg = int2hex(g).decode("hex") + msg
        else:
            msg = '?' + msg
        print "mensaje='" + msg + "'"
    mensaje = mensaje + (msg,)
    print "Mensaje bloque " + str(b) + ":" + mensaje[b-1]



iv = blocks[2]
block = blocks[3]

msg = '09'.decode("hex") * 9

for pos in range(10,17):
        pad = exor_pad(pos)
        lastmsg = rellenar_zero(msg.encode("hex"))
        getletter = 0
        for g in probable_range:
            gpad = exor_g(g,pos-1)
            print "probando " + int2hex(g)
            if query("".join(blocks[:(b-1)]) + hexexor(lastmsg,hexexor(iv,hexexor(gpad,pad))) + block):
                getletter = 1
                break
        if getletter:
            msg = int2hex(g).decode("hex") + msg
        else:
            msg = '?' + msg
        print "mensaje='" + msg + "'"
    mensaje = mensaje + (msg,)
    print "Mensaje bloque " + str(b) + ":" + mensaje[b-1]

