       #converting binary,octagonal,hexagonal  to decimal
#binary,octagonal,hexagonal
#binary possibal values are 0 and 1
           #binary
#101101 ----->from right starting(1*2 power 0) +(0*2 power 1)+(1*2 power 2)+(1*2power 3)+(0*2 power 4)+(1*2 power 5)+45
#101011 -1*1+1*2+0*4+1*8+0*16+1*32
#1111101-1*1+0*2+1*4+
         #octagonal 
# #octagonal -base-8 possible values-0-7
#same as binary but power 8
#1256-686(6*8power 0)+(8* 8power 1)(+6*8 power 2)
            #hexagonal
#hexagonal -base-16-possible values 0 to 15
#10-a
#11-b
#12-c
#13-d
#14-e
#15-f
#af1-10151(1*1+15*16+10*32) =2801
#111 -
#^binary output- 1*1+1*2+1*4=7
#^octagonal output -1*1+1*8+1*64=73
#^hexagonal output -1*1+1*16+1*256=273
            #converting decimal number into binary,octagonal,hexagonal
num1 = 84
print(bin(num1))
print(oct(num1))
print(hex(num1))
print(int(0o124))
 #operators-----------
#Arthematic operators +,-,*,/,%,//,**.
#Reational operator -<,>,<=,>=,==,!=.
#Assignment operator - =,+=,-=,*=,**=,/=,//=.
#BODMAS
num1  = 2
num1 += 1
num1 += -1
num1 -= 2
num1 *= 5
num1 **= 2
num1 /= 3
num1 //= 3
num1 %= 3
print(num1)