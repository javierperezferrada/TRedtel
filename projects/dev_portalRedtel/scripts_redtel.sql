SELECT user,T2.nombres, T2.apellidos,T2.FechaIngreso, T1.zonal, rut, T1.email, cargo
FROM usuarios T1
INNER JOIN tecnicos T2 ON T1.id = T2.idUsuario
