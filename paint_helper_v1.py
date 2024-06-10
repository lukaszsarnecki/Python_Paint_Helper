import os

count = 0

while True:
    print("Czy chcesz uwzględnić w pomiarze okna i drzwi?")
    print("Tak (Y/y)")
    print("Nie (N/n)")
    print("Wyjście (X/x)\n")
    
    choice = input("Twój wybór: ")
    
    
    # Wyliczanie ilości litów gruntu i farby w przypadku odliczania powieszchni, które zajmują okna oraz drzwi
    
    if choice.lower() == "y":
        
        
        os.system('clear') # Czyszczenie ekranu
        
        # Obliczanie powieszchni okien
        
        print("Poodaj długość oraz szerokość okien, podanej w metrach np: 3.5")
        high_windows = float(input("Podaj wysokość okien: "))
        width_windows = float(input("Podaj szerokość okien: "))
        total_windows = high_windows * width_windows
        
        os.system('clear') # Czyszczenie ekranu
        
        # Obliczanie powieszchni drzwi
        
        print("Podaj długość oraz szerokość drzwi podanych w metrach np 2.5")
        high_doors = float(input("Podaj wyokosć drzwi: "))
        width_doors = float(input("Podaj szerokość drzwi: "))
        total_doors = high_doors * width_doors
        
        os.system('clear') # Czyszczenie ekranu
        
        total = 0
        
        # Obliczanie łączniej powieszchni do malowania, na podstawie podanej ilośći cian, ich wysokości oraz szerokości
        
        walls = int(input("Ile ścian chcesz pomalować: \n"))
        
        high_walls = float(input("Podaj wysokość pomieszczenia: \n"))
        for count in range(walls):
            width_walls = float(input(f"Podaj szerokość {count +1} ściany: "))
            
            total += high_walls * width_walls
        total_area = total - total_windows - total_doors
        
        os.system('clear')
        
        print(f"Łączna powieszchnia do pomalowania wynosi: {total_area} \n")
        
        # Określenie warstw grunty i farby
        
        layers_of_base = int(input("Ilość warstw gruntu: "))
        layers_of_paint = int(input("Ilość warstw farby: "))
        print()
        
        # Określenie wydajności grunty oraz farby
        
        performance_of_base = int(input("Wydajność gruntu na m2: "))
        performance_of_paint = int(input("Wydajność farby na m2: "))
        print()
        
        # Obliczanie potrzebnej ilości gruntu oraz farby
        
        liters_of_base = layers_of_base * total_area / performance_of_base
        liters_of_paint = layers_of_paint * total_area / performance_of_paint
        
        print(f"Potrzebujesz {liters_of_base} litrów gruntu")
        print(f"Potrzebujesz {liters_of_paint} litrów farby")
        
     
        
        
    # Obliczanie łączniej powieszchni do malowania bez podoawania powieszchni która jest zajmowana przez drzwi i okna

    if choice.lower() == "n":
        total_area = 0
        
        walls = int(input("Ile ścian chcesz pomalować: \n"))
        
        high = float(input("Podaj wysokmość pomieszczenia: \n"))
        for count in range(walls):
            width = float(input(f"Podaj szerokość {count +1} ściany: "))
            
            total_area += high * width
            
        os.system('clear')
        
        print(f"Łączna powieszchnia do pomalowania wynosi: {total_area}")
        
        # Określenie ilość warstw gruntu oraz farby
        
        layers_of_base = int(input("Ilość warstw gruntu: "))
        layers_of_paint = int(input("Ilość warstw farby: "))
        
        # Podanie wydajności farby oraz gruntu
        
        performance_of_base = int(input("Wydajność gruntu podana w m2: "))
        performance_of_paint = int(input("Wydajność farby podana w m2: "))
        
        # Obliczanie potrzebnej ilości gruntu oraz farby
        
        liters_of_base = layers_of_base * total_area / performance_of_base
        liters_of_paint = layers_of_paint * total_area / performance_of_paint
        
        print(f"Potrzebujesz {liters_of_base} litrów gruntu")
        print(f"Potrzebujesz {liters_of_paint} litrów farby")
        
    
    if choice.lower() == "x":
        break