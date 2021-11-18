
from django.db import models

# Create your models here.
class TodoItem(models.Model):
  content = models.TextField()

class Colaborador(models.Model):
  nome = models.CharField("Nome", max_length=100)
  funcao = models.CharField("Função", max_length=100)
  foto = models.ImageField("Foto", width_field=200)
  class Meta:
      verbose_name = "Colaborador"
      verbose_name_plural = "Colaboradores"

class Duvida(models.Model):
  pergunta = models.TextField("Pergunta")
  resposta = models.TextField("Resposta")
  ordem = models.IntegerField("Ordem",default=0)

  def __str__(self):
      return str(self.pergunta)
  class Meta:
      verbose_name = "Dúvida frequente"
      verbose_name_plural = "Dúvidas frequentes"

class Pais(models.Model):
  nome = models.CharField("Nome", max_length=100)
  def __str__(self):
      return self.nome
  class Meta:
      verbose_name = "País"
      verbose_name_plural = "Países"
  
class Estado(models.Model):
  nome = models.CharField("Nome", max_length=100)
  pais = models.ForeignKey('Pais', on_delete=models.PROTECT, verbose_name="Pais")
  def __str__(self):
      return self.nome
  class Meta:
      verbose_name = "Estado"
      verbose_name_plural = "Estados"

class Cidade(models.Model):
  nome = models.CharField("Nome", max_length=100)
  estado = models.ForeignKey('Estado', on_delete=models.PROTECT, verbose_name="Estado")
  def __str__(self):
      return self.nome
  class Meta:
      verbose_name = "Cidade"
      verbose_name_plural = "Cidade"

class Bairro(models.Model):
  nome = models.CharField("Nome", max_length=100)
  cidade = models.ForeignKey('Cidade', on_delete=models.PROTECT, verbose_name="Cidade")
  def __str__(self):
      return self.nome
  class Meta:
      verbose_name = "Bairro"
      verbose_name_plural = "Bairro"


class Profissional(models.Model):
  nome = models.CharField("Nome", max_length=255)
  email = models.CharField("E-mail", max_length=100)
  apelido = models.CharField("Apelido", max_length=100, null=True)
  telefone = models.CharField("Telefone", max_length=100)
  dataNascimento = models.DateField("Data de Nascimento", null=True)
  tempoProfissao = models.CharField("Tempo como profissional de limpeza", max_length=100, null=True)
  assuntoConversa = models.TextField ("Sobre o que gosta de conversar")
  habilidadeDestaque = models.CharField("Habilidades em destaque", max_length=100, null=True)
  mensagemClientes = models.TextField ("Mensagem para clientes")
  hobbie = models.CharField("O que gosta de fazer fora do trabalho", max_length=100, null=True)
  banco = models.CharField("Banco para depósito", max_length=100, null=True)
  agencia = models.CharField("Agência para depósito", max_length=100, null=True)
  pix = models.CharField("PIX para depósito", max_length=100, null=True)
  senha = models.CharField("Senha", max_length=100)
  cpf = models.CharField("CPF", max_length=100)
  cep = models.CharField("CEP", max_length=100)
  endereco = models.CharField("Endereço", max_length=100)
  complemento = models.CharField ("Complemento", max_length=100, null=True )
  termosCondicoes = models.BooleanField("Termos e Condições")
  politicaPrivacidade = models.BooleanField("Política de Privacidade")
  cidade = models.ForeignKey('Cidade', on_delete=models.PROTECT, verbose_name="Cidade", null=True)
  estado = models.ForeignKey('Estado', on_delete=models.PROTECT, verbose_name="Estado", null=True)
  bairro = models.ForeignKey('Bairro', on_delete=models.PROTECT, verbose_name="Bairro", null=True)

class Usuario(models.Model):
  nome = models.CharField("Nome", max_length=255)
  sobrenome = models.CharField("Sobrenome", max_length=255, null=True)
  email = models.CharField("E-mail", max_length=100)
  apelido = models.CharField("Apelido", max_length=100, null=True)
  telefone = models.CharField("Telefone", max_length=100)
  dataNascimento = models.DateField("Data de Nascimento", null=True)
  senha = models.CharField("Senha", max_length=100)
  cpf = models.CharField("CPF", max_length=100)
  endereco = models.CharField("Endereço", max_length=100)
  complemento = models.CharField ("Complemento", max_length=100, null=True )
  pontoReferencia = models.CharField("Ponto de referência", max_length=100, blank=True)
  pets = models.BooleanField("Pets", default=False)
  termosCondicoes = models.BooleanField("Termos e Condições")
  politicaPrivacidade = models.BooleanField("Política de Privacidade")
  cidade = models.ForeignKey('Cidade', on_delete=models.PROTECT, verbose_name="Cidade", null=True)
  estado = models.ForeignKey('Estado', on_delete=models.PROTECT, verbose_name="Estado", null=True)
  bairro = models.ForeignKey('Bairro', on_delete=models.PROTECT, verbose_name="Bairro", null=True)
def __str__(self):
      return self.nome
class Meta:
      verbose_name = "Usuário"
      verbose_name_plural = "Usuários" 

class Agendamento(models.Model):
  data = models.DateField("Data")
  horario = models.TimeField ("Horário do serviço")
  duracaoServico = models.FloatField('Tempo de serviço', null=True)
  horas = models.IntegerField('Horas de serviço')
  minutos = models.IntegerField('Minutos de serviço')
  instrucoes = models.TextField('Instruções')
  quemRecebera = models.TextField('Quem receberá')
  incluirProduto = models.BooleanField("Incluir produtos")
  usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT, verbose_name="Usuário", null=True)
  profissional = models.ForeignKey('Profissional', on_delete=models.PROTECT, verbose_name="Profissional", null=True)
  def __str__(self):
      return self.nome
  class Meta:
      verbose_name = "Agendamento"
      verbose_name_plural = "Agendamento"
    
class Avaliacao(models.Model):
  nome = models.CharField("Nome", max_length=100)
  texto = models.TextField("Texto")
  nota = models.IntegerField ("Nota")
  def __str__(self):
      return self.nome
  class Meta:
      verbose_name = "Bairro"
      verbose_name_plural = "Bairro"

class Depoimento(models.Model):
  nome = models.CharField("Nome", max_length=100)
  resposta = models.TextField("Resposta")
  def __str__(self):
      return self.nome
  class Meta:
      verbose_name = "Depoimento"
      verbose_name_plural = "Depoimentos"
  