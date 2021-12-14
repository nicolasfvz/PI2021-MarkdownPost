from PIL import Image
import os, random
import hashlib


def picture():
    # all image credits goes to https://picrew.me/image_maker/1360413, I stole it :+1:
    # Importa LIBS
     
    
    curr_dir = str(os.path.dirname(os.path.realpath(__file__)))
    # Importa a bibliotecx de edição de imagens
    # Gera o/a id inicial do/a ape/a gerado/a
    
    monkeName = ''
    # Gera as camadx
    
    bgid      = str(random.choice(os.listdir(curr_dir + "\\bg")))
    skinid    = str(random.choice(os.listdir(curr_dir + "\\skin")))
    bocaid    = str(random.choice(os.listdir(curr_dir + "\\boca")))
    camisaid  = str(random.choice(os.listdir(curr_dir + "\\camisa")))
    olesosid  = str(random.choice(os.listdir(curr_dir + "\\oleos")))
    oculosid  = str(random.choice(os.listdir(curr_dir + "\\oculo")))
    cha_peuid = str(random.choice(os.listdir(curr_dir + "\\cha peu")))
    
    # Seta
    bgDir      = curr_dir +  '\\bg\\'      + bgid
    skinDir    = curr_dir +  '\\skin\\'    + skinid
    bocaDir    = curr_dir +  '\\boca\\'    + bocaid
    camisaDir  = curr_dir +  '\\camisa\\'  + camisaid
    olesosDir  = curr_dir +  '\\oleos\\'   + olesosid
    oculosDir  = curr_dir +  '\\oculo\\'   + oculosid
    cha_peuDir = curr_dir +  '\\cha peu\\' + cha_peuid
    # gera um id com base nas camadas escolhidas
    apename = [
         bgid.replace('.png', ''),
       skinid.replace('.png', ''),
       bocaid.replace('.png', ''),
     camisaid.replace('.png', ''),
     olesosid.replace('.png', ''),
     oculosid.replace('.png', ''),
    cha_peuid.replace('.png', '')
    ]

    for i in apename:
        monkeName += i
        monkeName += 'Penis'
    #define o nome
    monkeName = hashlib.md5(monkeName.encode('utf-8')).hexdigest()

    print(monkeName)    
    # Abre eles/elas para trabalhar com eles/elas
    L1 = Image.open(bgDir)
    L2 = Image.open(skinDir)
    L3 = Image.open(bocaDir)
    L4 = Image.open(camisaDir)
    L5 = Image.open(olesosDir)
    L6 = Image.open(oculosDir)
    L7 = Image.open(cha_peuDir)
    # Converte-(o)as para RGBA
    F1 = L1.convert("RGBA")
    F2 = L2.convert("RGBA")
    F3 = L3.convert("RGBA")
    F4 = L4.convert("RGBA")
    F5 = L5.convert("RGBA")
    F6 = L6.convert("RGBA")
    F7 = L7.convert("RGBA")
    # Estaca-(o)as
    IMG = Image.alpha_composite(F1 , F2)
    IMG = Image.alpha_composite(IMG, F3)
    IMG = Image.alpha_composite(IMG, F4)
    IMG = Image.alpha_composite(IMG, F5)
    IMG = Image.alpha_composite(IMG, F6)
    IMG = Image.alpha_composite(IMG, F7)
    
    
    
    # Seta o caminhx para 
    #         sai do macaco > sai do profiles > entra no media
    apes = curr_dir + '\\..\\..\\media\\monkes'
    # totalFiles = 0
    # # Verifica quantxs arquivxs tem nas pastxs
    # for base, dirs, files in os.walk(apes):
    #     for Files in files:
    #         totalFiles += 1
    # Gera o diretorixs para salvar

    

    filename = f"\\{monkeName}.png"

    dirToSave = apes + filename
    
    # print(dirToSave)
    # Checx se o/a arquivo existe
    if os.path.isfile(dirToSave):
       print("\nErro, esse arquivo ja existe,", dirToSave, '\nresolve isso ae sla, fiquei com preguiça de pensar em uma solução\n')
    else:
         IMG.save(dirToSave,"PNG")
         
    return f'monkes/{monkeName}.png'
         
