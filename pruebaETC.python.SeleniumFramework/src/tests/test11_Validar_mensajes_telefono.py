# -*- coding: utf-8 -*-
'''
Created on Sep 7, 2020

@author: rosin
'''
import unittest
import time


from selenium import webdriver
from selenium.webdriver.common.by import By

#Realiza validaciones al registrar un miembro sobre el campo telefono: 
#no se deje en blanco, que no contenga menos de 9 numeros y mas de 12
class Test11_Validar_mensajes_telefono(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NAME = "Prueba ETC"
        self.EMAIL = "pruebaetc@gmail.com"


    def test11_Validar_mensajes_telefono(self):
        
        self.driver.get("http://localhost:8080/jboss-kitchensink-html5-mobile/")
        time.sleep(1)
        
        self.driver.find_element_by_link_text("Add a Member").click()
        time.sleep(1)
        
        self.driver.find_element_by_id("name").send_keys(self.NAME)
        self.driver.find_element_by_id("email").send_keys(self.EMAIL)

        self.driver.find_element_by_id("register").click()
        
        elemento = self.driver.find_element(By.ID, "phoneNumber")   
        MENSAJE_OBTENIDO = elemento.get_attribute("validationMessage")      
        print(MENSAJE_OBTENIDO)
        
        validez = self.driver.execute_script("return arguments[0].checkValidity();", elemento)
        
        MENSAJE_ESPERADO = "Please fill out this field."
        self.assertEqual(MENSAJE_OBTENIDO, MENSAJE_ESPERADO, f"El mensaje es diferente al esperado: {MENSAJE_ESPERADO}")
        self.assertFalse(validez, "Validez del campo incorrecto")
        time.sleep(5)
        
        
        PHONE = "12345678"
        self.driver.find_element_by_id("phoneNumber").send_keys(PHONE)
        self.driver.find_element_by_id("register").click()
        
        elemento = self.driver.find_element(By.ID, "phoneNumber")   
        MENSAJE_OBTENIDO = elemento.get_attribute("validationMessage")      
        print(MENSAJE_OBTENIDO)
        
        validez = self.driver.execute_script("return arguments[0].checkValidity();", elemento)
        
        MENSAJE_ESPERADO = f"Please match the requested format."
        self.assertEqual(MENSAJE_OBTENIDO, MENSAJE_ESPERADO, f"El mensaje es diferente al esperado: {MENSAJE_ESPERADO}")
        self.assertFalse(validez, "Validez del campo incorrecto")
        time.sleep(5)
        
        
        PHONE = "1234567890123"
        self.driver.find_element_by_id("phoneNumber").clear()
        self.driver.find_element_by_id("phoneNumber").send_keys(PHONE)
        self.driver.find_element_by_id("register").click()
        
        elemento = self.driver.find_element(By.ID, "phoneNumber")   
        MENSAJE_OBTENIDO = elemento.get_attribute("validationMessage")      
        print(MENSAJE_OBTENIDO)
        
        validez = self.driver.execute_script("return arguments[0].checkValidity();", elemento)
        
        MENSAJE_ESPERADO = f"Please match the requested format."
        self.assertEqual(MENSAJE_OBTENIDO, MENSAJE_ESPERADO, f"El mensaje es diferente al esperado: {MENSAJE_ESPERADO}")
        self.assertFalse(validez, "Validez del campo incorrecto")
        time.sleep(5)
    
    
    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()