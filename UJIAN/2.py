""" 
# a. variable adalah sebuah tampat untuk menampung sebuah data
    contoh : namaVariable = data
             type_namaVar = data


#b. _t = 18,x = int 0->4  ,y2h = _t - x,

#c. 
    y2h <---
    _t=18
1. y2h di bagian paling atas code akan membuat masalah di mana y2h bukan sebuah syntax maupun variable
    lebih baik dimasukan nilai int(0)

    for x in range(5) <--
2. untuk memasuki block progam harus di awali dengan titik dua/colon(:)

    if x%2=1 : <--
3. perbandiangan nilai sama dengan(=) di python di tandai dengan dua simbol sama dengan (==) bukan (=)

    elif _t>x; <---
4. untuk memasuki blok program di python di tandai dengan titik dua/colon(:) bukan titik koma/semi colon(;)

    _t = _t//x <--
5. jika mau floor division pastikan nilai x bukan sama dengan 0
    ada beberapa solusi
    #1. for x in range(1, 5+1, 1) --> x = int 1 -> 5
    #2. if x != 0 : --> jika x bukan sama dengan 0 jalankan program 
    #3. elif _t > x and x != 0_: --> sama seperti  no 2 tapi lebih simpel
6. sepertinya maksud dari pembuat program di bagian--
    elif _t>x:
    --> _t = _t//x --> adalah y2h = _t//x
"""

y2h = 0
_t = 18
for x in range(5):
    if x%2==1:
        y2h = _t-x
    elif _t>x and x != 0:
        y2h = _t//x
    else:
        y2h = y2h+1
    print(x,y2h)
