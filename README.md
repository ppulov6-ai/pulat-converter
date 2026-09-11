# Pulat Converter

Конвертер плана закачки ГРП в эталонный Excel «Программа работ».

Репозиторий: https://github.com/ppulov6-ai/pulat-converter

## Что делает

На вход — унифицированный план (xlsx / docx / pdf).
На выход — файл `\u043dазвание (Программа).xlsx` в оформлении эталона.

## Стресс-тест

10 прогонов унифицированного плана: **10/10 OK**, 17 стадий, 1.56–1.98 с (среднее 1.69 с).

## Запуск

```bash
pip install -r requirements.txt
python grp_program.py "план.xlsx"
python app/start.py
```

Веб-окно: http://127.0.0.1:17831/
