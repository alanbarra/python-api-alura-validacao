from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "O CPF é inválido"})

        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Não inclua números no campo nome"})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve conter 9 dígitos"})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "O Celular deve estar no formato (XX) XXXX-XXXX"})
        
        return data