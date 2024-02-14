# Snack Tracker Project

Lab 27 - This project is a Snack Tracker application that allows users to keep track of various snacks, their details, and purchasers.

2.13.24

## Author

**Stephanie G. Johnson**

## Links and Resources

- [Model Documentation](https://docs.djangoproject.com/en/4.1/ref/models/)
- [Templates Documentation](https://docs.djangoproject.com/en/4.1/topics/templates/)
- [Superuser Guide](https://docs.djangoproject.com/en/4.1/ref/django-admin/)
- [Django Admin Documentation](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/)
- [What is int pk](https://docs.djangoproject.com/en/4.1/ref/models/fields/#integerfield)
- ChatGPT - the homie of the project

## Setup

### .env Requirements

- `PORT` - Port Number (default: 8000)
- `DATABASE_URL` - URL to the running Postgres instance/db

### How to Initialize/Run the Application

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/snack-tracker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd snack-tracker
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application in your browser: [http://localhost:8000/](http://localhost:8000/)

### Tests

#### Running Tests

To run tests, use the following command:

```bash
python manage.py test
```

#### Notes on Tests

- The test suite includes tests for basic functionality, such as views, models, and templates.

#### Incomplete/Skipped Tests

No tests were skipped or left incomplete.

## Troubleshooting

### Common Issues and Solutions

1. **Reverse for 'snack_detail' with no arguments not found:**

    - **Issue:** This error occurs when trying to reverse the URL for the `snack_detail` view without providing the required argument.
    - **Solution:** Make sure to include the `pk` (or `id`) argument when using the `{% url 'snack_detail' snack.pk %}` template tag.

2. **Django Reverse for 'snack_detail' with no arguments not found:**

    - **Issue:** The `snack_detail` reverse lookup fails, especially when using Django's `reverse` function in views or tests.
    - **Solution:** Ensure that the `snack_detail` URL pattern in `urls.py` includes the necessary argument, like `<int:pk>`.

3. **TemplateDoesNotExist at /:**

    - **Issue:** Django cannot find the specified template, resulting in a `TemplateDoesNotExist` error.
    - **Solution:** Double-check the template path provided in the view and make sure the template file exists in the correct location.

4. **Database-related Errors:**

    - **Issue:** Database-related errors may occur, such as migrations not being applied or missing database configurations.
    - **Solution:** Ensure that the database is properly configured in the `.env` file and run `python manage.py migrate` to apply migrations.

