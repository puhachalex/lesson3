a = 0
c = 0
z = str()

with open ("/home/alex/my/projects/lesson3/referat.txt","r", encoding="utf-8") as f:

    for i in f:
        
        b=len(i.split())
        a = a + b
        
        d = len(str(f))
        c = c + d

        y = i.replace(".","!")
        y = y.replace("\n","")
        z = z + "\n" + y



with  open ("/home/alex/my/projects/lesson3/referat2.txt", "w", encoding="utf-8") as new:
    new.write(z)
    new.write("\n\n"f"Количество слов {a}")
    new.write("\n"f"Длина строки {c}")
    




       

            



   

        






    
    

