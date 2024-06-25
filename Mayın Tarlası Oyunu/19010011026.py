import random
fonk = 0
while fonk == 0:
    Tarla = []
    dongu = 0

    while dongu == 0 :
         print("-"*80)
         boyut = int(input("Tarla boyutunu giriniz : "))
         if(boyut < 10) :
            print("!!oyun alanini büyütünüz!!")

         else:
             dongu +=1
             break

    for i in range(boyut):
        Tarla.append(["?"] * boyut)

    def Tarla_Yazdır(boyut):
        i=0
        print(end="\n* ")
        for j in range(0,boyut):
            print( j,end=" ")
        print(end="\n")
        for satir in Tarla:
            print(i ," ".join(satir))
            i += 1

    MayinSayisi = int((boyut*boyut)*0.3)
    Mayinlar = []
    Mayin =[]

    for i in range(MayinSayisi):
        Mayin = [random.randint(0,boyut-1),random.randint(0,boyut-1)]
        for j in Mayinlar:
           if Mayin[0]==j[0] and Mayin[1]==j[1]:
               Mayin = [random.randint(0,boyut-1),random.randint(0,boyut-1)]
        Mayinlar.append(Mayin)
    print("-"*80)
    mod = int(input("Kapalı mod için 1'e \nAçık mod için 2'ye tıklayınız : "))
    print("-"*80)
    if mod == 1:

        altkontrol = 0
        puan =0
        while altkontrol == 0:
            puan +=1
            print("\n"*30)
            Tarla_Yazdır(boyut)
            print("-"*80)
            Tahminkontrol =0
            while Tahminkontrol == 0:

                TahminSatır = int(input("Hangi Satırı Tahmin Ediyorsunuz : "))
                TahminSutun = int(input("Hangi Sütunu Tahmin Ediyorsunuz : "))
                if TahminSatır >boyut or TahminSutun > boyut:
                    print("!Alanın Dışına Çıkmayınız!")
                    print("-"*80)
                    continue
                elif TahminSatır <0 or TahminSutun<0:
                    print("!Alanın Dışına Çıkmayınız!")
                    print("-"*80)
                    continue
                else:
                    Tahminkontrol +=1
            print("-"*80)
            YakındakiMayin = 0
            Tahminler = []
            Tahmin = [TahminSatır, TahminSutun]
            Tahminler.append(Tahmin)
            for k in Tahminler:
               if TahminSatır == k[0] and TahminSutun == k[1]:
                   print("!Buraya Zaten Atış Yapmıştınız!")

            for i in Mayinlar:
                if Tahmin[0] == i[0] and Tahmin[1] == i[1]:
                    for j in range(boyut):
                        for x in range(boyut):
                            Tarla[j][x] = "X"

                    Tarla_Yazdır(boyut)
                    print("Puanınız : ")
                    print(puan)
                    print("!Maledef Mayına Bastınız!")
                    altkontrol +=1

                if TahminSatır-1== i[0] and TahminSutun-1 ==i[1]:
                    YakındakiMayin += 1
                if TahminSatır == i[0] and TahminSutun-1==i[1]:
                    YakındakiMayin +=1
                if TahminSatır+1 == i[0] and TahminSutun-1==i[1]:
                    YakındakiMayin +=1
                if TahminSatır-1== i[0] and TahminSutun ==i[1]:
                    YakındakiMayin +=1
                if TahminSatır== i[0] and TahminSutun ==i[1]:
                    YakındakiMayin +=1
                if TahminSatır+1== i[0] and TahminSutun ==i[1]:
                    YakındakiMayin +=1
                if TahminSatır-1== i[0] and TahminSutun+1 ==i[1]:
                    YakındakiMayin +=1
                if TahminSatır== i[0] and TahminSutun +1==i[1]:
                    YakındakiMayin +=1
                if TahminSatır+1== i[0] and TahminSutun+1 ==i[1]:
                    YakındakiMayin +=1

            Tarla[TahminSatır][TahminSutun] =  str( YakındakiMayin )


    elif mod == 2:

        for i in Mayinlar:
            Tarla [i[0]][i[1]] = "M"
        altkontrol = 0
        puan = 0
        while altkontrol == 0:
            print("\n"*30)
            puan +=1
            Tarla_Yazdır(boyut)
            print("-"*80)
            Tahminkontrol =0
            while Tahminkontrol == 0:

                TahminSatır = int(input("Hangi Satırı Tahmin Ediyorsunuz : "))
                TahminSutun = int(input("Hangi Sütunu Tahmin Ediyorsunuz : "))
                if TahminSatır >boyut or TahminSutun > boyut:
                    print("!Alanın Dışına Çıkmayınız!")
                    print("-"*80)
                    continue
                elif TahminSatır <0 or TahminSutun<0:
                    print("!Alanın Dışına Çıkmayınız!")
                    print("-"*80)
                    continue
                else:
                    Tahminkontrol +=1

            print("-"*80)
            YakındakiMayin = 0
            Tahminler = []
            Tahmin = [TahminSatır, TahminSutun]
            Tahminler.append(Tahmin)
            for k in Tahminler:
               if TahminSatır == k[0] and TahminSutun == k[1]:
                   print("!Buraya Zaten Atış Yapmıştınız!")

            for i in Mayinlar:
                if Tahmin[0] == i[0] and Tahmin[1] == i[1]:
                    for j in range(boyut):
                        for x in range(boyut):
                            Tarla[j][x] = "X"

                    Tarla_Yazdır(boyut)
                    print("Puanınız :")
                    print(puan)
                    print("!Maledef Mayına Bastınız!")
                    altkontrol +=1

                if TahminSatır-1== i[0] and TahminSutun-1 ==i[1]:
                    YakındakiMayin += 1
                if TahminSatır == i[0] and TahminSutun-1==i[1]:
                    YakındakiMayin +=1
                if TahminSatır+1 == i[0] and TahminSutun-1==i[1]:
                    YakındakiMayin +=1
                if TahminSatır-1== i[0] and TahminSutun ==i[1]:
                    YakındakiMayin +=1
                if TahminSatır== i[0] and TahminSutun ==i[1]:
                    YakındakiMayin +=1
                if TahminSatır+1== i[0] and TahminSutun ==i[1]:
                    YakındakiMayin +=1
                if TahminSatır-1== i[0] and TahminSutun+1 ==i[1]:
                    YakındakiMayin +=1
                if TahminSatır== i[0] and TahminSutun +1==i[1]:
                    YakındakiMayin +=1
                if TahminSatır+1== i[0] and TahminSutun+1 ==i[1]:
                    YakındakiMayin +=1

            Tarla[TahminSatır][TahminSutun] =  str( YakındakiMayin )
    
    Kazandıranpuan = int((boyut*boyut) - MayinSayisi)

    if Kazandıranpuan == puan:
        print("-"*80)
        print("! Tebrikler Oyunu Kazandınız !")
        print("puanınız :")
        print(puan)
        print("-"*80)


    kontrol = int(input("Devam etmek istiyorsanız 1'e istemiyorsanız 2'ye basınız : "))
    if kontrol == 1:
       print("\n"*30)
       continue
    else:
        fonk += 1


