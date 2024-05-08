GENDERS = [
    (0, 'Masculino'),
    (1, 'Feminino'),
    (2, 'Outros')
]

MARITAL_STATUS = [
    (0, 'Casado(a)'),
    (1, 'Reside com companheiro(a) / Namorado(a)'),
    (2, 'Solteiro(a)'),
    (3, 'Viúvo(a)'),
    (4, 'Divorciado(a)')
]

CLIENT_RELATION = [
    (0, 'O próprio'),
    (1, 'O próprio com CRV em transferência'),
    (2, 'Cônjuge/Companheiro(a)'),
    (3, 'Pai/Mãe'),
    (4, 'Filho(a)/Enteado(a)'),
    (5, 'Condutor indeterminado'),
    (6, 'Outros')
]

EXTENDED_COVERAGES = [
    (0, 'Sim, porém são maiores que 24 anos e menores que 26 anos.'),
    (1, 'Não tem condutores menores de 26 anos.'),
    (2, 'Sim, e são menores de 24 anos.'),
    (3, 'Sim, porém não dirige o veículo'),
    (4, 'Não'),
]

USE_TYPES = [
    (0, 'Particular (locomoção diária)'),
    (1, 'Particular (somente para lazer)'),
    (2, 'Utilizado para visitas ou representação comercial'),
    (3, 'Utilizado para transporte de passageiros'),
    (4, 'Utilizado para entregas')
]

LIVE_IN = [
    (0, 'Casa/Sobrado'),
    (1, 'Apartamento'),
    (2, 'Condomínio de Casas'),
    (3, 'Outros')
]

STORAGE_IN = [
    (0, 'Sim, com portão manual'),
    (1, 'Sim, com portão automático'),
    (2, 'Sim, em estacionamento privado ou pago'),
    (3, 'Não')
]

IS_TO_WORK = [
    (0, 'Sim'),
    (1, 'Não'),
    (2, 'Não trabalha')
]

IS_TO_COLLEGE = [
    (0, 'Sim, Ensino Médio'),
    (1, 'Sim, Ensino Superior'),
    (2, 'Sim, Pós-Graduação'),
    (3, 'Sim, Outros'),
    (4, 'Estuda mas não utiliza o veículo'),
    (5, 'Não estuda')
]

class DataModel:
    def __init__(self, message_title='', message_text=''):

        self.data = {
            'has_message': False,
            'message_title': 'Operação inválida',
            'message_text': 'Verifique se todas as entradas de dados estão corretas e tente novamente'
        }

        if message_title != '' or message_text != '':
            self.data['message_title'] = message_title
            self.data['message_text'] = message_text

    def SetItem(self, key, value):
        self.data[key] = value

    def GetData(self):
        return self.data