echo. ##################### TEST PATH #####################
cd /d D:\Prueba ETC\pruebaETC.python.SeleniumFramework\src\tests

@echo off

echo. ##################### PRUEBAS #####################


python -m pytest test01_Agregar_miembro.py test02_Limpiar_campos.py test03_Validar_nombre_con_numeros.py test04_Validar_nombre_mas_25_letras_espacios.py test05_Validar_correo_registrado_en_sistema.py test06_Validar_JSON_fila.py test07_Validar_JSON_tabla.py test08_Validar_orden_tabla.py test09_Validar_mensajes_nombre.py test10_Validar_mensajes_correo.py test11_Validar_mensajes_telefono.py test12_Refrescar_tabla.py --junitxml=results.xml





pause