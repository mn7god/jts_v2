#!usr/bin/env python3
r = "\033[0;49;91m"
g = "\033[0;49;92m"
y = "\033[0;49;93m"
b = "\033[0;49;94m"
p = "\033[0;49;95m"
b2 = "\033[0;49;96m"
d = "\033[2;37m"
w = "\033[0m"
espaco = ""
linhas = espaco + "_"*9
headers = {"User-Agent":"Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.334; U; id) Presto/2.5.25 Version/10.54"}
import phonenumbers
import sys
import os
import json
import time
import math # é do w3irdguy xddd
import phonenumbers
import requests
import pprint
import http.client
import re, sys, textwrap, socket
from lxml.html import fromstring
from getpass import getpass
from shutil import which
os.system("clear")
def banner():
        print(f"""{r}
  888888 88888888888  .d8888b.
    "88b     888     d88P  Y88b
     888     888     Y88b.
     888     888      "Y888b.
     888     888         "Y88b.
     888     888           "888
     88P     888     Y88b  d88P
     888     888      "Y8888P"
   .d88p                      :-:  .:---=
  .d88p"                      @@@@@@@@@@@=
 888P"                       #@@@@@@@@@@@@
                            -@@@@@@@@@@@@@@

                           :+#@@@@@@@@@@@%*-          
                       +@@@@@@@@@@@@@@@@@@@@@@@#:      
                            :+*+:     .+**-         
                          :%+   +@-=-%#.  -@=        
                          ++     *@:*@.    :%         
                          :%+   +@: .%#.  -@=        
                            :+#+-     :=#*-        
        \033[m""")

try:
  while True:
      os.system("clear")
      banner()
      print(f"{r} 01 {y} Benefícios Sociais")
      print(f"{r} 02 {y} Pessoas Desaparecidas")
      print(f"{r} 03 {y} Consulta De Processos")
      print(f"{r} 04 {y} Busca de Informações Via CPF/CNPJ/CRM/CNA")
      print(f"{r} 05 {y} Telecom(número telefônico)")
      print(f"{r} 06 {y} Estação Rádio Base - ERBs")
      print(f"{r} 07 {y} Informações Acadêmicas")
      print(f"{r} 08 {y} Mapas e Georreferenciamento")
      print(f"{r} 09 {y} Saúde")
      print(f"{r} 10 {y} Motores de Busca Contexto Brasil")
      print(f"{r} 11 {y} Rede Social")
      print(f"{r} 12 {y} Indexadores de Serviço de Mensagens Instantâneas")
      print(f"{r} 13 {y} Consulta de Tranporte Terrestre")
      print(f"{r} 14 {y} Consulta de Transporte Áereo")
      print(f"{r} 15 {y} Câmeras Online")
      print(f"{r} 16 {y} Outros...")
      print("")
      print(f"{g} <99> {y} Voltar para o menu principal")
      print(f"{g} <00> {y} Sair")
      resp = int(input(f"{r} Opção: {g}"))
      if(resp == 1):
        while True:
          os.system("clear")
          banner()
          print(f"{g} 1 {y} Consulta Benefícios Sociais")
          print(f"{g} 2 {y} Consulta Auxílio Emergencial")
          print(f"{g} 3 {y} Comprovante De Situação Cadastral de PJ")
          print(f"{g} 4 {y} Consulta de Valores a Receber do Sistema Financeiro")
          print(f"{g} 5 {y} Consulta de Valores a Receber do Sistema Financeiro 2")
          print(" ")
          print(f"{g} 0 {y} Voltar")
          rsp = int(input(">>> "))
          if(rsp == 1):
            os.system("xdg-open https://www.beneficiossociais.caixa.gov.br/consulta/beneficio/04.01.00-00_00.asp")
            time.sleep(1)
            continue
          elif(rsp == 2):
            os.system("xdg-open https://consultaauxilio.cidadania.gov.br/consulta/#/")
            time.sleep(1)
            continue
          elif(rsp == 3):
            os.system("xdg-open http://www.receita.fazenda.gov.br/PessoaJuridica/CNPJ/cnpjreva/Cnpjreva_Solicitacao.asp")
            time.sleep(1)
            continue
          elif(rsp == 4):
            os.system("xdg-open https://valoresareceber.bcb.gov.br/publico/")
            time.sleep(1)
            continue
          elif(rsp == 5):
            inpt = input("Digite o CPF sem traços ou símbolos: ")
            antiput = input("Digite a data de nascimento separada por traços(Ex: 2001-12-01)> ")
            os.system("xdg-open https://valoresareceber.bcb.gov.br/publico/rest/valoresAReceber/{iput}/{antiput}")
            time.sleep(1)
            continue
          elif(rsp == 0):
            break
          else:
            time.sleep(1)
            continue
      elif(resp == 2):
        while True:
          os.system("clear")
          banner()
          print(f"{r} 01 {y} Site 1")
          print(f"{r} 02 {y} Site 2")
          print(f"{r} 03 {y} Site 3")
          print(f"{r} 04 {y} Site 4")
          print(f"{r} 05 {y} Site 5")
          print(f"{r} 06 {y} Site 6")
          print(f"{r} 07 {y} Site 7")
          print(f"{r} 08 {y} Site 8")
          print(f"{r} 09 {y} Site 9")
          print(f"{r} 10 {y} Site 10")
          print(f"{r} 11 {y} Site 11")
          print(f"{r} 12 {y} Site 12")
          print(f"{r} 13 {y} Site 13")
          print(f"{r} 14 {y} Site 14")
          print(f"{r} 15 {y} Site 15")
          print(f"{r} 16 {y} Site 16")
          print(f"{r} 17 {y} Site 17")
          print(f"{r} 18 {y} Site 18")
          print(f"{r} 19 {y} Site 19")
          print(f"{r} 20 {y} Site 20")
          print(f"{r} 21 {y} Site 21(Usa o CPF do desaparecido)")
          print(f"{r} 22 {y} Site 22(Usa o CPF do desaparecido)")
          print(f"")
          print(f"{g} 0 {y} Voltar")
          rsp = int(input(">>> "))
          if(rsp == 1):
            os.system("xdg-open https://desaparecidos.pcivil.rj.gov.br/pesquisar")
            time.sleep(1)
            continue
          elif(rsp == 2):
            os.system("xdg-open https://www.desaparecidos.pr.gov.br/desaparecidos/")
            time.sleep(1)
            continue
          elif(rsp == 3):
            os.system("xdg-open https://www.pc.rs.gov.br/desaparecidos")
            time.sleep(1)
            continue
          elif(rsp == 4):
            os.system("xdg-open https://desaparecidos.pjc.mt.gov.br/inicio")
            time.sleep(1)
            continue
          elif(resp == 5):
            os.system("xdg-open https://carapicuiba.sp.gov.br/desaparecido")
            time.sleep(1)
            continue
          elif(rsp == 6):
            os.system("xdg-open https://desaparecidosdobrasil.org/pesquisar-desaparecidos/")
            time.sleep(1)
            continue
          elif(rsp == 7):
            time.sleep(1)
            os.system("xdg-open https://desaparecidosdobrasil.org/pesquisar-desaparecidos/")
            continue
          elif(rsp == 8):
            os.system("xdg-open https://www.pcdf.df.gov.br/servicos/desaparecidos")
            time.sleep(1)
            continue
          elif(resp == 9):
            os.system("xdg-open https://www.disquedenuncia.org.br/desaparecidos-list")
            time.sleep(1)
            continue
          elif(rsp == 10):
            os.system("xdg-open https://www.ssp.ma.gov.br/disque-denuncia/desaparecidos/")
            time.sleep(1)
            continue
          elif(rsp == 11):
            os.system("xdg-open https://desaparecidos.pc.sc.gov.br/#/")
            time.sleep(1)
            continue
          elif(rsp == 12):
            os.system("xdg-open https://www.pm.sc.gov.br/sos-desaparecidos/default/index?sort=-desaparecido_desaparecimento_data")
            time.sleep(1)
            continue
          elif(resp == 13):
            os.system("xdg-open http://www.policiacivil.pe.gov.br/adultos-desaparecidos")
            time.sleep(1)
            continue
          elif(rsp == 14):
            os.system("xdg-open https://www2.bauru.sp.gov.br/desaparecidos/")
            time.sleep(1)
            continue
          elif(rsp == 15):
            os.system("xdg-open https://www.pm.ce.gov.br/desaparecidos/")
            time.sleep(1)
            continue
          elif(rsp == 16):
            os.system("xdg-open https://desaparecidos.pb.gov.br/desaparecidos/desaparecidos.jsf")
            time.sleep(1)
            continue
          elif(resp == 17):
            os.system("xdg-open https://desaparecidos.pr.gov.br/desaparecidos/desaparecidos.do?action=iniciarProcesso&m=false")
            time.sleep(1)
            continue
          elif(rsp == 18):
            os.system("xdg-open http://sisgou.seds.al.gov.br/base2/desaparecidos_almanaque/")
            time.sleep(1)
            continue
          elif(rsp == 19):
            os.system("xdg-open http://www.feiradesantana.ba.gov.br/seprev/desaparecidos/desaparecidos.asp")
            time.sleep(1)
            continue
          elif(rsp == 20):
            os.system("xdg-open https://www.policiacivil.se.gov.br/desaparecidos/")
            time.sleep(1)
            continue
          elif(resp == 21):
            os.system("xdg-open https://www.ssp.sp.gov.br/servicos/desaparecidos")
            time.sleep(1)
            continue
          elif(rsp == 22):
            os.system("xdg-open https://www.policiacientifica.sp.gov.br/iml/consultadesaparecidos")
            time.sleep(1)
            continue
          elif(rsp == 0):
            break
          else:
            print("invalid option")
            time.sleep(1)
            continue
      elif(resp == 3):
        while True:
          os.system("clear")
          banner()
          print(f"{r} 01 {y} Site 1")
          print(f"{r} 02 {y} Site 2")
          print(f"{r} 03 {y} Site 3")
          print(f"{r} 04 {y} Site 4")
          print(f"{r} 05 {y} Site 5")
          print(f"{r} 06 {y} Site 6")
          print(f"{r} 07 {y} Site 7")
          print(f"{r} 08 {y} Site 8")
          print(f"{r} 09 {y} Banco Nacional de Mnadados de Prisão")
          print(f"{r} 10 {y} TRF 1")
          print(f"{r} 11 {y} TRF 2")
          print(f"{r} 12 {y} TRF 3")
          print(f"{r} 13 {y} JusBRASIL")
          print(f"{r} 14 {y} Escavador")
          print(f"")
          print(f"{g} 0 {y} Voltar")
          rsp = int(input(">>> "))
          if(rsp == 1):
            os.system("xdg-open https://esaj.tjac.jus.br/esaj/portal.do?servico=190090#")
            time.sleep(1)
            continue
          elif(rsp == 2):
            os.system("xdg-open https://www.tjba.jus.br/portal/busca-resultado/#")
            time.sleep(1)
            continue
          elif(rsp == 3):
            os.system("xdg-open https://esaj.tjce.jus.br/esaj/portal.do?servico=190090#")
            time.sleep(1)
            continue
          elif(rsp == 4):
            os.system("xdg-open https://esaj.tjsc.jus.br/esaj/portal.do?servico=190090#")
            time.sleep(1)
            continue
          elif(resp == 5):
            os.system("xdg-open https://esaj.tjsp.jus.br/esaj/portal.do?servico=190090#")
            time.sleep(1)
            continue
          elif(rsp == 6):
            os.system("xdg-open http://esaj.tjac.jus.br/esaj/portal.do?servico=190090#")
            time.sleep(1)
            continue
          elif(rsp == 7):
            os.system("xdg-open http://esaj.tjam.jus.br/esaj/portal.do?servico=190090#")
            time.sleep(1)
            continue
          elif(rsp == 8):
            os.system("xdg-open http://esaj.tjce.jus.br/esaj/portal.do?servico=190090#")
            time.sleep(1)
            continue
          elif(resp == 9):
            os.system("xdg-open https://portalbnmp.cnj.jus.br/#/pesquisa-peca#")
            time.sleep(1)
            continue
          elif(rsp == 10):
            os.system("xdg-open https://portal.trf1.jus.br/")
            time.sleep(1)
            continue
          elif(rsp == 11):
            os.system("xdg-open https://portal.trf2.jus.br/")
            time.sleep(1)
            continue
          elif(rsp == 12):
            os.system("xdg-open https://portal.trf5.jus.br/")
            time.sleep(1)
            continue
          elif(resp == 13):
            os.system("xdg-open https://www.jusbrasil.com.br/")
            time.sleep(1)
            continue
          elif(rsp == 14):
            os.system("xdg-open https://www.escavador.com/")
            time.sleep(1)
            continue
          elif(rsp == 0):
            break
          else:
            print("invalid option")
            time.sleep(1)
            continue
      elif(resp == 4):
        while True:
          print(f"{r} 01 {y} Site 1 CNPJ")
          print(f"{r} 02 {y} Site 2 CNPJ")
          print(f"{r} 03 {y} Site 3 CNPJ")
          print(f"{r} 04 {y} Site 4 CNPJ")
          print(f"{r} 05 {y} Site 5 CNPJ")
          print(f"{r} 06 {y} Site 6 CNPJ")
          print(f"{r} 07 {y} Site 7 CNPJ")
          print(f"{r} 08 {y} Site 8 CNPJ")
          print(f"{r} 09 {y} Site 9 CNPJ")
          print(f"{r} 10 {y} Busca Nome pelo CPF/CNPJ")
          print(f"{r} 11 {y} Nome Completo pelo CPF/CNPJ")
          print(f"{r} 12 {y} Visualização de Dados Públicos(CNPJ)")
          print(f"{r} 13 {y} Visualização de Dados Públicos 2(CNPJ)")
          print(f"{r} 14 {y} Antecedentes Criminais")
          print(f"{r} 15 {y} Consulta Cadastro Nacional dos Advogados(CNA)")
          print(f"{r} 16 {y} Consulta Conselho Federal de Medicina(CFM)")
          print(f"{r} 17 {y} Consulta Conselho Federal de Psicologia(CFP)")
          print(f"{r} 18 {y} Consulta Conselho Federal de Engenharia e Agronomia(Confea)")
          print(f"{r} 19 {y} Consulta MEI")
          print(f"{r} 20 {y} Declaração Simples Nacional")
          print(f"{r} 21 {y} Declaração Simples Nacional 2")
          print(f"{r} 22 {y} Consulta Comunicação de Decisão so Requerimento/Benefício")
          print(f"{r} 23 {y} Consulta Restituição do Imposto de Renda")
          print(f"{r} 24 {y} Consulta Junta Comercial do Estado de São Paulo")
          print(f"{r} 25 {y} Consulta Entrevistador do IBGE")
          print(f"{r} 25 {y} Consulta Entrevistador do IBGE 2")
          print(f"")
          print(f"{g} 0 {y} Voltar")
          rsp = int(input(">>> "))
          if(rsp == 1):
            os.system("xdg-open http://servicos.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao.asp")
            time.sleep(1)
            continue
          elif(rsp == 2):
            os.system("xdg-open https://brasilcnpj.net/")
            time.sleep(1)
            continue
          elif(rsp == 3):
            os.system("xdg-open https://cnpj.biz/")
            time.sleep(1)
            continue
          elif(rsp == 4):
            os.system("xdg-open https://cadastroempresa.com.br/")
            time.sleep(1)
            continue
          elif(resp == 5):
            os.system("xdg-open https://casadosdados.com.br/")
            time.sleep(1)
            continue
          elif(rsp == 6):
            os.system("xdg-open https://cnpjs.rocks/")
            time.sleep(1)
            continue
          elif(rsp == 7):
            os.system("xdg-open https://www.informecadastral.com.br/")
            time.sleep(1)
            continue
          elif(rsp == 8):
            os.system("xdg-open https://www.situacaocadastral.info/")
            time.sleep(1)
            continue
          elif(resp == 9):
            os.system("xdg-open http://www8.receita.fazenda.gov.br/simplesnacional/aplicacoes.aspx?id=21")
            time.sleep(1)
            continue
          elif(rsp == 10):
            os.system("xdg-open https://www.situacao-cadastral.com/")
            time.sleep(1)
            continue
          elif(rsp == 11):
            os.system("xdg-open https://sistemas.trt3.jus.br/certidao/feitosTrabalhistas/aba1.emissao.htm")
            time.sleep(1)
            continue
          elif(rsp == 12):
            os.system("xdg-open https://www.redecnpj.com.br/rede/")
            time.sleep(1)
            continue
          elif(resp == 13):
            os.system("xdg-open https://github.com/rictom/rede-cnpj/")
            time.sleep(1)
            continue
          elif(rsp == 14):
            os.system("xdg-open https://antecedentes.policiacivil.pa.gov.br/consulta")
            time.sleep(1)
            continue
          elif(rsp == 15):
            os.system("xdg-open https://cna.oab.org.br/")
            time.sleep(1)
            continue
          elif(rsp == 16):
            os.system("xdg-open https://portal.cfm.org.br/busca-medicos/")
            time.sleep(1)
            continue
          elif(resp == 17):
            os.system("xdg-open https://cadastro.cfp.org.br/")
            time.sleep(1)
            continue
          elif(rsp == 18):
            os.system("xdg-open https://consultaprofissional.confea.org.br/")
            time.sleep(1)
            continue
          elif(rsp == 19):
            os.system("xdg-open http://www22.receita.fazenda.gov.br/inscricaomei/private/pages/certificado_acesso.jsf")
            time.sleep(1)
            continue
          elif(rsp == 20):
            os.system("xdg-open http://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATSPO/dasnsimei.app/Default.aspx")
            time.sleep(1)
            continue
          elif(resp == 21):
            os.system("xdg-open https://www8.receita.fazenda.gov.br/SimplesNacional/controleAcesso/Autentica.aspx?id=16")
            time.sleep(1)
            continue
          elif(rsp == 22):
            os.system("xdg-open https://www2.dataprev.gov.br/sabiweb/relatorio/imprimirCRER.view?acao=imprimir_CRER")
            time.sleep(1)
            continue
          elif(rsp == 23):
            os.system("xdg-open http://solucoes.receita.fazenda.gov.br/Servicos/ConsRest/Atual.app/paginas/mobile/restituicaoMobi.asp")
            time.sleep(1)
            continue
          elif(resp == 24):
            os.system("xdg-open https://www.jucesponline.sp.gov.br/Pre_Visualiza.aspx?nire=%7BVALOR%7D&idproduto=")
            time.sleep(1)
            continue
          elif(rsp == 25):
            os.system("xdg-open https://respondendo.ibge.gov.br/verifique-a-identidade-do-entrevistador.html")
            time.sleep(1)
            continue
          elif(rsp == 26):
            os.system("xdg-open https://www.ibge.gov.br/acesso-informacao/institucional/documentos-ibge/1861-novo-portal/institucional/17422-servidores.html")
            time.sleep(1)
            continue
          elif(rsp == 0):
            break
          else:
            print("invalid option")
            time.sleep(1)
            continue
      elif(resp == 5):
        while True:
          print(f"{r} 01 {y} Busca Através do IMEI/Legalidade do Aparelho")
          print(f"{r} 02 {y} Busca de Situação Cadastro/Portabilidade de Números Celulares e Fixos")
          print(f"{r} 03 {y} Busca de Situação Cadastro/Portabilidade de Números Celulares e Fixos 2")
          print(f"{r} 04 {y} Busca Operadora por Número Celular")
          print(f"{r} 05 {y} Busca Operadora por Número Celular 2")
          print(f"{r} 06 {y} Busca Operadora por Número Celular 3")
          print(f"{r} 07 {y} Busca Operadora/Linha pré-ativa por CPF")
          print(f"{r} 08 {y} Base de Orelhão X Mapa")
          print(f"{r} 09 {y} Consultar e identificar Frequências de Rádios/SISTEMA DE SERVIÇOS DE TELECOMUNICAÇÕES (STEL)")
          print(f"{r} 10 {y} Consultar um responsável por indicativo")
          print(f"{r} 11 {y} Mais informações sobre Radio amador")
          print(f"{r} 12 {y} Números de Discagem Direta a Distância(DDD)")
          print(f"{r} 12 {y} Números de Discagem Direta a Distância(DDD) 2")
          print(f"")
          print(f"{g} 0 {y} Voltar")
          rsp = int(input(">>> "))
          if(rsp == 1):
            os.system("xdg-open https://www.consultaaparelhoimpedido.com.br/public-web/welcome")
            time.sleep(1)
            continue
          elif(rsp == 2):
            os.system("xdg-open https://consultanumero.abrtelecom.com.br/consultanumero/consulta/consultaSituacaoAtualCtg")
            time.sleep(1)
            continue
          elif(rsp == 3):
            os.system("xdg-open https://consultanumero.abrtelecom.com.br/consultanumero/consulta/consultaHistoricoRecenteCtg")
            time.sleep(1)
            continue
          elif(rsp == 4):
            os.system("xdg-open https://consultanumero.info/")
            time.sleep(1)
            continue
          elif(resp == 5):
            os.system("xdg-open https://www.qualoperadora.net/")
            time.sleep(1)
            continue
          elif(rsp == 6):
            os.system("xdg-open http://consultaoperadora.com.br/site2015/")
            time.sleep(1)
            continue
          elif(rsp == 7):
            os.system("xdg-open https://cadastropre.com.br/#/consulta")
            time.sleep(1)
            continue
          elif(rsp == 8):
            os.system("xdg-open http://sistemas.anatel.gov.br/sgmu/fiqueligado/tups.asp")
            time.sleep(1)
            continue
          elif(resp == 9):
            print("""
            Abrirá uma página para preenchimento, preencha da seguinte forma:

            1 - Em recuperação de dados: marque UF;
            2 - Em apresentar dados por: marque a letra J (frequência e entidade) em faixa de frequência: coloque a frequência que deseja scanear, ex.: inicial: 450,000 final: 460,000 (NÃO ESQUEÇA DA VÍRGULA) OBS: não de um espaço de frequencia muito largo,as vezes dá erro na pesquisa;
            3 - Em unidade coloque MHZ nos dois;
            4 - Em sigla da UF: coloque a sigla do seu estado
            5 - Em serviço inicial e serviço final nao coloque nada, deixe do jeito que está em grupo de estações: marque todos (consolidado);
            6 - Agora clique abaixo em exportar excel e salve o arquivo em seu micro;
            """)
            print(" ")
            print(" ")
            input("aperte enter quando terminar de ler...")
            os.system("xdg-open https://sistemas.anatel.gov.br/stel/Consultas/RecuperacaoFrequencias/tela.asp?SISQSmodulo=9896")
            continue
          elif(rsp == 10):
            os.system("xdg-open https://sistemas.anatel.gov.br/easp/Novo/ConsultaIndicativo/Tela.asp")
            time.sleep(1)
            continue
          elif(rsp == 11):
            os.system("xdg-open https://araf.org.br/anatel-links-rapidos")
            time.sleep(1)
            continue
          elif(rsp == 12):
            os.system("xdg-open https://pt.wikipedia.org/wiki/Discagem_direta_a_dist%C3%A2ncia")
            time.sleep(1)
            continue
          elif(rsp == 13):
            os.system("xdg-open https://www.mbi.com.br/mbi/biblioteca/utilidades/estado-onde-fica-ddd/")
            time.sleep(1)
            continue
          elif(rsp == 0):
            break
          else:
            print("invalid option")
            time.sleep(1)
            continue
      elif(resp == 6):
        while True:
          print(f"{r} 01 {y} Site 1")
          print(f"{r} 02 {y} Site 2")
          print(f"{r} 03 {y} Site 3")
          print(f"{r} 04 {y} Site 4")
          print(f"{r} 05 {y} Site 5")
          print(f"{r} 06 {y} Site 6")
          print(f"{r} 07 {y} Site 7")
          print(f"{r} 08 {y} Site 8")
          print(f"{r} 09 {y} Site 9")
          print(f"{r} 10 {y} Site 10")
          print(f"")
          print(f"{g} 0 {y} Voltar")
          rsp = int(input(">>> "))
          if(rsp == 1):
            os.system("xdg-open https://www.teleco.com.br/erb.asp")
            time.sleep(1)
            continue
          elif(rsp == 2):
            os.system("xdg-open https://sistemas.anatel.gov.br/stel/consultas/ListaEstacoesLocalidade/tela.asp?pNumServico=010")
            time.sleep(1)
            continue
          elif(rsp == 3):
            os.system("xdg-open http://www.telecocare.com.br/telebrasil/mapa_erb.php")
            time.sleep(1)
            continue
          elif(rsp == 4):
            os.system("xdg-open https://conexis.org.br/numeros/mapa-de-antenas-2/")
            time.sleep(1)
            continue
          elif(resp == 5):
            os.system("xdg-open http://sistemas.anatel.gov.br/se/public/view/b/licenciamento.php")
            time.sleep(1)
            continue
          elif(rsp == 6):
            os.system("xdg-open http://sistemas.anatel.gov.br/siec-servico-movel-web/")
            time.sleep(1)
            continue
          elif(rsp == 7):
            os.system("xdg-open https://dados.gov.br/dataset?tags=ERB")
            time.sleep(1)
            continue
          elif(rsp == 8):
            os.system("xdg-open https://www.google.com/maps/d/u/0/viewer?msa=0&mid=1Xh8EWBDY97vtLnEYuAVLvRGvu2o&ll=-16.816639560865948%2C-51.73607799999998&z=5")
            time.sleep(1)
            continue
          elif(resp == 9):
            os.system("xdg-open http://www.coberturacelular.com.br/")
            time.sleep(1)
            continue
          elif(rsp == 10):
            os.system("xdg-open https://servicos.pc.sc.gov.br/antena/")
            time.sleep(1)
            continue
          elif(rsp == 0):
            break
          else:
            print("invalid option")
            time.sleep(1)
            continue
      elif(resp == 7):
        while True:
          print(f"{r} 01 {y} Buscar Currículo Lattes")
          print(f"{r} 02 {y} Buscar Informações de Instituições de Ensino Superior")
          print(f"")
          print(f"{g} 0 {y} Voltar")
          rsp = int(input(">>> "))
          if(rsp == 1):
            os.system("xdg-open https://buscatextual.cnpq.br/buscatextual/busca.do?metodo=apresentar")
            continue
          elif(rsp == 2):
            os.system("xdg-open https://emec.mec.gov.br/emec/nova#avancada")
            continue
          elif(rsp == 0):
            break
          else:
            print("invalid option")
            time.sleep(1)
            continue
      elif(resp == 8):
        while True:
          print(f"{r} 01 {y} Imagens de Satélite via inpe.br 1")
          print(f"{r} 02 {y} Imagens de Satélite via inpe.br 2")
          print(f"{r} 03 {y} Imagens de Satélite via inpe.br 3")
          print(f"{r} 04 {y} Imagens de Satélite via inpe.br 4")
          print(f"{r} 05 {y} Imagens de Satélite via inpe.br 5")
          print(f"{r} 06 {y} Imagens de Satélite via inpe.br 6")
          print(f"{r} 07 {y} Imagens de Satélite via inpe.br 7")
          print(f"{r} 08 {y} Imagens de Satélite via inpe.br 8")
          print(f"{r} 09 {y} Imagens de Satélite via inpe.br 9")
          print(f"{r} 10 {y} Imagens de Satélite via inpe.br 10")
          print(f"{r} 11 {y} Imagens de Satélite via inpe.br 11")
          print(f"{r} 12 {y} Imagens de Satélite via inpe.br 12")
          print(f"{r} 13 {y} Imagens de Satélite via inpe.br 13")
          print(f"{r} 14 {y} Imagens de Satélite via inpe.br 14")
          print(f"{r} 15 {y} Imagens de Satélite via inpe.br 15")
          print(f"{r} 16 {y} Imagens de Satélite via inpe.br 16")
          print(f"{r} 17 {y} Imagens de Satélite via inpe.br 17")
          print(f"{r} 18 {y} Imagens de Satélite via inpe.br 18")
          print(f"{r} 19 {y} Imagens de Satélite via inpe.br 19")
          print(f"{r} 20 {y} Imagens de Satélite via inpe.br 20")
          print(f"{r} 21 {y} Imagens de Satélite via inpe.br 21")
          print(f"{r} 22 {y} Imagens de Satélite via inpe.br 22")
          print(f"{r} 23 {y} Imagens de Satélite via inpe.br 23")
          print(f"{r} 24 {y} Sistema Nacional de Cadastro Ambiental Rural (SICAR-CAR)")
          print(f"{r} 25 {y} Sistema Nacional de Cadastro Ambiental Rural (SICAR-CAR) 2")
          print(f"{r} 26 {y} Instituto do Patrimônio Histórico e Artístico Nacional (IPHAN)")
          print(f"{r} 27 {y} Rede de Meteorologia do Comando da Aeronáutica (REDEMET)")
          print(f"{r} 28 {y} Rede de Meteorologia do Comando da Aeronáutica (REDEMET)")
          print(f"{r} 29 {y} Banco de Dados Geográficos do Exército (BDGEx)")
          print(f"{r} 30 {y} Radar de Aeronaves")
          print(f"{r} 31 {y} Radar de Aeronaves 2")
          print(f"{r} 32 {y} Radar de Aeronaves 3")
          print(f"{r} 33 {y} Radar de Aeronaves 4")
          print(f"{r} 34 {y} Consulta de Licença Aeronáutica (CHT)")
          print(f"")
          print(f"{g} 0 {y} Voltar")
          rsp = int(input(">>>> "))
          if(rsp == 1):
            os.system("xdg-open http://www.dgi.inpe.br/catalogo/")
            time.sleep(1)
            continue
          elif(rsp == 2):
            os.system("xdg-open http://sigma.cptec.inpe.br/")
            time.sleep(1)
            continue
          elif(rsp == 3):
            os.system("xdg-open http://sigma2.cptec.inpe.br/")
            time.sleep(1)
            continue
          elif(rsp == 4):
            os.system("xdg-open http://sigma.cptec.inpe.br/radar/")
            time.sleep(1)
            continue
          elif(resp == 5):
            os.system("xdg-open http://sigma.cptec.inpe.br/prec_sat/")
            time.sleep(1)
            continue
          elif(rsp == 6):
            os.system("xdg-open http://sigma.cptec.inpe.br/fortracc/")
            time.sleep(1)
            continue
          elif(rsp == 7):
            os.system("xdg-open http://satelite.cptec.inpe.br/vento/")
            time.sleep(1)
            continue
          elif(rsp == 8):
            os.system("xdg-open http://satelite.cptec.inpe.br/radiacao/")
            time.sleep(1)
            continue
          elif(resp == 9):
            os.system("xdg-open http://terrabrasilis.dpi.inpe.br/app/map/alerts?hl=pt-br")
            time.sleep(1)
            continue
          elif(rsp == 10):
            os.system("xdg-open http://terrabrasilis.dpi.inpe.br/app/map/deforestation?hl=pt-br")
            time.sleep(1)
            continue
          elif(rsp == 11):
            os.system("xdg-open http://www2.dgi.inpe.br/catalogo/explore")
            time.sleep(1)
            continue
          elif(rsp == 12):
            os.system("xdg-open http://satelite.cptec.inpe.br/mapsat/")
            time.sleep(1)
            continue
          elif(resp == 13):
            os.system("xdg-open http://sigma-soschuva.cptec.inpe.br/#")
            time.sleep(1)
            continue
          elif(rsp == 14):
            os.system("xdg-open http://sigma-soschuva.cptec.inpe.br/#")
            time.sleep(1)
            continue
          elif(rsp == 15):
            os.system("xdg-open https://queimadas.dgi.inpe.br/queimadas/bdqueimadas")
            time.sleep(1)
            continue
          elif(rsp == 16):
            os.system("xdg-open https://queimadas.dgi.inpe.br/queimadas/portal-static/situacao-atual/")
            time.sleep(1)
            continue
          elif(resp == 17):
            os.system("xdg-open https://queimadas.dgi.inpe.br/queimadas/portal/videoaulas")
            time.sleep(1)
            continue
          elif(rsp == 18):
            os.system("xdg-open https://queimadas.dgi.inpe.br/queimadas/mapas-mensais/")
            time.sleep(1)
            continue
          elif(rsp == 19):
            os.system("xdg-open http://www.dgi.inpe.br/CDSR/")
            time.sleep(1)
            continue
          elif(rsp == 20):
            os.system("xdg-open https://www.arcgis.com/home/webmap/viewer.html?url=https%3A%2F%2Farcgis.sema.df.gov.br%2Fserver%2Frest%2Fservices%2FAreas_Queimadas%2FMapServer&source=sd")
            time.sleep(1)
            continue
          elif(resp == 21):
            os.system("xdg-open https://arcgis.sema.df.gov.br/server/rest/services/Areas_Queimadas/MapServer")
            time.sleep(1)
            continue
          elif(rsp == 22):
            os.system("xdg-open https://www.cptec.inpe.br/dsat/")
            time.sleep(1)
            continue
          elif(rsp == 23):
            os.system("xdg-open http://www.inpe.br/webelat/homepage/")
            time.sleep(1)
            continue
          elif(rsp == 24):
            os.system("xdg-open https://www.car.gov.br/publico/imoveis/index")
            time.sleep(1)
            continue
          elif(rsp == 25):
            os.system("xdg-open https://www.car.gov.br/#/consultar")
            time.sleep(1)
            continue
          elif(rsp == 26):
            os.system("xdg-open https://sicg.iphan.gov.br/sicg/pesquisarBem")
            time.sleep(1)
            continue
          elif(resp == 27):
            os.system("xdg-open https://redemet.decea.gov.br/#")
            time.sleep(1)
            continue
          elif(rsp == 28):
            os.system("xdg-open https://redemet.decea.gov.br/novo/")
            time.sleep(1)
            continue
          elif(rsp == 29):
            os.system("xdg-open https://bdgex.eb.mil.br/bdgexapp/mobile/")
            time.sleep(1)
            continue
          elif(rsp == 30):
            os.system("xdg-open https://www.radarbox.com/@-19.21547,-46.45469,z5")
            time.sleep(1)
            continue
          elif(resp == 31):
            os.system("xdg-open https://www.flightradar24.com/-18.82,-52.19/5")
            time.sleep(1)
            continue
          elif(rsp == 32):
            os.system("xdg-open https://www.edestinos.com.br/radar")
            time.sleep(1)
            continue
          elif(rsp == 33):
            os.system("xdg-open https://planefinder.net/airport/BSB")
            time.sleep(1)
            continue
          elif(rsp == 34):
            os.system("xdg-open https://sistemas.anac.gov.br/consultadelicencas/")
            time.sleep(1)
            continue
          elif(rsp == 0):
            break
          else:
            print("invalid option")
            time.sleep(1)
            continue
      elif(resp == 9):
        while True:
          print(f"{r} 01 {y} Cadastro Nacional de Estabelecimentos de Saúde")
          print(f"{r} 02 {y} Fundo Nacional de Saúde (FNS)")
          print(f"")
          print(f"{g} 0 {y} Voltar")
          rsp = int(input(">>> "))
          if(rsp == 1):
            os.system("xdg-open https://cnes.datasus.gov.br/")
            time.sleep(1)
            continue
          elif(rsp == 2):
            os.system("xdg-open https://consultafns.saude.gov.br/#/consolidada")
            time.sleep(1)
            continue
          elif(rsp == 0):
            break
          else:
            print("invalid option")
            time.sleep(1)
            continue
      elif(resp == 10):
        os.system("clear")
        banner()
        os.system("cat index.md")
        print(" ")
        input("aperte enter quando terminar de ler...")
      elif(resp == 11):
        while True:
          os.system("clear")
          banner()
          print(f"{r} 01 {y} Linkedin")
          print(f"{r} 04 {y} Maptimize Demo Sentiment Analysis on Tweets")
          print(f"{r} 05 {y} TweetStats Graficamente")
          print(f"{r} 06 {y} Trend24 Trends e buscas locais e global")
          print(f"{r} 07 {y} Snap Map")
          print(f"{r} 08 {y} Facebook Biblioteca de Anúncios")
          print(f"{r} 09 {y} Procurador de redes sociais")
          print(f"{r} 10 {y} UVRX buscador de redes sociais")
          print(f"")
          print(f"{g} 0 {y} Voltar")
          rsp = int(input(">>> "))
          if(rsp == 1):
            alvo = input("Digite o seu alvo(tudo junto ou com _ ao invés do espaço) do Linkedin: ")
            os.system(f"xdg-open https://www.linkedin.com/jobs/search/?keywords={alvo}&location=Brasil")
            continue
          elif(rsp == 2):
            alvo = input("Digite o seu alvo(tudo junto ou com _ ao invés do espaço) do Twitter: ")
            os.system(f"xdg-open https://twitter.com/search?q={alvo}+lang%3Apt&src=typed_query")
            continue
          elif(rsp == 3):
            os.system("xdg-open https://www.omnisci.com/demos/tweetmap")
            time.sleep(1)
            continue
          elif(rsp == 4):
            alvo = input("Digite o seu alvo(tudo junto ou com _ ao invés do espaço): ")
            os.system(f"xdg-open https://onemilliontweetmap.com/?center=-18.79191774423444,-39.33105468750001&zoom=5&search={alvo}")
            continue
          elif(resp == 5):
            pfalvo = input("Digite o seu alvo(tudo junto ou com _ ao invés do espaço): ")
            os.system(f"xdg-open https://www.tweetstats.com/graphs/{pfalvo}")
            continue
          elif(rsp == 6):
            sealvo = input("Digite o seu alvo(tudo junto ou com _ ao invés do espaço): ")
            os.system(f"xdg-open https://trends24.in/{sealvo}/")
            time.sleep(1)
            continue
          elif(rsp == 7):
            os.system("xdg-open https://map.snapchat.com/@-15.127315,-51.412151,4.51z")
            time.sleep(1)
            continue
          elif(rsp == 8):
            os.system("xdg-open https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=BR&media_type=all")
            time.sleep(1)
            continue
          elif(resp == 9):
            palvo = input("Digite o primeiro nome do seu alvo(tudo junto ou com _ ao invés do espaço): ")
            salvo = input("Digite o segundo nome(tudo junto ou com _ ao invés do espaço): ")
            os.system(f"xdg-open https://www.social-searcher.com/search-users/?q6={palvo}+{salvo}")
            continue
          elif(rsp == 10):
            os.system("xdg-open http://www.uvrx.com/social.html")
            time.sleep(1)
            continue
          elif(rsp == 0):
            break
          else:
            print("invalid option")
            time.sleep(1)
            continue
      elif(resp == 12):
        while True:
          os.system("clear")
          banner()
          print(f"{r} 01 {y} Grupos de WhatsApp")
          print(f"{r} 02 {y} Grupos de WhatsApp 2")
          print(f"{r} 03 {y} Grupos de WhatsApp 3")
          print(f"{r} 04 {y} Grupos de WhatsApp 4")
          print(f"{r} 05 {y} Grupos de WhatsApp 5")
          print(f"{r} 06 {y} Grupos de WhatsApp 6")
          print(f"{r} 07 {y} Grupos de Telegram 1")
          print(f"{r} 08 {y} Grupos de Telegram 2")
          print(f"{r} 09 {y} Grupos de Telegram 3")
          print(f"{r} 10 {y} Grupos de Telegram 4")
          print(f"{r} 11 {y} Grupos de Telegram 5")
          print(f"{r} 12 {y} Grupos de Telegram 6")
          print(f"{r} 13 {y} Grupos de Telegram 7")
          print(f"{r} 14 {y} Grupos de Telegram 8")
          print(f"")
          print(f"{g} 0 {y} Voltar")
          rsp = int(input(">>> "))
          if(rsp == 1):
            os.system("xdg-open https://gruposwhats.app/")
            time.sleep(1)
            continue
          elif(rsp == 2):
            os.system("xdg-open https://grupos-online.com/")
            time.sleep(1)
            continue
          elif(rsp == 3):
            os.system("xdg-open https://grupowhats.online/")
            time.sleep(1)
            continue
          elif(rsp == 4):
            os.system("xdg-open https://buscagrupos.com.br/")
            time.sleep(1)
            continue
          elif(resp == 5):
            os.system("xdg-open https://www.gruposwats.com/")
            time.sleep(1)
            continue
          elif(rsp == 6):
            os.system("xdg-open https://gruposdezap.com/")
            time.sleep(1)
            continue
          elif(rsp == 7):
            os.system("xdg-open https://tgstat.com/search")
            time.sleep(1)
            continue
          elif(rsp == 8):
            os.system("xdg-open https://cse.google.com/cse?cx=008239573640124656331:o29gdxc2osj")
            time.sleep(1)
            continue
          elif(resp == 9):
            os.system("xdg-open https://www.telegram-group.com/en/#")
            time.sleep(1)
            continue
          elif(rsp == 10):
            os.system("xdg-open https://tgstat.com/")
            time.sleep(1)
            continue
          elif(rsp == 11):
            alvo = input("Digite o seu alvo(tudo junto ou com _ ao invés do espaço) do Telegram: ")
            os.system(f"xdg-open https://xtea.io/ts_en.html#gsc.tab=0&gsc.q={alvo}")
            continue
          elif(rsp == 12):
            alvo = input("Digite o seu alvo(tudo junto ou com _ ao invés do espaço) do Telegram: ")
            os.system(f"xdg-open https://telemetr.io/en/channels?language=pt&channel={alvo}&period=30")
            continue
          elif(resp == 13):
            alvo = input("Digite o seu alvo(tudo junto ou com _ ao invés do espaço) do Telegram: ")
            os.system(f"xdg-open https://combot.org/telegram/top/groups?lng=pt&page=1&q={alvo}")
            continue
          elif(rsp == 14):
            alvo = input("Digite o seu alvo(tudo junto ou com _ ao invés do espaço) do Telegram: ")
            os.system(f"xdg-open https://lyzem.com/search?f=all&l=pt&p=1&per-page=100&q={alvo}")
            continue
          elif(rsp == 0):
            break
          else:
            print("invalid option")
            time.sleep(1)
            continue
      elif(resp == 13):
        while True:
          os.system("clear")
          banner()
          print(f"{r} 01 {y} Consulta de Licenciamento Veicular")
          print(f"{r} 02 {y} Consulta de Bicicletas / São Paulo")
          print(f"{r} 03 {y} Consulta de Dados via Placa 1")
          print(f"{r} 04 {y} Consulta de Dados via Placa 2")
          print(f"{r} 05 {y} Consulta de Dados via Placa 3")
          print(f"{r} 06 {y} Consulta de Dados via Placa 4")
          print(f"{r} 07 {y} Consulta de Dados via Placa 5")
          print(f"{r} 08 {y} Consulta de Dados via Placa 6")
          print(f"{r} 09 {y} Consulta de Dados via Placa 7")
          print(f"{r} 10 {y} Consulta de Dados via Placa 8")
          print(f"{r} 11 {y} Consulta de Dados via Placa 9")
          print(f"{r} 12 {y} Consulta de Dados via Placa 10")
          print(f"{r} 13 {y} Consulta de Dados via Placa 11")
          print(f"{r} 14 {y} Consulta de Dados via Placa 12")
          print(f"{r} 15 {y} Consulta de Dados via Placa 13")
          print(f"{r} 16 {y} Consulta de Dados via Placa 14")
          print(f"{r} 17 {y} Consulta de Dados via Placa 15")
          print(f"{r} 18 {y} Consulta de Dados via Placa 16")
          print(f"{r} 19 {y} Consulta de Dados FIPE 1")
          print(f"{r} 20 {y} Consulta de Dados FIPE 2")
          print(f"{r} 21 {y} Consulta de Dados FIPE 3")
          print(f"{r} 22 {y} Consulta de Dados FIPE 4")
          print(f"{r} 23 {y} Consulta de Dados FIPE 4")
          print(f"{r} 24 {y} Consulta de Dados FIPE 6")
          print(f"{r} 25 {y} Consulta de Dados FIPE 7")
          print(f"{r} 26 {y} Consulta de Dados FIPE 8")
          print(f"{r} 27 {y} Consulta Terminais Ônibus São Paulo")
          print(f"{r} 28 {y} Consulta Terminais Ônibus São Paulo 2")
          print(f"{r} 29 {y} Consulta Históricos de Ônibus")
          print(f"{r} 30 {y} Consulta Veículos Habilitados pela ANTT")
          print(f"{r} 31 {y} Consulta Linhas de Ônibus")
          print(f"{r} 32 {y} Consulta Horários e Passagens Ônibus")
          print(f"{r} 33 {y} Empresas Habilitadas")
          print(f"{r} 34 {y} Consulta Pública de Transportadores")
          print(f"{r} 35 {y} Pesquisar no Portal de Dados Abertos da ANTT")
          print(f"")
          print(f"{g} 0 {y} Voltar")
          rsp = int(input(">>> "))
          if(rsp == 1):
            os.system("xdg-open http://licenciamento.detran.ma.gov.br/Licenciamento/consulta/Home.xhtml")
            time.sleep(1)
            continue
          elif(rsp == 2):
            os.system("xdg-open https://www.ssp.sp.gov.br/consultabicicleta")
            time.sleep(1)
            continue
          elif(rsp == 3):
            os.system("xdg-open https://carfacts.com.br/ConsultaGratis")
            time.sleep(1)
            continue
          elif(rsp == 4):
            os.system("xdg-open https://www.qualveiculo.net/")
            time.sleep(1)
            continue
          elif(resp == 5):
            os.system("xdg-open https://www.olhonocarro.com.br/")
            time.sleep(1)
            continue
          elif(rsp == 6):
            os.system("xdg-open https://www.consultarplaca.com.br/")
            time.sleep(1)
            continue
          elif(rsp == 7):
            os.system("xdg-open http://infocarrosp.com.br/")
            time.sleep(1)
            continue
          elif(rsp == 8):
            os.system("xdg-open https://www.iq.com.br/veiculos/consulta-placa/")
            time.sleep(1)
            continue
          elif(resp == 9):
            os.system("xdg-open https://www.carcheck.com.br/")
            time.sleep(1)
            continue
          elif(rsp == 10):
            os.system("xdg-open https://www.consultapelaplaca.com.br/")
            time.sleep(1)
            continue
          elif(rsp == 11):
            os.system("xdg-open https://site.bibipecas.com.br/home")
            time.sleep(1)
            continue
          elif(rsp == 12):
            os.system("xdg-open https://www.historicar.com.br/")
            time.sleep(1)
            continue
          elif(resp == 13):
            os.system("xdg-open https://www.keplaca.com/")
            time.sleep(1)
            continue
          elif(rsp == 14):
            os.system("xdg-open https://www.fipeplaca.com.br/")
            time.sleep(1)
            continue
          elif(rsp == 15):
            os.system("xdg-open https://placafipe.com/")
            time.sleep(1)
            continue
          elif(rsp == 16):
            os.system("xdg-open https://placaipva.com.br/")
            time.sleep(1)
            continue
          elif(resp == 17):
            os.system("xdg-open https://www.tabelafipebrasil.com/placa")
            time.sleep(1)
            continue
          elif(rsp == 18):
            os.system("xdg-open https://www.tabelafipebrasil.com/placa")
            time.sleep(1)
            continue
          elif(rsp == 19):
            os.system("xdg-open https://veiculos.fipe.org.br/")
            time.sleep(1)
            continue
          elif(rsp == 20):
            os.system("xdg-open https://www.tabelafipebrasil.com/")
            time.sleep(1)
            continue
          elif(resp == 21):
            os.system("xdg-open https://www.tabelafipe.website/")
            time.sleep(1)
            continue
          elif(rsp == 22):
            os.system("xdg-open https://www.tabelafipemotos.com.br/")
            time.sleep(1)
            continue
          elif(rsp == 19):
            os.system("xdg-open https://www.fipeveiculos.com.br/")
            time.sleep(1)
            continue
          elif(rsp == 20):
            os.system("xdg-open https://www.valortabelafipe.com.br/")
            time.sleep(1)
            continue
          elif(resp == 21):
            os.system("xdg-open https://veiculosfipe.org/")
            time.sleep(1)
            continue
          elif(rsp == 22):
            os.system("xdg-open https://fipevalor.com.br/")
            time.sleep(1)
            continue
          elif(rsp == 23):
            os.system("xdg-open https://www.sptrans.com.br/terminais")
            time.sleep(1)
            continue
          elif(rsp == 24):
            os.system("xdg-open https://sistemas.sptrans.com.br/PlanOperWeb/")
            time.sleep(1)
            continue
          elif(resp == 25):
            os.system("xdg-open https://onibusbrasil.com/placas")
            time.sleep(1)
            continue
          elif(rsp == 26):
            os.system("xdg-open https://appweb1.antt.gov.br/scff/conPlaca.asp")
            time.sleep(1)
            continue
          elif(rsp == 27):
            os.system("xdg-open https://www.sptrans.com.br/terminais")
            time.sleep(1)
            continue
          elif(rsp == 28):
            os.system("xdg-open https://sistemas.sptrans.com.br/PlanOperWeb/")
            time.sleep(1)
            continue
          elif(resp == 29):
            os.system("xdg-open https://onibusbrasil.com/placas")
            time.sleep(1)
            continue
          elif(rsp == 30):
            os.system("xdg-open https://appweb1.antt.gov.br/scff/conPlaca.asp")
            time.sleep(1)
            continue
          elif(rsp == 31):
            os.system("xdg-open https://portal.antt.gov.br/linhas-de-onibus")
            time.sleep(1)
            continue
          elif(rsp == 32):
            os.system("xdg-open https://www.buscaonibus.com.br/")
            time.sleep(1)
            continue
          elif(resp == 33):
            os.system("xdg-open https://dados.antt.gov.br/dataset/empresas-habilitadas")
            time.sleep(1)
            continue
          elif(rsp == 34):
            os.system("xdg-open https://consultapublica.antt.gov.br/Site/ConsultaRNTRC.aspx/consultapublica")
            time.sleep(1)
            continue
          elif(rsp == 35):
            os.system("xdg-open https://dados.antt.gov.br/")
            time.sleep(1)
            continue
          elif(rsp == 0):
            break
          else:
            print("invalid option")
            time.sleep(1)
            continue
      elif(resp == 14):
        while True:
          os.system("clear")
          banner()
          print(f"{r} 01 {y} Consulta de Vôos via Infraero")
          print(f"{r} 02 {y} Consulta de Vôos de autoridades Brasileiras")
          print(f"{r} 03 {y} Consulta de Empresas e de Aeronaves de Táxi-Aéreo")
          print(f"{r} 04 {y} Consulta de Nada Consta de Multas do CBAER")
          print(f"{r} 05 {y} Consultas ao Registro Aeronáutico Brasileiro (RAB)")
          print(f"")
          print(f"{g} 0 {y} Voltar")
          rsp = int(input(">>> "))
          if(rsp == 1):
            os.system("xdg-open http://voos.infraero.gov.br/voos/index.aspx")
            time.sleep(1)
            continue
          elif(rsp == 2):
            os.system("xdg-open https://www.fab.mil.br/voos")
            time.sleep(1)
            continue
          elif(rsp == 3):
            os.system("xdg-open https://sistemas.anac.gov.br/voeseguro/")
            time.sleep(1)
            continue
          elif(rsp == 4):
            os.system("xdg-open https://sistemas.anac.gov.br/nadaconsta/")
            time.sleep(1)
            continue
          elif(resp == 5):
            os.system("xdg-open https://sistemas.anac.gov.br/aeronaves/cons_rab.asp")
            time.sleep(1)
            continue
          elif(rsp == 0):
            break
          else:
            print("invalid option")
            time.sleep(1)
            continue
      elif(resp == 15):
        while True:
          os.system("clear")
          banner()
          print(f"{r} 01 {y} Projeto City Câmeras")
          print(f"{r} 02 {y} Câmeras Cia. de Engenharia de Tráfego (CET)")
          print(f"{r} 03 {y} Câmeras DER - Departamento de Estradas de Rodagem (DER)")
          print(f"{r} 04 {y} Câmeras Rodovias Online 1")
          print(f"{r} 05 {y} Câmeras Rodovias Online 2")
          print(f"{r} 06 {y} Câmeras Rodovias Online 3")
          print(f"{r} 07 {y} Câmeras Rodovias Online 4")
          print(f"{r} 08 {y} Câmeras Rodovias Online 5")
          print(f"{r} 09 {y} Câmeras Concessionária Tamoios 1")
          print(f"{r} 10 {y} Câmeras Concessionária Tamoios 2")
          print(f"{r} 11 {y} Câmeras Concessionária Tamoios 3")
          print(f"{r} 12 {y} Câmeras Concessionária Tamoios 4")
          print(f"{r} 13 {y} Câmeras Concessionária Tamoios 5")
          print(f"{r} 14 {y} Câmeras Concessionária Tamoios 6")
          print(f"{r} 15 {y} Câmeras Concessionária EcoRodovias 1")
          print(f"{r} 16 {y} Câmeras Concessionária EcoRodovias 2")
          print(f"{r} 17 {y} Câmeras Concessionária EcoRodovias 3")
          print(f"{r} 18 {y} Câmeras Concessionária EcoRodovias 4")
          print(f"{r} 19 {y} Câmeras Concessionária EcoRodovias 5")
          print(f"{r} 20 {y} Câmeras Concessionária EcoRodovias 6")
          print(f"{r} 21 {y} Câmeras Concessionária EcoRodovias 7")
          print(f"{r} 22 {y} Câmeras Concessionária EcoRodovias 8")
          print(f"{r} 23 {y} Câmeras Concessionária EcoRodovias 9")
          print(f"{r} 24 {y} Câmeras Concessionária EcoRodovias 10")
          print(f"{r} 25 {y} Câmeras Concessionária EcoRodovias 11")
          print(f"{r} 26 {y} Câmeras Concessionária EcoRodovias 12")
          print(f"{r} 27 {y} Câmeras Concessionária EcoRodovias 13")
          print(f"{r} 28 {y} Câmeras Concessionária EcoRodovias 14")
          print(f"{r} 29 {y} Câmeras Concessionária EcoRodovias 15")
          print(f"{r} 30 {y} Câmeras Concessionária EcoRodovias 16")
          print(f"{r} 31 {y} Câmeras Concessionária EcoRodovias 17")
          print(f"{r} 32 {y} Câmeras DAER - Rio Grande do Sul")
          print(f"{r} 33 {y} Câmeras Governo de Santa Catarina")
          print(f"{r} 34 {y} Câmeras Governo de Santa Catarina 2")
          print(f"{r} 35 {y} Câmeras Governo de Santa Catarina 3")
          print(f"{r} 36 {y} Câmeras Governo de Santa Catarina 4")
          print(f"{r} 37 {y} Câmeras Governo de Santa Catarina 5")
          print(f"{r} 38 {y} Câmeras Governo de Santa Catarina 6")
          print(f"{r} 39 {y} Câmeras da Prefeitura de João Pessoa - PB (SEMOB)")
          print(f"{r} 40 {y} Câmeras da Prefeitura de Recife - PE (CTTU)")
          print(f"{r} 41 {y} Câmeras do Centro Integrado de Operações de Belém do Pará (Segup no Trânsito)")
          print(f"{r} 42 {y} Câmeras da BHTRANS (Em beta ainda)")
          print(f"{r} 43 {y} Câmeras do Aeroporto Internacional de São Paulo/Guarulhos - SGBR")
          print(f"{r} 44 {y} Câmera do Aeroporto de Congonhas São Paulo - SBSP FULL ATC")
          print(f"{r} 45 {y} Câmera do Aeroporto Santos Dumont - Rio de Janeiro - SBRJ FULL ATC")
          print(f"{r} 46 {y} Câmera do Aeroporto Galeão - Rio de Janeiro - SBGL")
          print(f"{r} 47 {y} Câmera do Aeroporto Internacional de Florianópolis - SBFL Com Fonia")
          print(f"{r} 48 {y} Câmera do Aeroporto da Pampulha - Belo Horizonte 24 horas (BHZ)(SBBH)")
          print(f"{r} 49 {y} Câmera do Aeroporto do Recife - SBRF")
          print(f"{r} 50 {y} Câmeras de Obras em Andamento de Mato Grosso (SINFRA)")
          print(f"")
          print(f"{g} 0 {y} Voltar")
          rsp = int(input(">>> "))
          if(rsp == 1):
            os.system("xdg-open https://www.citycameras.prefeitura.sp.gov.br/home")
            time.sleep(1)
            continue
          elif(rsp == 2):
            os.system("xdg-open http://cameras.cetsp.com.br/")
            time.sleep(1)
            continue
          elif(rsp == 3):
            os.system("xdg-open http://www.der.sp.gov.br/WebSite/Servicos/ServicosOnline/CamerasOnlineMapa.aspx")
            time.sleep(1)
            continue
          elif(rsp == 4):
            os.system("xdg-open http://www.rodoviasonline.com.br/rodovias-der-sp/")
            time.sleep(1)
            continue
          elif(resp == 5):
            os.system("xdg-open http://www.rodoviasonline.com.br/cameras-ao-vivo-das-rodovias-do-estado-do-parana/")
            time.sleep(1)
            continue
          elif(rsp == 6):
            os.system("xdg-open https://www.rodoviasonline.com.br/cameras-ao-vivo-nas-rodovias-do-rio-grande-de-sul-daer-rs/")
            time.sleep(1)
            continue
          elif(rsp == 7):
            os.system("xdg-open https://www.rodoviasonline.com.br/rodovia-governador-ney-braga-br-277/")
            time.sleep(1)
            continue
          elif(rsp == 8):
            os.system("xdg-open https://www.rodoviasonline.com.br/cameras-ao-vivo-viapar-parana/")
            time.sleep(1)
            continue
          elif(resp == 9):
            os.system("xdg-open https://concessionariatamoios.com.br/cameras/ver/12")
            time.sleep(1)
            continue
          elif(rsp == 10):
            os.system("xdg-open https://concessionariatamoios.com.br/cameras/ver/14")
            time.sleep(1)
            continue
          elif(rsp == 11):
            os.system("xdg-open https://concessionariatamoios.com.br/cameras/ver/10")
            time.sleep(1)
            continue
          elif(rsp == 12):
            os.system("xdg-open https://concessionariatamoios.com.br/cameras/ver/9")
            time.sleep(1)
            continue
          elif(resp == 13):
            os.system("xdg-open https://concessionariatamoios.com.br/cameras/ver/8")
            time.sleep(1)
            continue
          elif(rsp == 14):
            os.system("xdg-open https://concessionariatamoios.com.br/cameras/ver/13")
            time.sleep(1)
            continue
          elif(rsp == 15):
            os.system("xdg-open https://www.ecovias.com.br/condicoes-da-via#condition-camera")
            time.sleep(1)
            continue
          elif(rsp == 16):
            os.system("xdg-open https://www.ecovias.com.br/boletim/camera/2")
            time.sleep(1)
            continue
          elif(resp == 17):
            os.system("xdg-open http://site.ecovias.com.br/cameras/vpon/0kamera1.jpg")
            time.sleep(1)
            continue
          elif(rsp == 18):
            os.system("xdg-open https://www.ecovias.com.br/boletim/camera/4")
            time.sleep(1)
            continue
          elif(rsp == 19):
            os.system("xdg-open http://site.ecovias.com.br/cameras/vpon/0kamera6.jpg")
            time.sleep(1)
            continue
          elif(rsp == 20):
            os.system("xdg-open https://www.ecovias.com.br/boletim/camera/6")
            time.sleep(1)
            continue
          elif(resp == 21):
            os.system("xdg-open https://www.ecovias.com.br/boletim/camera/7")
            time.sleep(1)
            continue
          elif(rsp == 22):
            os.system("xdg-open https://www.ecovias.com.br/boletim/camera/8")
            time.sleep(1)
            continue
          elif(rsp == 23):
            os.system("xdg-open https://www.ecovias.com.br/boletim/camera/15")
            time.sleep(1)
            continue
          elif(rsp == 24):
            os.system("xdg-open https://www.ecovias.com.br/boletim/camera/1")
            time.sleep(1)
            continue
          elif(rsp == 25):
            os.system("xdg-open https://www.ecovias.com.br/boletim/camera/11")
            time.sleep(1)
            continue
          elif(resp == 26):
            os.system("xdg-open https://www.ecovias.com.br/boletim/camera/12")
            time.sleep(1)
            continue
          elif(rsp == 27):
            os.system("xdg-open https://www.ecovias.com.br/boletim/camera/13")
            time.sleep(1)
            continue
          elif(rsp == 28):
            os.system("xdg-open https://www.ecovias.com.br/boletim/camera/14")
            time.sleep(1)
            continue
          elif(rsp == 29):
            os.system("xdg-open https://www.ecovias.com.br/boletim/camera/16")
            time.sleep(1)
            continue
          elif(resp == 30):
            os.system("xdg-open https://www.ecovias.com.br/boletim/camera/9")
            time.sleep(1)
            continue
          elif(rsp == 31):
            os.system("xdg-open https://www.ecovias.com.br/boletim/camera/10")
            time.sleep(1)
            continue
          elif(rsp == 32):
            os.system("xdg-open https://daer.kopp.com.br/ftp/imagem.php?id=Santa_Maria")
            time.sleep(1)
            continue
          elif(rsp == 33):
            os.system("xdg-open https://www.ssp.sc.gov.br/dtic/index.php/cameras/cameras-online")
            time.sleep(1)
            continue
          elif(resp == 34):
            os.system("xdg-open https://www.ssp.sc.gov.br/dtic/index.php/cameras/cameras-online-florianopolis")
            time.sleep(1)
            continue
          elif(rsp == 35):
            os.system("xdg-open https://www.ssp.sc.gov.br/dtic/index.php/cameras/cameras-online-florianopolis-trindade")
            time.sleep(1)
            continue
          elif(rsp == 36):
            os.system("xdg-open https://www.ssp.sc.gov.br/dtic/index.php/cameras/cameras-online-florianopolis-2")
            time.sleep(1)
            continue
          elif(rsp == 37):
            os.system("xdg-open https://www.ssp.sc.gov.br/dtic/index.php/cameras/cameras-online-sao-jose")
            time.sleep(1)
            continue
          elif(resp == 38):
            os.system("xdg-open https://www.ssp.sc.gov.br/dtic/index.php/cameras/cameras-online-biguacu")
            time.sleep(1)
            continue
          elif(rsp == 39):
            os.system("xdg-open http://transito.gtrans.com.br/semobjp/index.php")
            time.sleep(1)
            continue
          elif(rsp == 40):
            os.system("xdg-open http://transito.gtrans.com.br/cttupe/index.php/mapa")
            time.sleep(1)
            continue
          elif(rsp == 41):
            os.system("xdg-open https://www.ciop.pa.gov.br/aovivo/index.html")
            time.sleep(1)
            continue
          elif(resp == 42):
            os.system("xdg-open http://infotrafego.pbh.gov.br/info_trafego_cameras.html")
            time.sleep(1)
            continue
          elif(rsp == 43):
            os.system("xdg-open https://www.youtube.com/watch?v=iA_TQxQS9Sw")
            time.sleep(1)
            continue
          elif(rsp == 44):
            os.system("xdg-open https://www.youtube.com/watch?v=rKM8wSr3ORU")
            time.sleep(1)
            continue
          elif(rsp == 45):
            os.system("xdg-open https://www.youtube.com/watch?v=dS2eAlS9UBE")
            time.sleep(1)
            continue
          elif(resp == 46):
            os.system("xdg-open https://www.youtube.com/watch?v=EPGfz0QibL0")
            time.sleep(1)
            continue
          elif(rsp == 47):
            os.system("xdg-open https://www.youtube.com/watch?v=xLen1r-iwfU")
            time.sleep(1)
            continue
          elif(rsp == 48):
            os.system("xdg-open https://www.youtube.com/watch?v=NuyRxze2iUo")
            time.sleep(1)
            continue
          elif(rsp == 49):
            os.system("xdg-open https://www.youtube.com/watch?v=BhTY_GHvSmg")
            time.sleep(1)
            continue
          elif(rsp == 50):
            os.system("xdg-open https://mapas.sinfra.mt.gov.br/portal/apps/sites/#/central-infra-20-2-1/pages/monitoramento-de-obras")
            time.sleep(1)
            continue
          elif(rsp == 0):
            break
          else:
            print("invalid option")
            time.sleep(1)
            continue
      elif(resp == 16):
        while True:
          os.system("clear")
          banner()
          print(f"{r} 01 {y} Categorias de domínios")
          print(f"{r} 02 {y} Antecedentes Criminais")
          print(f"{r} 03 {y} Busca de Falecidos/Óbitos")
          print(f"{r} 04 {y} Consulta de Embarcações Navais")
          print(f"{r} 05 {y} Estatísticas de Nascimentos, Óbitos, Registros e Casamentos")
          print(f"{r} 06 {y} Informações sobre um endereço de e-mail")
          print(f"{r} 07 {y} Informações Sobre Domínios")
          print(f"{r} 08 {y} Informações Sobre Domínios 2")
          print(f"{r} 09 {y} Informações Sobre Domínios 3")
          print(f"{r} 10 {y} Informações Sobre Domínios 4")
          print(f"{r} 11 {y} Sites Notificados pelo Procon-SP")
          print(f"{r} 12 {y} Lista Telefônica")
          print(f"{r} 13 {y} Consulta no Instituto Nacional da Propriedade Industrial (INPI)")
          print(f"{r} 14 {y} Consulta de Licitações, Contratos e Compras Públicas")
          print(f"{r} 15 {y} Consulta de Licitações, Contratos e Compras Públicas 2")
          print(f"{r} 16 {y} Consulta de Licitações, Contratos e Compras Públicas 3")
          print(f"{r} 17 {y} Acesso a Infromação - SPTRANSd")
          print(f"{r} 18 {y} Repositório com Dados Públicos")
          print(f"{r} 19 {y} Consulta os Processos Licitatórios da SPTrans")
          print(f"{r} 20 {y} Consulta os Processos Licitatórios da SPTrans 2")
          print(f"{r} 21 {y} Consulta os Processos Licitatórios da SPTrans 3")
          print(f"{r} 22 {y} Consulta os Processos Licitatórios da SPTrans 4")
          print(f"")
          print(f"{g} 0 {y} Voltar")
          rsp = int(input(">>> "))
          if(rsp == 1):
            os.system("cat dominio.txt")
            input("aperte enter")
            continue
          elif(rsp == 2):
            os.system("xdg-open https://servicos.dpf.gov.br/antecedentes-criminais/certidao")
            time.sleep(1)
            continue
          elif(rsp == 3):
            os.system("xdg-open https://www.falecidosnobrasil.org.br/")
            time.sleep(1)
            continue
          elif(rsp == 4):
            os.system("xdg-open https://www.mercante.transportes.gov.br/g36127/html/Manife/EmbarcConsul.html?noCampo=cdIrin")
            time.sleep(1)
            continue
          elif(resp == 5):
            os.system("xdg-open https://transparencia.registrocivil.org.br/registros")
            time.sleep(1)
            continue
          elif(rsp == 6):
            os.system("xdg-open https://tools.epieos.com/email.php")
            time.sleep(1)
            continue
          elif(rsp == 7):
            os.system("xdg-open https://registro.br/dominio/lista-processo-liberacao.txt")
            time.sleep(1)
            continue
          elif(rsp == 8):
            os.system("xdg-open https://rdap.registro.br/domain/seu_dominio_exemplo.com.br")
            time.sleep(1)
            continue
          elif(resp == 9):
            os.system("xdg-open https://registro.br/tecnologia/ferramentas/whois/")
            time.sleep(1)
            continue
          elif(rsp == 10):
            os.system("xdg-open https://registro.br/tecnologia/ferramentas/pesquisa-de-usuario/")
            time.sleep(1)
            continue
          elif(rsp == 11):
            os.system("xdg-open https://sistemas.procon.sp.gov.br/evitesite/list/evitesites.php")
            time.sleep(1)
            continue
          elif(rsp == 12):
            os.system("xdg-open https://www.telenumeros.com/")
            time.sleep(1)
            continue
          elif(resp == 13):
            os.system("xdg-open https://busca.inpi.gov.br/pePI/servlet/LoginController?action=login")
            time.sleep(1)
            continue
          elif(rsp == 14):
            os.system("xdg-open https://alertalicitacao.com.br/")
            time.sleep(1)
            continue
          elif(rsp == 15):
            os.system("xdg-open https://www.portaldecompraspublicas.com.br/18/Processos/")
            time.sleep(1)
            continue
          elif(rsp == 16):
            os.system("xdg-open http://www.portaltransparencia.gov.br/")
            time.sleep(1)
            continue
          elif(resp == 17):
            os.system("xdg-open https://www.prefeitura.sp.gov.br/cidade/secretarias/mobilidade/institucional/sptrans/acesso_a_informacao/index.php")
            time.sleep(1)
            continue
          elif(rsp == 18):
            os.system("xdg-open https://brasil.io/home/")
            time.sleep(1)
            continue
          elif(rsp == 19):
            os.system("xdg-open https://sistemas.sptrans.com.br//licitlovnew/hilicwebfrt2rc_Ano.aspx")
            time.sleep(1)
            continue
          elif(rsp == 20):
            os.system("xdg-open https://sptrans.com.br/licitacoes/")
            time.sleep(1)
            continue
          elif(resp == 21):
            os.system("xdg-open https://sistemas.sptrans.com.br/licitlovnew/hilicwebfrtcp.aspx")
            time.sleep(1)
            continue
          elif(rsp == 22):
            os.system("xdg-open https://www.prefeitura.sp.gov.br/cidade/secretarias/mobilidade/edital/index.php?p=247319")
            time.sleep(1)
            continue
          elif(rsp == 0):
            break
          else:
            print("invalid option")
            time.sleep(1)
            continue
      elif(resp == 99):
      	os.system("python3 jhonny.py")
      	break
      elif(resp == 0):
        break
      else:
        print("Invalid Opiton")
        time.sleep(1)
        continue
except KeyboardInterrupt:
  print("bruh")
