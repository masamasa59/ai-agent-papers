# AI Agents Papers

This repository curates the latest research papers on the applications and architectural technologies of AI agents. We perform weekly Arxiv searches using specific keywords and pick only those that are particularly interesting. Rather than striving for comprehensiveness, we add papers when they introduce a distinctively new approach or novel concept that stands out from existing methods.

## AI Agent
An AI Agent is an autonomous system powered by large language models that can perceive its environment, reason through complex tasks, and use tools to take actions in pursuit of specific goals. It combines reasoning, planning, memory, and tool-use capabilities to operate independently or as part of a multi-agent system.

<figure style="text-align: center;">
    <img alt="" src="./assets/ai-agent-workflow.png" width="500" />
    <figcaption style="text-align: center;">AI Agent Workflows</figcaption>
</figure>

## Paper Categories
🔥: Recommended papers  
📖: Survey papers  
⚖️: Benchmark papers

> 🔄 Badges show papers added in the last 2 months (Jul–Aug 2026): `(+N)` recent additions, 🔥 = high activity. Regenerate: `python scripts/update_readme_badges.py`.
>
> 📂 See [**TAXONOMY.md**](TAXONOMY.md) for the full directory map and the rules for where each paper is filed.

- **Agent Capabilities**
  - *Core Cognition*
    - [Reasoning](capabilities/core-cognition/reasoning.md) (+2)
    - [Planning](capabilities/core-cognition/planning.md) (+1)
    - [Ideation](capabilities/core-cognition/ideation.md) (+2)
    - [Perception](capabilities/core-cognition/perception.md)
  - *Knowledge & Context*
    - [Memory](capabilities/knowledge-context/memory.md) (+6)
    - [Context Engineering](capabilities/knowledge-context/context-engineering.md) (+4)
    - [Knowledge Graphs & Ontology](capabilities/knowledge-context/knowledge-graph.md) (+2)
  - *Action*
    - [Tool Use](capabilities/action/tool-use.md) (+2)
    - [Skills](capabilities/action/skills.md) (+11) 🔥
  - *Adaptation & Self-Improvement*
    - [Exploration & Discovery](capabilities/adaptation/exploration.md) (+2)
    - [Experience & Trajectory Learning](capabilities/adaptation/experience.md) (+3)
    - [Failure Attribution & Error Localization](capabilities/adaptation/failure-attribution.md) (+8)
    - [Self-Correction](capabilities/adaptation/self-correction.md) (+2)
    - [Verification](capabilities/adaptation/verification.md)
    - [Self-Evolution](capabilities/adaptation/self-evolution.md/#self-evolution-self-improvement) (+13) 🔥
    - [Agent Tuning](capabilities/adaptation/learning.md) (+5)
  - *Trust & Measurement*
    - [Safety](capabilities/trust/safety.md) (+7)
    - [Agent Evaluation](capabilities/trust/evaluation.md) (+14) 🔥
  - *Other*
    - [Environment (World Models & Simulations)](capabilities/other/environment.md) (+1)
    - [Profile](capabilities/other/profile.md) (+1)
    - [Prediction](capabilities/other/prediction.md) (+1)
- **AI Agents Architecture**
  - [Agent Design & Frameworks](architecture/agent-design.md) (+1)
  - [Multi-Agent Systems](architecture/multi-agent.md) (+4)
  - [Harness](architecture/harness.md) (+21) 🔥
- **Operations & Interaction**
  - [AgentOps & Observability](operations/agentops.md)
  - [Human-AI Interaction & UX](operations/human-ai.md)
  - [Governance & Governed Self-Improvement](operations/governance.md) (+6)
- **AI Agents Applications**
  - *By Embodiment / Interface*
    - [Embodied Agents](applications/interface/embodied-agents.md)
    - [Computer-Use (GUI) Agents](applications/interface/computer-use-agents.md)
    - [Web Agents](applications/interface/web-agents.md)
    - [Mobile Agents](applications/interface/mobile-agents.md)
  - *By Domain / Vertical*
    - [Financial Agents](applications/domain/finance-agents.md) (+4)
    - [Enterprise Agents](applications/domain/enterprise-agents.md) (+8)
    - [AI Scientist (Research Automation)](applications/domain/ai-scientist.md) (+7)
    - [Vertical / Domain Agents](applications/domain/vertical-agents.md) (+5)
  - *By System Pattern / Task Form*
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

# Monthly Highlights

Monthly curated picks (a handful of standout papers per month) are archived under [`highlights/`](highlights/):

- [2026-05 May](highlights/2026-05-may.md)
- [2026-04 April](highlights/2026-04-april.md)
- [2026-03 March](highlights/2026-03-march.md)
- [2026-02 February](highlights/2026-02-february.md)
- [2026-01 January](highlights/2026-01-january.md)
- [2025-12 December](highlights/2025-12-december.md)
- [2025 Review (Apr–Dec)](highlights/2025-review.md)
