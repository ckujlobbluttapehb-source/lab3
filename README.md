# Лабораторная работа #3
## Этап выполнения задания с заменой данных в БД

Итог выполненных команд: 

```UPDATE "articles_article" SET "text" = 'Django - это мощный веб-фреймворк для Python. [ИЗМЕНЕНО ЧЕРЕЗ SQL] Он следует архитектуре MVT и предоставляет множество встроенных функций.' WHERE "id" = 1;```

``` UPDATE "articles_article" SET "title" = '[РЕДАКТИРОВАНО] Работа с административной панелью Django' WHERE "id" = 2; ```

``` INSERT INTO "articles_article" ("title", "author_id", "text", "created_date") VALUES ('Статья созданная через SQL', 1, 'Этот текст был добавлен напрямую в базу данных через SQL-запрос.', date('now')); ```

<img width="1629" height="619" alt="image" src="https://github.com/user-attachments/assets/c54d4ae1-0745-4524-b4f2-558c02da1184" />

