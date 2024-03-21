## Указываем переменные окружения

1. Копируем файл [.env.example](.env.example) и указываем префикс переменных ```LOCAL_```

```
sed 's/EXAMPLE_/LOCAL_/' .env.example > .env.local
```

2. В созданном файле меняем необходимые переменные

## Запускаем Сервис

с корневой директории проекта 
```
make local_build && make local_up
```