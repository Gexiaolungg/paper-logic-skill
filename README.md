# Paper Logic Skill

A small toolkit of prompts, checklists and integration examples to audit and improve academic paper structure, paragraph flow, transitions and language expression. This repository provides ready-to-use prompt templates, a reversible-outline based checklist, and a minimal example showing how to feed paragraph-level text (from a PDF parser such as MinerU) into an LLM for reverse-outline and transition suggestions.

Features
- Reverse-outline prompts for paragraph- and section-level logic checks
- Paragraph flow & transition prompt templates (Chinese)
- Checklist for structure/logic review
- An example adapter for MinerU-style structured_content.json (example)

Quick start
1. Extract paragraph-level blocks from your PDF. Recommended: MinerU (https://github.com/opendatalab/MinerU) or any parser that produces a structured JSON with paragraph items.
2. Use prompts/prompts.md to run reverse-outline checks and generate transition sentence candidates.
3. Review suggestions and accept/modify them in your draft.

Attribution & license notes
This project was informed by and inspired by several existing open-source projects and prompt collections. We DID NOT copy GPLv3 code or large passages from GPL projects. Where we used ideas or templates from permissive-licensed sources (Apache-2.0 / MIT), we rewrote them in our own words and list the sources below.

If you reuse fragments verbatim from upstream projects, follow their license terms (we document sources and licenses in LICENSE_NOTICE.md).

Contributing
- Please include source attribution for any third-party content you add.
- When in doubt about licensing, add a link rather than copying large sections.

