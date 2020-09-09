# -*- coding: utf-8 -*-
'''
Created on Sep 7, 2020

@author: rosin
'''
import unittest
import time


from selenium import webdriver
from selenium.webdriver.common.by import By

#Verifica que al registrar un miembro el campo nombre no se deje en blanco
class Test09_Validar_mensajes_nombre(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.MENSAJE_ESPERADO = "Please fill out this field."


    def test09_Validar_mensajes_nombre(self):
        
        self.driver.get("http://localhost:8080/jboss-kitchensink-html5-mobile/")
        time.sleep(1)
        
        self.driver.find_element_by_link_text("Add a Member").click()
        time.sleep(1)
        
        self.driver.find_element_by_id("register").click()
        time.sleep(1)
        
        elemento = self.driver.find_element(By.ID, "name")   
        MENSAJE_OBTENIDO = elemento.get_attribute("validationMessage")      
        print(MENSAJE_OBTENIDO)
        
        validez = self.driver.execute_script("return arguments[0].checkValidity();", elemento)
        
        self.assertEqual(MENSAJE_OBTENIDO, self.MENSAJE_ESPERADO, f"El mensaje es diferente al esperado: {self.MENSAJE_ESPERADO}")
        self.assertFalse(validez, "Validez del campo incorrecto")
        
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()