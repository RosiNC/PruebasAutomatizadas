# -*- coding: utf-8 -*-
'''
Created on Sep 7, 2020

@author: rosin
'''
import unittest
import time


from selenium import webdriver
from selenium.webdriver.common.by import By

#Realiza validaciones al registrar un miembro sobre el campo correo: 
#no se deje en blanco, que incluya un @, que ingrese una parte despues del @ y 
#que el “.” se encuentre en una posicion correcta
class Test10_Validar_mensajes_correo(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NAME = "Prueba ETC"
    

    def test10_Validar_mensajes_correo(self):
        
        self.driver.get("http://localhost:8080/jboss-kitchensink-html5-mobile/")
        time.sleep(1)
        
        self.driver.find_element_by_link_text("Add a Member").click()
        time.sleep(1)
        
        self.driver.find_element_by_id("name").send_keys(self.NAME)

        self.driver.find_element_by_id("register").click()
        
        elemento = self.driver.find_element(By.ID, "email")   
        MENSAJE_OBTENIDO = elemento.get_attribute("validationMessage")      
        print(MENSAJE_OBTENIDO)
        
        validez = self.driver.execute_script("return arguments[0].checkValidity();", elemento)
        
        MENSAJE_ESPERADO = "Please fill out this field."
        self.assertEqual(MENSAJE_OBTENIDO, MENSAJE_ESPERADO, f"El mensaje es diferente al esperado: {MENSAJE_ESPERADO}")
        self.assertFalse(validez, "Validez del campo incorrecto")
        time.sleep(5)
        
        
        EMAIL = "pruebaetc"
        self.driver.find_element_by_id("email").send_keys(EMAIL)
        self.driver.find_element_by_id("register").click()
        
        elemento = self.driver.find_element(By.ID, "email")   
        MENSAJE_OBTENIDO = elemento.get_attribute("validationMessage")      
        print(MENSAJE_OBTENIDO)
        
        validez = self.driver.execute_script("return arguments[0].checkValidity();", elemento)
        
        MENSAJE_ESPERADO = f"Please include an '@' in the email address. '{EMAIL}' is missing an '@'."
        self.assertEqual(MENSAJE_OBTENIDO, MENSAJE_ESPERADO, f"El mensaje es diferente al esperado: {MENSAJE_ESPERADO}")
        self.assertFalse(validez, "Validez del campo incorrecto")
        time.sleep(5)
        
        
        EMAIL = "pruebaetc@"
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys(EMAIL)
        self.driver.find_element_by_id("register").click()
        
        elemento = self.driver.find_element(By.ID, "email")   
        MENSAJE_OBTENIDO = elemento.get_attribute("validationMessage")      
        print(MENSAJE_OBTENIDO)
        
        validez = self.driver.execute_script("return arguments[0].checkValidity();", elemento)
        
        MENSAJE_ESPERADO = f"Please enter a part following '@'. '{EMAIL}' is incomplete."
        self.assertEqual(MENSAJE_OBTENIDO, MENSAJE_ESPERADO, f"El mensaje es diferente al esperado: {MENSAJE_ESPERADO}")
        self.assertFalse(validez, "Validez del campo incorrecto")
        time.sleep(5)
        
        
        EMAIL = "pruebaetc@.g"
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys(EMAIL)
        self.driver.find_element_by_id("register").click()
        
        elemento = self.driver.find_element(By.ID, "email")   
        MENSAJE_OBTENIDO = elemento.get_attribute("validationMessage")      
        print(MENSAJE_OBTENIDO)
        
        validez = self.driver.execute_script("return arguments[0].checkValidity();", elemento)
        
        MENSAJE_ESPERADO = f"'.' is used at a wrong position in '{EMAIL.replace('pruebaetc@', '')}'."
        self.assertEqual(MENSAJE_OBTENIDO, MENSAJE_ESPERADO, f"El mensaje es diferente al esperado: {MENSAJE_ESPERADO}")
        self.assertFalse(validez, "Validez del campo incorrecto")
        time.sleep(5)
        
        EMAIL = ".@"
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys(EMAIL)
        self.driver.find_element_by_id("register").click()
        
        elemento = self.driver.find_element(By.ID, "email")   
        MENSAJE_OBTENIDO = elemento.get_attribute("validationMessage")      
        print(MENSAJE_OBTENIDO)
        
        validez = self.driver.execute_script("return arguments[0].checkValidity();", elemento)
        
        MENSAJE_ESPERADO = f"Please enter a part following '@'. '{EMAIL}' is incomplete."
        self.assertEqual(MENSAJE_OBTENIDO, MENSAJE_ESPERADO, f"El mensaje es diferente al esperado: {MENSAJE_ESPERADO}")
        self.assertFalse(validez, "Validez del campo incorrecto")
        time.sleep(5)
        
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()