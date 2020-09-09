# -*- coding: utf-8 -*-
'''
Created on Sep 6, 2020

@author: rosin
'''
import unittest
import time

from selenium import webdriver

#Verifica que no se permita registrar un miembro con un correo que ya exista en el sistema
class Test05_Validar_correo_registrado_en_sistema(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NAME = "Prueba ETC"
        self.EMAIL = "john.smith@mailinator.com"
        self.PHONE = "0123456789"
        self.MENSAJE_ESPERADO = "Email taken"


    def test05_Validar_correo_registrado_en_sistema(self):
        
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
        
        MENSAJE_OBTENIDO = self.driver.find_element_by_xpath("//*[@id='reg']/fieldset/div[2]/div/span").text
        
        self.assertEqual(MENSAJE_OBTENIDO, self.MENSAJE_ESPERADO, f"El mensaje es diferente al esperado: {self.MENSAJE_ESPERADO}")
    
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()