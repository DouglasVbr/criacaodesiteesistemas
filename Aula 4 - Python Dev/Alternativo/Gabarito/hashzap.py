# tela inicial 
#titulo
#botão iniciar chat
# caixa de texto 
# botao entrar no chat 
# quando clicar no botao sumir com o titulo 
# sumir com o botao iniciar chat 
# carregar o chat 
# carregar o campo de enviar msg
#botao enviar 
# quando clicar no botão enviar enviar a msg limpar a caixa de texto



# importar o flet 
import flet as ft


# criar uma função principal para rodar seu app 
def main(pagina):


 # titulo 
   titulo = ft.Text("hashzap")
   
   def enviar_mensagem_tunel(mensagem):
       # todos os usuarios enviarem msg
       texto = ft.Text(mensagem)
       chat.controls.append(texto)
       pagina.update()
       
   pagina.pubsub.subscribe(enviar_mensagem_tunel)   
   
   def enviar_mensagem(evento):
       nome_usuario = caixa_nome.value
       texto_campo_mensagem = campo_enviar_mensagem.value
       mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
       pagina.pubsub.send_all(mensagem)
       texto = ft.Text (f"{nome_usuario}: {texto_campo_mensagem}")
       chat.controls.append(texto)
       # limpar a caixa de enviar mensagem 
       campo_enviar_mensagem.value =""
       pagina.update()
    
   campo_enviar_mensagem = ft.TextField (label= "Digite aqui sua mensagem", on_submit=enviar_mensagem)
   botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
   
   linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
   
   chat = ft.Column()
    
   def entrar_chat(evento):
       #fechar popup
       popup.open = False
       # sumir co o titulo
       pagina.remove(titulo)
       # sumir com o botao iniciar chat
       pagina.remove(botao)
       #carregar o chat
       pagina.add(chat) 
       # carregar o campo de enviar mensagem
       pagina.add(linha_enviar)
       
       # adicionar no chat fulano entrou no chat
       nome_usuario = caixa_nome.value
       mensagem = f"{nome_usuario} entrou no chat"
       pagina.pubsub.send_all(mensagem)
       pagina.update()
       
       
       
       
    
   # criar o popup
   titulo_popup = ft.Text("Bem Vindo ao hashzap")
   caixa_nome = ft.TextField(label="Digite o seu Nome")
   botao_popup = ft.ElevatedButton("entrar no chat", on_click=entrar_chat)
   popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions= [botao_popup])

 
   #botao inicial
   def abrir_popup(evento):
       pagina.dialog = popup
       popup.open = True
       pagina.update()
       
 
   botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
  
   # colocar os elementos na pagina 
   pagina.add(titulo)
   pagina.add(botao)
  
#executar essa função com o flet
ft.app(main, view=ft.WEB_BROWSER)



    

