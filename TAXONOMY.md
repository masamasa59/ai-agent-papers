# Taxonomy & Filing Guide

How this repository is organized and where to file a new paper. The goal is a **fast, consistent weekly triage**: pick the layer, then the file, using the boundary rules below.

## Directory map (4 layers)

```
capabilities/           — building blocks: what an agent can do
  core-cognition/       reasoning · planning · ideation · perception
  knowledge-context/    memory · context-engineering · knowledge-graph
  action/               tool-use · skills
  adaptation/           exploration · experience · failure-attribution · self-correction · verification · self-evolution · learning
  trust/                safety · evaluation
  other/                environment · profile · prediction
architecture/           — how an agent is built (single-agent design, MAS, runtime)
  agent-design · multi-agent · harness
operations/             — how an agent is run & interacts in production
  agentops · human-ai · governance
applications/           — where agents are used
  interface/            embodied · computer-use · web · mobile
  domain/               finance · enterprise · ai-scientist · vertical
  system/               coding · data · deep-research · world-simulation
```

## Boundary rules (which file?)

| If you're unsure between… | File it by this rule |
|---|---|
| **learning vs self-evolution** | updates model **weights** → `learning`; weight-free (in-context / prompt / memory / harness) → `self-evolution` |
| **self-evolution vs RSI** | improves **task performance** → main list; improves the **improvement mechanism itself** (meta-level, Gödel-machine) → `self-evolution` § *Recursive Self-Improvement* |
| **harness vs self-evolution** | the runtime **scaffold** (loop, tool interface, context mgmt, substrate) → `harness`; the agent's **internals** → `self-evolution` |
| **environment vs harness** | the **world** the agent acts on (world model / simulator / RL env) → `environment`; the **scaffold** running the agent → `harness` |
| **memory vs context-engineering** | long-term **storage** → `memory`; assembling the **per-step context window** (compression, offload, packing, rot) → `context-engineering` |
| **memory/context vs knowledge-graph** | symbolic / structured knowledge (KG, ontology) → `knowledge-graph` |
| **tool-use vs skills** | a single tool/API **call** → `tool-use`; a reusable **procedure** (SKILL.md, skill library, skill evolution) → `skills` |
| **verification vs self-correction vs evaluation vs failure-attribution** | inference-time **checking** (verifier/critic/step-verify) → `verification`; reflection / retry / **repair** → `self-correction`; benchmark **methodology** → `evaluation`; diagnosing **what/where/why** it failed (localization, credit assignment, trajectory debugging) → `failure-attribution` |
| **experience vs self-evolution vs learning** | trajectory/experience as a **reusable resource** (experience bank, learning-from-experience, trajectory-as-data) → `experience`; the **loop** that consumes experience to change behavior → `self-evolution`; **weight** training → `learning` |
| **governance vs safety** | **controlled / permissioned change** (governed self-improvement, verifier-gated updates, approval / audit, access control) → `operations/governance`; attacks / defenses / harm → `safety` |
| **exploration vs ai-scientist** | search / discovery **method** (capability) → `exploration`; **scientific** research automation (application) → `ai-scientist` |
| **reasoning vs long-horizon** | reasoning is a **capability axis**; long-horizon is a **task property** — do NOT create a long-horizon category, tag it instead |
| **multi-agent: architecture vs application** | MAS **design/coordination** (frameworks, orchestration, debate) → `architecture/multi-agent`; MAS **applications** (world/social simulation, domain task-solving) → `applications/system/world-simulation` or the relevant `domain/` file |
| **ai-scientist vs deep-research** | automating **scientific** research (experiment/paper/review) → `ai-scientist`; **web deep-research** report generation (Agentic RAG) → `deep-research` |
| **coding vs software** | agents that write/fix code → `coding-agents` (the term "software agents" is legacy/ambiguous — avoid) |
| **agent-ops vs human-ai** | observability / deployment / spec / business → `agentops`; collaboration / UX / alignment / UI → `human-ai` |
| **vertical vs a dedicated domain file** | if a dedicated domain file exists (finance/enterprise/ai-scientist) use it; otherwise a subsection of `vertical` |

## Conventions

- **Format:** `* [emoji] [Mon YYYY] **"Title"** [[paper](url)]` — `🔥` recommended, `📖` survey, `⚖️` benchmark.
- **Order:** entries within a file/subsection are kept in **ascending date order** (arXiv id ascending ≈ chronological).
- **Cross-listing:** a paper may appear in **up to 2 files** when it genuinely spans two categories.
- **Subsections before new files:** when a theme grows inside a file, add a `###` subsection first; only split into a new file once it is large and coherent enough (roughly ≥ 40 entries).
- **Cross-cutting tags (not categories):** *long-horizon* and *RSI* are handled as a tag / flagship subsection, not as their own files, because they intersect many categories.

## Watch-list (emerging themes; monitor, don't split yet)

- **Governance & accountability** (currently `safety` § *Governance*) — split out if it keeps growing.
- **Agent economics / marketplaces** (negotiation, reputation, auctions — currently scattered across `multi-agent` / `safety` / `world-simulation`).
- **Agent security** (prompt injection, trajectory poisoning — currently `safety` § *Attacks*).
