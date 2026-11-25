from enum import Enum

class Estado(Enum):
    M = "M"
    E = "E"
    S = "S"
    I = "I"

class Linha:
    def __init__(self):
        self.tag = None
        self.estado = Estado.I
        



class Memoria:

    def __init__(self):
        self.writebacks = 0
class Bus:

    def __init__(self, memoria):
        self.memoria = memoria
        self.processadores = []
        self.transacao = None
        self.instrucao_processador = None
        self.instrucao_tipo = None
        self.instrucao_endereco = None


    def instrucao(self, processador, tipo, endereco):
        self.instrucao_processador = processador
        self.instrucao_tipo = tipo
        self.instrucao_endereco = endereco

        if tipo == "W":
            self.processadores[processador].escrever(endereco)
        else:
            self.processadores[processador].ler(endereco)

    def snoop(self, origem, transacao, endereco):
        resultado = {
            "tinha_copia": False,
            "writeback": False,
            "cache_to_cache": False,
            "transicoes": [],
        }

        for i, cache in enumerate(self.processadores):
            if i == origem:
                continue
            tag, indice = cache.decompor(endereco)
            linha = cache.linhas[indice]

            if linha.tag != tag or linha.estado == Estado.I:
                continue

            resultado["tinha_copia"] = True
            antigo = linha.estado

            if transacao == "BusRd":
                if antigo == Estado.M:
                    resultado["writeback"] = True
                    self.memoria.writebacks += 1
                if antigo in (Estado.M, Estado.E):
                    resultado["cache_to_cache"] = True
                linha.estado = Estado.S

            else:
                if antigo == Estado.M:
                    resultado["writeback"] = True
                    self.memoria.writebacks += 1
                    if transacao == "BusRdX":
                        resultado["cache_to_cache"] = True
                linha.estado = Estado.I

            resultado["transicoes"].append(f"Core {i}: {antigo.value} -> {linha.estado.value}")

        return resultado