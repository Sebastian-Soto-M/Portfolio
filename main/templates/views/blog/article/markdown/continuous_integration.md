# ¿Qué es?

Lo habitual entre desarrolladores es que cada uno programe por separado
una parte de la aplicación y el tiempo de integración de todas las
partes suelen ser bastante prolongadas y difíciles, esto provocaba que
se acumularan errores por mucho tiempo y los clientes tardaran más
tiempo en recibir la finalización del software.

Cuando se distribuye el trabajo entre los miembros del equipo, y cada
uno comienza a trabajar, normalmente se asumen cosas de otros
componentes del software que todavía no están implementados o que se
encuentran en desarrollo.

Y hasta que no juntamos todo ese código, no nos damos cuenta de los
errores cometidos. Antes, lo que se tendía a realizar es que cada
desarrollador programara de forma independiente y luego al final, se
realizaba la integración de todo el código.

Esto se traduce en integraciones difíciles, que tardan mucho en
completarse y mucho sufrimiento, ya que hay muchos cambios y mucho
código que integrar.

Uno de los motivos por los que surge la integración continua es para
evitar esto. La idea es que en vez de dejar la integración para el
final, se vayan haciendo pequeñas integraciones de código
frecuentemente.

La integración continua (Continuous Integration) es una práctica que
utilizan los desarrolladores de software para realizar los cambios en el
código de un repositorio de manera periódica, para ejecutar versiones y
pruebas automáticas que comprueban el código del repositorio de
versiones varias veces al día.

Generalmente la integración continua trae un gran aporte y ayuda a las
siguientes áreas del desarrollo de software:

* Calidad de proceso:

    * La integración continua mejora la productividad del equipo al liberar a los desarrolladores de las tareas manuales y fomentar comportamientos que ayudan a reducir la cantidad de errores y fallos enviados a los clientes.

* Calidad del producto:

    * Así se introducen varios tipos de pruebas y comprobaciones, minimizando los riesgos, y haciendo que el software tenga menos fallos al contrario de que no utilizáramos la integración continua.

    * Por otra parte, en fases ya avanzadas de la integración continua se suelen lanzar inspecciones continuas de código, análisis periódicos para detectar problemas de calidad en él.

    * Los desarrolladores tendrán que mejorar esas deficiencias, e incluso en ciertas ocasiones, se puede impedir que los desarrolladores suban el código al control de versiones si no cumplen los estándares de calidad definidos por la empresa

* Calidad de desarrolladores:

    * También se mejora la calidad del equipo. Si no sabía, el equipo acaba aprendiendo a hacer distintos tipos de pruebas (unitarias, de integración), mejores prácticas de programación y en general a desarrollar código de mayor calidad

    * Además de que le ahorra muchísimo tiempo, porque se automatizan procesos repetitivos y le da más confianza al equipo

# ¿Para qué sirve?:

Los principales objetivos que presenta la integración continua son:

* Encontrar y resolver errores con rapidez.

* Mejorar la calidad del software.

* Cuando el producto o aplicación está en el mercado favorece validar y publicar nuevas actualizaciones del software en menor tiempo.

* Los cambios pequeños son más fáciles de integrar en porciones de código más grandes.

* Los errores en trabajos más grandes se identifican temprano, lo que hace que sean más fáciles de solucionar, lo que resulta en menos trabajo de depuración

* Menos problemas de integración que permiten la entrega rápida de código

Con la integración continua, los desarrolladores envían los cambios de
forma periódica a un repositorio compartido con un sistema de control de
versiones. Antes de cada envío, los desarrolladores pueden elegir
ejecutar pruebas de unidad local en el código como medida de
verificación adicional antes de la integración. Un servicio de
integración continua crea y ejecuta automáticamente pruebas de unidad en
los nuevos cambios realizados en el código para identificar
inmediatamente cualquier error.
