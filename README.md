# Курсова робота за 2 семестр 3 курсу
<b>Дисципліна</b>: Технології паралельних обчислень<br>
<b>Тема</b>: Алгоритм пошуку оберненої матриці (за методом Крамера)<br>
<b>Задача</b>: Розпаралелити будь-який алгоритм пошуку оберненої матриці та пришвидшити його як мінімум на 20%. Модифікації дозволені

# Набори даних
Створені за допомогою бібліотеки [pickle](https://docs.python.org/3/library/pickle.html) та находяться у папці [./test_data/](https://github.com/SosnoviyBor/CourseWerk-y3-s2/tree/master/test_data). У назві кожного файлу вказано розмір матриці (d) та їх кількість (с)

# Результати:
### Послідовний алгоритм
| Кількість = 1 | 25*25 | 50*50 | 75*75 | 100*100 | 150*150 | 200*200 | 250*250 | 300*300 |
|--------------:|-------|-------|-------|---------|---------|---------|---------|---------|
| Послідовний   |       |       |       |         |         |         |         |         |
| Паралельний   |       |       |       |         |         |         |         |         |

### Розпаралелений алогритм
| Кількість = 1 | 25*25 | 50*50 | 75*75 | 100*100 | 150*150 | 200*200 | 250*250 | 300*300 |
|--------------:|-------|-------|-------|---------|---------|---------|---------|---------|
| Послідовний   |       |       |       |         |         |         |         |         |
| Паралельний   |       |       |       |         |         |         |         |         |

(сюди, напевно, потім прикручу картинку з графіком з екселю)
<br>
<br>
<br>

# Невдалі спроби
<img src="https://cdn.discordapp.com/attachments/493348617298378773/1094034621458554910/photo_2023-03-03_00-30-47.jpg"><br>
Знаходяться у папці [./algorithms/failures/](https://github.com/SosnoviyBor/CourseWerk-y3-s2/tree/master/algorithms/failures)<br>
Я би навіть не подумав їх зберігати, якби не витратив на них 3 дні від світанку до сумерків. Нехай будуть тут в знак ганьби
### Метод Гауса
Сам по собі алгоритм хороший. Занадто хороший, навіть. Іронічно, але я на нього часу вбив занадто багато<br>
Він значно швидший за Крамера і навіть в одному потоці капітально його обганяє, але через його природу, паралелити його важко, бо там треба стежити за колізіями даних. Не здивуюся, що це й було причиною того, що дві єдині <i>працюючі</i> паралельні реалізації написані лише на С++ із використанням OpenMP або CUDA. Єдиною ідеєю була модифікація його LU-декомпозицією, але й та вигоріла через створюємий додатковими підготовками оверхед. "Yes pain, no gain", так би мовити
0. Синхронний ванільний Гаусс - 13.0s per d-500
    * Таких значень не сягає навіть багатопоточний Крамер. Навіть близько не стоїть
1. Синхронна LU-декомпозиція + паралельне обернення LU через concurrent.futures - 23.0s per d-500
2. Паралельна LU-декомпозиція + паралельне обернення LU через concurrent.futures - 24.4s per d-500
    * Це мене просто вбило
3. Синхронна LU-декомпозиція + паралельне обернення LU через multiprocessing - 23.0s per d-500
    * Здебільшого це був лише експеримент для себе, щоб порівняти швидкодію бібліотек concurrent.futures та multiprocessing