list = ["wiliam","kate","anderson","jame","mady"]

print("a, buat list : {}".format(list))

list.append("jones")
print("b, penambahan jones {}".format(list))

list[2] = "grace"
print("c, Jones menjadi Grace {}".format(list))

check_thomson = "Thomson" in list
print("d, Check thomson : {}".format(check_thomson))

data_urut = sorted(list)
print("e, Sesuai abjad nama : {}".format(data_urut))

print("f, Cetak data menggunakan for")
for index, data in enumerate(data_urut):
	print("kursi ke {} diisi oleh {}".format(index, data))
	
data_urut.clear()
print("g, Clear data : {}".format(data_urut))
