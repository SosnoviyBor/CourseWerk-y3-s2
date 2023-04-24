# Курсова робота за 2 семестр 3 курсу
<b>Дисципліна</b>: Технології паралельних обчислень<br>
<b>Тема</b>: Алгоритм пошуку оберненої матриці (за [методом Крамера](https://uk.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%9A%D1%80%D0%B0%D0%BC%D0%B5%D1%80%D0%B0))<br>
<b>Задача</b>: Розпаралелити будь-який алгоритм пошуку оберненої матриці та пришвидшити його як мінімум на 20%. Модифікації дозволені

# Набори даних
Створені за допомогою бібліотеки [numpy](https://numpy.org/) та збережені за допомогою бібліотеки [pickle](https://docs.python.org/3/library/pickle.html) та находяться у папці [/test_data/benchmark](https://github.com/SosnoviyBor/CourseWerk-y3-s2/tree/master/test_data/benchmark). У назві кожного файлу вказано розмір матриці (d) та їх кількість (с)

# Результати:
Можна переглянути у файлі results.xlsx

# Невдалі спроби
![dang, my meme died again](https://github.com/SosnoviyBor/CourseWerk-y3-s2/blob/master/literlly_me.jpg?raw=true)<br>
Знаходяться у папці [./algorithms/failures/](https://github.com/SosnoviyBor/CourseWerk-y3-s2/tree/master/algorithms/failures)<br>
Я би навіть не подумав їх зберігати, якби не витратив на них 3 дні від світанку до сумерків. Нехай будуть тут в знак ганьби
### [Метод Гауса](https://uk.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%93%D0%B0%D1%83%D1%81%D0%B0)
Сам по собі алгоритм хороший. Занадто хороший, навіть. Іронічно, але я на нього часу вбив занадто багато<br>
Він значно швидший за Крамера і навіть в одному потоці капітально його обганяє, але через його природу, паралелити його важко, бо там треба стежити за колізіями даних. Не здивуюся, що це й було причиною того, що дві єдині <i>працюючі</i> паралельні реалізації написані лише на С++ із використанням OpenMP або CUDA. Єдиною ідеєю була модифікація його LU-декомпозицією, але й та вигоріла через створюємий додатковими підготовками оверхед. "Yes pain, no gain", так би мовити

0. Синхронний ванільний Гаус - 13.0s per d-500
    * Таких значень не сягає навіть багатопоточний Крамер. Навіть близько не стоїть
1. Синхронна LU-декомпозиція + паралельне обернення LU через concurrent.futures - 23.0s per d-500
2. Паралельна LU-декомпозиція + паралельне обернення LU через concurrent.futures - 24.4s per d-500
    * Це мене просто вбило
3. Синхронна LU-декомпозиція + паралельне обернення LU через multiprocessing - 23.0s per d-500
    * Здебільшого це був лише експеримент для себе, щоб порівняти швидкодію бібліотек concurrent.futures та multiprocessing
