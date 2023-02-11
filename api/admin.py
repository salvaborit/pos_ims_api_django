from django.contrib import admin
from .models import Terminal
from .models import Acquirer
from .models import Model
from .models import Location
from .models import Status
from .models import Connectivity

admin.site.register(Terminal)
admin.site.register(Acquirer)
admin.site.register(Model)
admin.site.register(Location)
admin.site.register(Status)
admin.site.register(Connectivity)
