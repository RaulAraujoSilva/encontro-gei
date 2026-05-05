// app — design canvas wiring

const { DesignCanvas, DCSection, DCArtboard } = window;

const App = () => (
  <DesignCanvas>
    <DCSection id="overview" title="01 · Visão geral" subtitle="Capa, princípios e diagnóstico — a leitura curta do documento.">
      <DCArtboard id="cover" label="Capa" width={1280} height={780}>
        <Cover />
      </DCArtboard>
      <DCArtboard id="principles" label="Princípios de redesign" width={1280} height={780}>
        <Principles />
      </DCArtboard>
    </DCSection>

    <DCSection id="diagnosis" title="02 · Diagnóstico" subtitle="Nove problemas concretos identificados na página atual, com severidade e impacto.">
      <DCArtboard id="d1" label="01 · Hero genérico" width={460} height={400}>
        <DiagnosisCard n="01" sev="high" sevLabel="Alta · Identidade"
          title="O hero parece um SaaS, não um evento científico."
          body="Gradiente azul-violeta, título com text-clip em gradient, botões pill brancos — é o template padrão de landing de produto. O evento tem 4 universidades, 8 agências reguladoras e ISBN. A apresentação atual subaproveita esse capital simbólico."
          impact="Impacto · Confiança institucional menor que a real" />
      </DCArtboard>
      <DCArtboard id="d2" label="02 · Nav inflada" width={460} height={400}>
        <DiagnosisCard n="02" sev="high" sevLabel="Alta · Navegação"
          title="Sete itens na nav, com peso visual igual."
          body="Programação, Eventos, Visitas, Submissão, Parceiros, Claro, Inscreva-se. O toggle de tema 'Claro' aparece como link. Não há prioridade — tudo grita o mesmo volume. As três tarefas reais do usuário (inscrever, submeter, ver programa) ficam escondidas."
          impact="Impacto · Atrito na descoberta da CTA primária" />
      </DCArtboard>
      <DCArtboard id="d3" label="03 · Stats sem hierarquia" width={460} height={400}>
        <DiagnosisCard n="03" sev="med" sevLabel="Média · Hierarquia"
          title="Cinco números brigam pela mesma atenção."
          body="3 dias / 4 eventos / 8 visitas / 13 eixos / ISBN — todos no mesmo tamanho, mesma cor. 'ISBN' não é sequer um número. A leitura vira lista de bullets numéricos sem narrativa. Dois números de destaque + três métricas de apoio resolveriam."
          impact="Impacto · Mensagem central dilui-se" />
      </DCArtboard>
      <DCArtboard id="d4" label="04 · Falta urgência" width={460} height={400}>
        <DiagnosisCard n="04" sev="high" sevLabel="Alta · Conversão"
          title="Prazos críticos não aparecem acima da dobra."
          body="A submissão Fase 1 encerra em 15/05 — daqui a poucos dias da publicação. Esse prazo é a notícia mais acionável da página. Hoje, ele só aparece dentro da seção de submissão, depois de 6 outros blocos. Deveria estar fixo na nav."
          impact="Impacto · Submissões perdidas por desconhecimento" />
      </DCArtboard>
      <DCArtboard id="d5" label="05 · 8 visitas iguais" width={460} height={400}>
        <DiagnosisCard n="05" sev="med" sevLabel="Média · Densidade"
          title="Oito cards de visita com identidade visual idêntica."
          body="Petrobras (energia), CSN (indústria), AGENERSA (regulação) — setores muito diferentes recebem o mesmo cartão genérico. Sem cor por setor, sem indicador de ocupação, sem distinção entre simples e integradas além de uma palavra. Difícil escolher."
          impact="Impacto · Decisão por desistência, não por preferência" />
      </DCArtboard>
      <DCArtboard id="d6" label="06 · Submissão dispersa" width={460} height={400}>
        <DiagnosisCard n="06" sev="med" sevLabel="Média · Fluxo"
          title="Submissão em 4 blocos desconexos."
          body="Cronograma como timeline vertical, eixos numerados 1–13, normas em PDF, formulário Even3 em outro lugar. O autor precisa montar mentalmente o caminho. Uma timeline horizontal única + cards de formato (RE/PA/R3/AC) lado a lado consolida o fluxo."
          impact="Impacto · Submissões em formato errado, retrabalho" />
      </DCArtboard>
      <DCArtboard id="d7" label="07 · Logos no rodapé" width={460} height={400}>
        <DiagnosisCard n="07" sev="med" sevLabel="Média · Credenciais"
          title="A rede institucional fica enterrada no rodapé."
          body="UFF, ABAR, ANP, AGENERSA, Firjan, IBP, Fecomércio, CAU/RJ, CREA-RJ — esse é o ativo simbólico mais forte do evento. Aparece só após scroll completo. Uma faixa logo abaixo do hero estabeleceria credibilidade nos primeiros 5 segundos."
          impact="Impacto · Visitante não-acadêmico subdimensiona o evento" />
      </DCArtboard>
      <DCArtboard id="d8" label="08 · Acessibilidade" width={460} height={400}>
        <DiagnosisCard n="08" sev="high" sevLabel="Alta · A11y"
          title="Contraste, foco e leitura assistida sub-ótimos."
          body="Texto branco sobre gradiente violeta-azul falha em pontos da página. Itálicos coloridos em amarelo neon no escuro reduzem legibilidade. Links de rodapé 'Política / Acessibilidade' apontam para '#'. Para um evento que valoriza ESG e inclusão, o site precisa ser AAA."
          impact="Impacto · Barreira para PCDs · risco institucional" />
      </DCArtboard>
      <DCArtboard id="d9" label="09 · Mobile reativo" width={460} height={400}>
        <DiagnosisCard n="09" sev="med" sevLabel="Média · Mobile"
          title="Mobile é responsivo, mas não pensado."
          body="Em telas pequenas o conteúdo simplesmente empilha. Sem CTA persistente, sem filtragem das 8 visitas, sem caminho compacto da submissão. 70% do tráfego acadêmico hoje vem via celular — merece tratamento próprio, não só layout que cabe."
          impact="Impacto · Conversão mobile menor que desktop" />
      </DCArtboard>
    </DCSection>

    <DCSection id="hero" title="03 · Redesign · Hero" subtitle="Antes e depois. A primeira tela carrega o tom de tudo o que vem depois.">
      <DCArtboard id="hero-before" label="Antes · estado atual" width={1440} height={900}>
        <HeroBefore />
      </DCArtboard>
      <DCArtboard id="hero-after" label="Depois · proposta editorial" width={1440} height={900}>
        <HeroAfter />
      </DCArtboard>
    </DCSection>

    <DCSection id="nav" title="04 · Redesign · Navegação" subtitle="A barra superior é o componente mais reutilizado do site. Ela precisa carregar três coisas: identidade institucional, ação e prazo.">
      <DCArtboard id="nav" label="Comparativo · antes/depois" width={1280} height={680}>
        <NavCompare />
      </DCArtboard>
    </DCSection>

    <DCSection id="program" title="05 · Redesign · Programa" subtitle="Os três dias têm naturezas diferentes (institucional / imersão / acadêmico). Visualizar isso ajuda o público a decidir a modalidade.">
      <DCArtboard id="prog" label="Três dias com identidade visual própria" width={1440} height={780}>
        <ProgramAfter />
      </DCArtboard>
    </DCSection>

    <DCSection id="visits" title="06 · Redesign · Visitas técnicas" subtitle="Oito jornadas em paralelo. O design original trata todas como iguais — a proposta diferencia por setor, ocupação e tipo (simples/integrada).">
      <DCArtboard id="visits" label="Grade de 8 visitas com cor por setor" width={1440} height={820}>
        <VisitsAfter />
      </DCArtboard>
    </DCSection>

    <DCSection id="submission" title="07 · Redesign · Submissão" subtitle="O fluxo de submissão hoje exige que o autor cruze 4 blocos. A proposta consolida cronograma + formatos em uma única tela.">
      <DCArtboard id="sub" label="Cronograma horizontal + 4 formatos" width={1440} height={820}>
        <SubmissionAfter />
      </DCArtboard>
    </DCSection>

    <DCSection id="mobile" title="08 · Mobile" subtitle="Três telas-chave repensadas especificamente para celular.">
      <DCArtboard id="mob" label="Home · visitas · tracker" width={1280} height={760}>
        <MobileBoard />
      </DCArtboard>
    </DCSection>

    <DCSection id="system" title="09 · Sistema de design" subtitle="A base tipográfica e cromática que sustenta todas as telas anteriores. Reutilizável e expansível.">
      <DCArtboard id="sys" label="Tipografia + paleta" width={1440} height={820}>
        <SystemBoard />
      </DCArtboard>
    </DCSection>
  </DesignCanvas>
);

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
