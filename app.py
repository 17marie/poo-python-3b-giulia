class Conteudo:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero
        def exibir_info(self):
                print("Título:", self.titulo)
                print("Gênero:", self.genero)

class Filme(Conteudo):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo, genero)
        self.duracao = duracao

    def exibir_info(self):
        print("Título:", self.titulo)
        print("Gênero:", self.genero)
        print("Duração:", self.duracao)


class Serie(Conteudo):
    def __init__(self, titulo, genero, temporadas):
        super().__init__(titulo, genero)
        self.temporadas = temporadas

    def exibir_info(self):
        print("Título:", self.titulo)
        print("Gênero:", self.genero)
        print("Temporadas:", self.temporadas)

class Documentario(Conteudo):
    def __init__(self, titulo, genero, tema):
        super().__init__(titulo, genero)
        self.tema = tema

    def exibir_info(self):
            print("Título:", self.titulo)
            print("Gênero:", self.genero)
            print("Tema:", self.tema)


class Podcast(Conteudo):
    def __init__(self, titulo, genero, episodios):
        super().__init__(titulo, genero)
        self.episodios = episodios

    def exibir_info(self):
            print("Título:", self.titulo)
            print("Gênero:", self.genero)
            print("Episódios:", self.episodios)





catalogo = [
Filme("Interestelar", "Ficcao", 169),
Filme("Shrek", "Animacao", 90),
Serie("Stranger Things", "Ficcao", 4),
Serie("Round 6", "Suspense", 2),
Documentario("Nosso Planeta", "Natureza", "Vida selvagem"),
Podcast("Almoço","Comida", 10)
]

for item in catalogo:
     item.exibir_info()

# TE AMO PAVLOVIC <3
