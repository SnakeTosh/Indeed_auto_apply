from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Saisir les filtres et le mot clé à rechercher manuellement

browser = webdriver.Safari()
browser.get("https://fr.indeed.com")

what = browser.find_element(By.ID, "text-input-what")
what.send_keys('python')
where = browser.find_element(By.ID, "text-input-where")
where.send_keys('France')
entry = browser.find_element(By.XPATH, "//button[@class='yosegi-InlineWhatWhere-primaryButton']")
entry.click()
filters = browser.find_element(By.ID, "filter-jobtype")
filters.click()
down = filters.find_element(By.XPATH, "//ul[@class='yosegi-FilterPill-dropdownList']")
alternance = down.find_element(By.LINK_TEXT,'/emplois?q=python&l=France&sc=0kf%3Ajt(permanent)%3B')
alternance.click()


# --------------------------------------------------------------------------------------------------------

# Démarrer le script avec un lien directement

browser.get("https://fr.indeed.com/emplois?q=python&l=France&sc=0kf%3Ajt%28apprenticeship%29%3B&vjk=d973a03fee2dd47a")
original_window = browser.current_window_handle
browser.maximize_window()

# Se connecter

browser.find_element(By.LINK_TEXT,'Connexion').click()
sleep(3)
mail = browser.find_element(By.ID,"ifl-InputFormField-3")
mail.send_keys("Remplir_avec_identifiant")

input("Résoudre le capcha puis appuyer sur entrée")

def found_mdp():
    try :
        mdp = browser.find_element(By.XPATH, "//input[@class='css-5ye0j e1jgz0i3']")
        mdp.send_keys("Remplir_avec_password")
        mdp.send_keys(Keys.ENTER)
        return True
    except :
        return False

while True :
    if found_mdp() == True:
        break
    else :
        continue


input("Résoudre le capcha puis appuyer sur entrée")

try :
    browser.find_element(By.XPATH, "//button[@class='css-yi9nv e8ju0x51']").click()
except Exception :
    pass

def click():
    try :
        jobs_container.find_element(By.XPATH, "//li[1]").click()
    except :
        return False

jobs_container = browser.find_element(By.XPATH, "//ul[@class='css-zu9dh eu4oa1w0']")
all_jobs = jobs_container.find_elements(By.XPATH, "//li[@class='css-5lfsm eu4oa1w0']")
jobs = jobs_container.find_element(By.XPATH, "//h2[1]")
easy_apply = jobs_container.find_elements(By.XPATH, "//span[@class='iaIcon']")

easy_jobs = []
tour = 1

for easy in all_jobs :
    try :
        easy_jobs.append(easy.find_element(By.XPATH, "//span[@class='iaIcon']"))
    except :
        pass
    tour+=1

while True :

    cliquer = click()
    if cliquer == False:
        continue
    else :
        break

for job in jobs:
    try:
        job.location_once_scrolled_into_view
    except:
        pass
    # essaie = 0

    while True:

        cliquer = click(job)
        if cliquer == False:
            break
        else:
            break
    tour += 1

jobs = browser.find_elements(By.XPATH, "//tr[@class='css-mvfiq eu4oa1w0']")

def postuler():

    try:

        # selectionner lettre de motivation obligatoire
        browser.find_element(By.XPATH, '//span[@class= "css-p27d4n e1wnkr70"]').click()
        sleep(2)
        # continuer apres lettre de motivation obligatoire
        browser.find_element(By.XPATH, '//button[@class="ia-continueButton ia-SupportingDocument-continue css-1gjdq7 e8ju0x51"]').click()
        sleep(2)
        # valider candidature
        browser.find_element(By.XPATH, '//button[@class="ia-continueButton css-njr1op e8jux51"]').click()
        sleep(2)

    except Exception :
        pass


sleep(10)
print('Fin du programme')
browser.close()


# --------------------------------------------------------------------------------------------------------
