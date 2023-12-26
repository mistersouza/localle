# Localle )) Your Local Hub Marketplace

![localle logo](https://github.com/mistersouza/localle/blob/main/static/assets/images/localle%20_%20logo.png)

▷ Alright, picture this: Localle is on a mission to amp up your neighborhood vibes! We're kicking things off by building a marketplace where you can connect with your neighbors, support local businesses, and buy or sell cool stuff right from your area. Imagine a hub where the coolest finds and local gems are just a click away. We're on a mission to make your neighborhood the go-to spot for connections, sales, and that awesome community vibe. Join us in this exciting venture as we craft the first step towards an epic neighborhood experience!

Check it live out [here.](https://localle-marketplace-0ed3b7e33a22.herokuapp.com/)

## Planning & Development

### Business Strategy 🚀

Introducing Localle Marketplace's Game Plan! It's all about rocking our unique vibe and unlocking doors to some serious growth and impact.

- Boosting Local Swagger: Let's amp up our street cred by teaming up with local legends and getting our name out there in the community.

- Community Empowerment: We're all about backing the little guys! Let's create a space where local businesses can thrive together, building a tight-knit community.

- Smooth Shopping Vibes: Our mantra? Easy peasy! We're making sure both buyers and sellers have the slickest shopping experience around.

### Wireframes

▷ We're all about that sleek vibe with a single font family to keep things clean and seamless. But hey, the future looks spicy! We're diving into custom font territory, backed by loads of UX research, sharper business goals, and some epic partnerships.

Started with a free template to hustle up our MVP launch - gotta nail those must-haves, you know? But hey, that's just phase one! Digging deep into UX research and leveling up with TechLabs training means big things for this project's next chapter.

![Wireframes](https://github.com/mistersouza/localle/blob/main/static/assets/images/localle_wireframes.png)

### Color Scheme
▷ In the initial design phase, we're rocking a grayscale palette to highlight content structure and nail that user experience. Once we've aced the UX research, we're bringing in accent colors to jazz up the design and make user interaction smoother.

![Color Scheme](https://github.com/mistersouza/localle/blob/main/static/assets/images/localle_color-scheme.png)

### Typography
▷ I'm on a mission to level up the site's flair and user experience by picking fonts that perfectly match our design and audience vibe.

![Roboto](https://github.com/mistersouza/localle/blob/main/static/assets/images/localle_font.png)

### Database 

▷ Check it out—the backstage of our database magic! This diagram reveals the intricate web of connections between our database models. It's a snapshot of simplicity and power. But hey, there's a deeper story to each model. Take a closer peek to unravel their secrets and see how they all come together!

![DBDiagram](https://github.com/mistersouza/localle/blob/main/static/assets/images/localle_dbdiagram.png)

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

## Toolbox Essentials

- [Gitpod](https://www.gitpod.io) - My trusty coding hangout for this project.
- [Git](https://git-scm.com/) - Keeping things organized with version control.
- [Github](https://github.com/) - Home to my precious code repository.
- [Heroku](https://dashboard.heroku.com/) - Where my deployed web app finds its cozy home.
- [Am I Responsive](http://ami.responsivedesign.is/) - My go-to for testing and capturing those sleek web page shots for different devices.
- [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Testing and fixing, one site glitch at a time.
- [w3 html validator](https://validator.w3.org/) -Making sure my HTML plays by the rules.
- [w3 css validator](https://jigsaw.w3.org/) - Keeping my style game sharp and error-free.
- [jshint](https://jshint.com/) -  Giving my JS code the thumbs-up after testing and validating.
- [Dead Link Checker](https://www.deadlinkchecker.com/website-dead-link-checker.asp) - Keeping those links alive and kicking.
- [DBDiagram](https://dbdiagram.io/) - The mastermind behind my DB models' cool diagrams.

## Deployment

### GitPod

▷ Getting your app ready

- Open up your settings.py file 
    - Setup databse
        ```python
        import dj_database_url

        DATABASES = {
            'default': dj_database_url.parse("<your Postrgres database URL>")
        }
        ```
    - Update settings.py in your Django app
        ```python
        DEBUG = False
        ```
    - Update Allowed Hosts
        ```python
        ALLOWED_HOSTS = ['.herokuapp.com', 'localhost']
        ```

- On the CL
    - Create a requirements. This file tells Heroku what your app needs to run smoothly.
        ```bash
        pip3 freeze --local > requirements.txt
        ```
    - Craft a Procfile. This tells Heroku how to run your app. Think of it as the main instruction manual.
        ```bash
        echo web: python app.py > Procfile
        ```
    - Shift models to ElephantSQL.
        ```bash
        python3 manage.py makemigrations
        python3 manage.py migrate
        ```

▷ The site first brewed up in GitPod and then landed in this remote [GitHub repository](https://github.com/mistersouza/localle.git).And let's talk GIT – the commands that made the magic real.

- **git status** >> It's like peeking into the project's mood board - shows any changes or new stuff.
- **git add --all** >> The "get ready to party" move - stages files for the big commit.
- **git commit -m " "** >> The official seal of approval - commits all the files.
- **git push** >> The grand finale - sends everything to the master branch up there on GitHub. Boom!

### Heroku 

▷ After all that hustle, it's time to set this project free in the wild, wild web world. Let it spread its wings and conquer the digital realm! 

- Started fresh on Heroku and gave our app a European vibe.
- Swiped right for GitHub as our deployment wingman.
- Dropped in some super-secret config vars for that behind-the-scenes magic. Check out the cool settings
![Config Vars](https://github.com/mistersouza/localle/blob/main/static/assets/images/localle_heroku-vars.png)
- Finally hit that deploy button and let the awesomeness unfold

## Credits

▷ Sure, I've been the lone wolf, architecting this whole thing—planning, designing, and coding away. But truth be told, I owe a lot to the squad that's had my back. And you know what? I wouldn't have it any other way. The teamwork vibe in coding is what makes this journey epic, and I'm all about embracing that collaborative spirit. Cheers to coding camaraderie!

### Inpired by

- Code With Stein [ Online Marketplace ](https://youtu.be/ZxMB6Njs3ck?si=PwGJLUVuzSV4XKiB)
- Code Institute's [I Think Therefore I Blog ](https://github.com/mistersouza/django-blog.git)

### Thanks

- David Calikes, Code Institute Cohort Facilitator.
  - Positive and Uplifting. David's Always available and boosts my confidence time we chat.
- Oluwafemi Medale, Code Institute Mentor.
  - Bugs terminator. He always make times, when there's no time at all.
- Chat GPT, Mister know it all.
  - Documenting King. Not always correct, but frequently inspiring.