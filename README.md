# Zajęcia laboratoryjne z Przetwarzania Obrazów
Krótkie opisy przeprowadzonych zajęć laboratoryjnych z Przetwarzania Obrazów. Zajęcia są prowadzone w języku Python 3.6 z wykorzystaniem Spyder IDE. Wykorzystywane są biblioteki Numpy, Matplotlib oraz OpenCV.
<br/>
<p align="center">
<img width="256" height="256" src="https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/Lenna.png"><br />
Wykorzystywane podczas zajęć część zdjęcia szwedzkiej modelki Leny Söderberg, autorstwa Dwight Hooker'a opublikowane w listopadowym wydaniu Playboy'a z 1972. Oficjalnie wykorzystuje się warstwę zieloną do transformacji z RGB na skalę szarości [1].
</p>
<br/>

**L1-L2 zajęcia** - Podstawy Pythona.<br />
Wygenerowania rysunki sinusa z pełnymi matematycznymi atrybutami, jak przesunięcie fazowe czy zmienna amplituda.
<br/>
<p align="center">
<img src="https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/Z1-some_plot.png" width="350"> 
<img src="https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/Z1_sin_img.png" width="250">
</p>
<br/>

**L3** - Tworzenie i analiza histogramów.<br />
Wykonać zaprezentowany poniżej wykres histogramów każdej z warstw RGB obrazu Lenny. Dokładny opis zadania wraz z propozycją rozwiązania w [pliku](https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/L3%20-%20histogramy.py). Funkcje generującą histogram wrzucić do ogólnej biblioteki [polib.py](https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/polib.py) - przetwarzanie obrazów library. 
<p align="center">
<img width="256" height="256" src="https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/L3%20-%20Lenna_histogram.png"><br />
Wykresy słupkowe histogramów zdjęcia Lenny z każdej warstwy RGB. Histogram koloru zielonego jest najszerszy i z tego powodu jest często wybierany jako reprezentacja w skali szarości.
</p>
<br />

**L4** - Binaryzacja obrazów z progiem globalnym in adaptacyjnym.<br />
Napisać dwie funkcje binaryzujące obraz jak poniżej. Pierwsza z progiem globalnym druga z progiem adaptacyjnym. Dokładny opis zadania wraz z propozycją rozwiązania w [pliku](https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/L4%20-%20binaryzacja.py). Funkcje binaryzujące wrzucić do ogólnej biblioteki [polib.py](https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/polib.py)
<p align="center">
<img src="https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/tekst.png" width="250"> 
<img src="https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/L4%20-%20text_binarized_global_threshold.png" width="250">
<img src="https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/L4%20-%20text_binarized_global_adaptive.png" width="250">
Od lewej zdjęcie oryginalne, zdjęcie binaryzowane globalnie z progiem 5px, zdjęcie binaryzowane adaptacyjnie z ramką 3 i globalnym podwyższeniem progu 0.
</p>

**L5** - Wyliczanie entropii obrazu. Wygeneruj N-bitowy obraz białego szumu i policz czy entropia jest równa zdefiniowanej ilości bitów. Dokładny opis zadania wraz z propozycją rozwiązania w [pliku](https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/). Wykorzystać własną funkcję histogramu. Funkcje liczącą entropię wrzucić do ogólnej biblioteki [polib.py](https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/polib.py)

**L6** - Filtracja kontekstowa, rozmazywanie obrazu. Wykonaj filtracje rozmazującą poniższego obrazu, który przedstawia "Ciemną stronę księżyca". Filtracja powinna być wykonana za pomocą 3 metod - uśredniającej, medianowej i gaussowskiej. Dokładniejszy opis zadania wraz z propozycją rozwiązania znajduje się w [pliku](https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/L6%20-%20image_blurring.py). Funkcje wykonywujące rozmazywanie wrzucić do ogólnej biblioteki [polib.py](https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/polib.py).
<p align="center">
<img src="https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/ciemna_strona_ksiezyca_org.png" width="250"> 
<img src="https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/ciemna_strona_ksiezyca_brud.png" width="250">
</br>
Oryginalne zdjęcie ciemnej strony księżyca (lewo) wraz z zanieczyszczeniami (prawo).
</p>
</br>

<p align="center">
<img src="https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/L6 - mean_filter_3-5-7.png" width="800">
<img src="https://github.com/Miloszek1990/Zajecia_Matematyka_PO/blob/master/L6 - median_filter_3-5-7.png" width="800">
</br>
Wyniki rozmazywania ramkami o bokach 3, 5, 7 dla filtru uśredniającego (góra) i medianowego (dół).
</p>
</br>

<ul>
[1] https://pl.wikipedia.org/wiki/Lenna_(fotografia)
</ul>

