
#存放ascll的字符串
str="84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 103, 104, 111, 101, 108, 99, 97, 112, 108, 112, 99, 109"
str2="""37 5F 5F 54 20 5A 5F 52 1C 20 69 5F 65 20 63 5F 5C 66 55 54 20 5F 5E 55 20 5D 5F 62 55 20 53 58 51 5C 5C 55 5E 57 55 20 59 5E 20 69 5F 65 62 20 5A 5F 65 62 5E 55 69 1E 20 44 58 59 63 20 5F 5E 55 20 67 51 63 20 56 51 59 62 5C 69 20 55 51 63 69 20 64 5F 20 53 62 51 53 5B 1E 20 47 51 63 5E 17 64 20 59 64 2F 20 21 22 28 20 5B 55 69 63 20 59 63 20 51 20 61 65 59 64 55 20 63 5D 51 5C 5C 20 5B 55 69 63 60 51 53 55 1C 20 63 5F 20 59 64 20 63 58 5F 65 5C 54 5E 17 64 20 58 51 66 55 20 64 51 5B 55 5E 20 69 5F 65 20 64 5F 5F 20 5C 5F 5E 57 20 64 5F 20 54 55 53 62 69 60 64 20 64 58 59 63 20 5D 55 63 63 51 57 55 1E 20 47 55 5C 5C 20 54 5F 5E 55 1C 20 69 5F 65 62 20 63 5F 5C 65 64 59 5F 5E 20 59 63 20 56 56 57 53 63 51 5D 51 60 5E 5E 5F 1E"""


"""
16 Good0job,0you0solved0one0more0challenge0in0your0journey.0This0one0was0fairly0
easy0to0crack.0Wasn't0it?01280keys0is0a0quite0small0keyspace,0so0it0shouldn't0ha
ve0taken0you0too0long0to0decrypt0this0message.0Well0done,0your0solution
0is0ffgcsamapnno.
"""

res=str2.split(" ")
print(len(res))
j=""
for p in range(10):
	p+=10
	for i in res:
		num=(int(i.strip(),16)+p)%127
		j+=chr(num)
	print(p,j)
	print("")
	j=""