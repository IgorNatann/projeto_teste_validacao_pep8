import secrets

# Probabilidades "reais" de sucesso de cada braco (o algoritmo nao sabe isso)
prob_reais = [0.2, 0.5, 0.8]

# Estimativas do algoritmo
tentativas = [0, 0, 0]
media_recompensa = [0.0, 0.0, 0.0]

epsilon = 0.1  # 10% das vezes explora aleatoriamente
rodadas = 200
ESCALA = 10_000


def random_unit():
    """Retorna um float pseudo-uniforme no intervalo [0, 1)."""
    return secrets.randbelow(ESCALA) / ESCALA


def puxar_braco(i):
    """Retorna 1 (sucesso) ou 0 (falha) baseado na prob real."""
    return 1 if random_unit() < prob_reais[i] else 0


for _ in range(rodadas):
    # Escolha: explorar ou aproveitar o melhor ate agora
    if random_unit() < epsilon:
        braco = secrets.randbelow(len(prob_reais))  # explora
    else:
        braco = max(
            range(len(prob_reais)), key=lambda i: media_recompensa[i]
        )  # explota

    recompensa = puxar_braco(braco)

    # Atualiza media incremental
    tentativas[braco] += 1
    n = tentativas[braco]
    media_recompensa[braco] += (recompensa - media_recompensa[braco]) / n

print("Tentativas por braco:", tentativas)
print("Media estimada por braco:", [round(x, 3) for x in media_recompensa])
print(
    "Melhor braco (estimado):",
    max(range(len(prob_reais)), key=lambda i: media_recompensa[i]),
)
