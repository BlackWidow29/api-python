from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'msg': 'Pessoa não encontrada'
            }
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

    def delete(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            status = 'success'
            msg = 'Pessoa {} excluída com sucesso'.format(pessoa.nome)
            pessoa.delete()
        except AttributeError:
            status = 'error'
            msg = 'Nome {} não encontrado'.format(nome)

        return jsonify({'status': status, 'mensagem': msg})


class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id,'nome':i.nome,'idade':i.idade} for i in pessoas]
        return  jsonify(response)
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


class ListaAtividades(Resource):
    def get(self):
        ativdades = Atividades.query.all()
        response = [{'id': i.id,'nome':i.nome, 'pessoa': i.pessoa.nome} for i in ativdades]
        return  jsonify(response)

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'atividade': atividade.nome,
            'id': atividade.id
        }
        return jsonify(response)


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)