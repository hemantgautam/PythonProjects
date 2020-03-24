from django.shortcuts import render


# Create your views here.
def myresume(request):
    pro_skills = {"Python3, Django, Rest Framework": "75",
                  "Python Web Scraping ": "70",
                  "PHP, Drupal 6,7,8": "70",
                  "Acquia, Pantheon, Bit Bucket, GIT, SVN, Heroku": "80",
                  "SQLite, MySQL, MongoDB, PostgreSQL": "60",
                  "CSS, HTML, jQuery, Bootstrap": "75"}

    personal_skills = {"Leadership ": "85",
                       "Proactive Team Member": "80",
                       "Communication": "85",
                       "Good at Problem Solving": "90",
                       "Ability to Work Under Pressure": "95"}

    interests = ['Fitness Freak', 'Guitar', 'Swimming', 'Squash', 'Travelling']
    return render(request, 'index.html',
                  {'pro_skills': pro_skills, 'personal_skills': personal_skills, 'interests': interests})
