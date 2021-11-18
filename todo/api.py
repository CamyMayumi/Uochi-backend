
from rest_framework import routers, serializers, viewsets, mixins
from todo.models import Duvida, Usuario, Agendamento, Cidade, Estado, Bairro

# Serializers define the API representation.
class DuvidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duvida
        fields = ['pergunta', 'resposta']

# ViewSets define the view behavior.
class DuvidaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Duvida.objects.all().order_by("-ordem","pergunta")
    serializer_class = DuvidaSerializer

# Serializers define the API representation.
class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = ['id', 'nome']

# ViewSets define the view behavior.
class CidadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cidade.objects.all().order_by('nome')
    serializer_class = CidadeSerializer  

# Serializers define the API representation.
class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['id', 'nome']

# ViewSets define the view behavior.
class EstadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Estado.objects.all().order_by('nome')
    serializer_class = EstadoSerializer  

# Serializers define the API representation.
class BairroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bairro
        fields = ['id', 'nome']

# ViewSets define the view behavior.
class BairroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bairro.objects.all().order_by('nome')
    serializer_class = BairroSerializer  

#Cadastro
class CreateUsuarioSerializer(serializers.ModelSerializer):
    cidade: CidadeSerializer()
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'sobrenome', 'email', 'telefone', 'senha',
       'dataNascimento','senha','cpf','endereco', 'complemento','pontoReferencia','pets','termosCondicoes','politicaPrivacidade','cidade','estado','bairro']

class CreateUsuarioViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  serializer_class = CreateUsuarioSerializer   
  queryset = Usuario.objects.all()

#Agendamento
class CreateAgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ['data', 'horario', 'horas', 'minutos', 'duracaoServico','instrucoes','quemRecebera']

class CreateAgendamentoViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  serializer_class = CreateAgendamentoSerializer 
  queryset = Agendamento.objects.all()

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'duvidas', DuvidaViewSet)

router.register(r'usuarios-create', CreateUsuarioViewSet)
router.register(r'agendamentos-create', CreateAgendamentoViewSet)
router.register(r'cidades', CidadeViewSet)
router.register(r'estados', EstadoViewSet)
router.register(r'bairros', BairroViewSet)