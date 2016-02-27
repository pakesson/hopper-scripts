# Deobfuscate strings in rezk2ll's BeatME
# http://crackmes.de/users/rezk2ll/beatme/
#
# Philip Akesson

doc = Document.getCurrentDocument()
seg = doc.getCurrentSegment()
start = doc.getCurrentAddress()

seg_addr = seg.getStartingAddress()
seg_len = seg.getLength()

tmp = []

doc.log("Starting address: 0x%X" % seg_addr)

for addr in range(start, seg_addr + seg_len):
    b = seg.readByte(addr)
    if b == 0:
        break
    tmp.append(b-1)

deobfuscated_string = ''.join([chr(i) for i in tmp]).replace("\n", "")
doc.log("Deobfuscated string: %s" % deobfuscated_string)
seg.setInlineCommentAtAddress(start, deobfuscated_string)
