# AI Agents Papers

This repository curates the latest research papers on the applications and architectural technologies of AI agents. We perform weekly Arxiv searches using specific keywords and pick only those that are particularly interesting. Rather than striving for comprehensiveness, we add papers when they introduce a distinctively new approach or novel concept that stands out from existing methods.

## AI Agent
An AI Agent is an autonomous system powered by large language models that can perceive its environment, reason through complex tasks, and use tools to take actions in pursuit of specific goals. It combines reasoning, planning, memory, and tool-use capabilities to operate independently or as part of a multi-agent system.

<figure style="text-align: center;">
    <img alt="" src="./assets/ai-agent-workflow.png" width="500" />
    <figcaption style="text-align: center;">AI Agent Workflows</figcaption>
</figure>

## Paper Categories

Papers are filed in **four layers** — *capabilities* (what an agent can do), *architecture* (how it's built), *operations* (how it's run), and *applications* (where it's used). Each entry links to a curated, date-ordered reading list.
🔥: Recommended papers  
📖: Survey papers  
⚖️: Benchmark papers

> 🔄 Badges show papers added in the last 2 months (Jul–Aug 2026); cluster headings show the sum: `(+N)` recent additions, 🔥 = high activity. Regenerate: `python scripts/update_readme_badges.py`.
>
> 📂 See [**TAXONOMY.md**](TAXONOMY.md) for the full directory map and the rules for where each paper is filed.

- **Agent Capabilities** — what an agent can do: cognition, knowledge, action, and how it learns & improves
  - *Core Cognition* — reason, plan, ideate, perceive (+5)
    - [Reasoning](capabilities/core-cognition/reasoning.md) (+2)
    - [Planning](capabilities/core-cognition/planning.md) (+1)
    - [Ideation](capabilities/core-cognition/ideation.md) (+2)
    - [Perception](capabilities/core-cognition/perception.md)
  - *Knowledge & Context* — what the agent knows and carries between steps (+12) 🔥
    - [Memory](capabilities/knowledge-context/memory.md) (+6)
    - [Context Engineering](capabilities/knowledge-context/context-engineering.md) (+4)
    - [Knowledge Graphs & Ontology](capabilities/knowledge-context/knowledge-graph.md) (+2)
  - *Action* — acting through tools and reusable skills (+13) 🔥
    - [Tool Use](capabilities/action/tool-use.md) (+2)
    - [Skills](capabilities/action/skills.md) (+11) 🔥
  - *Adaptation & Self-Improvement* — getting better from experience (+33) 🔥
    - [Exploration & Discovery](capabilities/adaptation/exploration.md) (+2)
    - [Experience & Trajectory Learning](capabilities/adaptation/experience.md) (+3)
    - [Failure Attribution & Error Localization](capabilities/adaptation/failure-attribution.md) (+8)
    - [Self-Correction](capabilities/adaptation/self-correction.md) (+2)
    - [Verification](capabilities/adaptation/verification.md)
    - [Self-Evolution](capabilities/adaptation/self-evolution.md/#self-evolution-self-improvement) (+13) 🔥
    - [Agent Tuning](capabilities/adaptation/learning.md) (+5)
  - *Trust & Measurement* — is it safe, and how well does it work? (+21) 🔥
    - [Safety](capabilities/trust/safety.md) (+7)
    - [Agent Evaluation](capabilities/trust/evaluation.md) (+14) 🔥
  - *Other* — world models, user profiles, forecasting (+3)
    - [Environment (World Models & Simulations)](capabilities/other/environment.md) (+1)
    - [Profile](capabilities/other/profile.md) (+1)
    - [Prediction](capabilities/other/prediction.md) (+1)
- **AI Agents Architecture** — how an agent is built: single-agent design, multi-agent systems, and the runtime harness (+26) 🔥
  - [Agent Design & Frameworks](architecture/agent-design.md) (+1)
  - [Multi-Agent Systems](architecture/multi-agent.md) (+4)
  - [Harness](architecture/harness.md) (+21) 🔥
- **Operations & Interaction** — how an agent is run and works with people: observability, UX, and governance (+6)
  - [AgentOps & Observability](operations/agentops.md)
  - [Human-AI Interaction & UX](operations/human-ai.md)
  - [Governance & Governed Self-Improvement](operations/governance.md) (+6)
- **AI Agents Applications** — where agents are deployed, grouped by interface, domain, and task pattern
  - *By Embodiment / Interface* — where the agent acts
    - [Embodied Agents](applications/interface/embodied-agents.md)
    - [Computer-Use (GUI) Agents](applications/interface/computer-use-agents.md)
    - [Web Agents](applications/interface/web-agents.md)
    - [Mobile Agents](applications/interface/mobile-agents.md)
  - *By Domain / Vertical* — the industry it serves (+24) 🔥
    - [Financial Agents](applications/domain/finance-agents.md) (+4)
    - [Enterprise Agents](applications/domain/enterprise-agents.md) (+8)
    - [AI Scientist (Research Automation)](applications/domain/ai-scientist.md) (+7)
    - [Vertical / Domain Agents](applications/domain/vertical-agents.md) (+5)
  - *By System Pattern / Task Form* — the shape of the task or system (+15) 🔥
    - [Coding Agents](applications/system/coding-agents.md) (+3)
    - [Data Agents](applications/system/data-agents.md) (+3)
    - [Deep Research Agents](applications/system/deep-research-agents.md) (+5)
    - [World Simulation](applications/system/world-simulation.md) (+4)
- **GenAI Agents Presentations**
  - [Tutorial & Lecture](lectures/tutorial-lecture.md)

## References
- [LLM Agents Papers](https://github.com/zjunlp/LLMAgentPapers)
- [Awesome LLM-Powered Agent](https://github.com/hyp1231/awesome-llm-powered-agent/)
 - [Awesome LLM agents](https://github.com/kaushikb11/awesome-llm-agents)

# Trend Newsletters（研究トレンド）

カテゴリ別の月次トレンド深掘り。2026-06 以降は各論文の **arXiv HTML 本文を精読**し、**図を引用**、複数論文で裏付けたファクトを中心にまとめています（作成手順は `.claude/skills/newsletter`）。

**2026-07**
- [Harness](newsletters/jul_2026/harness_trends.md) · [Agent Evaluation](newsletters/jul_2026/evaluation_trends.md) · [Self-Evolution](newsletters/jul_2026/self_evolution_trends.md)

**2026-06**
- [Self-Evolution](newsletters/jun_2026/self_evolution_trends.md) · [Coding Agents](newsletters/jun_2026/coding_agents_trends.md) · [Skills](newsletters/jun_2026/skills_trends.md)

**2026-05**
- [May Trends（総合）](newsletters/may_2026/trends_2026_05.md)

**2026-04**
- [Self-Evolution](newsletters/apr_2026/self_evolution_trends.md) · [Memory](newsletters/apr_2026/memory_trends.md) · [Tool Use](newsletters/apr_2026/tool_use_trends.md) · [Cybersecurity（2025 総覧）](newsletters/apr_2026/cybersecurity_2025.md)

**2026-02**
- [Skills](newsletters/feb_2026/skills.md) · [Deep Research](newsletters/feb_2026/deep_research.md) · [Ideation](newsletters/feb_2026/ideation_trends.md) · [Prediction](newsletters/feb_2026/prediction_trends.md)

**2026-01**
- [Self-Evolution](newsletters/jan_2026/self_evolution_trends.md) · [Memory](newsletters/jan_2026/memory_trends.md)

# Monthly Highlights

Monthly curated picks (a handful of standout papers per month) are archived under [`highlights/`](highlights/):

- [2026-05 May](highlights/2026-05-may.md)
- [2026-04 April](highlights/2026-04-april.md)
- [2026-03 March](highlights/2026-03-march.md)
- [2026-02 February](highlights/2026-02-february.md)
- [2026-01 January](highlights/2026-01-january.md)
- [2025-12 December](highlights/2025-12-december.md)
- [2025 Review (Apr–Dec)](highlights/2025-review.md)
