import os 
restaurantes= [{'nome': 'tenperinho', 'categoria':'secreto', 'ativo':True},
              {'nome': 'niki sabores', 'categoria':'delicia','ativo':False},
              {'nome':'cinderela', 'categoria':'cristal','ativo':False}]
              
            
            
def exibir_nome_do_programa():
    print ("""██╗░░░░░███████╗░█████╗░░█████╗░
██║░░░░░██╔════╝██╔══██╗██╔══██╗
██║░░░░░█████╗░░███████║██║░░██║
██║░░░░░██╔══╝░░██╔══██║██║░░██║
███████╗███████╗██║░░██║╚█████╔╝
╚══════╝╚══════╝╚═╝░░╚═╝░╚════╝░\n""")

def exibir_opções():
    print ("1-cadastrar restaurante")
    print ("2-listar restaurante")
    print ("3-ativar restaurante")
    print ("4-sair")
    
    
def Encerrando_programa():
    exibir_subtitulo('cadastro de novos restaurante')
    voltar_ao_menu_principal()
    
def voltar_ao_menu_principal():
    input('\n digiti uma tecla para voltar ao menu principal')   
    main() 
    
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()
    
def opção_invalida():
    print('Opção invalida"!\n')
    voltar_ao_menu_principal()
 
 
def cadastrar_novo_restaurante():
     exibir_subtitulo('cadastro de novos restaurante')
     nome_do_restaurante =input('digite o nome do restaurante que deseja cadastrar:')
     restaurantes.append(nome_do_restaurante)  
     print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso!') 
     voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('cadastro de novos restaurante')
    print('Listando os restaurantes\n')
    
    for restaurante in restaurantes:
        print(f'.(restaurante)')
     
def escolher_opção():
    try:
        
        opção = int( input("escolha uma opção:"))
        print(f'a opção escolhida foi: {opção}\n')
        
        if opção == 1:
            cadastrar_novo_restaurante()
        
        elif opção == 2:
            listar_restaurante()
        
        elif opção == 3:
            print("ativar restaurante")
        elif opção == 4:
            Encerrando_programa()
        else:
            opção_invalida()
    except:
            opção_invalida()
def main():
        os.system('cls')
        exibir_nome_do_programa()
        exibir_opções()
        escolher_opção()
            
if __name__ == '__main__':
   main()
    
