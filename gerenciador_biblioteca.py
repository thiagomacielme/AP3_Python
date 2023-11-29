import json

class Livro:
    def __init__(self, titulo, autor, ano, genero, exemplares_disponiveis):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
        self.exemplares_disponiveis = exemplares_disponiveis

class SistemaDeGerenciamentoDeBiblioteca:
    def __init__(self):
        self.livros = {}

    def cadastrar_livro(self, livro):
        self.livros[livro.titulo] = livro

    def consultar_livro(self, titulo):
        if titulo in self.livros:
            livro = self.livros[titulo]
            print(f"Título: {livro.titulo}\nAutor: {livro.autor}\nAno: {livro.ano}\nGênero: {livro.genero}\nExemplares Disponíveis: {livro.exemplares_disponiveis}")
        else:
            print("Livro não encontrado.")

    def listar_livros_por_autor(self, autor):
        livros_do_autor = [livro for livro in self.livros.values() if livro.autor == autor]
        if livros_do_autor:
            for livro in livros_do_autor:
                print(f"{livro.titulo} - {livro.ano}")
        else:
            print("Nenhum livro encontrado para o autor especificado.")

    def listar_livros_por_genero(self, genero):
        livros_do_genero = [livro for livro in self.livros.values() if livro.genero == genero]
        if livros_do_genero:
            for livro in livros_do_genero:
                print(f"{livro.titulo} - {livro.autor}")
        else:
            print("Nenhum livro encontrado para o gênero especificado.")

    def salvar_dados(self, nome_arquivo="dados_biblioteca.json"):
        dados = {
            "livros": {livro.titulo: {"autor": livro.autor, "ano": livro.ano, "genero": livro.genero, "exemplares_disponiveis": livro.exemplares_disponiveis} for livro in self.livros.values()}
        }
        with open(nome_arquivo, "w") as arquivo:
            json.dump(dados, arquivo)

    def carregar_dados(self, nome_arquivo="dados_biblioteca.json"):
        try:
            with open(nome_arquivo, "r") as arquivo:
                dados = json.load(arquivo)
                for titulo, info in dados["livros"].items():
                    livro = Livro(titulo, info["autor"], info["ano"], info["genero"], info["exemplares_disponiveis"])
                    self.livros[titulo] = livro
            print("Dados carregados com sucesso.")
        except FileNotFoundError:
            print("Arquivo de dados não encontrado.")

# Exemplo de Uso:

# Criando instância do sistema de gerenciamento de biblioteca
biblioteca = SistemaDeGerenciamentoDeBiblioteca()

# Cadastrando alguns livros
livro1 = Livro("Python para Iniciantes", "John Smith", 2020, "Programação", 5)
livro2 = Livro("Algoritmos e Estruturas de Dados", "Maria Silva", 2018, "Programação", 3)
biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_livro(livro2)

# Consultando um livro
biblioteca.consultar_livro("Python para Iniciantes")

# Listando livros por autor
biblioteca.listar_livros_por_autor("John Smith")

# Listando livros por gênero
biblioteca.listar_livros_por_genero("Programação")

# Salvando dados
biblioteca.salvar_dados()

# Carregando dados
biblioteca.carregar_dados()