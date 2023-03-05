def está_explorado(t, inicio, fin):
   
    segmentos = obtener_segmentos(t, inicio, fin)

   
    for segmento in segmentos:
        if no_está_explorado(segmento):
            return False

    return True


def obtener_segmentos(t, inicio, fin):
    
    segmentos = []
    i = inicio

    while i <= fin:
        j = i + 1
        while j <= fin and t[j] >= t[j-1]:
            j += 1
        segmentos.append(t[i:j])
        i = j

    return segmentos


def no_está_explorado(segmento):
    
    if len(segmento) <= 1:
        return False
    maximo = max(segmento)
    return maximo != segmento[0]
