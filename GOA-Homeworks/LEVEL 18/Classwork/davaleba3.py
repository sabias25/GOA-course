# საკლასო დავალება 3: 10-დან 30-ის ჩათვლით დაბეჭდეთ ყველა რიცხვი და თან მიუწერეთ ლუწია თუ კენტი, მაგ: 10 - even, 11 - odd, 12 - even და ასე გაგრძელდება 30-ის ჩათვლი

for i in range(10, 31):  
    if i % 2 == 0:  
        print(f"(i) - even")
    else:  
        print(f"(i) - odd")