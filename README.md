# Django Band Website

This is a Django-based web application for a band's website. It includes features for user authentication, displaying concert information, exclusive content, songs, and albums.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/TDKasala/Band-website.git
   ```

2. Navigate to the project directory:

   ```shell
   cd Band-website
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```shell
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```shell
     source venv/bin/activate
     ```

5. Install project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Migrate the database:

   ```shell
   python manage.py migrate
   ```

7. Create a superuser account (admin) to access the admin panel:

   ```shell
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```shell
   python manage.py runserver
   ```

9. Access the website at `http://localhost:8000/`.

## Usage

### User Authentication

- Users can sign up for an account by visiting the registration page (`/signup`). After successful registration, they are redirected to the login page.
- Users can log in with their credentials on the login page (`/login`).

### Band Pages

- Home Page (`/`): Displays general information about the band.
- About Page (`/about`): Provides information about the band's history and members.
- Contact Page (`/contact`): Allows users to get in touch with the band.

### Band Member Access (Requires Login)

- Band Page (`/bandpage`): A protected page accessible only to logged-in users (band members).
- Concert List (`/concert_list`): Displays concert information.
- Exclusive Content (`/exclusive_content`): Provides access to exclusive band content.
- Songs (`/song`): Displays a list of songs.
- Albums (`/album`): Displays a list of albums.

### Admin Panel

- Access the Django admin panel at `http://localhost:8000/admin/` to manage users, concert information, exclusive content, songs, and albums.

## Functionality

### `views.py`

- `home(request)`: Renders the home page.
- `about(request)`: Renders the about page.
- `contact(request)`: Renders the contact page.
- `login_view(request)`: Handles user login.
- `signup(request)`: Handles user registration.
- `bandpage(request)`: Renders the band page (requires login).
- `concert_list(request)`: Renders the concert list (requires login).
- `exclusive_content(request)`: Renders exclusive content (requires login).
- `song(request)`: Renders song information (requires login).
- `album(request)`: Renders album information (requires login).
- `user_logout(request)`: Logs the user out and redirects to the band page.

### Authentication

- User registration is handled using Django's built-in `UserCreationForm`.
- Users can log in and out.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to your fork: `git push origin feature-name`.
5. Create a pull request to the main repository.
