// Boards — content cells used inside the design canvas

const Cover = () => (
  <div className="ab">
    <div className="cover">
      <div className="cover-meta">
        <div>
          <div>Análise UX/Design</div>
          <div style={{marginTop:6, color:'var(--amber)'}}>encontro-gei.vercel.app</div>
        </div>
        <div style={{textAlign:'right'}}>
          <div>05 maio 2026</div>
          <div style={{marginTop:6}}>Documento interno · v1</div>
        </div>
      </div>
      <div>
        <div className="eyebrow" style={{marginBottom:24}}>— Diagnóstico, princípios, redesigns propostos</div>
        <h1 className="serif">
          Mais <em>institucional</em>, menos<br/>landing page.
        </h1>
        <p className="lede serif">
          O 1º Encontro GEI carrega 4 eventos, 8 visitas e 13 eixos temáticos sob um único guarda-chuva.
          A página atual comunica volume, mas trata o conteúdo como uma landing comercial. Esta análise
          propõe redesenhá-la como uma <em>plataforma de programa científico</em>: editorial na forma,
          funcional na navegação, sóbria na cor.
        </p>
      </div>
      <div className="cover-foot">
        <div><div className="k">Escopo</div><div className="v">Home, navegação, programa, visitas, submissão e inscrição</div></div>
        <div><div className="k">Método</div><div className="v">Heurísticas de Nielsen, hierarquia editorial e arquitetura de informação</div></div>
        <div><div className="k">Entregas</div><div className="v">9 diagnósticos · 6 redesigns · sistema de design</div></div>
        <div><div className="k">Estado atual</div><div className="v">Hero genérico, navegação inflada, denso porém raso</div></div>
      </div>
    </div>
  </div>
);

const DiagnosisCard = ({n, sev, sevLabel, title, body, impact}) => (
  <div className="ab">
    <div className="diag">
      <div className="num">{n}</div>
      <div style={{display:'flex', flexDirection:'column'}}>
        <span className={`severity ${sev}`}>{sevLabel}</span>
        <h3>{title}</h3>
        <p>{body}</p>
        <div className="impact">{impact}</div>
      </div>
    </div>
  </div>
);

const HeroBefore = () => (
  <div className="ab">
    <div className="hero-before">
      <div className="nav-b">
        <div className="logo-b">[ logo gradient ]</div>
        <div className="nav-links">
          <span>Programação</span><span>Eventos</span><span>Visitas</span>
          <span>Submissão</span><span>Parceiros</span><span style={{color:'#ffd56a'}}>Claro</span>
          <span style={{padding:'8px 16px', background:'#ffd56a', color:'#091136', borderRadius:999, fontWeight:600}}>Inscreva-se →</span>
        </div>
      </div>
      <div className="body-b">
        <div className="title-b">1° Encontro de Governança, Estratégia e Inovação Governamental</div>
        <div className="meta-b">08, 09 e 10 de julho de 2026 · Rio de Janeiro</div>
        <div className="lede-b">A primeira plataforma nacional que integra <em>academia, regulação, gestão pública, engenharia de produção e setor produtivo</em>.</div>
        <div className="stats-b">
          <div className="stat-b"><strong>3</strong><span>DIAS CONSECUTIVOS</span></div>
          <div className="stat-b"><strong>4</strong><span>EVENTOS INTEGRADOS</span></div>
          <div className="stat-b"><strong>8</strong><span>VISITAS EM PARALELO</span></div>
          <div className="stat-b"><strong>13</strong><span>EIXOS INDEXADOS ODS</span></div>
          <div className="stat-b"><strong>ISBN</strong><span>ANAIS DEZ/26</span></div>
        </div>
        <div className="ctas-b">
          <div className="btn-b">Inscreva-se agora →</div>
          <div className="btn-b outline">Ver programação</div>
        </div>
      </div>
    </div>
    {/* Critique annotations */}
    <div className="note" style={{top: 90, right: 20}}>
      <span className="num">1</span><span>Toggle de tema "Claro" misturado entre links de seção</span>
    </div>
    <div className="note" style={{top: 240, left: 60, maxWidth: 240}}>
      <span className="num">2</span><span>Título genérico de SaaS, gradiente decorativo, sem hierarquia editorial</span>
    </div>
    <div className="note" style={{top: 460, left: 60}}>
      <span className="num">3</span><span>5 estatísticas competindo por atenção; "ISBN" não é uma métrica</span>
    </div>
    <div className="note" style={{top: 600, left: 80}}>
      <span className="num">4</span><span>Falta urgência (prazo de submissão? vagas?)</span>
    </div>
  </div>
);

const HeroAfter = () => (
  <div className="ab">
    <div className="hero-after">
      <div className="nav-a">
        <div className="logo-a">
          <div className="l1">Encontro <em style={{color:'var(--amber)', fontStyle:'italic'}}>GEI</em></div>
          <div className="l2">UFF · ABAR · PPGEP · Escola de Regulação</div>
        </div>
        <div className="nav-a-links">
          <span>Programa</span>
          <span>Eventos</span>
          <span>Visitas</span>
          <span>Submeter</span>
          <span>Apoio</span>
          <span style={{color:'var(--rust)', fontFamily:'var(--mono)', fontSize:11, letterSpacing:'.06em', textTransform:'uppercase'}}>
            <span className="ind"></span>Submissão até 15/05
          </span>
          <span className="btn primary" style={{height:38, padding:'0 16px', fontSize:14}}>Inscrever-se</span>
        </div>
      </div>
      <div className="left-a">
        <div>
          <div className="pretitle">Conferência inaugural · 08–10 julho 2026</div>
          <h1 className="title-a">
            Governança,<br/>
            regulação e<br/>
            <em>inovação</em><br/>
            governamental.
          </h1>
          <p className="lede-a">
            Quatro eventos oficiais reunidos em três dias no Rio de Janeiro.
            13ª Lean Six Sigma Congress, 4º SSEP, 2º Seminário de Regulação
            e 1º Seminário de Inteligência Governamental — sob uma mesma agenda.
          </p>
        </div>
        <div className="ctas-a">
          <a className="btn primary">Inscrever-se <span className="arrow">→</span></a>
          <a className="btn ghost">Ver programa completo</a>
          <span className="micro" style={{marginLeft:'auto'}}>Gratuito · vagas limitadas</span>
        </div>
      </div>
      <div className="right-a">
        <div className="dots">
          <i style={{background:'var(--violet)'}}></i>
          <i style={{background:'var(--orange)'}}></i>
          <i style={{background:'var(--gold)'}}></i>
          <i style={{background:'var(--green)'}}></i>
          <i style={{background:'var(--cyan)'}}></i>
        </div>
        <div className="date-card">
          <div className="date-num">08<br/>—10</div>
          <div className="date-meta">
            <div className="m1">Quarta a sexta · julho 2026</div>
            <div className="m2">Rio de Janeiro · Niterói</div>
          </div>
        </div>
        <div className="key-list">
          <div className="key-row"><span className="n">04</span><span className="lbl">Eventos oficiais integrados</span><span className="sub">Lean · SSEP · Reg · Intel</span></div>
          <div className="key-row"><span className="n">08</span><span className="lbl">Visitas técnicas em campo</span><span className="sub">Petrobras · CSN · Eneva ...</span></div>
          <div className="key-row"><span className="n">13</span><span className="lbl">Eixos indexados aos ODS</span><span className="sub">Anais ISBN dez/26</span></div>
          <div className="key-row"><span className="n">24h</span><span className="lbl">Carga horária certificada</span><span className="sub">UFF · ABAR · PPGEP</span></div>
        </div>
        <div className="urgency">
          <span className="dot"></span>
          Submissão Fase 1 encerra em 10 dias
        </div>
      </div>
    </div>
  </div>
);

const Principles = () => (
  <div className="ab ab-dark">
    <div className="principles">
      <div className="eyebrow on-dark">Princípios de redesign</div>
      <h2 style={{marginTop:18}}>
        Da landing comercial<br/>
        para a <em>plataforma</em><br/>
        de programa científico.
      </h2>
      <p className="lede">
        Quatro decisões orientam todas as recomendações deste documento. Elas não são ornamento — são
        a forma como o evento deve se apresentar para o seu público real: pesquisadores, reguladores
        e gestores públicos.
      </p>
      <div className="principles-grid">
        <div className="principle">
          <div className="pn">P—01</div>
          <h3>Editorial, não SaaS</h3>
          <p>Tipografia serifada com hierarquia de revista científica. Itálicos editoriais marcam ênfase. Gradientes e neons saem; preto-creme entram.</p>
          <div className="ex">→ Source Serif 4 + Inter Tight + JetBrains Mono</div>
        </div>
        <div className="principle">
          <div className="pn">P—02</div>
          <h3>Densidade com hierarquia</h3>
          <p>O conteúdo é volumoso por natureza (4 eventos, 8 visitas, 13 eixos). A solução não é cortar — é estruturar com pesos tipográficos, retículas e silêncio entre blocos.</p>
          <div className="ex">→ Cards com baseline grid · espaços generosos · cor para grupos</div>
        </div>
        <div className="principle">
          <div className="pn">P—03</div>
          <h3>Navegação por tarefa</h3>
          <p>Visitantes vêm para 3 ações: <b>inscrever-se</b>, <b>submeter</b> ou <b>conhecer o programa</b>. A nav e a home devem espelhar isso, não enumerar 7 seções equivalentes.</p>
          <div className="ex">→ CTA primária persistente · prazo crítico sempre visível</div>
        </div>
        <div className="principle">
          <div className="pn">P—04</div>
          <h3>Credenciais à mostra</h3>
          <p>O peso institucional (UFF, ABAR, ANP, AGENERSA, Firjan, IBP) é o ativo mais forte — hoje fica enterrado no rodapé. Subir essa rede para perto do hero gera confiança imediata.</p>
          <div className="ex">→ Faixa de logos · sigilo institucional na nav · ISBN como selo</div>
        </div>
      </div>
    </div>
  </div>
);

const ProgramAfter = () => (
  <div className="ab">
    <div className="program">
      <div className="program-head">
        <div>
          <div className="eyebrow">Programa · 3 dias</div>
          <h2 style={{marginTop:14}}>Três dias com <em>identidades distintas</em>.</h2>
        </div>
        <div style={{display:'flex', gap:8}}>
          <span className="chip solid">Visão de programa</span>
          <span className="chip">Linha do tempo detalhada</span>
          <span className="chip">Em sua agenda ↓</span>
        </div>
      </div>
      <div className="program-grid">
        <div className="day-card">
          <div className="day-tag">
            <div className="day-num">01</div>
            <div className="day-meta"><div className="a">Quarta · 08 jul</div><div className="b">Abertura</div></div>
          </div>
          <h3>Mesa institucional<br/>e conferência magna.</h3>
          <div className="where">Local em definição · Rio de Janeiro</div>
          <div className="timeline">
            <div className="tl-row"><span className="t">13:30</span><span className="l">Credenciamento digital e recepção</span></div>
            <div className="tl-row"><span className="t">14:15</span><span className="l">Mesa de abertura institucional</span></div>
            <div className="tl-row"><span className="t">15:30</span><span className="l">Painel de apresentação do evento</span></div>
            <div className="tl-row"><span className="t">16:10</span><span className="l">Conferência magna · Magda Chambriard, Petrobras</span></div>
            <div className="tl-row"><span className="t">17:00</span><span className="l">Coquetel de networking</span></div>
          </div>
          <div className="footer"><span>Modalidade 1 e 2</span><span>↗ detalhes</span></div>
        </div>
        <div className="day-card active">
          <div className="day-tag">
            <div className="day-num" style={{color:'var(--amber-soft)'}}>02</div>
            <div className="day-meta"><div className="a">Quinta · 09 jul</div><div className="b">Imersão</div></div>
          </div>
          <h3>Oito visitas técnicas<br/>simultâneas em campo.</h3>
          <div className="where">Região metropolitana do RJ</div>
          <div className="timeline">
            <div className="tl-row"><span className="t">06:30</span><span className="l">Concentração e café no hub</span></div>
            <div className="tl-row"><span className="t">07:00</span><span className="l">Primeira janela de partida</span></div>
            <div className="tl-row"><span className="t">07:30</span><span className="l">Partidas escalonadas · 30 min</span></div>
            <div className="tl-row"><span className="t">09–17</span><span className="l">Realização das 8 jornadas</span></div>
            <div className="tl-row"><span className="t">⌑</span><span className="l">Produto: Relato de Visita (2–3 pp.) para o livro</span></div>
          </div>
          <div className="footer"><span style={{color:'var(--amber-soft)'}}>Modalidade 1 e 4 · vagas/ônibus</span><span>↗ ver visitas</span></div>
        </div>
        <div className="day-card">
          <div className="day-tag">
            <div className="day-num">03</div>
            <div className="day-meta"><div className="a">Sexta · 10 jul</div><div className="b">Síntese</div></div>
          </div>
          <h3>Trilhas, sessões<br/>e premiação acadêmica.</h3>
          <div className="where">NAB UFF · Campus Gragoatá · Niterói</div>
          <div className="timeline">
            <div className="tl-row"><span className="t">09:00</span><span className="l">Plenária + Painel "IA e soberania"</span></div>
            <div className="tl-row"><span className="t">10:30</span><span className="l">Trilhas A, B, C e D simultâneas</span></div>
            <div className="tl-row"><span className="t">14:00</span><span className="l">Sessões técnicas e acadêmicas</span></div>
            <div className="tl-row"><span className="t">16:30</span><span className="l">Premiação dos melhores trabalhos</span></div>
            <div className="tl-row"><span className="t">18:00</span><span className="l">Encerramento · 19h coquetel</span></div>
          </div>
          <div className="footer"><span>Modalidade 1 e 2</span><span>↗ trilhas</span></div>
        </div>
      </div>
    </div>
  </div>
);

const VisitsAfter = () => {
  const visits = [
    {n:'01', name:'Petrobras', desc:'Regulação de energia e transformação digital em operações de E&P.', tags:['Energia','Regulação'], color:'#1f5b8e', vacancy:'18 / 25'},
    {n:'02 ⇄', name:'Águas do Rio + ETE/Biogás', desc:'Saneamento e regulação seguidos de ESG e inovação em saneamento.', tags:['Saneamento','ESG'], color:'#2d6a4f', vacancy:'12 / 25', integrated:true},
    {n:'03', name:'Guandu / Lameirão', desc:'Infraestrutura hídrica e governança no maior sistema de abastecimento da AMRJ.', tags:['Infraestrutura'], color:'#2d6a4f', vacancy:'21 / 25'},
    {n:'04', name:'Ternium · Santa Cruz', desc:'Indústria consumidora de gás, ESG e Lean Six Sigma.', tags:['Indústria','Lean'], color:'#a0451f', vacancy:'09 / 25'},
    {n:'05', name:'Gerdau · Santa Cruz', desc:'Indústria consumidora de gás, transformação digital e ESG.', tags:['Indústria','Digital'], color:'#a0451f', vacancy:'15 / 25'},
    {n:'06 ⇄', name:'Eneva + TAG', desc:'Regulação de energia e GovTech, seguido de transporte de gás natural.', tags:['Energia','GovTech'], color:'#1f5b8e', vacancy:'06 / 25', integrated:true},
    {n:'07 ⇄', name:'IRM + AGENERSA', desc:'Inteligência governamental e saneamento, seguido de sandbox regulatório.', tags:['Inteligência','Sandbox'], color:'#5b3b8e', vacancy:'19 / 25', integrated:true},
    {n:'08', name:'CSN', desc:'Indústria consumidora de gás, ESG e Lean Six Sigma.', tags:['Indústria','Lean'], color:'#a0451f', vacancy:'04 / 25'},
  ];
  return (
    <div className="ab">
      <div className="visits">
        <div className="visits-head">
          <div className="eyebrow">Dia 2 · 09 julho</div>
          <h2 style={{marginTop:14}}>Oito jornadas técnicas <em>exclusivas</em>.</h2>
          <p className="sub">Cada cartão exibe a cor do setor (energia, saneamento, indústria, inteligência), barra de ocupação ao vivo e marcador "⇄" para jornadas integradas. Uma decisão visual — não 8 cartões iguais.</p>
        </div>
        <div className="visits-grid">
          {visits.map((v,i) => {
            const filled = parseInt(v.vacancy)/25;
            const lo = filled > 0.7;
            return (
              <div key={i} className={"visit" + (v.integrated ? " integrated" : "")} style={{['--accent']: v.color}}>
                <div className="n mono">Jornada {v.n}</div>
                <div className="name">{v.name}</div>
                <div className="desc">{v.desc}</div>
                <div className="tags">
                  {v.tags.map((t,j) => <span key={j} className="tag">{t}</span>)}
                </div>
                <div className="vacancy">
                  <span>Vagas preenchidas</span>
                  <span style={{color: lo ? 'var(--rust)' : 'var(--ink-900)'}}>{v.vacancy}</span>
                </div>
                <span className="bar"><i style={{width: (filled*100)+'%', background: lo ? 'var(--rust)' : 'var(--emerald)'}}></i></span>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

const NavCompare = () => (
  <div className="ab">
    <div className="nav-compare">
      <div>
        <div className="eyebrow">Navegação · antes / depois</div>
        <h2 style={{marginTop:14}}>Sete links concorrentes <em>versus</em> hierarquia.</h2>
      </div>
      <div className="nav-row">
        <div className="lbl">Antes</div>
        <div className="nav-mock dark">
          <div className="ml">
            <div className="logo"></div>
            <div className="links">
              <span>Programação</span><span>Eventos</span><span>Visitas</span>
              <span>Submissão</span><span>Parceiros</span><span style={{color:'#ffd56a'}}>Claro</span>
            </div>
          </div>
          <div className="ctas"><span className="pill">Inscreva-se →</span></div>
        </div>
      </div>

      <div className="nav-row">
        <div className="lbl">Depois</div>
        <div className="nav-mock">
          <div className="ml">
            <div style={{display:'flex', flexDirection:'column'}}>
              <div className="serif" style={{fontSize:16, color:'var(--ink-900)'}}>Encontro <em style={{color:'var(--amber)', fontStyle:'italic'}}>GEI</em> <span style={{fontSize:10, fontFamily:'var(--mono)', color:'var(--ink-500)', letterSpacing:'.1em', marginLeft:6}}>2026</span></div>
              <div style={{fontSize:9, fontFamily:'var(--mono)', color:'var(--ink-500)', letterSpacing:'.1em', textTransform:'uppercase'}}>UFF · ABAR · PPGEP · Escola de Regulação</div>
            </div>
            <div className="links" style={{color:'var(--ink-700)', marginLeft:24}}>
              <span>Programa</span><span>Eventos</span><span>Visitas</span><span>Submeter</span><span>Apoio</span>
            </div>
          </div>
          <div className="ctas">
            <span className="ind"><span className="dot"></span>Submissão até 15/05</span>
            <span className="pill">Inscrever-se →</span>
            <span style={{fontFamily:'var(--mono)', fontSize:11, color:'var(--ink-500)', marginLeft:6}}>☾</span>
          </div>
        </div>
      </div>

      <div style={{marginTop:24}}>
        <div className="eyebrow">Quatro correções</div>
        <div className="fix-list">
          <div className="item"><span className="n">1</span><div><b>Sigla institucional + filiações</b> ancoram credibilidade no instante zero. Hoje, o logo é só uma imagem.</div></div>
          <div className="item"><span className="n">2</span><div><b>Reduzir 7 → 5 itens</b> e renomear "Submissão" para "Submeter" e "Parceiros" para "Apoio" (ação > rótulo abstrato).</div></div>
          <div className="item"><span className="n">3</span><div><b>Indicador de prazo crítico</b> em cor distinta. O evento tem deadline real (15/05) — ele precisa estar visível em cada página.</div></div>
          <div className="item"><span className="n">4</span><div><b>Toggle de tema reduzido a glifo</b> à direita, fora do fluxo de leitura. Hoje "Claro" parece um link de seção.</div></div>
        </div>
      </div>
    </div>
  </div>
);

const SubmissionAfter = () => (
  <div className="ab">
    <div className="subflow">
      <div className="subflow-head">
        <div>
          <div className="eyebrow">Submissão · cronograma</div>
          <h2 style={{marginTop:14}}>Seis marcos, um <em>caminho contínuo</em>.</h2>
        </div>
        <div style={{display:'flex', flexDirection:'column', alignItems:'flex-end', gap:6}}>
          <span className="chip warn">⏱ Fase 1 encerra em 10 dias</span>
          <span style={{fontFamily:'var(--mono)', fontSize:11, color:'var(--ink-500)', letterSpacing:'.06em'}}>15.05.2026 · 23h59 BRT</span>
        </div>
      </div>

      <div className="timeline-h">
        <div className="tl-step active">
          <div className="dot">1</div>
          <div className="label">Resumo + vídeo</div>
          <div className="date urgent">até 15/05</div>
        </div>
        <div className="tl-step">
          <div className="dot">2</div>
          <div className="label">Resultado</div>
          <div className="date">31/05/2026</div>
        </div>
        <div className="tl-step">
          <div className="dot">3</div>
          <div className="label">Programa</div>
          <div className="date">25/06/2026</div>
        </div>
        <div className="tl-step">
          <div className="dot">4</div>
          <div className="label">Apresentação</div>
          <div className="date">10/07 · NAB UFF</div>
        </div>
        <div className="tl-step">
          <div className="dot">5</div>
          <div className="label">Artigo final</div>
          <div className="date">30/09/2026</div>
        </div>
        <div className="tl-step">
          <div className="dot">6</div>
          <div className="label">Anais ISBN</div>
          <div className="date">dezembro/2026</div>
        </div>
      </div>

      <div className="formats">
        <div className="fmt">
          <div className="badge">RE</div>
          <div className="code">01</div>
          <h3>Resumo Expandido</h3>
          <div className="summary">Fase 1. Texto curto + vídeo de pitch para triagem inicial pela comissão.</div>
          <div className="specs">
            <div className="row"><span className="k">Páginas</span><span>2 a 4</span></div>
            <div className="row"><span className="k">Palavras</span><span>até 700</span></div>
            <div className="row"><span className="k">Vídeo</span><span>5 min · YouTube</span></div>
            <div className="row"><span className="k">Formato</span><span>.docx / .pdf</span></div>
          </div>
          <div className="dl">↓ baixar normas</div>
        </div>
        <div className="fmt">
          <div className="badge">PA</div>
          <div className="code">02</div>
          <h3>Pôster A3</h3>
          <div className="summary">Diagramação visual em A3, exposta em sessão dedicada no Dia 3.</div>
          <div className="specs">
            <div className="row"><span className="k">Tamanho</span><span>A3 · vertical</span></div>
            <div className="row"><span className="k">Sessão</span><span>Dia 3 · NAB UFF</span></div>
            <div className="row"><span className="k">Vídeo</span><span>opcional</span></div>
            <div className="row"><span className="k">Avaliação</span><span>presencial</span></div>
          </div>
          <div className="dl">↓ baixar normas</div>
        </div>
        <div className="fmt">
          <div className="badge">R3</div>
          <div className="code">03</div>
          <h3>Relatório A3</h3>
          <div className="summary">Modelo DMAIC em uma única folha A3 — para trabalhos aplicados de melhoria.</div>
          <div className="specs">
            <div className="row"><span className="k">Páginas</span><span>1 · A3</span></div>
            <div className="row"><span className="k">Modelo</span><span>DMAIC</span></div>
            <div className="row"><span className="k">Aplicação</span><span>melhoria operacional</span></div>
            <div className="row"><span className="k">Trilha</span><span>Lean Six Sigma</span></div>
          </div>
          <div className="dl">↓ baixar normas</div>
        </div>
        <div className="fmt">
          <div className="badge">AC</div>
          <div className="code">04</div>
          <h3>Artigo Completo</h3>
          <div className="summary">Fase 2. Versão integral em ABNT que será publicada nos anais com ISBN.</div>
          <div className="specs">
            <div className="row"><span className="k">Páginas</span><span>8 a 15</span></div>
            <div className="row"><span className="k">Norma</span><span>ABNT</span></div>
            <div className="row"><span className="k">Prazo final</span><span>30/09/2026</span></div>
            <div className="row"><span className="k">Saída</span><span>livro · ISBN dez/26</span></div>
          </div>
          <div className="dl">↓ baixar normas</div>
        </div>
      </div>
    </div>
  </div>
);

const SystemBoard = () => (
  <div className="ab">
    <div className="system">
      <div>
        <div className="eyebrow">Sistema de design</div>
        <h2 style={{marginTop:14}}>Tipografia <em>editorial</em>.</h2>
        <p className="serif" style={{fontSize:17, lineHeight:1.5, color:'var(--ink-700)', maxWidth:520}}>
          Source Serif 4 para títulos e citações; Inter Tight para corpo e UI; JetBrains Mono para datas,
          códigos e metadados. A serifa carrega o tom acadêmico; o sans dá leitura confortável; o mono
          ancora dados. Uma família por papel — sem ambiguidade.
        </p>
        <div className="type-list" style={{marginTop:32}}>
          <div className="type-row h">
            <div className="meta">Display · Source Serif 4 · 56–96 px · −2% letter-spacing</div>
            <div className="specimen">Governança, regulação<br/>e <span style={{color:'var(--amber)', fontStyle:'italic'}}>inovação</span>.</div>
          </div>
          <div className="type-row t">
            <div className="meta">Lede · Source Serif 4 · 20–22 px · 1.45 line-height</div>
            <div className="specimen serif">Quatro eventos oficiais reunidos em três dias no Rio de Janeiro.</div>
          </div>
          <div className="type-row b">
            <div className="meta">Corpo · Inter Tight · 14–15 px · 1.55 line-height</div>
            <div className="specimen">Cada evento preserva sua identidade e comunidade. O encontro-matriz promove unidade conceitual e sinergia institucional entre as quatro trilhas integradas.</div>
          </div>
          <div className="type-row m">
            <div className="meta">Metadado · JetBrains Mono · 11 px · 0.06 letter-spacing</div>
            <div className="specimen">SUBMISSÃO ATÉ 15/05 · ISBN DEZ/2026 · 24H CERTIFICADAS</div>
          </div>
        </div>
      </div>
      <div>
        <h2 style={{marginTop:14}}>Paleta <em>sóbria</em>.</h2>
        <p className="serif" style={{fontSize:17, lineHeight:1.5, color:'var(--ink-700)'}}>
          Navy profundo como tinta institucional. Creme tonificado para não cansar a vista em leituras
          longas. Âmbar — não amarelo neon — como acento editorial: itálicos, marcadores, urgência. Três
          cores funcionais (verde-floresta para confirmações, ferrugem para prazos, navy para títulos).
        </p>
        <div className="swatches">
          <div className="sw"><div className="ch" style={{background:'#08153d'}}></div><div className="meta"><div className="n">Navy 950</div><div className="h">#08153D · fundo do logo</div></div></div>
          <div className="sw"><div className="ch" style={{background:'#fbf8f1'}}></div><div className="meta"><div className="n">Cream 50</div><div className="h">#FBF8F1 · base clara</div></div></div>
          <div className="sw"><div className="ch" style={{background:'#f7c948'}}></div><div className="meta"><div className="n">Gold</div><div className="h">#F7C948 · "Governança"</div></div></div>
          <div className="sw"><div className="ch" style={{background:'#5fb84a'}}></div><div className="meta"><div className="n">Green</div><div className="h">#5FB84A · "Estratégia"</div></div></div>
          <div className="sw"><div className="ch" style={{background:'#2db8e0'}}></div><div className="meta"><div className="n">Cyan</div><div className="h">#2DB8E0 · "Inovação"</div></div></div>
          <div className="sw"><div className="ch" style={{background:'#6b3fb8'}}></div><div className="meta"><div className="n">Violet</div><div className="h">#6B3FB8 · ponto</div></div></div>
          <div className="sw"><div className="ch" style={{background:'#ee7e2b'}}></div><div className="meta"><div className="n">Orange</div><div className="h">#EE7E2B · ponto · prazo</div></div></div>
          <div className="sw"><div className="ch" style={{background:'#0d1430'}}></div><div className="meta"><div className="n">Ink 900</div><div className="h">#0D1430 · texto</div></div></div>
          <div className="sw"><div className="ch" style={{background:'linear-gradient(135deg,#2db8e0 0%,#5fb84a 50%,#f7c948 100%)'}}></div><div className="meta"><div className="n">Swoosh</div><div className="h">cyan → green → gold</div></div></div>
        </div>
        <div className="stat-band">
          <div className="l">Contraste mínimo</div>
          <div className="v">7.4 : 1</div>
          <div style={{fontFamily:'var(--mono)', fontSize:11, color:'var(--ink-500)', letterSpacing:'.04em', marginTop:4}}>WCAG AAA · texto sobre cream-50</div>
        </div>
      </div>
    </div>
  </div>
);

const MobileBoard = () => (
  <div className="ab">
    <div className="mobile-section">
      <div>
        <div className="eyebrow">Mobile · 3 ajustes-chave</div>
        <h2 style={{marginTop:14}}>O celular merece <em>tratamento próprio</em>.</h2>
        <p className="lede">
          Em telas pequenas, hierarquia importa mais. Três decisões de mobile que pagam dividendos
          imediatos: barra de CTA persistente com prazo, picker de visita técnica como primeira
          classe, e tracker de inscrição como página de confirmação real.
        </p>
        <div className="fix-list" style={{marginTop:32}}>
          <div className="item"><span className="n">A</span><div><b>Sticky bottom bar</b> com prazo de submissão sempre visível e botão de inscrição.</div></div>
          <div className="item"><span className="n">B</span><div><b>Filtros por setor</b> (energia / saneamento / indústria / inteligência) para escolher a visita técnica em três toques.</div></div>
          <div className="item"><span className="n">C</span><div><b>Tracker passo-a-passo</b> da inscrição → submissão → apresentação → certificação.</div></div>
        </div>
      </div>
      <div className="phone-row">
        <div style={{position:'relative'}}>
          <div className="phone">
            <div className="notch"></div>
            <div className="body">
              <div className="p-eyebrow">— Encontro GEI 2026</div>
              <div className="p-h serif">Governança,<br/>regulação e <em>inovação</em>.</div>
              <div className="p-meta">08–10 JUL · RJ</div>
              <div className="p-card">
                <div className="r"><span>Eventos</span><span>04</span></div>
                <div className="r"><span>Visitas</span><span>08</span></div>
                <div className="r"><span>Eixos · ODS</span><span>13</span></div>
                <div className="r"><span>Carga horária</span><span>24h</span></div>
              </div>
              <div className="p-card" style={{marginTop:6, background:'var(--cream-100)', border:'none'}}>
                <div style={{fontSize:8, fontFamily:'var(--mono)', letterSpacing:'.06em', color:'var(--rust)', textTransform:'uppercase'}}>● Submissão fase 1</div>
                <div style={{fontFamily:'var(--serif)', fontSize:11, color:'var(--ink-900)', marginTop:2}}>Encerra em 10 dias</div>
              </div>
            </div>
            <div className="p-cta-bar">
              <div className="a"><strong>Inscreva-se</strong>Gratuito · 400 vagas</div>
              <div className="b">Inscrever →</div>
            </div>
          </div>
          <div className="label">A · Home + sticky CTA</div>
        </div>
        <div style={{position:'relative'}}>
          <div className="phone">
            <div className="notch"></div>
            <div className="body">
              <div className="p-eyebrow">Visitas · 09 jul</div>
              <div className="p-h serif" style={{fontSize:14}}>Escolha sua jornada</div>
              <div className="p-tabs" style={{marginTop:8}}>
                <div className="p-tab act">Todos</div>
                <div className="p-tab">Energia</div>
                <div className="p-tab">Indústria</div>
              </div>
              <div className="p-visit-card">
                <div className="n">JORNADA 01</div>
                <div className="t">Petrobras</div>
                <div className="meta"><span>Energia · Reg</span><span style={{color:'var(--rust)'}}>04 vagas</span></div>
              </div>
              <div className="p-visit-card" style={{['--accent']:'#2d6a4f'}}>
                <div className="n">JORNADA 02 ⇄</div>
                <div className="t">Águas do Rio + ETE</div>
                <div className="meta"><span>Saneamento</span><span>13 vagas</span></div>
              </div>
              <div className="p-visit-card">
                <div className="n">JORNADA 06 ⇄</div>
                <div className="t">Eneva + TAG</div>
                <div className="meta"><span>Energia · GovTech</span><span style={{color:'var(--rust)'}}>06 vagas</span></div>
              </div>
              <div className="p-visit-card">
                <div className="n">JORNADA 08</div>
                <div className="t">CSN</div>
                <div className="meta"><span>Indústria · Lean</span><span style={{color:'var(--rust)'}}>04 vagas</span></div>
              </div>
            </div>
          </div>
          <div className="label">B · Picker de visita</div>
        </div>
        <div style={{position:'relative'}}>
          <div className="phone">
            <div className="notch"></div>
            <div className="body">
              <div className="p-eyebrow">Sua participação</div>
              <div className="p-h serif" style={{fontSize:14}}>Andamento</div>
              <div className="p-meta">Modalidade 1 · 3 dias</div>
              <div className="p-track" style={{marginTop:10}}>
                <div className="p-track-step done"><div className="d"></div><div><div className="lbl">Inscrição confirmada</div><div className="sub">QR · 02/05/2026</div></div></div>
                <div className="p-track-step done"><div className="d"></div><div><div className="lbl">Visita técnica escolhida</div><div className="sub">Jornada 06 · Eneva + TAG</div></div></div>
                <div className="p-track-step act"><div className="d"></div><div><div className="lbl">Submissão Fase 1</div><div className="sub" style={{color:'var(--rust)'}}>10 dias restantes</div></div></div>
                <div className="p-track-step"><div className="d"></div><div><div className="lbl">Apresentação Dia 3</div><div className="sub">10/07 · NAB UFF</div></div></div>
                <div className="p-track-step"><div className="d"></div><div><div className="lbl">Artigo + Certificado</div><div className="sub">30/09 · ISBN dez/26</div></div></div>
              </div>
            </div>
          </div>
          <div className="label">C · Tracker pessoal</div>
        </div>
      </div>
    </div>
  </div>
);

Object.assign(window, {
  Cover, DiagnosisCard, HeroBefore, HeroAfter, Principles,
  ProgramAfter, VisitsAfter, NavCompare, SubmissionAfter, SystemBoard, MobileBoard
});
