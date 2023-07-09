# primer-proyecto

Trabajo práctico número 3 - Giorgi 

Requerimientos básicos:
-Windows
-Python 3.11.13

1) Instalar las especificaciones del proyecto guardadas en el file requirements.txt corriendo el comando `pip install -r requirements.txt`.
2) Correr el comando `python manage.py makemigrations`, y luego `python manage.py migrate`, para migrar los modelos a la base de datos.
3) Ejecutar el comando `python manage.py runserver` e ir a la URL base del proyecto: http://localhost:8000/.
4) En la página de inicio se pueden ver  las siguientes opciones: Acerca de mi, Mensajes, Pokemons, Entrenadores, Gimnasios, Login y Registrarse.
5) En Acerca de mi se puede ver el motivo de creacion del proyecto.
6) Para poder acceder a las opciones de Pokemones, Entrenadores y Gimnasios, primero es necesario crearse un usuario en la opcion Registrarse. Al crear un usuario se le van a pedir las opciones: Nombre de usuario, Email, Contraseña y repetir la contraseña.
7)Una vez creado su usuario, automáticamente lo va a llevar a la pantalla de Login en donde debe ingresar su nombre de usuario y contraseña.
8) Una vez logueado, además de poder acceder a las opciones antes mencionadas, va a tener dos nuevas opciones: Su perfil (Cuyo boton se indica con el nombre de usuario) y Logout.
9) Con el boton de Logout, puede volver a la primera pantalla en donde se vuelven a aparecer las opciones de Login y Registrarse.
10) En la opcion de perfil, va a poder visualizar los datos de usuario y además tiene la opcion de Editar los datos.
11) En la opcion de editar los datos de su perfil, además de poder cambiar el mail que le fue requerido al registrarse, puede completar los siguientes: Nombre, Apellido, Lema Personal y Avatar.
12) A su vez, en esta pantalla tiene la opcion de Cambiar contraseña.
13) En la parte de Pokemons se puede ver el listado de los pokemons creados, así como crear uno nuevo en la opcion "Crear pokemon". Una vez creado el nuevo pokemon se puede optar por seguir creando o volver al listado. Por otra parte, con la opcion buscar se puede filtrar el listado con los parámetros deseados. 
El modelo Pokemon es la única clase de las 3 que esta hecha enteramente con clases basadas en vista, y además de los campos Nombre, Tipo y Evolicion (Charfields) cuenta con los campos Fecha de creacion(DateField), descripcion(RichField) e ícono (ImageField)
14) En la parte de Entrenadores se puede ver el listado de los entrenadores creados, así como crear uno nuevo en la opcion "Crear entrenador". Una vez creado el nuevo entrenador se puede optar por seguir creando o volver al listado. Por otra parte, con la opcion buscar se puede filtrar el listado con los parámetros deseados.
15) En la parte de Gimnasios se puede ver el listado de los gimnasios creados, así como crear uno nuevo en la opcion "Crear gimnasio". Una vez creado el nuevo gimnasio se puede optar por seguir creando o volver al listado. Por otra parte, con la opcion buscar se puede filtrar el listado con los parámetros deseados.
16) En la sección de mensajes los usuarios pueden dejar mensajes, que se veran en un listado al ingresar, indicandose el nombre del usuario que lo creo.