from django.contrib import admin

# Register your models here.

from .models import Duvida
from .models import Colaborador
from .models import Pais
from .models import Estado
from .models import Cidade
from .models import Bairro
from .models import Usuario
from .models import Agendamento
from .models import Depoimento
from .models import Avaliacao

admin.site.register(Duvida)
admin.site.register(Colaborador)
admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(Usuario)
admin.site.register(Agendamento)
admin.site.register(Depoimento)
admin.site.register(Avaliacao)