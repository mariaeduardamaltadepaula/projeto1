import os 
restaurantes= [{'nome': 'temperinho', 'categoria':'salgado', 'ativo':True},
              {'nome': 'niki sabores', 'categoria':'apimentado', 'ativo':False},
              {'nome': 'cinderela', 'categoria':'doce', 'ativo':False}]
              
            
            
def exibir_nome_do_programa():
    '''e o nome do restaurante'''
    print ("""██╗░░░░░███████╗░█████╗░░█████╗░
██║░░░░░██╔════╝██╔══██╗██╔══██╗
██║░░░░░█████╗░░███████║██║░░██║
██║░░░░░██╔══╝░░██╔══██║██║░░██║
███████╗███████╗██║░░██║╚█████╔╝
╚══════╝╚══════╝╚═╝░░╚═╝░╚════╝░\n""")

def exibir_opções():
    '''essa opçao e responsavel para escolher a o que voce quer realizar no restaurante'''
    print ("1-cadastrar restaurante")
    print ("2-listar restaurante")
    print ("3-alternar estado de restaurante")
    print ("4-sair")
    
    
def Encerrando_programa():
    '''essa oçao e responsavel por cadastrar o restaurante'''
    exibir_subtitulo('cadastro de novos restaurante')
    voltar_ao_menu_principal()                           
    
def voltar_ao_menu_principal():
    '''essa oçao e responsavel para voltar ao menu princial'''
    input('\n digite uma tecla para voltar ao menu principal')   
    main() 
    
def exibir_subtitulo(texto):
    '''essa oçao e responsavel para organizar a linha das listas do restaurante'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def opção_invalida():
    '''exibe uma oçao invalida e faz voltar ao menu principal'''
    print('Opção invalida"!\n')
    voltar_ao_menu_principal()
 
 
def cadastrar_novo_restaurante():
     exibir_subtitulo('cadastro de novos restaurante')
     '''responsavel para cadastrar novo restaurante'''
     
     nome_do_restaurante =input('digite o nome do restaurante que deseja cadastrar:')
     categoria = input(f"digite o nome da categoria do restaurante{nome_do_restaurante}: ")
     dados_do_restaurante ={"nome":nome_do_restaurante,"categoria":categoria,"ativo":False}
     restaurantes.append(nome_do_restaurante)  
     print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso!') 
     
     voltar_ao_menu_principal()

def listar_restaurante():
    '''responsavel para listar o restaurante'''
    exibir_subtitulo('cadastro de novos restaurante')
    
    print(f'{'nome do restaurante'.ljust(21)} | {'categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante ["ativo"] else "desativado"
        print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        
        voltar_ao_menu_principal
        
def alterar_estado_restaurante():
  exibir_subtitulo('alterando estado do restaurante')
  '''responsavel para alterar o estado do restaurante'''
  
  nome_restaurante = input('digite o nome do restaurante que deseja alterar o estado: ')
  restaurante_encontrado = False
  for restaurante in restaurante:
      if nome_restaurante == restaurante['nome']:
          restaurante_encontrado = True
          restaurante['ativo'] = not restaurante['ativo']
          mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso' 
          print(mensagem)
      if not restaurante_encontrado:
          print('o restaurante nao foi encontrado')
  
     
def escolher_opção():
    '''responsavel para escolher a opçao que voce desejar'''
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
        '''responsavel para mostar as opçoes'''
            
if __name__ == '__main__':
   main()
    
