import numpy as np
import matplotlib.pyplot as plt
import time

def read_metadata_file(filename):
    """
    Llegeix un fitxer de metadades tipus 'clau : valor' i
    retorna un diccionari amb la informació.
    """
    metadata = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or ':' not in line:
                continue
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            if value.isdigit():
                value = int(value)
            else:
                try:
                    value = float(value)
                except ValueError:
                    pass

            metadata[key] = value

    return metadata


# ---------------------------------------------------------------------
# 1. Llegim el fitxer de metadades
# ---------------------------------------------------------------------
filename = "Initialize (1).doc"
info = read_metadata_file(filename)

# Mostrem la informació llegida:
print("Dades llegides del fitxer:")
for k, v in info.items():
    print(f"{k} = {v}")

# ---------------------------------------------------------------------
# 2. Obtenim rows i cols del diccionari de metadades
# ---------------------------------------------------------------------
# Podem fer servir 'rows' i 'columns' per a definir la mida del nostre grid
# (Assegura't que el fitxer conté aquestes claus exactes: "rows" i "columns")
rows = info.get('rows', 10)      # Si no troba 'rows', usa 10 per defecte
cols = info.get('columns', 1)   # Si no troba 'columns', usa 10

print(f"-> Configuració de la simulació: grid de {rows} x {cols}")

# ---------------------------------------------------------------------
# 3. Preparem les nostres matrius segons la mida llegida
# ---------------------------------------------------------------------
# EXEMPLE: assignem valors aleatoris per a la humitat i la vegetació
humidity = np.random.randint(low=1, high=3,  size=(rows, cols))   # 1..2 hores de retard
vegetation = np.random.randint(low=5, high=15, size=(rows, cols)) # 5..14 hores de cremada

# ---------------------------------------------------------------------
# 4. Matriu d’estats de l’incendi
#    0 = pendent, 1 = cremant, 2 = cremat
# ---------------------------------------------------------------------
state = np.zeros((rows, cols), dtype=int)

# ---------------------------------------------------------------------
# 5. Contadors associats a cada cel·la
# ---------------------------------------------------------------------
humidity_counter = humidity.copy()
burn_counter = np.zeros((rows, cols), dtype=int)

# ---------------------------------------------------------------------
# 6. Inicialitzem un focus de foc, per exemple al centre de la matriu
# ---------------------------------------------------------------------
start_r = rows // 2
start_c = cols // 2
state[start_r, start_c] = 1
burn_counter[start_r, start_c] = vegetation[start_r, start_c]

# ---------------------------------------------------------------------
# 7. Funció per obtenir els veïns (veïnatge de Moore)
# ---------------------------------------------------------------------
def get_neighbors(r, c, max_r, max_c):
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            rr = r + dr
            cc = c + dc
            if 0 <= rr < max_r and 0 <= cc < max_c:
                neighbors.append((rr, cc))
    return neighbors

# ---------------------------------------------------------------------
# 8. Un pas de simulació
# ---------------------------------------------------------------------
def step_fire(state, humidity_counter, burn_counter, vegetation):
    """
    state            : matriu d'estats (0,1,2)
    humidity_counter : nombre d’hores que encara falta per “encendre’s” la cel·la
    burn_counter     : nombre d’hores que li queda cremant-se fins a quedar cremada
    vegetation       : valor fix que indica el temps total de cremada (per a cada cel·la)
    """
    rows, cols = state.shape

    # Preparem còpies per fer l'actualització sincrònica
    new_state    = state.copy()
    new_humidity = humidity_counter.copy()
    new_burn     = burn_counter.copy()

    for r in range(rows):
        for c in range(cols):
            if state[r, c] == 0:  # Pendent de cremar-se
                # Si algun veí està cremant, anem reduint la humitat
                neighbors = get_neighbors(r, c, rows, cols)
                # Comprovem si com a mínim un veí és "1" (cremant-se)
                if any(state[nr, nc] == 1 for (nr, nc) in neighbors):
                    if new_humidity[r, c] > 0:
                        new_humidity[r, c] -= 1

                    # Si la humitat ja ha arribat a 0, la cel·la s'encén
                    if new_humidity[r, c] <= 0:
                        new_state[r, c] = 1
                        new_burn[r, c]  = vegetation[r, c]

            elif state[r, c] == 1:  # En procés de cremar-se
                # Reduïm el burn_counter
                if new_burn[r, c] > 0:
                    new_burn[r, c] -= 1

                # Si s'ha consumit tota la vegetació, estat=CREMAT
                if new_burn[r, c] <= 0:
                    new_state[r, c] = 2

            # Si és 2 (CREMAT), no fem res més

    return new_state, new_humidity, new_burn

# ---------------------------------------------------------------------
# 9. Bucle principal de simulació
# ---------------------------------------------------------------------
num_steps = 20  # fem 20 passos de simulació

for t in range(num_steps):
    # Actualitzem l'estat del foc
    state, humidity_counter, burn_counter = step_fire(
        state,
        humidity_counter,
        burn_counter,
        vegetation
    )

    # Mostrem la simulació (opcional) per veure'n l'evolució
    plt.figure()
    plt.imshow(state, cmap='hot', vmin=0, vmax=2)
    plt.title(f"Time step = {t}")
    plt.colorbar(label="Estat de la cel·la (0=pendent, 1=cremant, 2=cremat)")
    plt.show()

    # Petita pausa entre passos, si ho desitges
    time.sleep(0.5)
