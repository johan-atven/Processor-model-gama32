notepad=open("Input Register.txt",'r')  #ambil file basis IR dari notepad
dataA=notepad.readlines()               #membaca banyaknya baris data IR                        
notepad.close()
R0=hex(0)
R1=hex(0)
R2=hex(0)
R3=hex(0)
R4=hex(0)
R5=hex(0)
R6=hex(0)
R7=hex(0)
R8=hex(0)
R9=hex(0)
R10=hex(0)
R11=hex(0)
R12=hex(0)
R13=hex(0)
R14=hex(0)
R15=hex(0)
for Z in range(len(dataA)):
    notepad=open("Input Register.txt",'r')  #ambil file basis IR dari notepad
    data_IR=notepad.readlines()
    IR=data_IR[Z]                       #mendefinisikan setiap iterasi sbg IR
    IRin=IR[0:10]
    PC=hex(Z+68719476736)
    PCin=PC[4:12]
    notepad.close()
#parsing input register
    OP=IR[2:4]                          #parsing data perintah operand
    hasil=IR[4:5]                       #Parsing hasil perintah komputasi
    X_input=IR[5:6]                     #Parsing data input-1
    Y_input=IR[6:7]                     #Parsing data input-2 
#variabel hasil parsing IR
    p=OP                                #melihat perintah operand
    h=hasil                             #melihat hasil perintah komputasi
    x=X_input                           #melihat data input-2
    y=Y_input                           #melihat data input-1
#keterangan nilai awal
    #R0='00', R1='01', R2='02',  R3='03',  R4='04',  R5='05',  R6='06',  R7='07',
    #R8='08', R9='09', R10='10', R11='11', R12='12', R13='13', R14='14', R15='15'
#identifikasi perintah
    if p=='10':
        p='Add'
    if p=='12':
        p='Sub'
    if p=='14':
        p='And'
    if p=='15':
        p='Or'
    if p=='18':
        p='Shl'
    if p=='19':
        p='Shr'
    if p=='20':
        p='AddI'
    if p=='32':
        p='Mov'
#identifikasi tempat hasil komputasi
    if h=='0':
        h='R0'
    elif h=='1':
        h='R1'
    elif h=='2':
        h='R2'
    elif h=='3':
        h='R3'
    elif h=='4':
        h='R4'
    elif h=='5':
        h='R5'
    elif h=='6':
        h='R6'
    elif h=='7':
        h='R7'
    elif h=='8':
        h='R8'
    elif h=='9':
        h='R9'
    elif h=='a':
        h='R10'
    elif h=='b':
        h='R1'
    elif h=='c':
        h='R12'
    elif h=='d':
        h='R13'
    elif h=='e':
        h='R14'
    elif h=='f':
        h='R15'
#Identifikasi input-1
    if x=='0':
        x='R0'
    elif x=='1':
        x='R1'
    elif x=='2':
        x='R2'
    elif x=='3':
        x='R3'
    elif x=='4':
        x='R4'
    elif x=='5':
        x='R5'
    elif x=='6':
        x='R6'
    elif x=='7':
        x='R7'
    elif x=='8':
        x='R8'
    elif x=='9':
        x='R9'
    elif x=='a':
        x='R10'
    elif x=='b':
        x='R11'
    elif x=='c':
        x='R12'
    elif x=='d':
        x='R13'
    elif x=='e':
        x='R14'
    elif x=='f':
        x='R15'
#Identifikasi input-2
    if y=='0':
        y='R0'
    elif y=='1':
        y='R1'
    elif y=='2':
        y='R2'
    elif y=='3':
        y='R3'
    elif y=='4':
        y='R4'
    elif y=='5':
        y='R5'
    elif y=='6':
        y='R6'
    elif y=='7':
        y='R7'
    elif y=='8':
        y='R8'
    elif y=='9':
        y='R9'
    elif y=='a':
        y='R10'
    elif y=='b':
        y='R11'
    elif y=='c':
        y='R12'
    elif y=='d':
        y='R13'
    elif y=='e':
        y='R14'
    elif y=='f':
        y='R15'
#menampilkan instruksi
    if OP=='20':
        s=IR[6:10]                      #input immidiate
        s=int(s,16)
        s=hex(s)
        s=str(s)
        v=s
        print( )
        print('PC =0x'+PCin,'IR ='+IRin,p,h,x,'#'+'0x'+'{0:0>4x}'.format(int(s,16)))
    elif OP=='32':
        print( )
        print('PC =0x'+PCin,'IR ='+IRin,p,h,x)
    else:
        print( )
        print('PC =0x'+PCin,'IR=',IRin,p,h,x,y)
    if X_input=='0':
        X_input=R0
    elif X_input=='1':
        X_input=R1
    elif X_input=='2':
        X_input=R2
    elif X_input=='3':
        X_input=R3
    elif X_input=='4':
        X_input=R4
    elif X_input=='5':
        X_input=R5
    elif X_input=='6':
        X_input=R6
    elif X_input=='7':
        X_input=R7
    elif X_input=='8':
        X_input=R8
    elif X_input=='9':
        X_input=R9
    elif X_input=='a':
        X_input=R10
    elif X_input=='b':
        X_input=R11
    elif X_input=='c':
        X_input=R12
    elif X_input=='d':
        X_input=R13
    elif X_input=='e':
        X_input=R14
    elif X_input=='f':
        X_input=R15

    if Y_input=='0':
        Y_input=R0
    elif Y_input=='1':
        Y_input=R1
    elif Y_input=='2':
        Y_input=R2
    elif Y_input=='3':
        Y_input=R3
    elif Y_input=='4':
        Y_input=R4
    elif Y_input=='5':
        Y_input=R5
    elif Y_input=='6':
        Y_input=R6
    elif Y_input=='7':
        Y_input=R7
    elif Y_input=='8':
        Y_input=R8
    elif Y_input=='9':
        Y_input=R9
    elif Y_input=='a':
        Y_input=R10
    elif Y_input=='b':
        Y_input=R11
    elif Y_input=='c':
        Y_input=R12
    elif Y_input=='d':
        Y_input=R13
    elif Y_input=='e':
        Y_input=R14
    elif Y_input=='f':
        Y_input=R15
#perintah masukan (AddI)
    if OP=='20':       
        if hasil=='0':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R0=output
        if hasil=='1':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R1=output
        if hasil=='2':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R2=output
        if hasil=='3':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R3=output
        if hasil=='4':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R4=output
        if hasil=='5':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R5=output
        if hasil=='6':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R6=output
        if hasil=='7':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R7=output
        if hasil=='8':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R8=output
        if hasil=='9':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R9=output
        if hasil=='a':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R10=output
        if hasil=='b':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R11=output
        if hasil=='c':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R12=output
        if hasil=='d':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R13=output
        if hasil=='e':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R14=output
        if hasil=='f':
            X_input=int(X_input,16)
            v=int(v,16)
            output = X_input + v
            output = hex(output)
            R15=output    
        R0=int(R0,16)+68719476736
        R0=hex(R0)
        R0=R0[4:12]
        R1=int(R1,16)+68719476736
        R1=hex(R1)
        R1=R1[4:12]
        R2=int(R2,16)+68719476736
        R2=hex(R2)
        R2=R2[4:12]
        R3=int(R3,16)+68719476736
        R3=hex(R3)
        R3=R3[4:12]
        R4=int(R4,16)+68719476736
        R4=hex(R4)
        R4=R4[4:12]
        R5=int(R5,16)+68719476736
        R5=hex(R5)
        R5=R5[4:12]
        R6=int(R6,16)+68719476736
        R6=hex(R6)
        R6=R6[4:12]
        R7=int(R7,16)+68719476736
        R7=hex(R7)
        R7=R7[4:12]
        R8=int(R8,16)+68719476736
        R8=hex(R8)
        R8=R8[4:12]
        R9=int(R9,16)+68719476736
        R9=hex(R9)
        R9=R9[4:12]
        R10=int(R10,16)+68719476736
        R10=hex(R10)
        R10=R10[4:12]
        R11=int(R11,16)+68719476736
        R11=hex(R11)
        R11=R11[4:12]
        R12=int(R12,16)+68719476736
        R12=hex(R12)
        R12=R12[4:12]
        R13=int(R13,16)+68719476736
        R13=hex(R13)
        R13=R13[4:12]
        R14=int(R14,16)+68719476736
        R14=hex(R14)
        R14=R14[4:12]
        R15=int(R15,16)+68719476736
        R15=hex(R15)
        R15=R15[4:12]
#perintah penjumlahan (Add)
    if OP=='10':
        if hasil=='0':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input + Y_input
            output = hex(output)
            R0=output
        if hasil=='1':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input + Y_input
            output = hex(output)
            R1=output
        if hasil=='2':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input + Y_input
            output = hex(output)
            R2=output
        if hasil=='3':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input + Y_input
            output = hex(output)
            R3=output
        if hasil=='4':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input + Y_input
            output = hex(output)
            R4=output
        if hasil=='5':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input + Y_input
            output = hex(output)
            R5=output
        if hasil=='6':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input + Y_input
            output = hex(output)
            R6=output
        if hasil=='7':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input + Y_input
            output = hex(output)
            R7=output
        if hasil=='8':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input + Y_input
            output = hex(output)
            R8=output
        if hasil=='9':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input + Y_input
            output = hex(output)
            R9=output
        if hasil=='a':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input + Y_input
            output = hex(output)
            R10=output
        if hasil=='b':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input + Y_input
            output = hex(output)
            R11=output
        if hasil=='c':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input + Y_input
            output = hex(output)
            R12=output
        if hasil=='d':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input + Y_input
            output = hex(output)
            R13=output
        if hasil=='e':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input + Y_input
            output = hex(output)
            R14=output
        if hasil=='f':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input + Y_input
            output = hex(output)
            R15=output
        R0=int(R0,16)+68719476736
        R0=hex(R0)
        R0=R0[4:12]
        R1=int(R1,16)+68719476736
        R1=hex(R1)
        R1=R1[4:12]
        R2=int(R2,16)+68719476736
        R2=hex(R2)
        R2=R2[4:12]
        R3=int(R3,16)+68719476736
        R3=hex(R3)
        R3=R3[4:12]
        R4=int(R4,16)+68719476736
        R4=hex(R4)
        R4=R4[4:12]
        R5=int(R5,16)+68719476736
        R5=hex(R5)
        R5=R5[4:12]
        R6=int(R6,16)+68719476736
        R6=hex(R6)
        R6=R6[4:12]
        R7=int(R7,16)+68719476736
        R7=hex(R7)
        R7=R7[4:12]
        R8=int(R8,16)+68719476736
        R8=hex(R8)
        R8=R8[4:12]
        R9=int(R9,16)+68719476736
        R9=hex(R9)
        R9=R9[4:12]
        R10=int(R10,16)+68719476736
        R10=hex(R10)
        R10=R10[4:12]
        R11=int(R11,16)+68719476736
        R11=hex(R11)
        R11=R11[4:12]
        R12=int(R12,16)+68719476736
        R12=hex(R12)
        R12=R12[4:12]
        R13=int(R13,16)+68719476736
        R13=hex(R13)
        R13=R13[4:12]
        R14=int(R14,16)+68719476736
        R14=hex(R14)
        R14=R14[4:12]
        R15=int(R15,16)+68719476736
        R15=hex(R15)
        R15=R15[4:12]
#perintah pengurangan (Sub)
    if OP=='12':
        if hasil=='0':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input - Y_input
            output = hex(output)
            R0=output
        if hasil=='1':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input - Y_input
            output = hex(output)
            R1=output
        if hasil=='2':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input - Y_input
            output = hex(output)
            R2=output
        if hasil=='3':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input - Y_input
            output = hex(output)
            R3=output
        if hasil=='4':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input - Y_input
            output = hex(output)
            R4=output
        if hasil=='5':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input - Y_input
            output = hex(output)
            R5=output
        if hasil=='6':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input - Y_input
            output = hex(output)
            R6=output
        if hasil=='7':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input - Y_input
            output = hex(output)
            R7=output
        if hasil=='8':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input - Y_input
            output = hex(output)
            R8=output
        if hasil=='9':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input - Y_input
            output = hex(output)
            R9=output
        if hasil=='a':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input - Y_input
            output = hex(output)
            R10=output
        if hasil=='b':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input - Y_input
            output = hex(output)
            R11=output
        if hasil=='c':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input - Y_input
            output = hex(output)
            R12=output
        if hasil=='d':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input - Y_input
            output = hex(output)
            R13=output
        if hasil=='e':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input - Y_input
            output = hex(output)
            R14=output
        if hasil=='f':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input - Y_input
            output = hex(output)
            R15=output
        R0=int(R0,16)+68719476736
        R0=hex(R0)
        R0=R0[4:12]
        R1=int(R1,16)+68719476736
        R1=hex(R1)
        R1=R1[4:12]
        R2=int(R2,16)+68719476736
        R2=hex(R2)
        R2=R2[4:12]
        R3=int(R3,16)+68719476736
        R3=hex(R3)
        R3=R3[4:12]
        R4=int(R4,16)+68719476736
        R4=hex(R4)
        R4=R4[4:12]
        R5=int(R5,16)+68719476736
        R5=hex(R5)
        R5=R5[4:12]
        R6=int(R6,16)+68719476736
        R6=hex(R6)
        R6=R6[4:12]
        R7=int(R7,16)+68719476736
        R7=hex(R7)
        R7=R7[4:12]
        R8=int(R8,16)+68719476736
        R8=hex(R8)
        R8=R8[4:12]
        R9=int(R9,16)+68719476736
        R9=hex(R9)
        R9=R9[4:12]
        R10=int(R10,16)+68719476736
        R10=hex(R10)
        R10=R10[4:12]
        R11=int(R11,16)+68719476736
        R11=hex(R11)
        R11=R11[4:12]
        R12=int(R12,16)+68719476736
        R12=hex(R12)
        R12=R12[4:12]
        R13=int(R13,16)+68719476736
        R13=hex(R13)
        R13=R13[4:12]
        R14=int(R14,16)+68719476736
        R14=hex(R14)
        R14=R14[4:12]
        R15=int(R15,16)+68719476736
        R15=hex(R15)
        R15=R15[4:12]
#perintah logika benar jika semua benar(And)
    if OP=='14':
        if hasil=='0':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input & Y_input
            output = hex(output)
            R0=output
        if hasil=='1':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input & Y_input
            output = hex(output)
            R1=output
        if hasil=='2':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input & Y_input
            output = hex(output)
            R2=output
        if hasil=='3':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input & Y_input
            output = hex(output)
            R3=output
        if hasil=='4':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input & Y_input
            output = hex(output)
            R4=output
        if hasil=='5':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input & Y_input
            output = hex(output)
            R5=output
        if hasil=='6':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input & Y_input
            output = hex(output)
            R6=output
        if hasil=='7':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input & Y_input
            output = hex(output)
            R7=output
        if hasil=='8':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input & Y_input
            output = hex(output)
            R8=output
        if hasil=='9':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input & Y_input
            output = hex(output)
            R9=output
        if hasil=='a':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input & Y_input
            output = hex(output)
            R10=output
        if hasil=='b':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input & Y_input
            output = hex(output)
            R11=output
        if hasil=='c':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input & Y_input
            output = hex(output)
            R12=output
        if hasil=='d':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input & Y_input
            output = hex(output)
            R13=output
        if hasil=='e':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input & Y_input
            output = hex(output)
            R14=output
        if hasil=='f':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input & Y_input
            output = hex(output)
            R15=output
        R0=int(R0,16)+68719476736
        R0=hex(R0)
        R0=R0[4:12]
        R1=int(R1,16)+68719476736
        R1=hex(R1)
        R1=R1[4:12]
        R2=int(R2,16)+68719476736
        R2=hex(R2)
        R2=R2[4:12]
        R3=int(R3,16)+68719476736
        R3=hex(R3)
        R3=R3[4:12]
        R4=int(R4,16)+68719476736
        R4=hex(R4)
        R4=R4[4:12]
        R5=int(R5,16)+68719476736
        R5=hex(R5)
        R5=R5[4:12]
        R6=int(R6,16)+68719476736
        R6=hex(R6)
        R6=R6[4:12]
        R7=int(R7,16)+68719476736
        R7=hex(R7)
        R7=R7[4:12]
        R8=int(R8,16)+68719476736
        R8=hex(R8)
        R8=R8[4:12]
        R9=int(R9,16)+68719476736
        R9=hex(R9)
        R9=R9[4:12]
        R10=int(R10,16)+68719476736
        R10=hex(R10)
        R10=R10[4:12]
        R11=int(R11,16)+68719476736
        R11=hex(R11)
        R11=R11[4:12]
        R12=int(R12,16)+68719476736
        R12=hex(R12)
        R12=R12[4:12]
        R13=int(R13,16)+68719476736
        R13=hex(R13)
        R13=R13[4:12]
        R14=int(R14,16)+68719476736
        R14=hex(R14)
        R14=R14[4:12]
        R15=int(R15,16)+68719476736
        R15=hex(R15)
        R15=R15[4:12]
#perintah logika benar jika salah satu benar(Or)
    if OP=='15':
        if hasil=='0':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input | Y_input
            output = hex(output)
            R0=output
        if hasil=='1':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input | Y_input
            output = hex(output)
            R1=output
        if hasil=='2':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input | Y_input
            output = hex(output)
            R2=output
        if hasil=='3':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input | Y_input
            output = hex(output)
            R3=output
        if hasil=='4':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input | Y_input
            output = hex(output)
            R4=output
        if hasil=='5':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input | Y_input
            output = hex(output)
            R5=output
        if hasil=='6':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input | Y_input
            output = hex(output)
            R6=output
        if hasil=='7':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input | Y_input
            output = hex(output)
            R7=output
        if hasil=='8':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input | Y_input
            output = hex(output)
            R8=output
        if hasil=='9':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input | Y_input
            output = hex(output)
            R9=output
        if hasil=='a':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input | Y_input
            output = hex(output)
            R10=output
        if hasil=='b':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input | Y_input
            output = hex(output)
            R11=output
        if hasil=='c':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input | Y_input
            output = hex(output)
            R12=output
        if hasil=='d':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input | Y_input
            output = hex(output)
            R13=output
        if hasil=='e':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input | Y_input
            output = hex(output)
            R14=output
        if hasil=='f':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input | Y_input
            output = hex(output)
            R15=output
        R0=int(R0,16)+68719476736
        R0=hex(R0)
        R0=R0[4:12]
        R1=int(R1,16)+68719476736
        R1=hex(R1)
        R1=R1[4:12]
        R2=int(R2,16)+68719476736
        R2=hex(R2)
        R2=R2[4:12]
        R3=int(R3,16)+68719476736
        R3=hex(R3)
        R3=R3[4:12]
        R4=int(R4,16)+68719476736
        R4=hex(R4)
        R4=R4[4:12]
        R5=int(R5,16)+68719476736
        R5=hex(R5)
        R5=R5[4:12]
        R6=int(R6,16)+68719476736
        R6=hex(R6)
        R6=R6[4:12]
        R7=int(R7,16)+68719476736
        R7=hex(R7)
        R7=R7[4:12]
        R8=int(R8,16)+68719476736
        R8=hex(R8)
        R8=R8[4:12]
        R9=int(R9,16)+68719476736
        R9=hex(R9)
        R9=R9[4:12]
        R10=int(R10,16)+68719476736
        R10=hex(R10)
        R10=R10[4:12]
        R11=int(R11,16)+68719476736
        R11=hex(R11)
        R11=R11[4:12]
        R12=int(R12,16)+68719476736
        R12=hex(R12)
        R12=R12[4:12]
        R13=int(R13,16)+68719476736
        R13=hex(R13)
        R13=R13[4:12]
        R14=int(R14,16)+68719476736
        R14=hex(R14)
        R14=R14[4:12]
        R15=int(R15,16)+68719476736
        R15=hex(R15)
        R15=R15[4:12]
#perintah geser ke kiri(Shl)
    if OP=='18':
        if hasil=='0':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input << Y_input
            output = hex(output)
            R0=output
        if hasil=='1':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input << Y_input
            output = hex(output)
            R1=output
        if hasil=='2':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input << Y_input
            output = hex(output)
            R2=output
        if hasil=='3':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input << Y_input
            output = hex(output)
            R3=output
        if hasil=='4':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input << Y_input
            output = hex(output)
            R4=output
        if hasil=='5':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input << Y_input
            output = hex(output)
            R5=output
        if hasil=='6':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input << Y_input
            output = hex(output)
            R6=output
        if hasil=='7':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input << Y_input
            output = hex(output)
            R7=output
        if hasil=='8':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input << Y_input
            output = hex(output)
            R8=output
        if hasil=='9':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input << Y_input
            output = hex(output)
            R9=output
        if hasil=='a':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input << Y_input
            output = hex(output)
            R10=output
        if hasil=='b':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input << Y_input
            output = hex(output)
            R11=output
        if hasil=='c':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input << Y_input
            output = hex(output)
            R12=output
        if hasil=='d':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input << Y_input
            output = hex(output)
            R13=output
        if hasil=='e':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input << Y_input
            output = hex(output)
            R14=output
        if hasil=='f':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input << Y_input
            output = hex(output)
            R15=output
        R0=int(R0,16)+68719476736
        R0=hex(R0)
        R0=R0[4:12]
        R1=int(R1,16)+68719476736
        R1=hex(R1)
        R1=R1[4:12]
        R2=int(R2,16)+68719476736
        R2=hex(R2)
        R2=R2[4:12]
        R3=int(R3,16)+68719476736
        R3=hex(R3)
        R3=R3[4:12]
        R4=int(R4,16)+68719476736
        R4=hex(R4)
        R4=R4[4:12]
        R5=int(R5,16)+68719476736
        R5=hex(R5)
        R5=R5[4:12]
        R6=int(R6,16)+68719476736
        R6=hex(R6)
        R6=R6[4:12]
        R7=int(R7,16)+68719476736
        R7=hex(R7)
        R7=R7[4:12]
        R8=int(R8,16)+68719476736
        R8=hex(R8)
        R8=R8[4:12]
        R9=int(R9,16)+68719476736
        R9=hex(R9)
        R9=R9[4:12]
        R10=int(R10,16)+68719476736
        R10=hex(R10)
        R10=R10[4:12]
        R11=int(R11,16)+68719476736
        R11=hex(R11)
        R11=R11[4:12]
        R12=int(R12,16)+68719476736
        R12=hex(R12)
        R12=R12[4:12]
        R13=int(R13,16)+68719476736
        R13=hex(R13)
        R13=R13[4:12]
        R14=int(R14,16)+68719476736
        R14=hex(R14)
        R14=R14[4:12]
        R15=int(R15,16)+68719476736
        R15=hex(R15)
        R15=R15[4:12]
#perintah geser ke kanan(Shr)
    if OP=='19':
        if hasil=='0':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input >> Y_input
            output = hex(output)
            R0=output
        if hasil=='1':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input >> Y_input
            output = hex(output)
            R1=output
        if hasil=='2':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input >> Y_input
            output = hex(output)
            R2=output
        if hasil=='3':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input >> Y_input
            output = hex(output)
            R3=output
        if hasil=='4':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input >> Y_input
            output = hex(output)
            R4=output
        if hasil=='5':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input >> Y_input
            output = hex(output)
            R5=output
        if hasil=='6':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input >> Y_input
            output = hex(output)
            R6=output
        if hasil=='7':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input >> Y_input
            output = hex(output)
            R7=output
        if hasil=='8':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input >> Y_input
            output = hex(output)
            R8=output
        if hasil=='9':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input >> Y_input
            output = hex(output)
            R9=output
        if hasil=='a':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input >> Y_input
            output = hex(output)
            R10=output
        if hasil=='b':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input >> Y_input
            output = hex(output)
            R11=output
        if hasil=='c':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input >> Y_input
            output = hex(output)
            R12=output
        if hasil=='d':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output = X_input >> Y_input
            output = hex(output)
            R13=output
        if hasil=='e':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input >> Y_input
            output = hex(output)
            R14=output
        if hasil=='f':
            X_input=int(X_input,16)
            Y_input=int(Y_input,16)
            output =  X_input >> Y_input
            output = hex(output)
            R15=output
        R0=int(R0,16)+68719476736
        R0=hex(R0)
        R0=R0[4:12]
        R1=int(R1,16)+68719476736
        R1=hex(R1)
        R1=R1[4:12]
        R2=int(R2,16)+68719476736
        R2=hex(R2)
        R2=R2[4:12]
        R3=int(R3,16)+68719476736
        R3=hex(R3)
        R3=R3[4:12]
        R4=int(R4,16)+68719476736
        R4=hex(R4)
        R4=R4[4:12]
        R5=int(R5,16)+68719476736
        R5=hex(R5)
        R5=R5[4:12]
        R6=int(R6,16)+68719476736
        R6=hex(R6)
        R6=R6[4:12]
        R7=int(R7,16)+68719476736
        R7=hex(R7)
        R7=R7[4:12]
        R8=int(R8,16)+68719476736
        R8=hex(R8)
        R8=R8[4:12]
        R9=int(R9,16)+68719476736
        R9=hex(R9)
        R9=R9[4:12]
        R10=int(R10,16)+68719476736
        R10=hex(R10)
        R10=R10[4:12]
        R11=int(R11,16)+68719476736
        R11=hex(R11)
        R11=R11[4:12]
        R12=int(R12,16)+68719476736
        R12=hex(R12)
        R12=R12[4:12]
        R13=int(R13,16)+68719476736
        R13=hex(R13)
        R13=R13[4:12]
        R14=int(R14,16)+68719476736
        R14=hex(R14)
        R14=R14[4:12]
        R15=int(R15,16)+68719476736
        R15=hex(R15)
        R15=R15[4:12]
#perintah Pindahkan (MOV)
    if OP=='32':       
        if hasil=='0':
            X_input=int(X_input,16)
            output = X_input
            output = hex(output)
            R0=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        if hasil=='1':
            X_input=int(X_input,16)
            output = X_input
            output = hex(output)
            R1=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        if hasil=='2':
            X_input=int(X_input,16)
            output = X_input
            output = hex(output)
            R2=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        if hasil=='3':
            X_input=int(X_input,16)
            output = X_input
            output = hex(output)
            R3=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        if hasil=='4':
            X_input=int(X_input,16)
            output = X_input
            output = hex(output)
            R4=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        if hasil=='5':
            X_input=int(X_input,16)
            output = X_input
            output = hex(output)
            R5=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        if hasil=='6':
            X_input=int(X_input,16)
            output = X_input
            output = hex(output)
            R6=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        if hasil=='7':
            X_input=int(X_input,16)
            output = X_input
            output = hex(output)
            R7=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        if hasil=='8':
            X_input=int(X_input,16)
            output = X_input
            output = hex(output)
            R8=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        if hasil=='9':
            X_input=int(X_input,16)
            output = X_input
            output = hex(output)
            R9=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        if hasil=='a':
            m=IR[5:6]
            X_input=int(X_input,16)
            output = X_input
            output = hex(output)
            R10=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        if hasil=='b':
            X_input=int(X_input,16)
            output = X_input
            output = hex(output)
            R11=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        if hasil=='c':
            X_input=int(X_input,16)
            output = X_input
            output = hex(output)
            R12=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        if hasil=='d':
            X_input=int(X_input,16)
            output = X_input
            output = hex(output)
            R13=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        if hasil=='e':
            X_input=int(X_input,16)
            output = X_input + v
            output = hex(output)
            R14=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        if hasil=='f':
            X_input=int(X_input,16)
            output = X_input
            output = hex(output)
            R15=output
            if m=='0':
                R0=hex(0)
            elif m=='1':
                R1=hex(0)
            elif m=='2':
                R2=hex(0)
            elif m=='3':
                R3=hex(0)
            elif m=='4':
                R4=hex(0)
            elif m=='5':
                R5=hex(0)
            elif m=='6':
                R6=hex(0)
            elif m=='7':
                R7=hex(0)
            elif m=='8':
                R8=hex(0)
            elif m=='9':
                R9=hex(0)
            elif m=='a':
                R10=hex(0)
            elif m=='b':
                R11=hex(0)
            elif m=='c':
                R12=hex(0)
            elif m=='d':
                R13=hex(0)
            elif m=='e':
                R14=hex(0)
            elif m=='f':
                R15=hex(0)
        R0=int(R0,16)+68719476736
        R0=hex(R0)
        R0=R0[4:12]
        R1=int(R1,16)+68719476736
        R1=hex(R1)
        R1=R1[4:12]
        R2=int(R2,16)+68719476736
        R2=hex(R2)
        R2=R2[4:12]
        R3=int(R3,16)+68719476736
        R3=hex(R3)
        R3=R3[4:12]
        R4=int(R4,16)+68719476736
        R4=hex(R4)
        R4=R4[4:12]
        R5=int(R5,16)+68719476736
        R5=hex(R5)
        R5=R5[4:12]
        R6=int(R6,16)+68719476736
        R6=hex(R6)
        R6=R6[4:12]
        R7=int(R7,16)+68719476736
        R7=hex(R7)
        R7=R7[4:12]
        R8=int(R8,16)+68719476736
        R8=hex(R8)
        R8=R8[4:12]
        R9=int(R9,16)+68719476736
        R9=hex(R9)
        R9=R9[4:12]
        R10=int(R10,16)+68719476736
        R10=hex(R10)
        R10=R10[4:12]
        R11=int(R11,16)+68719476736
        R11=hex(R11)
        R11=R11[4:12]
        R12=int(R12,16)+68719476736
        R12=hex(R12)
        R12=R12[4:12]
        R13=int(R13,16)+68719476736
        R13=hex(R13)
        R13=R13[4:12]
        R14=int(R14,16)+68719476736
        R14=hex(R14)
        R14=R14[4:12]
        R15=int(R15,16)+68719476736
        R15=hex(R15)
        R15=R15[4:12]
    print('R0 =0x'+R0,'R1 =0x'+R1,'R2 =0x'+R2,'R3 =0x'+R3)
    print('R4 =0x'+R4,'R5 =0x'+R5,'R6 =0x'+R6,'R7 =0x'+R7)
    print('R8 =0x'+R8,'R9 =0x'+R9,'R10=0x'+R10,'R11=0x'+R11)
    print('R12=0x'+R12,'R13=0x'+R13,'R14=0x'+R14,'R15=0x'+R15)
