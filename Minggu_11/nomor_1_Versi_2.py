f = open('nama_kelompok.txt','r')
text = f.read()
text = text.replace('\n',' ')
print(text)
f1 = open('nama_kelompok_baru.txt','w')
f1.write(text)
