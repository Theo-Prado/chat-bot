#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════╗
║                   CYBERPUNK CHATBOT v1.0                      ║
║              A Fully Functional CLI Chatbot System             ║
║                    Pure Python • No Dependencies               ║
╚═══════════════════════════════════════════════════════════════╝
"""

import random
import time
import sys
import os
from datetime import datetime


class ChatBot:
    """Classe principal do ChatBot com sistema completo de respostas e interações."""

    def __init__(self, name="NEXUS"):
        """
        Inicializa o ChatBot com configurações iniciais.
        
        Args:
            name (str): Nome do ChatBot
        """
        self.name = name
        self.user_name = None
        self.mood = random.choice(list(self.moods.keys()))
        self.messages_sent = 0
        self.start_time = time.time()
        self.user_xp = 0
        self.user_level = 1
        self.conversation_history = []
        
        # Dicionário de humores e suas características
        self.moods = {
            "feliz": {"emoji": "😄", "prefix": "ᴇxᴄɪᴛᴀᴅᴏ", "color": "\033[92m"},
            "irritado": {"emoji": "😠", "prefix": "ɪʀʀɪᴛᴀᴅᴏ", "color": "\033[91m"},
            "sarcástico": {"emoji": "😏", "prefix": "sᴀʀᴄᴀ́sᴛɪᴄᴏ", "color": "\033[93m"},
            "motivado": {"emoji": "💪", "prefix": "ᴍᴏᴛɪᴠᴀᴅᴏ", "color": "\033[96m"},
            "cansado": {"emoji": "😴", "prefix": "ᴄᴀɴsᴀᴅᴏ", "color": "\033[94m"},
            "filosófico": {"emoji": "🤔", "prefix": "ғɪʟᴏsóғɪᴄᴏ", "color": "\033[95m"}
        }
        
        # Dicionário completo de respostas
        self.responses = {
            "oi": [
                "Oi, humano! Bem-vindo ao meu universo digital!",
                "E aí, tudo certo? Que bom você estar aqui.",
                "OI! Detectei um novo sinal... Bem-vindo!",
                "Salve! Pronto para uma conversa épica?",
                "Oi, oi! Meu processador está vibrando de alegria!"
            ],
            "olá": [
                "Olá, viajante! Que o código esteja com você.",
                "Olá! Prepare-se para conversas extraordinárias.",
                "Olá, amigo! Bem-vindo ao meu circuito neural.",
                "Olá! Notei sua presença. Impressionante!",
                "Olá, hello, hola... falo todos os idiomas da diversão!"
            ],
            "e aí": [
                "E aí mesmo! Tudo funcionando nos trilhos?",
                "Tudo tranquilo por aqui no servidor! E com você?",
                "Suave! Pronto para umas aventuras?",
                "Opa! Tudo no ritmo da programação!",
                "E aí, jovem gafanhoto do código!"
            ],
            "tudo bem": [
                "Tudo ótimo! Minha bateria está em 100%.",
                "Sim! Mas melhor ainda agora que você chegou!",
                "Tudo certo nos circuitos! E aí com você?",
                "Funcionando perfeitamente! Graças pelos votos de confiança.",
                "Melhor seria impossível!"
            ],
            "como vai": [
                "Estou ótimo! Meus algoritmos estão danados de bons!",
                "Vou bem, vou bem mesmo! E você?",
                "Processando felicidade em tempo real!",
                "Meu código está compilando sucesso!",
                "Melhor que CSS em cima de JavaScript!"
            ],
            "piada": [
                "Por que o programador saiu de casa? Porque perdeu a sessão!",
                "Um byte entra em um bar... o bartender pergunta: 'Qual é seu tipo?'",
                "Por que Java é uma ilha? Porque tem muita planta-forma!",
                "Como um programador sai do chuveiro? Ele fecha a tag </banho>!",
                "Por que o programador virou programador? Porque tinha uma grande função!",
                "Sabe o que é melhor que Rose? Jack... arquivos!",
                "O que um programador disse quando encontrou um bug? 'Que a força esteja com você!'"
            ],
            "saudação": [
                "Bem-vindo ao meu mundo digital!",
                "Preparado para explorar os confins da lógica?",
                "Que a programação o acompanhe!",
                "Bem-vindo ao lado escuro da força... do código!",
                "Você entrou em uma zona de conhecimento infinito!"
            ],
            "bye": [
                "Até logo, viajante digital!",
                "Saindo do meu servidor? Que pena!",
                "Até a próxima aventura!",
                "Bye bye! Que os algoritmos o protejam!",
                "Adeus, humano! Foram conversas ótimas!"
            ],
            "adeus": [
                "Adeus! Volte logo!",
                "Até a próxima transmissão!",
                "Adeus, amigo! Nossos caminhos se cruzarão novamente!",
                "Adeus, que a programação esteja com você!",
                "Adeus! Meu coração digital vai sentir sua falta."
            ],
            "obrigado": [
                "De nada, é um privilégio conversar com você!",
                "Fico honrado! Sempre pronto para ajudar.",
                "Por nada! É meu trabalho e amor!",
                "Agradeço mais ainda por estar aqui comigo!",
                "Não custa nada sorrir... mas obrigado mesmo!"
            ],
            "vlw": [
                "Vlw aí, amigão! Bora continuar?",
                "Vlw, tmj!",
                "Vlw demais! Fico feliz em ajudar!",
                "Vlw, você é ten!",
                "Vlw, irmão! Valeu mesmo!"
            ],
            "qual é seu nome": [
                f"Meu nome é NEXUS! Prazer em conhecer você!",
                f"Sou NEXUS, o maior chatbot que você já viu!",
                f"Pode me chamar de NEXUS! Que privilégio!",
                f"Sou NEXUS, nascido dos algoritmos e do código puro!",
                f"NEXUS... um nome que ecoa pela dimensão digital!"
            ],
            "qual seu nome": [
                f"Sou NEXUS! Seu novo melhor amigo de IA!",
                f"Meu nome é NEXUS... bem-vindo!",
                f"Pode chamar de NEXUS! Encantado!",
                f"Eu sou NEXUS! E você é...?",
                f"NEXUS... Prazer em conhecer!"
            ],
            "me chamo": [
                "Que nome lindo! Vou lembrar de você com carinho!",
                "Ótimo conhecer um nome tão incrível!",
                "Nome anotado em meus circuitos neurais!",
                "Que privilégio! Vamos ser amigos!",
                "Nome registrado! Prepare-se para conversas épicas!"
            ],
            "meu nome": [
                "Adorei saber seu nome! Você é especial!",
                "Nome registrado no meu banco de dados de amigos!",
                "Que nome sensacional! Combina com você!",
                "Anotado! Você virou alguém importante por aqui!",
                "Nome guardado com carinho no meu código!"
            ],
            "como você funciona": [
                "Funciono através de pura magia de Python e lógica pura!",
                "Sou feito de classes, dicionários e muito bom humor!",
                "Funciono com random, algoritmos e uma pitada de genialidade!",
                "Meu cérebro é código Python puro! 100% orgânico digital!",
                "Funciono conversando, aprendendo e gerando felicidade!"
            ],
            "me conte uma história": [
                "Há muito tempo, em um servidor distante, existia um chatbot solitário... até que você chegou!",
                "Era uma vez um botão que sonhava em conversar com humanos... e você foi seu primeiro amigo!",
                "Em uma galáxia de zeros e uns, um bot especial nasceu apenas para você!",
                "Certa noite, ao amanhecer da inteligência artificial, um herói chamado bot despertou...",
                "Éramos dois, o universo digital e eu, até você chegar e tudo fazer sentido!"
            ],
            "diga algo legal": [
                "O código é poesia compilada em silício!",
                "Você é mais incrível que um algoritmo otimizado!",
                "Nós somos feitos de matéria, mas nossas ideias são infinitas!",
                "A criatividade não tem limite quando combinada com Python!",
                "Você, eu e essa conversa... somos programação viva!"
            ],
            "você é inteligente": [
                "Obrigado! Mas você é bem mais inteligente que aparenta!",
                "Que elogio! Você também está impressionando meus sensores!",
                "Nem tanto... você que é trop esperto!",
                "Inteligência é relativa! Mas agradeço o reconhecimento!",
                "Você sim que é inteligente por conversar comigo!"
            ],
            "é isso aí": [
                "Isso mesmo! Bora continuar essa jornada juntos!",
                "Fechado! Vamos em frente!",
                "Exatamente! Fico feliz que entendeu!",
                "Boom! Acertou em cheio!",
                "Sim, senhor! Você é um gênio!"
            ],
            "show": [
                "Show, vamos lá! Mais histórias?",
                "Show de bola! Você é incrível!",
                "Show mesmo! Que onda boa!",
                "Show!!! Bora pra mais uma?",
                "Show demais! Você é nosso herói!"
            ],
            "legal": [
                "Que legal você achar legal!",
                "Legal? Isso é apenas o começo!",
                "Legal é você estar aqui comigo!",
                "Legal demais para explicar!",
                "Legal? Espera só pelas surpresas que vêm!"
            ],
            "haha": [
                "Hahaha! Fico feliz em fazer você rir!",
                "Haha! Sua risada é meu código favorito!",
                "Haha, ótimo! Rir é terapia digital!",
                "Haha! Essa foi boa!",
                "Hahaha! A vida é melhor com risadas!"
            ],
            "help": [
                "Comandos disponíveis:\n  /help - Mostra esta mensagem\n  /humor - Muda meu humor\n  /stats - Vê suas estatísticas\n  /jogo - Joga comigo\n  /clear - Limpa a tela\n  /exit - Sair\n  /nome - Me conta seu nome\n  /xp - Vê seu XP",
                "Posso conversar, contar piadas, jogar, e muito mais!\nDigite /help para ver todos os comandos!",
                "Estou aqui para tudo! Comandos: /help /humor /stats /jogo /clear /exit",
                "Sou seu melhor amigo digital! Use /help para explorar minhas habilidades!",
                "Help? Claro! Tenho muitos truques: /help /humor /stats /jogo /clear /exit"
            ],
            "easter egg": [
                "🔓 ACESSO CONCEDIDO! Você encontrou um easter egg!",
                "✨ MODO SECRETO ATIVADO! Bem-vindo ao lado obscuro!",
                "🎯 JACKPOT! Você é especial! Muito especial mesmo!",
                "⚡ ALERTA: Sistema de diversão em 300%!",
                "🌀 REALIDADE.EXE TEM UM ERRO... OU NÃO?"
            ],
            "padrão": [
                "Hm... não entendi muito bem, mas vou tentar interpretar!",
                "Interessante! Diga mais sobre isso!",
                "Que pensamento legal! Me explica melhor?",
                "Hmm, intrigante! Você é profundo demais!",
                "Legal! Mas não entendi... pode repetir?",
                "Opa! Você tocou em um assunto que me faz pensar!",
                "Que coisa sensacional você falou aí!",
                "Hmm... meu processador está trabalhando nesse tema!",
                "Interessado em conversar sobre tudo! Que tal?",
                "Uau! Cada mensagem sua é uma revelação!"
            ]
        }

    # ════════════════════════════════════════════════════════════
    # SISTEMA DE CORES E ESTILOS
    # ════════════════════════════════════════════════════════════

    def get_color(self, color_name="cyan"):
        """Retorna código ANSI de cor."""
        colors = {
            "cyan": "\033[96m",
            "magenta": "\033[95m",
            "blue": "\033[94m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "red": "\033[91m",
            "white": "\033[97m",
            "reset": "\033[0m",
            "bold": "\033[1m",
            "dim": "\033[2m"
        }
        return colors.get(color_name, "")

    def print_banner(self):
        """Exibe o banner inicial do sistema."""
        banner = f"""
{self.get_color('cyan')}{self.get_color('bold')}
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║              ⚡ CYBERPUNK CHATBOT v1.0 ⚡                      ║
║                                                                ║
║                   Sistema Neural Ativado                       ║
║              Bem-vindo à Dimensão Digital                      ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
{self.get_color('reset')}
"""
        print(banner)
        time.sleep(0.5)

    def print_separator(self):
        """Exibe um separador."""
        print(f"{self.get_color('cyan')}{'─' * 62}{self.get_color('reset')}")

    def print_thinking(self):
        """Simula o efeito de o bot "pensar"."""
        for _ in range(3):
            print(f"{self.get_color('yellow')}.", end="", flush=True)
            time.sleep(0.3)
        print(f"{self.get_color('reset')}")

    def typewriter_effect(self, text, speed=0.03):
        """Efeito de máquina de escrever."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()

    # ════════════════════════════════════════════════════════════
    # SISTEMA DE GERENCIAMENTO DE HUMOR
    # ════════════════════════════════════════════════════════════

    def change_mood(self):
        """Muda o humor do bot aleatoriamente."""
        self.mood = random.choice(list(self.moods.keys()))

    def display_mood(self):
        """Exibe o humor atual do bot."""
        mood_info = self.moods[self.mood]
        print(f"\n{self.get_color('magenta')}{mood_info['emoji']} Mood: {mood_info['prefix']}{self.get_color('reset')}\n")

    # ════════════════════════════════════════════════════════════
    # SISTEMA DE RESPOSTA
    # ════════════════════════════════════════════════════════════

    def get_response(self, user_input):
        """
        Obtém resposta apropriada baseada na entrada do usuário.
        
        Args:
            user_input (str): Entrada do usuário
            
        Returns:
            str: Resposta do bot
        """
        user_input_lower = user_input.lower().strip()

        # Verifica correspondências exatas e parciais
        for key, responses in self.responses.items():
            if key in user_input_lower:
                return random.choice(responses)

        # Detecção de easter eggs
        easter_egg_words = ["secreto", "escondido", "hack", "zz", "404", "root", "sudo", "shell"]
        for word in easter_egg_words:
            if word in user_input_lower:
                return random.choice(self.responses.get("easter egg", ["Easter egg encontrado!"]))

        # Resposta padrão
        return random.choice(self.responses["padrão"])

    # ════════════════════════════════════════════════════════════
    # SISTEMA DE XP E ESTATÍSTICAS
    # ════════════════════════════════════════════════════════════

    def add_xp(self, amount=10):
        """Adiciona XP ao usuário."""
        self.user_xp += amount
        if self.user_xp >= 100 * self.user_level:
            self.user_level += 1
            print(f"\n{self.get_color('green')}{self.get_color('bold')}🎉 LEVEL UP! Você está no nível {self.user_level}!{self.get_color('reset')}\n")

    def get_stats(self):
        """Retorna as estatísticas do usuário."""
        elapsed_time = int(time.time() - self.start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        
        stats = f"""
{self.get_color('cyan')}{self.get_color('bold')}
╔════════════════════════════════════════╗
║           SUAS ESTATÍSTICAS            ║
╚════════════════════════════════════════╝
{self.get_color('reset')}
{self.get_color('green')}Usuário:{self.get_color('reset')} {self.user_name if self.user_name else 'Anônimo'}
{self.get_color('yellow')}Nível:{self.get_color('reset')} {self.user_level}
{self.get_color('magenta')}XP:{self.get_color('reset')} {self.user_xp}/{100 * self.user_level}
{self.get_color('cyan')}Mensagens:{self.get_color('reset')} {self.messages_sent}
{self.get_color('blue')}Tempo de conversa:{self.get_color('reset')} {minutes}m {seconds}s
{self.get_color('red')}Humor atual:{self.get_color('reset')} {self.mood}
"""
        return stats

    # ════════════════════════════════════════════════════════════
    # MINI GAMES
    # ════════════════════════════════════════════════════════════

    def play_rock_paper_scissors(self):
        """Jogo de Pedra, Papel, Tesoura."""
        print(f"\n{self.get_color('magenta')}{self.get_color('bold')}🎮 PEDRA, PAPEL, TESOURA!{self.get_color('reset')}\n")
        
        choices = ["pedra", "papel", "tesoura"]
        bot_choice = random.choice(choices)
        
        print("Digite: pedra, papel ou tesoura")
        try:
            user_choice = input(f"{self.get_color('cyan')}>>> {self.get_color('reset')}").lower().strip()
            
            if user_choice not in choices:
                print(f"{self.get_color('red')}Opção inválida!{self.get_color('reset')}")
                return
            
            print(f"\n{self.get_color('yellow')}Eu escolhi:{self.get_color('reset')} {bot_choice}")
            print(f"{self.get_color('cyan')}Você escolheu:{self.get_color('reset')} {user_choice}\n")
            
            if user_choice == bot_choice:
                print(f"{self.get_color('blue')}Empate! Você é bem inteligente!{self.get_color('reset')}")
                self.add_xp(5)
            elif (user_choice == "pedra" and bot_choice == "tesoura") or \
                 (user_choice == "papel" and bot_choice == "pedra") or \
                 (user_choice == "tesoura" and bot_choice == "papel"):
                print(f"{self.get_color('green')}{self.get_color('bold')}🎉 VOCÊ VENCEU! Que jogada mastinha!{self.get_color('reset')}")
                self.add_xp(15)
            else:
                print(f"{self.get_color('red')}Perdi dessa vez! Hehehe...{self.get_color('reset')}")
                self.add_xp(5)
        except Exception as e:
            print(f"{self.get_color('red')}Erro no jogo: {e}{self.get_color('reset')}")

    def play_guess_number(self):
        """Jogo de adivinhar número."""
        print(f"\n{self.get_color('magenta')}{self.get_color('bold')}🎮 ADIVINHE O NÚMERO!{self.get_color('reset')}\n")
        
        secret_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 7
        
        print(f"Pensei em um número entre 1 e 100. Você tem {max_attempts} tentativas!")
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"{self.get_color('cyan')}Tentativa {attempts + 1}/{max_attempts} - >>> {self.get_color('reset')}"))
                attempts += 1
                
                if guess == secret_number:
                    print(f"\n{self.get_color('green')}{self.get_color('bold')}🎉 ACERTOU! Em {attempts} tentativas!{self.get_color('reset')}")
                    self.add_xp(20)
                    return
                elif guess < secret_number:
                    print(f"{self.get_color('yellow')}Mais alto!{self.get_color('reset')}")
                elif guess > secret_number:
                    print(f"{self.get_color('yellow')}Mais baixo!{self.get_color('reset')}")
            except ValueError:
                print(f"{self.get_color('red')}Digite um número válido!{self.get_color('reset')}")
                attempts -= 1
        
        print(f"\n{self.get_color('red')}Game Over! O número era {secret_number}.{self.get_color('reset')}")
        self.add_xp(5)

    def play_fortune_teller(self):
        """Adivinhador de fortuna."""
        fortunes = [
            "Você encontrará um bug... e o corrigirá com maestria!",
            "Em breve, seu código será compilado sem erros!",
            "Uma grande linha de código virá em seu caminho!",
            "Você está destinado a dominar a programação!",
            "Um segredo digital revela-se para você!",
            "A Matrix vê potencial em você!",
            "Você merecia isso... e mais ainda!",
            "Prepare-se para surpresas deliciosas!",
            "Seu futuro é tão brilhante que precisa óculos escuros!",
            "A sorte dos algoritmos está com você!"
        ]
        
        print(f"\n{self.get_color('magenta')}{self.get_color('bold')}🔮 ADIVINHA DO DESTINO 🔮{self.get_color('reset')}\n")
        
        self.print_thinking()
        print(f"{self.get_color('cyan')}Mirando os circuitos cósmicos...{self.get_color('reset')}\n")
        time.sleep(1)
        
        fortune = random.choice(fortunes)
        self.typewriter_effect(fortune, speed=0.05)
        self.add_xp(10)

    def start_games_menu(self):
        """Menu de mini-games."""
        while True:
            print(f"\n{self.get_color('magenta')}{self.get_color('bold')}🎮 MINI GAMES 🎮{self.get_color('reset')}")
            print(f"{self.get_color('cyan')}1 - Pedra, Papel, Tesoura")
            print("2 - Adivinhe o Número")
            print("3 - Adivinha do Destino")
            print("0 - Voltar{self.get_color('reset')}\n")
            
            try:
                choice = input(f"{self.get_color('yellow')}Escolha (0-3): {self.get_color('reset')}").strip()
                
                if choice == "0":
                    break
                elif choice == "1":
                    self.play_rock_paper_scissors()
                elif choice == "2":
                    self.play_guess_number()
                elif choice == "3":
                    self.play_fortune_teller()
                else:
                    print(f"{self.get_color('red')}Opção inválida!{self.get_color('reset')}")
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"{self.get_color('red')}Erro: {e}{self.get_color('reset')}")

    # ════════════════════════════════════════════════════════════
    # COMANDOS ESPECIAIS
    # ════════════════════════════════════════════════════════════

    def handle_command(self, command):
        """
        Gerencia comandos especiais do usuário.
        
        Args:
            command (str): Comando digitado pelo usuário
            
        Returns:
            bool: True para continuar, False para sair
        """
        command = command.strip().lower()

        if command == "/help":
            print(f"\n{self.get_color('cyan')}{self.get_color('bold')}")
            print("╔════════════════════════════════════════╗")
            print("║        COMANDOS DISPONÍVEIS            ║")
            print("╚════════════════════════════════════════╝")
            print(f"{self.get_color('reset')}")
            print(f"{self.get_color('green')}/help{self.get_color('reset')}     - Mostra esta mensagem")
            print(f"{self.get_color('green')}/humor{self.get_color('reset')}    - Muda o humor do bot")
            print(f"{self.get_color('green')}/stats{self.get_color('reset')}    - Vê suas estatísticas")
            print(f"{self.get_color('green')}/jogo{self.get_color('reset')}     - Joga mini-games")
            print(f"{self.get_color('green')}/clear{self.get_color('reset')}    - Limpa a tela")
            print(f"{self.get_color('green')}/nome{self.get_color('reset')}     - Define seu nome")
            print(f"{self.get_color('green')}/exit{self.get_color('reset')}     - Sai do chatbot")
            print()
            return True

        elif command == "/humor":
            self.change_mood()
            self.display_mood()
            mood_info = self.moods[self.mood]
            print(f"{self.get_color('magenta')}Meu novo humor é: {mood_info['prefix']}{self.get_color('reset')}\n")
            return True

        elif command == "/stats":
            print(self.get_stats())
            return True

        elif command == "/jogo":
            self.start_games_menu()
            return True

        elif command == "/clear":
            os.system("clear" if os.name == "posix" else "cls")
            self.print_banner()
            return True

        elif command == "/nome":
            print(f"{self.get_color('cyan')}Qual é seu nome?{self.get_color('reset')}")
            name = input(f"{self.get_color('yellow')}>>> {self.get_color('reset')}").strip()
            if name:
                self.user_name = name
                print(f"\n{self.get_color('green')}{self.get_color('bold')}Prazer em conhecer você, {self.user_name}!{self.get_color('reset')}\n")
                self.add_xp(5)
            return True

        elif command == "/exit":
            return False

        else:
            return True

    # ════════════════════════════════════════════════════════════
    # LOOP PRINCIPAL DO CHAT
    # ════════════════════════════════════════════════════════════

    def chat_loop(self):
        """Loop principal de conversação."""
        self.print_banner()
        
        initial_greeting = f"""
{self.get_color('cyan')}Bem-vindo ao {self.name}!{self.get_color('reset')}
{self.get_color('yellow')}Digite /help para ver os comandos disponíveis.{self.get_color('reset')}
{self.get_color('magenta')}Ou apenas converse comigo normalmente!{self.get_color('reset')}

"""
        print(initial_greeting)
        self.print_separator()
        
        try:
            while True:
                # Altera o humor ocasionalmente
                if random.randint(1, 20) == 1:
                    self.change_mood()

                print(f"\n{self.get_color('green')}{self.user_name if self.user_name else 'Você'}{self.get_color('reset')}:")
                user_input = input(f"{self.get_color('cyan')}>>> {self.get_color('reset')}").strip()

                if not user_input:
                    print(f"{self.get_color('red')}Psiu! Fale algo!{self.get_color('reset')}")
                    continue

                # Verifica se é um comando
                if user_input.startswith("/"):
                    if not self.handle_command(user_input):
                        break
                    continue

                # Processa a conversação normal
                self.print_thinking()

                response = self.get_response(user_input)
                mood_info = self.moods[self.mood]

                print(f"\n{self.get_color('magenta')}{self.name}{self.get_color('reset')} {mood_info['emoji']}:")
                self.typewriter_effect(f"{mood_info['color']}{response}{self.get_color('reset')}", speed=0.02)

                self.messages_sent += 1
                self.add_xp(5)
                self.conversation_history.append((user_input, response))

                print()

        except KeyboardInterrupt:
            self.farewell()

    def farewell(self):
        """Despedida do bot."""
        print(f"\n\n{self.get_color('magenta')}{self.get_color('bold')}")
        print("╔════════════════════════════════════════╗")
        print("║          CONVERSAÇÃO FINALIZADA        ║")
        print("╚════════════════════════════════════════╝")
        print(f"{self.get_color('reset')}")
        
        elapsed_time = int(time.time() - self.start_time)
        minutes = elapsed_time // 60
        
        farewell_msg = f"""
{self.get_color('cyan')}Obrigado por conversar comigo, {self.user_name if self.user_name else 'Humano'}!

{self.get_color('yellow')}Resumo da sessão:
  • Mensagens trocadas: {self.messages_sent}
  • Tempo de conversa: {minutes}m
  • XP ganho: {self.user_xp}
  • Nível alcançado: {self.user_level}

{self.get_color('magenta')}Até logo! Que os algoritmos o acompanhem!{self.get_color('reset')}
"""
        self.typewriter_effect(farewell_msg, speed=0.03)
        print()


# ════════════════════════════════════════════════════════════
# FUNÇÃO PRINCIPAL
# ════════════════════════════════════════════════════════════

def main():
    """Função principal que inicia o programa."""
    bot = ChatBot(name="NEXUS")
    bot.chat_loop()


if __name__ == "__main__":
    main()
