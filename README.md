# Web Product Catalog

Catalogo de productos básico hecho con Django 5 y Bootstrap 5. Proyecto que permite agregar productos desde el panel admin de Django y ver los detalles de cada uno en la pagina, donde se podrá solicitar el producto.

## Vista previa

![Vista previa]

## Características


## 🛠️ Tecnologías utilizadas

- Python
- Django
- HTML5, CSS3
- SQLite3 (por defecto de Django)
- Bootstrap (opcional si se usa para estilos)

## ⚙️ Instalación

Sigue estos pasos para correr el proyecto en tu máquina local:


1. Clona el repositorio:
   ```bash
   git clone https://github.com/luisAngelDev/django-product-catalog.git
   
   ```

2. Crea y activa un entorno virtual:S
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplica las migraciones:
   ```bash
   python manage.py migrate
   ```

5. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

6. Accede al sitio en tu navegador:
   ```
   http://127.0.0.1:8000/
   ```

## 🔐 Acceso al panel de administración

Puedes acceder al panel de administración de Django en:

```
http://127.0.0.1:8000/admin
```

> ⚠️ Necesitas crear un superusuario:
> ```bash
> python manage.py createsuperuser
> ```

## 👨‍💻 Autor

**Luis Ramos**  
[GitHub: @luisAngelDev](https://github.com/luisAngelDev) 

## 📄 Licencia
Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](./LICENSE) para más detalles.































































