from django.db import models

# Create your models here.
class TodoItem(models.Model):
  content = models.TextField()

class Colaborador(models.Model):
  nome = models.CharField("Nome", max_length=100)
  funcao = models.CharField("Função", max_length=100)
  foto = models.ImageField("Foto", width_field=200)

class Duvida(models.Model):
  pergunta = models.TextField("Pergunta")
  resposta = models.TextField("Resposta")

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