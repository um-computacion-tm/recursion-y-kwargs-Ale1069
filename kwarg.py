
def buscar_datos(*args, **kwargs):
    resultados = []
    for key, value in kwargs.items():
        persona = {}
        for k, v in value.items():
            if v in args:
                persona[k] = v
        if len(persona) == len(args):  
            resultados.append(persona)
    return resultados    

database = {
    "persona1": {"nombre1": "Pablo", "nombre2": "Diego", "apellido1": "Ruiz", "apellido2": "Picasso"},
    "persona2": {"nombre1": "Elio", "apellido1": "Anci"},
    "persona3": {"nombre1": "Elias", "nombre2": "Marcos", "nombre3": "Luciano", "apellido1": "Marcelo", "apellido2": "Gonzalez"}
}


resultado = buscar_datos("Elio", "Anci", **database) 
print(resultado)  


