
class Calc:
    def __init__(self):
                self.worth = ["unit", "Ten", "Hundred", "Thousand", "Million", "Billion"]
                self.number = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
                self.number2 = ["Ten","Eleven","Twelve","Thirteen","Fourteen", "Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
                self.number3 = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
                self.addin = ""


                                                                  #Every number that is of  length 3 and above must be iterated , also check if the number has only zeros to make things easier
    def get_type(self,num):
            self.num = str(num)
            self.len_num = len(str(num))

            if self.len_num == 1:
                return self.convert_to_unit(self.num)

            elif self.len_num == 2:
                 return self.append_tys(self.num)

            elif self.len_num == 3:
                                                        # its a something hundred something
                 return self.append_hudreds(self.num)

            elif self.len_num == 4 or self.len_num == 5 or self.len_num == 6:
                 return self.append_thousands(self.num)

            elif self.len_num == 7 or self.len_num == 8 or self.len_num == 9:
                 return self.append_millions(self.num)

            elif self.len_num == 10 or self.len_num == 11 or self.len_num == 12:
                 return self.append_billions(self.num)

    def convert_to_unit(self, a):
            if a == "1":
                return self.number[0]
            elif a == "2":
                return self.number[1]
            elif a == "3":
                return self.number[2]
            elif a == "4":
                return self.number[3]
            elif a == "5":
                return self.number[4]
            elif a == "6":
                return self.number[5]
            elif a == "7":
                return self.number[6]
            elif a == "8":
                return self.number[7]
            elif a == "9":
                return self.number[8]

    def convert_to_teens(self,a): #fourteen fifteen sixteen eleven

             if a == "10":
                return self.number2[0]
             elif a == "11":
                return self.number2[1]  #wanted to be able to call a convert function,
             elif a == "12":
                return self.number2[2]
             elif a == "13":
                return self.number2[3]
             elif a == "14":
                return self.number2[4]
             elif a == "15":
                return self.number2[5]
             elif a == "16":
                return self.number2[6]
             elif a == "17":
                return self.number2[7]
             elif a == "18":
                return self.number2[8]
             elif a == "19":
                return self.number2[9]

    def convert_to_tys(self, a):          #twentys , thirthys , forties e.t.c trying to append.

             if a == "20" or a == "2":
                return self.number3[0]
             elif a == "30" or a == "3":
                return self.number3[1]
             elif a == "40" or a == "4":
                return self.number3[2]
             elif a == "50" or a == "5":
                return self.number3[3]
             elif a == "60" or a == "6":
                return self.number3[4]
             elif a == "70" or a == "7":
                return self.number3[5]
             elif a == "80" or a == "8":
                return self.number3[6]
             elif a == "90" or a == "9":
                return self.number3[7]

    def append_tys(self,x):   #twenty one , thirty-two , doing some appending get it ?

        if x[0] == "0":
             return self.convert_to_unit(x[1])  # Incase of 09 , 07, 09

        elif x[0] == "1":
             return self.convert_to_teens(x)  # 11,12,13,14

        elif "0" in x and x[0] != 0:
             return self.convert_to_tys(x)  # 20 , 30 ,40
        else:
            return self.convert_to_tys(x[0]) + " - " + self.convert_to_unit(x[1])





    def append_hudreds(self,y):

       if y.count("0") == 1 and y[0] == "0":
             return self.get_type(y[1:])  #011

       elif y.count("0") == 2 and y[0] == "0" and y[1] == "0":
            return self.get_type(y[2])#001

       elif y[0] == "0" and  y[1] != "0" and y[2] == "0":
            return self.get_type(y[1:]) #010

       elif y.count("0") == 2 and y[1] == "0" and y[2] == "0":
            return self.get_type(y[0]) + " " + self.worth[2] #100

       else:
           x = self.get_type(y[1:])
           return self.get_type(y[0]) + " " + self.worth[2] + " and " + x



    def append_thousands(self,z):
        #thouands why not just slice out the first 3 numbers and work on the rest

        if self.len_num == 4:
            if z[1] == "0" and z[2] == "0" and z[3] == "0":
                return self.get_type(z[0]) + " " + self.worth[3]
            else:
                return self.get_type(z[0]) + " " + self.worth[3] + " " + self.get_type(z[1:])

        # ten thousands careful of cases like 30004, 30040
        elif self.len_num == 5:
            if z[2] == "0" and z[3] == "0" and z[4] == "0":
                return self.get_type(z[0:2]) + " " + self.worth[3]
            else:
                return self.get_type(z[0:2]) + " " + self.worth[3] + " " + self.get_type(z[2:])


          #Hundreds of thousand careful of case liek 300040 300000 , 300005
        #why not just slice out the first 3 numbers and work with the rest !

        elif self.len_num == 6:
              if z[3] == "0" and z[4] == "0" and z[5] == "0":
                  return self.get_type(z[0:3]) + " " + self.worth[3]
              else:
                  return self.get_type(z[0:3]) + " " + self.worth[3] + " " + self.get_type(z[3:])


    def append_millions(self,m):
        #millions

       if self.len_num == 7:
           if m.count("0") == 6:
               return self.get_type(m[0]) + " " + self.worth[4]
           else:
               return self.get_type(m[0]) + " " + self.worth[4] + " " + self.get_type(m[1:])

        #tens of millions

       elif self.len_num == 8:
            if m.count("0") == 6 or m.count("0") == 7:
                return self.get_type(m[0:2]) + " " + self.worth[4]
            else:
                return self.get_type(m[0:2]) + " " + self.worth[4] + " " + self.get_type(m[2:])

        #Hundreds of millions

       elif self.len_num == 9:
            if m.count("0") == 6 or m.count("0") == 7 or m.count("0") == 8:
                return self.get_type(m[0:3]) + " " + self.worth[4]
            else:
                return self.get_type(m[0:3]) + " " + self.worth[4] + " " + self.get_type(m[3:])

    def append_billions(self,m):
        #billions

       if self.len_num == 10:
           if m.count("0") == 9:
               return self.get_type(m[0]) + " " + self.worth[5]
           else:
               return self.get_type(m[0]) + " " + self.worth[5] + " " + self.get_type(m[1:])

        #tens of billions

       elif self.len_num == 11:
            if m.count("0") == 9 or m.count("0") == 10:
                return self.get_type(m[0:2]) + " " + self.worth[5]
            else:
                return self.get_type(m[0:2]) + " " + self.worth[5] + " " + self.get_type(m[2:])
        #Hundreds of billions

       elif self.len_num == 12:
            if m.count("0") == 9 or m.count("0") == 10 or m.count("0") == 11:
                return self.get_type(m[0:3]) + " " + self.worth[5]
            else:
                return self.get_type(m[0:3]) + " " + self.worth[5] + " " + self.get_type(m[3:])
























num = int(input("Change this number to its Word Form :"))

sam = Calc()

print(sam.get_type(num))


#for i in range(10000,30000):
    #print(str(i) + "  -  " + sam.get_type(i))

























