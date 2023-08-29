def jerigonzo(oracion):
    oracion = oracion.replace('a', 'apa').replace('e', 'epe').replace('i', 'ipi').replace('o', 'opo').replace('u',
                                                                                                              'upu')
    oracion = oracion.replace('A', 'Apa').replace('E', 'Epe').replace('I', 'Ipi').replace('O', 'Opo').replace('U',
                                                                                                              'Upu')
    oracion = oracion.replace('á', 'ápa').replace('é', 'épe').replace('í', 'ípi').replace('ó', 'ópo').replace('ú',
                                                                                                              'úpu')
    oracion = oracion.replace('Á', 'Ápa').replace('É', 'Épe').replace('Í', 'Ípi').replace('Ó', 'Ópo').replace('Ú',
                                                                                                              'Úpu')
    return oracion
         