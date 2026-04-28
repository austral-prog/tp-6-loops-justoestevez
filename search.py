def index_of(target, lst):
    """Retorna el índice de la primera ocurrencia de target en lst, o -1."""
    # Usamos range(len(lst)) para tener el número del índice (i)
    for i in range(len(lst)):
        if lst[i] == target:
            return i  # Apenas lo encuentra, corta la función y devuelve el índice
            
    return -1  # Si salió del for sin encontrarlo, devuelve -1

def index_of_by_index(target, lst, start):
    """Retorna el índice de la primera ocurrencia a partir de start."""
    # El range empieza en 'start' en lugar de 0
    for i in range(start, len(lst)):
        if lst[i] == target:
            return i
            
    return -1

def index_of_empty(lst):
    """Retorna el índice del primer string vacío en lst, o -1."""
    for i in range(len(lst)):
        if lst[i] == "":  # Comparamos contra un string vacío
            return i
            
    return -1
