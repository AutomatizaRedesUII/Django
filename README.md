Esta muestra contiene el programa completo del tutorial, [Using Django in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-django). No se incluyen los pasos intermedios.

La muestra también incluye un archivo Docker para construir una imagen de contenedor lista para producción que utiliza uwsgi y nginx; el archivo uwsgi.ini proporciona la configuración de uwsgi.

Para ejecutar la muestra:

1. Cree un entorno virtual como se describe en el tutorial.
1. Instalar paquetes con `pip install -r requirements.txt`.
1. Active el entorno virtual ejecutando `source env/bin/activate` (Linux/MacOS) o `env\scripts\activate` (Windows).
1. Cree e inicialice la base de datos ejecutando `python manage.py migrate`.
1. Cree un superusuario como se describe al final del tutorial.

Las contribuciones a la muestra son bienvenidas. Cuando envíe cambios, considere también la posibilidad de enviar los cambios correspondientes al tutorial, cuyo archivo fuente es [tutorial-django.md]
(https://github.com/Microsoft/vscode-docs/blob/master/docs/python/tutorial-django.md).

# Problemas conocidos

- El CSS se pierde si se pone `DEBUG=False` en settings.py; la solución es incluir un script añadido al final de dockerfile.txt para servir el archivo estático de forma diferente. Ver [Issue 13](https://github.com/Microsoft/python-sample-vscode-django-tutorial/issues/13) para más detalles.

# Contribuyendo a

Este proyecto agradece las contribuciones y sugerencias.  La mayoría de las contribuciones requieren que usted acepte un Acuerdo de Licencia de Contribución (CLA) en el que se declara que tiene derecho, y de hecho nos concede, los derechos para utilizar su contribución. Para más detalles, visite https://cla.microsoft.com.

Cuando envíe una solicitud de extracción, un bot CLA determinará automáticamente si necesita proporcionar una CLA y decorará el PR de forma adecuada (por ejemplo, etiqueta, comentario). Sólo tiene que seguir las instrucciones proporcionadas por el bot. Sólo tendrá que hacer esto una vez en todos los repos que utilicen nuestro CLA.

Este proyecto ha adoptado el [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Para más información, consulte el [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) o contacte con [opencode@microsoft.com](mailto:opencode@microsoft.com) con cualquier pregunta o comentario adicional.
