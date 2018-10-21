# Risk corpus
Корпус статей на тему альпинизма и горного туризма

Источник: Risk.ru 
Фреймворк для сбора данных: python + scrapy

## Сведения о корпусе

||Количество|
|---|---|
|Статьи|33863|
|Абзацы|530169|
|Предложения|1016341|
|Слова|13348440|
|Различные слова|544005|
|Символы|91017948|

* Данные о статье:
  * Дата создания
  * Автор
  * Рейтинг пользователей
  * Наличие фото (24688 статей)
  * Наличие видео (1079 статей)
  * Тэги:
    * Вид активности
    * Категория
    * Группа 
    * Место
    * Специальный тип
    
## Разметка корпуса
#### Сегментация
python + nltk + russian language support (https://github.com/Mottl/ru_punkt)

Храниение: sentence.csv - каждому посту сопоставлен набор координат предложений

#### Токенизация
python + nltk
    
## Подробнее о тегах

#### Вид активности: 30506 статей

|Активность|Количество статей|Активность|Количество статей|
|----------|-----------------|----------|-----------------|
|Альпинизм|14553|Воздух|717|
|Скалолазание|4276|Ски-тур|496|
|Горный туризм|2069|Скайраннинг|448|
|Путешествия|1888|Туризм|359|
|Бэккантри/Фрирайд|1347|Вело|328|
|Ледолазание/Драйтуллинг|787|BASE|262|
|Вода|727|Спелеология|195|
|Мультигонки|719|Снегоступинг|106|
|Ropejumping|43|Слэклайн|7|

#### Категория: 20381 статья

|Категория|Количество статей|Категория|Количество статей|
|---------|-----------------|---------|-----------------|
|Новости|5949|Отчёт|3355|
|Видео|2015|Фото|1709|
|Оффтоп|1523|Творчество|1267|
|Снаряжение|1058|Юмор|592|
|Безопасность в горах|512|Библиотека|502|
|Легенды|302|Реклама|277|
|Помним|271|Взаимопомощь|241|
|Технические советы|222|Ищу попутчиков|205|
|Риск Онсайт|190|Интервью|159|
|Обсуждение сайта|30|Обучение|2|

#### Группа: 6556 статей

Самые популярные:

|Группа|Количество статей|
|------|-----------------|
|Творчество РИСКовчан|1143|
|Экзотические путешествия|488|
|Freeski|345|
|Gaugin Friends|266|
|Moscow Ice Climb|256|

#### Место: 4463 статьи

Самые популярные:

|Место|Количество статей|
|-----|-----------------|
|Эльбрус|173|
|Москва|145|
|Кавказ|123|
|Тюмень|95|
|Красноярск|88|
|Крым|75|
|Ала-Арча|50|
|Памир|49|
|Сосулька МАИ|39|
|Киргизия|35|
|Екатеринбург|34|
|Непал|34|

Всего упоминается 970 различных локаций, из них 482 более одного раза.

#### Тип: 1638 статей

|Тип|Количество статей|
|---|-----------------|
|События|890|
|Вопрос-ответ|748|

