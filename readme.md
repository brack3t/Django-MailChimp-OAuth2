To test out MailChimp's OAuth2 authentication with Django, just clone this project and replace a few variable and you're on your 
way.

1. Install the requirements by running `pip install -r requirements.txt`. You are using a virtualenv, right?

2. In `settings.py`, edit the following variables to be custom to your app.

    MAILCHIMP_CLIENT_ID
    MAILCHIMP_CLIENT_SECRET
    MAILCHIMP_COMPLETE_URI

3. On MailChimp.com, in your app settings, make sure you have `http://127.0.0.1` as your `redirect_uri` setting.

4. Set up the DB. Just run `python manage.py syncdb` from the `mailchimp_demo` directory. You don't need to create any 
   superusers.

5. Start the server with `python manage.py runserver` and load `http://127.0.0.1:8000/` in your browser of choice.

That's all!
