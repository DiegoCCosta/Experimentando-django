from django.contrib import admin
from .models import Cargo, Funcionario,Servico,Features
# Register your models here.

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativos', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'ativos', 'icone', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativos', 'cargo', 'modificado')


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('feature', 'descricao', 'icone')
