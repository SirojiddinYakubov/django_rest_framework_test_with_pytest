![logo jpg](banner.jpg "Logo")

<div align="center">
  <h1>Django Rest Frameworkda API larni pytest orqali testdan o'tkazish</h1>
</div>

<div align="center">
  Ushbu video seriyamizda Django Rest Framework yordamida chiqarilgan API larimizni pytest paketi orqali testdan o'tkazamiz. Serializerlar, servislar va viewslarimizdagi uchrashi mumkin bo'lgan barcha xato va kamchiliklarni oldini olamiz va birgalikda tuzatamiz. Darslarimiz davomida bizga qo'shimchasiga kerak bo'ladigan qo'shimcha paketlar  va web dasturlashda ishlatiladigan turli xil atamalar haqida ham ma'lumot beriladi.  Ushbu berilgan bilimlarni egallaganingizdan so'ng, dasturiy ta'minotingizga amalda qo'llash orqali siz, dasturiy ta'minotingiz to'xtovsiz va sifatli ishlashini, kodlaringiz siz o'ylagan darajada aniq natija chiqarishini, "Бизнес логика" laringiz mantiqiy jihatdan to'g'ri yoki noto'g'ri tuzilganligini aniqlay olasiz.
</div>

<br>

<div align="center">
  Webdasturlashga oid ko'proq yangiliklardan xabardor bo'lish uchun bizni kuzatib boring: <br>
  <a href="https://www.youtube.com/channel/UCeJ6Sc3SaKKArAurnCwlJBw">YouTube</a>
  <span> | </span>
  <a href="https://www.instagram.com/yakubovdeveloper">Instagram</a>
  <span> | </span>
  <a href="https://www.facebook.com/yakubovdeveloper">Facebook</a>
  <span> | </span>
  <a href="https://www.tiktok.com/@yakubovdeveloper">TikTok</a>
  <span> | </span>
  <a href="https://t.me/yakubovdeveloper">Telegram</a>
</div>

## Video seriyamiz qismlari va mazmuni

<details>
<summary><b>Part-1 Pytest va Fixturelar haqida tushuncha</b>
</summary>
<br>
<ul>
    <li>Unittest va pytest orasidagi qisqacha farq haqida tushuncha</li>
    <li>Pytest paketi va uning qulayliklari haqida qisqacha ma'lumot</li>
    <li>pytest-django, pytest-factoryboy va faker paketlarini o'rnatamiz</li>
    <li>Pytest paketida testlarni boshlashdan oldingi umumiy tushunchalar</li>
    <li>Fixturelar haqida ma'lumot</li>
    <li>Test jarayonida fixturelardan foydalanish usullari</li>
</ul>

To'liq video qo'llanma bu yerda: https://www.youtube.com/watch?v=CnSca84jOU8

</details>

<details>
<summary><b>Part-2 Serializerlarni pytest orqali testdan o'tkazish</b>
</summary>
<br>
<ul>
    <li>Django rest frameworkda serializerlar haqida qisqacha tushunchaga ega bo'lamiz</li>
    <li>Django rest framework orqali chiqarilgan API larni barcha dasturlash tillarida birdek foydalana olishimiz uchun JSON formatidan foydalanamiz. JSON formati haqida qisqacha ma'lumotga ega bo'lamiz</li>
    <li>Django rest framework orqali chiqarilgan API larni Postman orqali tekshirib ko'ramiz</li> 
    <li>Django rest framework serializerimiz uchun foydalanuvchimiz yo'l qo'yishi mumkin bo'lgan barcha xato va kamchiliklarni hisobga olgan holda test yozamiz</li>
</ul>

To'liq video qo'llanma bu yerda: https://www.youtube.com/watch?v=ROab5NYsjdE

</details>

<details>
<summary><b>Part-3 "Бизнес логика" larni pytest orqali testdan o'tkazish</b>
</summary>
<br>
<ul>
    <li>Arxitektura haqida qisqacha ma'lumotga ega bo'lamiz</li>
    <li>"Бизнес логика" nima ekanligi haqida qisqacha ma'lumotga ega bo'lamiz</li>
    <li>Kitob do'konimiz uchun "бизнес логика" ya'ni servislarimiz bilan tanishib chiqamiz</li>
    <li>Create, Read, Update, Delete, List API lar uchun yozilgan "бизнес логика" ya'ni servislarni pytest yordamida testdan o'tkazamiz</li>
</ul>

To'liq video qo'llanma bu yerda: https://www.youtube.com/watch?v=ceqjn96kjLw

</details>

</details>

<details>
<summary><b>Part-4 Viewslarni pytest orqali testdan o'tkazish </b></summary>
<br>

<ul>
    <li>Web so'rov va web javoblar haqida tushunchaga ega bo'lamiz</li>
    <li>"Django viewslar qanday ishlaydi ?" - ushbu savolimizga javob topamiz</li>
    <li>Status kodlar haqida ma'lumotga ega bo'lamiz va eng ko'p qo'llaniladigan status kodlarga to'liqroq to'xtalamiz</li>
    <li>Web so'rov jo'natish uchun API Client yaratamiz</li>
    <li>Postman orqali web so'rov va web javoblarni tekshirib ko'ramiz</li>
    <li>Create, Read, Update, Delete, List API lar uchun yozilgan viewslarni pytest yordamida testdan o'tkazamiz</li>
</ul>

To'liq video qo'llanma bu yerda: https://www.youtube.com/watch?v=csky_VjUTGk

</details>

</details>

## Installation

```bash
cp deploy/env.md deploy/.env

python -m venv venv

source venv/bin/activate

pip install poetry

poetry install
```

## Run tests

```bash
pytest
```

## Run server

```bash
python manage.py createsuperuser

python manage.py runserver
```

## Author
[Sirojiddin Yakubov](https://t.me/Sirojiddin_Yakubov)