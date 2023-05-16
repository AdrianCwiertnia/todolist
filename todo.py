def dodaj_zadanie(lista_zadan):
    zadanie = input("Podaj nazwę zadania: ")
    lista_zadan.append(zadanie)
    print("Dodano zadanie:", zadanie)

def wyswietl_liste_zadan(lista_zadan):
    print("Lista zadań:")
    for i, zadanie in enumerate(lista_zadan):
        print(i+1, zadanie)

def usun_zadanie(lista_zadan):
    do_usuniecia = int(input("Podaj numer zadania do usunięcia: "))
    if do_usuniecia > 0 and do_usuniecia <= len(lista_zadan):
        zadanie_usuniete = lista_zadan.pop(do_usuniecia-1)
        print("Usunięto zadanie:", zadanie_usuniete)
    else:
        print("Nie ma takiego numeru zadania.")

def zapisz_do_pliku(lista_zadan):
    with open("git/lista_zadan1.txt", "w") as plik:
        for zadanie in lista_zadan:
            plik.write(zadanie + "\n")
    print("Zapisano listę zadań do pliku.")

lista_zadan = []

while True:
    print("")
    print("Wybierz opcję:")
    print("1. Dodaj zadanie")
    print("2. Wyświetl listę zadań")
    print("3. Usuń zadanie")
    print("4. Zapisz listę zadań do pliku")
    print("5. Zakończ program")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        dodaj_zadanie(lista_zadan)
    elif wybor == "2":
        wyswietl_liste_zadan(lista_zadan)
    elif wybor == "3":
        usun_zadanie(lista_zadan)
    elif wybor == "4":
        zapisz_do_pliku(lista_zadan)
    elif wybor == "5":
        print("Koniec programu.")
        break
    else:
        print("Nieznana opcja.")
