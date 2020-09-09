# -*- coding: utf-8 -*-
'''
Created on Sep 6, 2020

@author: rosin
'''
import unittest
import time

from selenium import webdriver

#Verifica que se limpien los campos al dar clic al boton Reset
class Test02_Limpiar_campos(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NAME = "Prueba ETC"
        self.EMAIL = "pruebaetc@gmail.com"
        self.PHONE = "0123456789"


    def test02_Limpiar_campos(self):
        
        self.driver.get("http://localhost:8080/jboss-kitchensink-html5-mobile/")
        time.sleep(1)
        
        self.driver.find_element_by_link_text("Add a Member").click()
        time.sleep(1)
        
        self.driver.find_element_by_id("name").send_keys(self.NAME)
        self.driver.find_element_by_id("email").send_keys(self.EMAIL)
        self.driver.find_element_by_id("phoneNumber").send_keys(self.PHONE)
        time.sleep(1)
        
        self.driver.find_element_by_id("cancel").click()
        time.sleep(1)
        
        NOMBRE_OBTENIDO = self.driver.find_element_by_id("name").text
        EMAIL_OBTENIDO = self.driver.find_element_by_id("email").text
        TELEFONO_OBTENIDO = self.driver.find_element_by_id("phoneNumber").text
        
        self.assertEqual(NOMBRE_OBTENIDO, "", "El nombre no se limpió")
        self.assertEqual(EMAIL_OBTENIDO, "", "El correo no se limpió")
        self.assertEqual(TELEFONO_OBTENIDO, "", "El teléfono no se limpió")
        

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()