 def _init_(self):
    self.primero = None

  def insertar(self, receta):
    if self.primero is None:
      self.primero = nodo(receta = receta)
      return
    actual = self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo(receta = receta)

  def recorrer(self):
    actual = self.primero

    while actual != None:
      print("Paciente: ", actual.receta.paciente, 
            "| Fecha de nacimiento: ", actual.receta.fecha_nac,
            "| Doctor: ", actual.receta.doctor,
            "| Colegiado: ", actual.receta.colegiado,
            "| Fecha de cita: ", actual.receta.fecha_cita,
            "| Hora cita: ", actual.receta.hora_cita,
            "| Tipo de consulta: ", actual.receta.tipo_consulta,
            "| Tratamiento: ", actual.receta.tipo_consulta)
      
      actual = actual.siguiente
  
  def eliminar(self, colegiado, fecha_cita, hora_cita):
    actual = self.primero
    anterior = None

    while actual != None and actual.receta.colegiado != colegiado and actual.receta.fecha_cita != fecha_cita and actual.receta.hora_cita != hora_cita:
      anterior = actual
      actual = actual.siguiente
    
    if anterior is None:
      self.primero = actual.siguiente
      actual.siguiente = None
    elif actual:
      anterior.siguiente = actual.siguiente
      actual.siguiente = None
    
  def modificar(self, colegiado, fecha_cita, hora_cita, nueva_fecha_cita, nueva_hora_cita):
    actual = self.primero

    while actual != None and actual.receta.colegiado != colegiado and actual.receta.fecha_cita != fecha_cita and actual.receta.hora_cita != hora_cita:
        actual = actual.siguiente 
        
r1 = receta("Gerson López", "03-10-1990", "Melvin Ortiz", 20156,
            "17-01-2023", "11:30", "Medicina general",
            "2 pildoras de acetaminofén cada 6 horas")

r2 = receta("Karen Gómez", "08-05-2000", "Jorge Merida", 8567,
            "31-01-2023", "09:00", "Medicina interna",
            "Tylenol de 20 ml cada 4 horas")

r3 = receta("Luis García", "17-09-1987", "Melvin Ortiz", 20156, 
            "02-02-2023", "12:00", "Medicina general",
            "2 cucharadas de Pepto-Bismol cada hora hasta que la diarrea desaparezca")

     
#Inserción


lista_e = lista_enlazada()
lista_e.insertar(r1)
lista_e.insertar(r2)
lista_e.insertar(r3)
     
#Recorrer


lista_e.recorrer()
     
Paciente:  Gerson López | Fecha de nacimiento:  03-10-1990 | Doctor:  Melvin Ortiz | Colegiado:  20156 | Fecha de cita:  17-01-2023 | Hora cita:  11:30 | Tipo de consulta:  Medicina general | Tratamiento:  Medicina general
Paciente:  Karen Gómez | Fecha de nacimiento:  08-05-2000 | Doctor:  Jorge Merida | Colegiado:  8567 | Fecha de cita:  31-01-2023 | Hora cita:  09:00 | Tipo de consulta:  Medicina interna | Tratamiento:  Medicina interna
Paciente:  Luis García | Fecha de nacimiento:  17-09-1987 | Doctor:  Melvin Ortiz | Colegiado:  20156 | Fecha de cita:  02-02-2023 | Hora cita:  12:00 | Tipo de consulta:  Medicina general | Tratamiento:  Medicina general

#Eliminar


lista_e.eliminar(20156,"17-01-2023", "11:30")
     

lista_e.recorrer()
     
Paciente:  Karen Gómez | Fecha de nacimiento:  08-05-2000 | Doctor:  Jorge Merida | Colegiado:  8567 | Fecha de cita:  31-01-2023 | Hora cita:  09:00 | Tipo de consulta:  Medicina interna | Tratamiento:  Medicina interna
Paciente:  Luis García | Fecha de nacimiento:  17-09-1987 | Doctor:  Melvin Ortiz | Colegiado:  20156 | Fecha de cita:  02-02-2023 | Hora cita:  12:00 | Tipo de consulta:  Medicina general | Tratamiento:  Medicina general

lista_e.modificar(8567, "31-01-2023", "09:00", "1-02-2023", "10:00")
lista_e.modificar(20156, "02-02-2023", "12:00", "03-03-2023", "14:00")
     

lista_e.recorrer()
     
Paciente:  Karen Gómez | Fecha de nacimiento:  08-05-2000 | Doctor:  Jorge Merida | Colegiado:  8567 | Fecha de cita:  1-02-2023 | Hora cita:  10:00 | Tipo de consulta:  Medicina interna | Tratamiento:  Medicina interna
Paciente:  Luis García | Fecha de nacimiento:  17-09-1987 | Doctor:  Melvin Ortiz | Colegiado:  20156 | Fecha de cita:  03-03-2023 | Hora cita:  14:00 | Tipo de consulta:  Medicina general | Tratamiento:  Medicina general
