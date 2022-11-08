AUTHOR = 'Carlos Carrasco Varas'
SITENAME = 'Blog del desarrollador latinoamericano'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Santiago'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DATE_FORMATS = { "es": "%d-%m-%Y"}

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Krlitos_Forever'),
          ('LinkedIn', 'https://www.linkedin.com/in/mg-carlos-carrasco/'),
          ('GitHub','https://github.com/KrlitosForever'),)

# Social-Links
GITHUB_URL = 'https://github.com/KrlitosForever'
TWITTER_URL = 'https://twitter.com/Krlitos_Forever'
FACEBOOK_URL = 'https://www.linkedin.com/in/mg-carlos-carrasco/'

DEFAULT_PAGINATION = 10

TAGS = ()
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

OUTPUT_PATH = 'docs/'
THEME = 'gum'
