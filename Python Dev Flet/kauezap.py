import flet as ft 

# Função principal para rodar 
def main(pagina):
    # Título
    titulo = ft.Text("KaueZap")
    
    # Função para receber e adicionar mensagem no chat
    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)  # Adicionar nova mensagem no chat
        pagina.update()  # Atualizar a página para refletir a nova mensagem
    
    # Subscrição ao pubsub para receber mensagens de todos
    pagina.pubsub.subscribe(enviar_mensagem_tunel)        
    
    # Função para enviar mensagem
    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)  # Enviar mensagem para todos os subscritos
        
        # Limpar a caixa de enviar mensagem
        campo_enviar_mensagem.value = ""
        pagina.update()  # Atualizar a página para limpar a caixa
    
    # Campo de texto e botão de envio
    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
    
    chat = ft.Column()  # Coluna para exibir as mensagens do chat

    # Criar o popup
    titulo_popup = ft.Text("Bem vindo ao KaueZap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    
    # Função ao clicar no botão do popup
    def entrar_chat(evento):
        print(f"Nome: {caixa_nome.value}")
        # Fechar o popup
        popup.open = False
        
        # Remover o título e o botão inicial
        pagina.controls.remove(titulo)
        pagina.controls.remove(botao)
        
        # Carregar o chat e a área de envio de mensagem
        pagina.add(chat)
        pagina.add(linha_enviar)
        
        # Mensagem de que o usuário entrou no chat
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        
        pagina.update()

    # Botão dentro do popup
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    # Função para abrir o popup
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print("Clicou no botão")
          
    # Botão inicial para iniciar o chat
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    
    # Adicionar os elementos à página
    pagina.add(titulo)
    pagina.add(botao)

# Executar essa função com o flet
ft.app(target=main)
 