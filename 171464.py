def automat():
#czesc poswiecona produktom/jako tako interfejs automatu
    produkty = {1: ("Coca Cola", 5.00),2: ("Black Energy", 4.00),3: ("KitKat", 2.50),4: ("Snickers", 2.50)}
    print("Dostepne sa nastepujace produkty:")
    for numer, (nazwa, cena) in produkty.items():
        print(f"{numer}. {nazwa} - {cena:.2f} zł")
#wybieranie produktu, mozliwe anulowanie na tym etapie
    wybor = int(input("Proszę podać numer produktu (0 = anulowanie transakcji): "))
    if wybor == 0:
        print("Transakcja anulowana.")
        return
    if wybor not in produkty:
        print("Nie ma takiego produktu. Transakcja anulowana.")
        return
    if wybor in produkty:
        nazwa, cena = produkty[wybor]
        print(f"Wybrano: {nazwa}, do zaplaty: {cena:.2f} zł")
    else:
        print("Nie ma takiego produktu.")
#czesc programu poswiecona transakcji pienieznej, mozliwe anulowanie transakcji i zwrot wplaconych srodkow
    wrzucone_w_sumie = 0
    while wrzucone_w_sumie < produkty[wybor][1]:
        kwota = float(input(f"Prosze wrzucic monety, brakuje: {produkty[wybor][1] - wrzucone_w_sumie:.2f} zł (0 = anulowanie transakcji): "))
        if kwota == 0:
            print(f"Transakcja anulowana. Zwrócono {wrzucone_w_sumie:.2f} zł")
            return
        wrzucone_w_sumie += kwota
#odbieranie produktu z ewentualna reszta
    reszta = wrzucone_w_sumie - produkty[wybor][1]
    if reszta > 0:
        print(f"Prosze odebrac produkt. Wydano reszte: {reszta:.2f}")
    else:
        print("Prosze odebrac produkt.")
automat()