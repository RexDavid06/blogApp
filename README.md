# BlogApp

A Django-powered blog application where users can sign up, create posts, and manage their profile. This project demonstrates core Django features including user authentication, model relationships, and basic frontend styling.

## Features

- User authentication (sign up, sign in, sign out)
- Create, read, update, and delete blog posts
- User profile with profile picture and bio
- Responsive, user-friendly interface
- Categories and sidebar navigation for posts

## Getting Started

### Prerequisites

- Python 3.8+
- Django (tested with Django 4+)
- Pillow (for image uploads)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RexDavid06/blogApp.git
   cd blogApp
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Visit the app:**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser

### Static & Media Files

- Static files are served from the `static/` directory.
- Uploaded profile pictures are stored in `media/profile_pictures/`.
- Ensure you have set the following in `settings.py` for development:
  ```python
  STATIC_URL = '/static/'
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```
- In development, add this to your root `urls.py`:
  ```python
  from django.conf import settings
  from django.conf.urls.static import static

  urlpatterns = [
      # ... your URL patterns ...
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

## Project Structure

- `app/`: Contains Django app with models, views, templates, and static files
- `templates/`: HTML templates for rendering pages
- `static/`: CSS and static assets
- `media/`: Uploaded images (profile pictures)

## Customization

- Update `style.css` in the `static/` directory to change the blog’s appearance
- Extend the `Profile` model or blog post model for more features

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

- [RexDavid06](https://github.com/RexDavid06)

---

Feel free to contribute or open an issue if you find a bug or have suggestions!
