def shipping_label(*args, **kwargs) :
    for arg in args :
        print(arg, end=" ")
    print()
    
    print(f"{kwargs.get("street")}, {kwargs.get("apt")}")
    print(f"{kwargs.get("city")}, {kwargs.get("state")}, {kwargs.get("zip")}")
    
shipping_label(
                  "Dr.","Spongbob","Suarepants",
                   street="123 St",
                   apt="#100",
                   city="Detroit",
                   state="MI",
                   zip="48201"
                 )