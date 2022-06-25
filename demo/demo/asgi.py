import os

from configurations.asgi import get_asgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Demo")

application = get_asgi_application()
