#input
nama = input('Masukkan Nama : ')
tugas = float(input('Masukkan nilai Tugas : '))
uts = float(input('Masukkan nilai UTS : '))
uas = float(input('Masukkan nilai UAS : '))

#nilai akhir
nilai = (0.15 * tugas) + (0.35 * uts) + (0.50 * uas)

#grade
if nilai > 80:
    grade = 'A'
elif nilai > 70:
    grade = 'B'
elif nilai > 60:
    grade = 'C'
elif nilai > 50:
    grade = 'D'
else:
    grade = 'E'

#status
if nilai > 60:
    status = 'Lulus'
else:
    status = 'TIdak lulus'

#output
print (' ')
print ('Nama Siswa : ' , nama)
print ('Nilai Akhir : ' , nilai)
print ('Grade : ' , grade)
print ('Status : ' , status)
