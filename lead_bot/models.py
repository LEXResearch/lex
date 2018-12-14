from django.db import models

#modelos de textos para serem utilizados
class LeadModel(models.Model):
    description = models.TextField()

#assuntos trados no texto
class Subject(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

#noticias geradas
class LeadGerated(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    description = models.TextField()
    id_from_manancial = models.IntegerField()
    type_choices = (
        ('d', 'Dissertação'),
        ('t', 'Tese'),
        ('o', 'Outro'),
    )
    type = models.CharField(max_length=1, choices=type_choices)
    lead_model = models.ForeignKey(LeadModel, null=True, on_delete=models.SET_NULL)
    advisor = models.CharField(max_length=150)
    program = models.CharField(max_length=150)
    subjects = models.ManyToManyField(Subject, verbose_name="list of subjects")
    published = models.DateField()
