print(" "*10,"*"*40)
print(" "*10," "*10," KALKULATOR BMI"," "*10)
print(" "*10,"*"*40,"\n")
def  BMI():
    try:
      b=float(input("\t"*4+"1.Masukkan berat anda(kg) :"))
      t=float(input("\t"*4+"2.Masukkan ketinggian anda(m) :"))
      if (b>150):
              print("\nBerat tidak munasabah! Masukkan berat kurang daripada 150 !")
              if (t>1.9):
                      print("Tinggi tidak logik ! Masukkan tinggi kurang daripada 1.9 !")
                      if (t<1.2):
                              print("Tinggi tidak logik! Masukkan tinggi kurang daripada 1.2 !")
      elif (b<20):
              print("\nBerat tidak munasabah! Masukkan berat lebih daripada 20 !")    
              if (t>1.9):
                       print("Tinggi tidak logik! Masukkan tinggi kurang daripada 1.9 !")     
              elif(t<1.2):
                       print("Tinggi tidak logik! Masukkan tinggi kurang daripada 1.2 !") 
      elif (t>1.9):
         print("\nTinggi tidak logik! Masukkan tinggi kurang daripada 1.9 !")        
      elif (t<1.2):
          print("\nTinggi tidak logik! Masukkan tinggi kurang daripada 1.2 !")
      else:
                bmi=b/(t*t)
                if bmi <=18.5:
                  print("\nBMI:",round(bmi,2),"\nAnda berada dalam kategori kurang berat badan.")
                  print("Cadangan : Anda disarankan supaya minum susu setiap pagi.")
                elif 18.5 < bmi <=24.9:
                  print("\nBMI:",round(bmi,2),"\nAnda berada dalam kategori berat badan normal.")
                  print("Cadangan : Pastikan anda mempunyai tidur dan minum air yang mencukupi dalam seharian. ")
                elif 24.9 < bmi <=29.9:
                  print("\nBMI:",round(bmi,2),"\nAnda berada dalam kategori berat badan berlebihan.")
                  print("Cadangan : Anda perlu banyakkan aktiviti senaman. ")
                else:
                  print("\nBMI:",round(bmi,2),"\nAnda berada dalam kategori obesiti.")
                  print("Cadangan 1 : Kurangkan pemakanan rapu seperti  pizza, KFC dan Mc'Donald .\nCadangan 2 : Amalkan senaman.")
    except:
       print("\t"*5,"\f!!!!..Input ERROR..!!!!")
BMI()
while True:
 s=str(input("\n\nAnda ingin teruskan aturcara? (y/t) :"))
 if s=="y":
         print(" ")
         print("-"*58)
         BMI()
 elif s=="t":
         print("\n\n","-"*5,"Terima kasih menggunakan kalkulator BMI ini !","-"*5)
         break
 else:
         print("Sila masukkan (y) untuk teruskan aturcara ataupun (t) untuk tamatkan aturcara !")