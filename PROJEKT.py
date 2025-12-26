import pandas as pd
import matplotlib.pyplot as plt

def odczyt_danych(game):
    return pd.read_csv("game.csv")

def odczyt_curry():
    return pd.read_csv("currystats.csv")

def odczyt_lebron():
    return pd.read_csv("lebronstats.csv")

def przetwor_lebron(lebron):
    lebron['Date'] = pd.to_datetime(lebron['Date'])
    return lebron

#fg3_pct_home fg3_pct_away
def przetwor_danych(dane):
    dane['game_date']=pd.to_datetime(dane['game_date']) #Przetwor aby wyswietlano date w formacie dd.mm.rrrr

    dane['punkty']=dane['pts_home']+dane['pts_away'] # Suma pkt w meczu
    dane = dane[(dane['game_date'].dt.year >= 1980) & (dane['game_date'].dt.year <= 2023)] # Zwezenie danych, aby
    # zawieraly sie od 1980r., gdzie zaczela sie era 'wspolczesnej' koszykowki
    return dane

def statystyki(dane):
    dane = pd.DataFrame(dane)
    dane['rzutyza3']=(dane['fg3a_home'] + dane['fg3a_away']) # Suma rzutow w meczu za 3
    dane['rzutywolne']=(dane['ft_pct_home'] + dane['ft_pct_away']) #Skutecznosc rzutow wolnych w meczu
    return dane

def wykres1(dane):
    dane['year']=dane['game_date'].dt.year
    punktywrok=dane.groupby('year')['punkty'].mean()
    plt.figure(figsize=(10,5))
    punktywrok.plot(kind='bar')
    plt.xlabel("Rok")
    plt.ylabel("Średnia ilość punktów na mecz")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    plt.show()

def wykres2(dane):
    dane['year'] = dane['game_date'].dt.year
    rzutyza3=round(dane.groupby('year')['rzutyza3'].mean(), 2)
    plt.figure(figsize=(10, 5))
    rzutyza3.plot(kind='bar')
    plt.xlabel("Rok")
    plt.ylabel("Średnia ilość rzutów za 3 w meczu")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    plt.show()

def wykres3(dane):
    dane['year'] = dane['game_date'].dt.year
    rzutywolne=round(dane.groupby('year')['rzutywolne'].mean()/2*100, 2)
    plt.figure(figsize=(10, 5))
    rzutywolne.plot(kind='bar')
    plt.xlabel("Rok")
    plt.ylabel("Skuteczność w rzutach wolnych [%]")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    plt.show()

def wykres4(dane):
    dane['year'] = dane['game_date'].dt.year
    pktdom=(dane.groupby('year')['pts_home']).mean()
    pktwyj=(dane.groupby('year')['pts_away']).mean()
    lacznie=pd.DataFrame({'Punkty domowe': pktdom, 'Punkty wyjazdowe': pktwyj})
    lacznie.plot(kind='bar', figsize=(10,5))
    plt.tight_layout()
    plt.show()

def wykres5(curry):
    pktcurry=(curry.groupby('Season_year')['PTS']).mean()
    pktcurry.plot(kind='bar', figsize=(10,5))
    plt.xlabel("Sezon")
    plt.ylabel("Średnia punktów na mecz")
    plt.title("Średnia punktów Stephena Curry'ego w każdym sezonie")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def wykres6(curry):
    asystycurry=(curry.groupby('Season_year')['AST']).mean()
    asystycurry.plot(kind='bar', figsize=(10,5))
    plt.xlabel("Sezon")
    plt.ylabel("Średnia asyst na mecz")
    plt.title("Średnia asyst Stephena Curry'ego w każdym sezonie")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def wykres7(lebron):
    lebron['year'] = lebron['Date'].dt.year
    pktlebron=(lebron.groupby('year')['PTS']).mean()
    pktlebron.plot(kind='bar', figsize=(10,5))
    plt.xlabel("Sezon")
    plt.ylabel("Średnia punktów na mecz")
    plt.title("Średnia punktów Lebrona Jamesa w sezonach 2003-2023")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def wykres8(lebron):
    lebron['year'] = lebron['Date'].dt.year
    astlebron=(lebron.groupby('year')['AST']).mean()
    astlebron.plot(kind='bar', figsize=(10,5))
    plt.xlabel("Sezon")
    plt.ylabel("Średnia asyst na mecz")
    plt.title("Średnia asyst Lebrona Jamesa w sezonach 2003-2023")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def pokazdane(dane, curry, lebron):
    while True:
        print("Wybierz statystykę do wyświetlenia: ")
        print("1: Średnia ilość punktów na mecz w latach 1980-2023")
        print("2: Średnia ilość rzutów za 3 w meczach w latach 1980-2023")
        print("3: Średnia skuteczność rzutów wolnych w meczach w latach 1980-2023")
        print("4: Średnia ilość punktów gospodarzy vs. gości")
        print("5: Punkty na mecz Stephena Curry'ego w latach 2009-2023")
        print("6: Asysty na mecz Stephena Curry'ego w latach 2009-2023")
        print("7: Punkty na mecz Lebrona Jamesa w latach 2003-2023")
        print("8: Asysty na mecz Lebrona Jamesa w latach 2003-2023")
        print("0: Koniec programu")
        wybor = int(input("Wprowadz numer opcji: "))
        if wybor == 0:
            print("Koniec programu")
            break
        elif wybor in [1, 2, 3, 4]:
            switch = {
                1: wykres1,
                2: wykres2,
                3: wykres3,
                4: wykres4
            }
            funkcja=switch.get(wybor)
            if funkcja:
                funkcja(dane)
        elif wybor == 5:
            wykres5(curry)
        elif wybor == 6:
            wykres6(curry)
        elif wybor == 7:
            wykres7(lebron)
        elif wybor == 8:
            wykres8(lebron)
        else:
            print("Niepoprawna opcja")

def main():
    dane=odczyt_danych("game.csv")
    lebron=odczyt_lebron()
    lebron=przetwor_lebron(lebron)
    curry=odczyt_curry()
    dane=przetwor_danych(dane)
    dane = statystyki(dane)
    pokazdane(dane, curry, lebron)

if __name__ == "__main__":
    main()
