=====================================
Django Views Documentation
=====================================

This documentation provides information about various views in a Django web application.

.. _home:

Home View
---------

.. function:: home(request)

   Render the 'home.html' template.

   :param request: The HTTP request object.
   :type request: HttpRequest
   :return: A response containing the rendered 'home.html' template.
   :rtype: HttpResponse

.. _contact:

Contact View
------------

.. function:: contact(request)

   Render the 'contact.html' template.

   :param request: The HTTP request object.
   :type request: HttpRequest
   :return: A response containing the rendered 'contact.html' template.
   :rtype: HttpResponse

.. _about:

About View
----------

.. function:: about(request)

   Render the 'about.html' template.

   :param request: The HTTP request object.
   :type request: HttpRequest
   :return: A response containing the rendered 'about.html' template.
   :rtype: HttpResponse

.. _login_view:

Login View
----------

.. function:: login_view(request)

   Handle user login.

   If the HTTP request method is POST, this function attempts to authenticate the user based on the provided username and password. If authentication is successful, the user is logged in, and they are redirected to the 'bandpage'. If authentication fails, an error message is displayed on the 'signup.html' page.

   If the HTTP request method is GET, the function renders the 'login.html' page.

   :param request: The HTTP request object.
   :type request: HttpRequest
   :return: A response containing the rendered page or a redirection to 'bandpage' upon successful login.
   :rtype: HttpResponse

.. _signup:

Signup View
-----------

.. function:: signup(request)

   Handle user registration.

   If the HTTP request method is POST, this function validates and processes the registration form submitted by the user. If the form is valid, a new user account is created, and the user is redirected to the 'login' page. If the form is not valid, the 'signup.html' page is displayed with validation errors.

   If the HTTP request method is GET, the function renders the 'signup.html' page with an empty registration form.

   :param request: The HTTP request object.
   :type request: HttpRequest
   :return: A response containing the rendered page or a redirection to the 'login' page upon successful registration.
   :rtype: HttpResponse

.. _bandpage:

Bandpage View
------------

.. function:: bandpage(request)

   Render the 'bandpage.html' template.

   :param request: The HTTP request object.
   :type request: HttpRequest
   :return: A response containing the rendered 'bandpage.html' template.
   :rtype: HttpResponse

.. _concert_list:

Concert List View
-----------------

.. function:: concert_list(request)

   Render the 'concert_list.html' template with concert information.

   :param request: The HTTP request object.
   :type request: HttpRequest
   :return: A response containing the rendered 'concert_list.html' template.
   :rtype: HttpResponse

.. _exclusive_content:

Exclusive Content View
-----------------------

.. function:: exclusive_content(request)

   Render the 'exclusive_content.html' template with exclusive content.

   :param request: The HTTP request object.
   :type request: HttpRequest
   :return: A response containing the rendered 'exclusive_content.html' template.
   :rtype: HttpResponse

.. _song:

Song View
---------

.. function:: song(request)

   Render the 'song.html' template with song information.

   :param request: The HTTP request object.
   :type request: HttpRequest
   :return: A response containing the rendered 'song.html' template.
   :rtype: HttpResponse

.. _album:

Album View
----------

.. function:: album(request)

   Render the 'album.html' template with album information.

   :param request: The HTTP request object.
   :type request: HttpRequest
   :return: A response containing the rendered 'album.html' template.
   :rtype: HttpResponse

.. _user_logout:

User Logout View
----------------

.. function:: user_logout(request)

   Log the user out and redirect to the 'bandpage'.

   :param request: The HTTP request object.
   :type request: HttpRequest
   :return: A redirection to the 'bandpage'.
   :rtype: HttpResponse
