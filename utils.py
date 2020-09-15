from models import Pessoas

def insere_pessoas():
    pessoas = Pessoas(nome='Isabelly',idade=19)
    print(pessoas)
    pessoas.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    #pessoa = Pessoas.query.filter_by(nome='Isabelly').first()
    print(pessoa)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Isabelly').first()
    pessoa.nome = 'Lucas'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Lucas').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()