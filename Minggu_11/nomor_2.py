f = open('nama_kelompok.txt','r')
text = f.read()
jumlah_kata = text.split()
f1 = open('soal_2_nama_kelompok.txt','w')
for i in range(len(jumlah_kata)):
    f1.write("Kata ke %d adalah %s \n" % (i+1, jumlah_kata[i]))