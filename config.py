SECRET_KEY = 'jdofhjfmjcunhfuijhguifh'

# Flask-Mail
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'patrickpwiiliamson9@gmail.com'
MAIL_PASSWORD = 'Olayinka1'

#celery configuration 
CELERY_BROKER_URL = "redis://:olayinka@redis:6379/0" 
CELERY_RESULT_BACKEND = "redis://:olayinka@redis:6379/0" 