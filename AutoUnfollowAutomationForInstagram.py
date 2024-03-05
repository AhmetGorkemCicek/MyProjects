from PIL import Image
import customtkinter
import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import random
import threading
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.has_follower_list=[]
        self.browser=webdriver.Chrome()
    def starter(self):  
        instagram1=Instagram("username","password")#buraya bilgiler girilir.
       
        self.browser.get("https://www.instagram.com/")
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')))
        login=self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
        login.click()
        time.sleep(0.2)
        login.send_keys(instagram1.username)
        password=self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
        password.click()
        time.sleep(0.1)
        password.send_keys(instagram1.password)
        log_in=self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
        log_in.click()
        time.sleep(4)
        



    def unfollowpeople(self,followername):
        self.browser.get(f"https://www.instagram.com/{followername}/")
        time.sleep(4)
        text=self.browser.find_element(By.CSS_SELECTOR,"._ap3a._aaco._aacw._aad6._aade").text
        time.sleep(4)
        if(text=="Takiptesin"):
            self.browser.find_element(By.CSS_SELECTOR,"._ap3a._aaco._aacw._aad6._aade").click()

            time.sleep(3)
            self.browser.find_element(By.XPATH,"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div/div/div/div/div/span/span").click()
            time.sleep(3)
        else:
            time.sleep(2)
            pass




    def reachfollowerlist(self,has_follower_list):
        self.browser.get("https://www.instagram.com/gorkem23232323/")
        time.sleep(20)
        self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(20)
        counter=0
        followerList=self.browser.find_element(By.CSS_SELECTOR,"body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1) > div")
        while True:
            followerList.click()
            scrolls=4
            for i in range(scrolls):
                self.browser.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
                time.sleep(2)
            break

        
        users=self.browser.find_element(By.CSS_SELECTOR,"body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1) > div").find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
        for user in users:
            followername=user.find_element(By.CSS_SELECTOR,"._ap3a._aaco._aacw._aacx._aad7._aade").text
            followername=followername+"\n"
            has_follower_list.append(followername)
            counter+=1
        has_follower_list.append("1\n")
        counter+=1




def whitelist():
    listem=[]
    while True:
        input1=input("Lütfen beyaz listeye almak istediğiniz kullanıcının adını düzgün şekilde girin... Durmak için stop yazın...")
        if(input1=="stop"):
            break
        else:
            input1=input1+"\n"
            listem.append(input1)
    a="1\n"
    listem.append(a)
    with open("C:\Yedek\insta\Baslksz_e-tablo_-_Sayfa2.csv","w") as file:
            file.writelines(listem)
        





def getFollowers():
    while True:
        input1=input("Beyaz Listeye kullanıcı girmek için 1 e Takipçi değerlendirmesi için 2 ye basın durmak için stop yazın")
        if(input1=="stop"):
            break
        elif(input1=="1"):
            whitelist()
            continue
        elif(input1=="2"):
            checkstr="1\n"
            with open("C:\Yedek\insta\Baslksz_e-tablo_-_Sayfa1.csv","r") as file:
                all_lines=file.readlines()
            last_line=all_lines[-1]
            
            if(last_line==checkstr):
                time.sleep(1)
                with open("C:\Yedek\insta\Baslksz_e-tablo_-_Sayfa1.csv","r") as file:
                        all_lines2=file.readlines()
                with open("C:\Yedek\insta\Baslksz_e-tablo_-_Sayfa2.csv","r") as file:
                        all_lines3=file.readlines()
                followerList2=[]
                
                reachfollowerlist(followerList2)
                for a in all_lines2[0:-1:1]:
                    if (a not in all_lines3):
                        esitlik=0
                        for b in followerList2[0:-1:1]:
                            if(a==b):
                                esitlik+=1
                        if(esitlik==0):
                            new_a=a.rstrip("\n")
                            unfollowpeople(new_a)
                            print(new_a,"kullanıcısı takipten çıkıldı.")

                        else:
                            pass
                    else:
                        pass
                    
                with open("C:\Yedek\insta\Baslksz_e-tablo_-_Sayfa1.csv","w") as file:
                    file.writelines(followerList2)
                print("Eski takipçileri değerlendirme işlemi tamamlandı.")
                print()
                break

                        
                        
            else:
                reachfollowerlist(has_follower_list)
                with open("C:\Yedek\insta\Baslksz_e-tablo_-_Sayfa1.csv","w") as file:
                    file.writelines(has_follower_list)
            
                print("Takipçiler veri olarak ilk defa tutuldu.")
            continue
            
            

    
    
getFollowers()
            
            

    
    
