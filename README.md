# VKGroupLikes - VK Group Likes Bot #
## По-русски
VK Group Likes Bot - бот для автоматизации работы с группами Vk<br/>
Т.е, пока что ты можешь автоматизировать:
  - Автоматически ставить лайки на новые посты в группе
  - Пролайкать последние n-постов в группе
## Как начать ?
Ну что решились? Что ж начнем...
### Установка Python
Для начала нам потребуется скачать python [Оффициальный Сайт](https://www.python.org/downloads/)  
Устанавливаем и не забываем на всякий случай поставить __add to path__  
![Фото](http://www.swtestacademy.com/wp-content/uploads/2017/04/python-selenium-2.png "Python")
Установили? Молодцы!
### Установка библиотеки Vk Api
Далее открываем терминал и пишем __pip install vk-api__
![Фото](https://i.imgur.com/sQa68zX.png)
### Скачиваем и Настраеваем
#### В результаате у нас должно получиться 2 файла:  
  - main.py - Главный Файл  
  - config.py - Конфиг (Его то мы и будем редактировать)  
#### Открываем и тут нам нужно выбрать, как получим доступ к аккаунту:  <br/>
  - Через __Логин/Пароль__
  - Либо Через __Токен__
![Фото](https://i.imgur.com/s6Y5ur9.png)  
В первом случае пишем в поля YOUR_LOGIN/YOUR_PASSWORD cвой Логин/Пароль  
Во втором же, переходим по ссылке [https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username=**login**&password=**password**](https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username=**login**&password=**password**)  
  Где **login** и **password**, логин и пароль соответственно
  ![Фото](https://i.imgur.com/m2P5euh.png)
  Копируем всё что в кавычках после __access_token__ и вставляем в поле YOUR_TOKEN  
  Хух! С основным разобрались!  
  ## Разберём остальной Конфиг
  P.S Статья в процессе доработки, а пока можешь добавить в избранное)
