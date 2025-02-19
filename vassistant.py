import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import webbrowser
import os
import fnmatch
import tempfile
import pygame

pygame.mixer.init()

def falar(texto):
    """Converte texto em fala e reproduz."""
    tts = gTTS(text=texto, lang='pt')
    with tempfile.NamedTemporaryFile(delete=True, suffix='.mp3') as fp:
        tts.save(fp.name)
        playsound(fp.name)

def ouvir_comando():
    """Captura o comando de voz do usuário e converte em texto."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        falar("O que deseja fazer?")
        print("Ouvindo...")
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Comando reconhecido: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        falar("Desculpe, não entendi. Pode repetir?")
        return ouvir_comando()
    except sr.RequestError:
        falar("Erro ao se conectar ao serviço de reconhecimento de fala.")
        return ""

def abrir_navegador():
    """Abre o navegador padrão."""
    falar("Abrindo o navegador.")
    webbrowser.open("https://www.google.com")

def encontrar_arquivo(nome_arquivo, diretorio="C:/"):
    """Procura por um arquivo em um diretório e retorna o caminho se encontrado."""
    for root, _, files in os.walk(diretorio):
        for file in files:
            if fnmatch.fnmatch(file.lower(), f"*{nome_arquivo.lower()}*"):
                return os.path.join(root, file)
    return None

def reproduzir_musica():
    """Encontra e reproduz uma música solicitada pelo usuário."""
    falar("Qual música deseja ouvir?")
    nome_musica = ouvir_comando()

    falar("Procurando a música...")
    caminho_musica = encontrar_arquivo(nome_musica, diretorio="C:/Users/")  # Ajuste o diretório conforme necessário

    if caminho_musica:
        falar("Reproduzindo a música.")
        pygame.mixer.music.load(caminho_musica)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            comando = ouvir_comando()
            if "parar" in comando:
                pygame.mixer.music.stop()
                falar("Música parada.")
                break
    else:
        falar("Música não encontrada.")

def encontrar_arquivo_geral():
    """Permite que o usuário procure por qualquer arquivo pelo nome."""
    falar("Qual arquivo deseja encontrar?")
    nome_arquivo = ouvir_comando()

    falar("Procurando o arquivo...")
    caminho = encontrar_arquivo(nome_arquivo, diretorio="C:/Users/") # Ajuste o diretório conforme o necessário

    if caminho:
        falar("Arquivo encontrado.")
        print(f"Arquivo encontrado em: {caminho}")
    else:
        falar("Arquivo não encontrado.")

def executar_assistente():
    """Executa o assistente virtual, ouvindo comandos e executando ações."""
    while True:
        comando = ouvir_comando()

        if "abrir navegador" in comando:
            abrir_navegador()
        elif "reproduzir música" in comando or "tocar música" in comando:
            reproduzir_musica()
        elif "encontrar arquivo" in comando or "procurar arquivo" in comando:
            encontrar_arquivo_geral()
        elif "sair" in comando or "encerrar" in comando:
            falar("Encerrando o assistente. Até mais!")
            break
        else:
            falar("Comando não reconhecido. Por favor, tente novamente.")

if __name__ == "__main__":
    falar("Assistente iniciado.")
    executar_assistente()
