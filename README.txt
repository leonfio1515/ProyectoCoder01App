Vista simple de web con redireccionamiento de url

url de ingreso - localhost/AppCoder (Pagina de inicio)

Dentro de la pagina de inicio:

Todos los botones son funcionales.
Cuenta con un navbar funcional, el cual redirige a la url que corresponda y devuelve informacion realacionada a la misma
Toda la informacion mostrada tanto texto como img, es leida desde la BBDD
Se añadieron templates de bootstrap con distintos modelos y se agregaron adicionales como imagenes.
Los formularios son funcionales, solo queda pendiente realizar el submit con la BBDD
Segun la consigna de la clase pasada:

Se creo un total de 6 cursos - de los cuales se muestran los 3 primeros en la pantalla de inicio mediante un slide
Se crearon 3 alumnos de los cuales se muestra informacion en la pestaña correspondiente
Se crearon 4 profesores, de los cuales se muestra informacion e imagen de perfil
Dentro de la pagina de Inicio, en el boton de "Conocer mas" muestra 3 noticias del dia (leido desde BBDD)
Se puede acceder a los "Cursos" desde el navbar o desde el boton en el slide en la pagina de inicio
Todos los templates heredan de una base padre, y luego se añadieron distintos diseños y funcionalidades segun cada url
Existe un panel de Admin donde se pueden cargar los usuarios (Tanto alumnos como profesores entran por la misma BBDD, los diferencia la categoria.)
En el panel Admin tambien se puede ingresar informacion de los Cursos, y de las Noticias
En el panel Admin se puede realizar busqueda por cualquiera de los datos ingresados.
Las plantillas utilizadas contienen estaticos, descargadas de Bootstrap, y se creo una Media para la imagenes
En inicio esta filtrado los 3 primeros cursos, al ingresar a la url se muestran todos.
Aca lo estoy subiendo a github
Y este es el read que explica mas o menos como va la cosa.
Hay muchas cosas que quiero pulir, y agregar, pero ayudo monton a entender otras cosas. Algunas ya son de HTML y CSS que no termino de entender. 
En el Slide de los cursos el boton "Saber mas" quedo sobre la imagen, y no lo he sabido corregir aun.