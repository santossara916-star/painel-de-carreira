import streamlit as st

# Configuração da página do aplicativo
st.set_page_config(
    page_title="Seu Painel de Carreira", 
    page_icon="💼", 
    layout="centered"
)

# --- INICIALIZAÇÃO DO ESTADO DA SESSÃO (Banco de dados temporário do usuário) ---
if 'fase_atual' not in st.session_state:
    st.session_state.fase_atual = "Boas-Vindas"
if 'pontos_disc' not in st.session_state:
    st.session_state.pontos_disc = {"D": 0, "I": 0, "S": 0, "C": 0}
if 'expectativa' not in st.session_state:
    st.session_state.expectativa = ""
if 'gosto_faço' not in st.session_state:
    st.session_state.gosto_faço = []
if 'profissoes_selecionadas' not in st.session_state:
    st.session_state.profissoes_selecionadas = []
if 'pros_contras' not in st.session_state:
    st.session_state.pros_contras = {}
if 'notas_balanca' not in st.session_state:
    st.session_state.notas_balanca = {}
if 'plano_acao' not in st.session_state:
    st.session_state.plano_acao = {"futuro": "", "estudo": "", "conversa": "", "carta": ""}

# BANCO DE DADOS DE PROFISSÕES PARA O SHOPPING
BANCO_PROFISSÕES = {
    "Analista de Dados / BI": {"perfil": "C", "desc": "Coleta e estuda dados do mercado e da empresa para ajudar nas tomadas de decisões certas."},
    "Gestor de Logística": {"perfil": "C", "desc": "Organiza rotas, estoques e o transporte de mercadorias para garantir prazos com menor custo."},
    "Analista Financeiro": {"perfil": "C", "desc": "Cuida dos investimentos, custos, lucros e do planejamento de dinheiro de empresas ou pessoas."},
    "Desenvolvedor de Software": {"perfil": "C", "desc": "Escreve códigos, cria a estrutura de sistemas e gerencia os bastidores de apps e sites."},
    "Gerente de Projetos": {"perfil": "D", "desc": "Lidera equipes, controla prazos e garante que o planejamento de um produto/serviço seja entregue."},
    "Gestor de Tráfego Pago": {"perfil": "D", "desc": "Administra investimentos em anúncios na internet (Instagram, Google) focado em gerar vendas rápido."},
    "Administrador de Empresas": {"perfil": "D", "desc": "Coordena o dia a dia de uma empresa, cobra resultados das equipes e resolve problemas práticos."},
    "Engenheiro de Produção": {"perfil": "D", "desc": "Organiza fábricas, linhas de produção e processos industriais para produzir mais gastando menos."},
    "Executivo de Vendas": {"perfil": "I", "desc": "Negocia diretamente com clientes, descobre as necessidades deles e fecha contratos de alto valor."},
    "Profissional de Relações Públicas": {"perfil": "I", "desc": "Cuida da imagem de marcas ou pessoas e organiza grandes experiências e parcerias com o mercado."},
    "Sucesso do Cliente (CS)": {"perfil": "I", "desc": "Acompanha os clientes após a compra, garantindo que eles tenham a melhor experiência com o produto."},
    "Recrutamento e Seleção (RH)": {"perfil": "I", "desc": "Entrevista pessoas, analisa perfis profissionais e escolhe os talentos certos para as empresas."},
    "Designer de UX/UI": {"perfil": "S", "desc": "Cria o visual, as telas e o fluxo que tornam o uso de aplicativos e sites fácil, intuitivo e bonito."},
    "Estrategista de Social Media": {"perfil": "S", "desc": "Cria conceitos visuais, roteiros de vídeo e estratégias de posicionamento para marcas no digital."},
    "Designer Gráfico / Diretor de Arte": {"perfil": "S", "desc": "Traduz ideias em identidades visuais impactantes, campanhas publicitárias e projetos gráficos."},
    "Product Owner (PO)": {"perfil": "S", "desc": "Imagina o futuro de um produto tecnológico, mapeia novas funções e guia o que o time vai desenvolver."}
}

# --- TELA: BOAS-VINDAS ---
if st.session_state.fase_atual == "Boas-Vindas":
    st.title("💼 Seu Painel de Carreira")
    st.markdown("---")
    st.subheader("Seja bem-vindo!")
    st.write(
        "Você sabia que, no Brasil, **59% dos estudantes desistem ou trocam de curso** após entrarem na faculdade? "
        "É o que apontam os dados oficiais do **Inep/MEC**. E o principal motivo apontado por especialistas é um só: "
        "a escolha precoce e errada da profissão aos 17 ou 18 anos."
    )
    st.write(
        "Escolher uma carreira no escuro, baseado apenas no que os outros dizem que dá dinheiro, é a receita perfeita "
        "para rasgar o seu tempo e frustrar suas expectativas. Para você não fazer parte dessa estatística, criamos este sistema guiado."
    )
    st.info("Sua jornada será dividida em 4 fases práticas e automáticas. Vamos começar?")
    if st.button("Iniciar Missão Identidade 🚀"):
        st.session_state.fase_atual = "Fase 1"
        st.rerun()

# --- FASE 1: MISSÃO IDENTIDADE & COMPORTAMENTO ---
elif st.session_state.fase_atual == "Fase 1":
    st.title("🟢 Fase 1: Missão Identidade")
    st.progress(25)
    st.markdown("---")
    
    # Painel das Expectativas
    st.markdown("### 1. Alinhamento de Expectativas") [cite: 16]
    st.session_state.expectativa = st.text_input(
        "Em uma frase, qual o seu maior objetivo ao terminar este diagnóstico hoje?",
        placeholder="Ex: Descobrir se combino mais com Logística ou Tecnologia..."
    )
    
    st.markdown("---")
    
    # Gosto e Faço
    st.markdown("### 2. Painel de Habilidades (Gosto e Faço)") [cite: 15]
    st.write("Selecione as habilidades que você mais se identifica no dia a dia:")
    opcoes_habilidades = ["Gerenciar projetos/prazos", "Analisar dados e números", "Criar designs ou conceitos visuais", "Escrever ou criar conteúdo", "Negociar ou vender ideias", "Organizar fluxos e processos"]
    st.session_state.gosto_faço = st.multiselect("Eu gosto e tenho facilidade em:", opcoes_habilidades)
    
    st.markdown("---")
    
    # Teste DISC Camuflado
    st.markdown("### 3. Cenários de Comportamento") [cite: 20]
    st.write("Escolha a opção que melhor descreve sua forma real de agir, sem pensar em profissões ainda:")
    
    votos = {"D": 0, "I": 0, "S": 0, "C": 0}
    
    c1 = st.radio("Cenário 1: Diante de um desafio ou problema complexo:", ["Prefiro agir rápido, focar no resultado e resolver logo a situação.", "Prefiro analisar as regras, os dados e entender a lógica antes de fazer qualquer coisa."])
    votos["D" if "agir rápido" in c1 else "C"] += 1

    c2 = st.radio("Cenário 2: Em trabalhos de grupo ou projetos de equipe:", ["Gosto de organizar as tarefas nos bastidores, pesquisar e garantir que a entrega não tenha erros.", "Prefiro conversar com as pessoas, defender as ideias do grupo e cuidar da comunicação."])
    votos["C" if "bastidores" in c2 else "I"] += 1

    c3 = st.radio("Cenário 3: Em qual tipo de ambiente você sente que rende mais?", ["Em um ambiente previsível, com rotina bem definida e sem mudanças bruscas.", "Em um ambiente dinâmico, onde as coisas mudam rápido e surgem novidades."])
    votos["S" if "previsível" in c3 else "D"] += 1
    
    if st.button("Gravar Dados e Avançar 🔒"):
        if not st.session_state.expectativa or not st.session_state.gosto_faço:
            st.warning("Por favor, preencha o seu objetivo e selecione pelo menos uma habilidade antes de avançar.")
        else:
            st.session_state.pontos_disc = votos
            st.session_state.fase_atual = "Fase 2"
            st.rerun()

# --- FASE 2: O FILTRO DO MERCADO (SHOPPING OCUPACIONAL) ---
elif st.session_state.fase_atual == "Fase 2":
    st.title("🔵 Fase 2: Radar do Mercado")
    st.progress(50)
    st.markdown("---")
    
    st.markdown("### O Shopping das Profissões") [cite: 28, 32]
    st.write("Abaixo estão listadas algumas das profissões mais demandadas do mercado atual. Explore os cards e filtre os seus interesses.")
    
    interesses_verificados = []
    
    for prof, dados in BANCO_PROFISSÕES.items():
        with st.expander(f"💼 {prof}"):
            st.write(f"**O que faz na prática:** {dados['desc']}")
            escolha = st.radio(f"Classifique seu interesse em {prof}:", ["Não tenho interesse", "Tenho dúvidas", "Tenho interesse"], key=prof)
            if escolha == "Tenho interesse":
                interesses_verificados.append(prof)
                
    st.markdown("---")
    st.markdown("### Seus Finalistas (Mapeamento de Prós e Contras)") [cite: 34]
    st.write("Para avançar, selecione exatamente **3 profissões** que você marcou com 'Tenho interesse' no painel acima:")
    
    st.session_state.profissoes_selecionadas = st.multiselect("Suas 3 escolhas finalistas:", interesses_verificados)
    
    if len(st.session_state.profissoes_selecionadas) == 3:
        st.write("Preencha rapidamente um ponto positivo e um negativo que você enxerga para cada uma:")
        for p in st.session_state.profissoes_selecionadas:
            st.write(f"**{p}**")
            pro = st.text_input(f"Ponto Positivo de {p}:", key=f"pro_{p}")
            contra = st.text_input(f"Ponto Negativo de {p}:", key=f"contra_{p}")
            st.session_state.pros_contras[p] = {"pró": pro, "contra": contra}
            
        if st.button("Salvar Filtros e Rodar Diagnóstico ⚙️"):
            st.session_state.fase_atual = "Fase 3"
            st.rerun()
    else:
        st.warning("Selecione exatamente 3 profissões para liberar a próxima etapa.")

# --- FASE 3: A BALANÇA DA ESCOLHA & DEVOLUTIVA DISC ---
elif st.session_state.fase_atual == "Fase 3":
    st.title("🟡 Fase 3: A Balança da Escolha")
    st.progress(75)
    st.markdown("---")
    
    # Revelação do Perfil DISC
    st.markdown("### 1. Diagnóstico do seu Perfil de Comportamento") [cite: 24]
    maior_perfil = max(st.session_state.pontos_disc, key=st.session_state.pontos_disc.get)
    
    perfis_texto = {
        "D": ("Dominância (Executor)", "Focado em resultados, metas e ação rápida. Funciona muito bem sob pressão, gosta de desafios e tem uma liderança natural para tirar projetos do papel."),
        "I": ("Influência (Comunicador)", "Focado em pessoas, conexões e comunicação. Tem grande facilidade para expressar ideias, engajar equipes e negociar."),
        "S": ("Estabilidade (Planejador)", "Focado em colaboração, ritmo constante e segurança. Prefere ambientes com rotinas claras e busca equilíbrio e consistência."),
        "C": ("Conformidade (Analítico)", "Focado em lógica, precisão, dados e regras. Rende muito quando precisa analisar problemas complexos e organizar informações.")
    }
    
    st.success(f"**Seu perfil comportamental predominante é: {perfis_texto[maior_perfil][0]}**")
    st.write(perfis_texto[maior_perfil][1])
    
    st.markdown("---")
    
    # A Balança da Escolha
    st.markdown("### 2. Matriz de Critérios (A Balança)") [cite: 39, 42]
    st.write("Atribua uma nota de 1 a 5 para avaliar a realidade de cada uma das suas 3 profissões finalistas:")
    
    ranking = {}
    for p in st.session_state.profissoes_selecionadas:
        st.markdown(f"#### Avaliação para: {p}")
        
        # Sinalizador de compatibilidade inteligente de IA
        if BANCO_PROFISSÕES[p]["perfil"] == maior_perfil:
            st.caption("🔥 *Nota do Sistema: Esta profissão tem alto alinhamento com o seu perfil comportamental.*")
            
        financeiro = st.slider(f"Retorno Financeiro: O ganho dessa carreira atende aos meus objetivos de vida?", 1, 5, 3, key=f"fin_{p}")
        rotina = st.slider(f"Dia a Dia: Eu me vejo executando a rotina real e prática desse trabalho semanalmente?", 1, 5, 3, key=f"rot_{p}")
        entrada = st.slider(f"Custo de Entrada: Estou disposto a encarar a faculdade ou a preparação necessária?", 1, 5, 3, key=f"ent_{p}")
        
        # Cálculo da média das notas
        total = (financeiro + rotina + entrada) / 3
        ranking[p] = round(total, 2)
        
    st.markdown("---")
    if st.button("Calcular e Ver o Ranking Final 🏆"):
        st.session_state.notas_balanca = dict(sorted(ranking.items(), key=lambda item: item[1], reverse=True))
        st.session_state.fase_atual = "Fase 4"
        st.rerun()

# --- FASE 4: PLANO DE ATIVAÇÃO & DEVOLUTIVA FINAL ---
elif st.session_state.fase_atual == "Fase 4":
    st.title("🔴 Fase 4: Plano de Ativação")
    st.progress(100)
    st.markdown("---")
    
    # Exibição do Pódio
    st.markdown("### Seu Pódio de Carreiras Alinhadas")
    posições = ["🥇 1º Lugar", "🥈 2º Lugar", "🥉 3º Lugar"]
    for i, (prof, nota) in enumerate(st.session_state.notas_balanca.items()):
        st.subheader(f"{posições[i]}: {prof} (Média da Balança: {nota})")
        
    st.markdown("---")
    
    # Semana de Trabalho no Futuro e Plano de Ação
    st.markdown("### Construção da sua Rota Prática") [cite: 46, 47]
    carreira_vencedora = list(st.session_state.notas_balanca.keys())[0]
    
    st.session_state.plano_acao["futuro"] = st.text_area(
        f"Imagine uma semana de trabalho perfeita no futuro como {carreira_vencedora}. Descreva como seria sua rotina:", [cite: 46]
        placeholder="Onde você está trabalhando? O que está fazendo na tela do computador ou com as pessoas?"
    )
    
    st.session_state.plano_acao["estudo"] = st.text_input(
        "Qual faculdade, curso técnico ou certificação você vai pesquisar formalmente essa semana para começar?",
        placeholder="Ex: Grade curricular do curso X na faculdade Y..."
    )
    
    st.session_state.plano_acao["conversa"] = st.text_input(
        "Quem é o profissional da área ou canal que você vai acompanhar para entender o mercado real?",
        placeholder="Ex: Procurar um profissional de sucesso no LinkedIn e analisar os posts dele..."
    )
    
    st.session_state.plano_acao["carta"] = st.text_area(
        "Sua Carta para o Futuro: Deixe um recado para você mesmo lembrar o motivo de estar escolhendo esse caminho hoje:", [cite: 49]
        placeholder="Escreva o que espera de você nos próximos anos..."
    )
    
    st.markdown("---")
    
    # Relatório de Devolutiva Final e Ganho de Upsell
    if st.button("Finalizar e Emitir Projeto de Carreira 📑"): [cite: 48]
        st.success("Tudo pronto! Seus dados foram compilados com sucesso.")
        
        # Simulação estruturada do Relatório/PDF na tela
        with st.expander("👁️ Visualizar Resumo do seu Relatório de Devolutiva", expanded=True): [cite: 48]
            st.markdown(f"**Objetivo Declarado:** {st.session_state.expectativa}") [cite: 16]
            st.markdown(f"**Perfil Comportamental:** {perfis_texto[max(st.session_state.pontos_disc, key=st.session_state.pontos_disc.get)][0]}") [cite: 24]
            st.markdown(f"**Carreira Recomendada:** {carreira_vencedora}")
            st.markdown(f"**Próximo Passo Prático:** Pesquisar sobre: *{st.session_state.plano_acao['estudo']}*") [cite: 47]
            
        st.markdown("---")
        
        # Estratégia de Negócio / Upsell
        st.markdown("### ⚡ Próximo Passo Comigo")
        st.write(
            "Você acabou de mapear a sua direção e criar as suas primeiras metas sozinhos. "
            "Mas o mercado de trabalho real exige validação e conexões estratégicas."
        )
        st.info(
            "Quer que eu analise pessoalmente o seu Projeto de Carreira gerado aqui, valide o seu plano de ação "
            "e te acompanhe no passo a passo para garantir que você não erre o alvo? "
            "Toque no botão abaixo para agendar sua vaga na minha Mentoria Individual."
        )
        st.markdown("[Falar com a Mentora no WhatsApp (Agendar Mentoria)](https://wa.me/seu_numero_aqui)")
