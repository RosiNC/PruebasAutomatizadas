# -*- coding: utf-8 -*-
'''
Created on Sep 4, 2020

@author: rosin
'''
import unittest
import time

from selenium import webdriver

#Completa el formulario, registra un miembro y verifica que se agregue correctamente a la lista de miembros
class Test01_Agregar_miembro(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NAME = "Prueba ETC"
        self.EMAIL = "pruebaetc@gmail.com"
        self.PHONE = "0123456789"
        self.MENSAJE_ESPERADO = "Member Registered"


    def test01_Agregar_miembro(self):
        
        self.driver.get("http://localhost:8080/jboss-kitchensink-html5-mobile/")
        time.sleep(1)
        
        self.driver.find_element_by_link_text("Add a Member").click()
        time.sleep(1)
        
        self.driver.find_element_by_id("name").send_keys(self.NAME)
        self.driver.find_element_by_id("email").send_keys(self.EMAIL)
        self.driver.find_element_by_id("phoneNumber").send_keys(self.PHONE)
        time.sleep(1)
        
        self.driver.find_element_by_id("register").click()
        time.sleep(1)
        
        MENSAJE_OBTENIDO = self.driver.find_element_by_xpath("//*[@id='formMsgs']/span").text
        
        self.assertEqual(MENSAJE_OBTENIDO, self.MENSAJE_ESPERADO, f"El mensaje es diferente al esperado: {self.MENSAJE_ESPERADO}")
        
        self.driver.find_element_by_link_text("List Members").click()
        self.driver.find_element_by_id("refreshButton").click()
        time.sleep(1)
        
        rows = len(self.driver.find_elements_by_xpath("//*[@id='member-table']/tbody/tr"))
        
        ID_MAYOR = 0
        ROW_INDEX = 0
        for n in range(1, rows+1):
            dato = self.driver.find_element_by_xpath("//*[@id='member-table']/tbody/tr["+str(n)+"]/th").text
            datoInt = int(dato)
            if datoInt > ID_MAYOR:
                ID_MAYOR = datoInt
                ROW_INDEX=n

        print(ID_MAYOR)
        
        NOMBRE_OBTENIDO = self.driver.find_element_by_xpath("//*[@id='member-table']/tbody/tr["+str(ROW_INDEX)+"]/td[1]").text
        EMAIL_OBTENIDO = self.driver.find_element_by_xpath("//*[@id='member-table']/tbody/tr["+str(ROW_INDEX)+"]/td[2]").text
        TELEFONO_OBTENIDO = self.driver.find_element_by_xpath("//*[@id='member-table']/tbody/tr["+str(ROW_INDEX)+"]/td[3]").text
        
        print(NOMBRE_OBTENIDO)
        print(EMAIL_OBTENIDO)
        print(TELEFONO_OBTENIDO)        
        
        self.assertEqual(NOMBRE_OBTENIDO, self.NAME, f"El nombre es diferente al esperado: {self.NAME}")
        self.assertEqual(EMAIL_OBTENIDO, self.EMAIL, f"El correo es diferente al esperado: {self.EMAIL}")        
        self.assertIn(self.PHONE, TELEFONO_OBTENIDO, f"El teléfono es diferente al esperado: {self.PHONE}")        
        
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()