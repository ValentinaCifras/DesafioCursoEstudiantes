from app.models import Curso, Profesor, Estudiante, Direccion

def crear_curso(codigo,nombre,version):
    curso = Curso(
       codigo = codigo,
       nombre = nombre,
       version = version,
    )

    curso.save()
    return curso

def crear_profesor(rut, nombre, apellido, creado_por):
    profesor = Profesor(
        rut=rut, 
        nombre=nombre, 
        apellido=apellido, 
        creado_por=creado_por,
        )
    
    profesor.save()
    return profesor

def crear_estudiante(rut,nombre,apellido,fecha_nac,creado_por):
    estudiante = Estudiante(
        rut=rut, 
        nombre=nombre, 
        apellido=apellido, 
        fecha_nac=fecha_nac, 
        creado_por=creado_por
        )
    
    estudiante.save()
    return estudiante

def crear_direccion(calle, numero, depto, comuna, ciudad, region, estudiante):
    direccion = Direccion(
        calle=calle, 
        numero=numero, 
        depto=depto, 
        comuna=comuna, 
        ciudad=ciudad, 
        region=region, 
        estudiante_id=estudiante
        )
    
    direccion.save()
    return direccion

def obtiene_estudiante(rut):
    estudiante = Estudiante.objects.get(rut=rut)
    return estudiante

def obtiene_profesor(rut):
    profesor = Profesor.objects.get(rut=rut)
    return profesor

def obtiene_curso(codigo):
    curso = Curso.objects.get(codigo=codigo)
    return curso

def agrega_profesor_a_curso(rut,codigo):
    profesor = obtiene_profesor(rut=rut)
    curso = obtiene_curso(codigo=codigo)
    curso.profesores.add(profesor)
    curso.save()
    return curso

def agrega_cursos_a_estudiante(rut,codigo):
    estudiante = Estudiante.objects.get(rut=rut)
    curso = Curso.objects.get(codigo=codigo)
    curso.estudiantes.add(estudiante)
    curso.save()
    return curso

def imprime_estudiante_cursos(rut):
    estudiante = Estudiante.objects.get(rut=rut)
    print("Nombre del estudiante:", estudiante.nombre, estudiante.apellido)
    cursos = estudiante.curso.all()
    for curso in cursos:
        print("Curso:" + curso.nombre)
