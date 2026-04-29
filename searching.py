# Implementación de algoritmos de búsqueda

# Definimos una función llamada linear_search.
# Recibe una lista llamada arr y un número entero llamado target.
# Devuelve un número entero, que será la posición donde se encontró el dato.
def linear_search(arr: list, target: int) -> int:

    # Recorre la lista desde la posición 0 hasta la última posición.
    for i in range(len(arr)):

        # Verifica si el elemento en la posición i es igual al valor que buscamos.
        if arr[i] == target:

            # Si encuentra el valor, devuelve la posición donde está.
            return i

    # Si termina de recorrer toda la lista y no encuentra el valor, devuelve -1.
    return -1


# Definimos una función llamada binary_search.
# Recibe una lista llamada arr y un número entero llamado target.
# Devuelve un número entero, que será la posición donde se encontró el dato.
# Importante: para que funcione bien, la lista debe estar ordenada.
def binary_search(arr: list, target: int) -> int:

    # Define el límite inferior de búsqueda, empezando en la primera posición.
    low = 0

    # Define el límite superior de búsqueda, empezando en la última posición.
    high = len(arr) - 1

    # Mientras el límite inferior no se pase del límite superior,
    # todavía hay elementos donde buscar.
    while low <= high:

        # Calcula la posición del medio entre low y high.
        mid = (low + high) // 2

        # Verifica si el elemento del medio es igual al valor buscado.
        if arr[mid] == target:

            # Si lo encuentra, devuelve la posición del elemento.
            return mid

        # Si el elemento del medio es menor que el valor buscado,
        # significa que debemos buscar en la mitad derecha.
        elif arr[mid] < target:

            # Mueve el límite inferior una posición después del medio.
            low = mid + 1

        # Si el elemento del medio es mayor que el valor buscado,
        # significa que debemos buscar en la mitad izquierda.
        else:

            # Mueve el límite superior una posición antes del medio.
            high = mid - 1

    # Si el ciclo termina y no se encontró el valor, devuelve -1.
    return -1