xor = "\x7f\x18\x63\x02\x64\x08\x39\x49\x7a\x4a\x67\x0f\x22\x12\x3f\x5b\x2e\x03\x6d\x1e\x72\x5f\x6f\x1b\x2b\x5f\x37\x1a\x6c\x5f\x6e\x17\x3a\x58\x6d\x40\x28\x05\x67\x03\x37\x59\x3c\x49\x3a\x0e\x6f\x0c\x69\x44\x2d\x59\x74\x45\x36\x44\x3d\x0e\x23\x55\x78\x1f\x32\x5c\x30\x5f\x33\x1e\x72\x15\x25\x4b\x24\x48\x78\x55\x3b\x5c\x32\x02\x6c\x00\x67\x4a\x2d\x43\x24\x45\x68\x04\x29\x04\x60\x4e\x60\x4e\x27\x0a\x60\x09\x6d\x40\x35\x46\x27\x0a\x79\x0d\x74\x1a\x7d\x1c\x31\x5d\x62\x1b\x36\x58\x75\x14\x63\x0a\x7e\x53\x32\x4b\x66\x10\x75\x58\x31\x42\x30\x5f\x31\x5d\x24\x09\x6e\x0f\x68\x04\x29\x4f\x62\x4f\x3a\x5e\x3f\x51\x3f\x5b\x6a\x59\x29\x5b\x38\x54\x67\x05\x71\x10\x3d\x58\x75\x05\x6d\x02\x7b\x1f\x76\x5b\x34\x41\x25\x46\x29\x04\x6a\x1e\x73\x16\x64\x0c\x69\x44\x21\x0c\x64\x1d\x30\x52\x33\x7f\x30\x1d\x73\x17\x5b\x17\x5b\x17\x5b\x17\x5b\x17\x5b\x14\x58\x14\x58\x14\x58\x17\x5b\x17\x5b\x17\x5b\x17\x5b\x17\x5b\x17\x3a\x76\x39\x75\x18\x7d\x50\x32\x53\x2a\x5e\x73\x1a\x6e\x06\x67\x14\x7b\x0e\x60\x4d\x28\x4f\x3a\x49\x23\x4b\x66\x12\x6b\x09\x68\x45\x28\x4d\x01\x4d\x02\x2f\x63\x4e\x3d\x58\x75\x1a\x71\x03\x70\x1c\x69\x00\x6f\x16\x61\x50\x7d\x50\x39\x55\x21\x11\x24\x48\x65\x15\x38\x4a\x3e\x13\x22\x13\x7b\x48\x65\x02\x6a\x18\x18\x18\x18\x7d\x00"
stage2 = ''
for i in range(0,len(xor)-1):
	stage2 += chr(ord(xor[i])^ord(xor[i+1]))
stage2 += xor[-1]
StringIn=stage2 
print len(StringIn)%6 == 0
i = 0
NewString = ""
while (i < len(StringIn)):
	NewString += StringIn[i+3:i+4:1] + StringIn[i+4:i+5:1] + StringIn[i+2:i+3:1] + StringIn[i+0:i+1:1] + StringIn[i+1:i+2:1] + StringIn[i+5:i+6:1]
	i += 6
print NewString
StringIn = NewString