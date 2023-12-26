# Localle )) Your Local Hub Marketplace

![localle logo](https://github.com/mistersouza/localle/blob/main/static/assets/images/localle%20_%20logo.png?raw=true)

▷ Alright, picture this: Localle is on a mission to amp up your neighborhood vibes! We're kicking things off by building a marketplace where you can connect with your neighbors, support local businesses, and buy or sell cool stuff right from your area. Imagine a hub where the coolest finds and local gems are just a click away. We're on a mission to make your neighborhood the go-to spot for connections, sales, and that awesome community vibe. Join us in this exciting venture as we craft the first step towards an epic neighborhood experience!

Check it live out [here.](https://localle-marketplace-0ed3b7e33a22.herokuapp.com/)

## Tech Stack

### Languages Spoken Here

- HTML. The foundation of our web magic.
- CCSS. Adding that stylish flair to everything you see.
- JavaScript. Bringing life to elements and making things interactive while supporting the HTML & CSS groove.
- Python. Powering the brains behind the scenes.

### Framework used and abused

- [Django](https://www.djangoproject.com/). The web wizard behind this project's magic. It's the sleek toolkit that makes building powerful and secure websites a breeze.

### Storage trusted

- [Amazon Web Services (AWS)](https://aws.amazon.com). The home for all our static and media files, securely stored in the digital realm.
- [Cloudinary](https://cloudinary.com/) - Where media becomes magic. It's our creative hub, transforming images and videos into dazzling web assets.

### Database

- [ElephantSQL](https://www.elephantsql.com/). Your database sanctuary, where data roams freely and securely, as robust as an elephant.

### Libraries

- [Bootstrap](https://getbootstrap.com/). The hero behind our site's responsive design, stylish elements, and navbar magic.
- [Font Awesome](https://fontawesome.com/). The secret sauce sprinkled across our site, giving every element that visual edge with its array of icons.
- [Google Fonts](https://fonts.google.com/). Working its magic with the Roboto font family, giving our site that unique typography and unmistakable flair.

## Deployment

### GitPod

▷ Getting your app ready

- Open up your settings.py file 
    1. Setup databse
        ```python
        import dj_database_url

        DATABASES = {
            'default': dj_database_url.parse("<your Postrgres database URL>")
        }
        ```
    2. Update settings.py in your Django app
        ```python
        DEBUG = False
        ```
    3. Update Allowed Hosts
        ```python
        ALLOWED_HOSTS = ['.herokuapp.com', 'localhost']
        ```

- On the CL
    4. Create a requirements. This file tells Heroku what your app needs to run smoothly.
        ```bash
        pip3 freeze --local > requirements.txt
        ```
    5. Craft a Procfile. This tells Heroku how to run your app. Think of it as the main instruction manual.
        ```bash
        echo web: python app.py > Procfile
        ```
    6. Shift models to ElephantSQL.
        ```bash
        python3 manage.py makemigrations
        python3 manage.py migrate
        ```
- on Heroku
    7. Started fresh on Heroku and gave our app a European vibe.
    8. Swiped right for GitHub as our deployment wingman.
    9. Dropped in some super-secret config vars for that behind-the-scenes magic. Check out the cool settings
    ![Config Vars](https://github.com/mistersouza/localle/blob/main/static/assets/images/localle_heroku-vars.png?raw=true)
    10. Finally hit that deploy button and let the awesomeness unfold

▷ The site first brewed up in GitPod and then landed in this remote [GitHub repository](https://github.com/mistersouza/localle.git).And let's talk GIT – the commands that made the magic real.

- **git status** >> It's like peeking into the project's mood board - shows any changes or new stuff.
- **git add --all** >> The "get ready to party" move - stages files for the big commit.
- **git commit -m " "** >> The official seal of approval - commits all the files.
- **git push** >> The grand finale - sends everything to the master branch up there on GitHub. Boom!