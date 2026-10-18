# LICENSE & Attribution (sources and notes)

本文件记录本仓库在方法论、prompt 与设计上借鉴或参考的开源项目与资源，并说明许可处理策略。

1) 主要参考来源

- Yuan1z0825 / nature-skills
  - 关键参考文件：skills/nature-writing/references/paragraph-flow.md, skills/nature-writing/references/nature-summary-paragraph.md
  - 链接: https://github.com/Yuan1z0825/nature-skills
  - 许可：仓库内含 Apache-2.0（及部分子模块 MIT）。我们以原创改写形式采纳其方法论与模板，并在本仓库中以改写文本呈现；在本文件中列出其为重要启发来源。

- opendatalab / MinerU
  - 用途：推荐作为 PDF/Office -> paragraph-level structured JSON 的输入工具
  - 链接: https://github.com/opendatalab/MinerU
  - 许可/注意：请遵循 MinerU 的开源许可；本仓库不包含 MinerU 源码，仅提供适配示例。

- binary-husky / gpt_academic
  - 用途：作为设计思想（插件化、批量处理、多模型接入）的参考
  - 链接: https://github.com/binary-husky/gpt_academic
  - 许可说明：该仓库包含 GPLv3 许可内容。我们仅借鉴其工程与 UX 思路，不直接拷贝其代码或 README（以避免许可证冲突）。如需直接使用其代码，请遵循 GPLv3 的要求（或将本仓库以兼容许可方式处理）。

- prompts.chat
  - 用途：prompt 模板设计灵感来源
  - 链接: https://github.com/f/prompts.chat
  - 许可/注意：请在使用具体 prompt 时检查其原始许可。

2) 采纳原则与合规处理

- 对 Apache-2.0 / MIT 授权的内容：可改写并在 LICENSE_NOTICE 中注明原始来源及链接；如直接摘录（大量或完整段落），应一并保留原始 LICENSE 文本或 NOTICE 文件。
- 对 GPLv3 授权的内容：避免直接复制到本仓库。如确需使用其代码或较大段文本，请在使用前调整本仓库许可或将其作为子模块并保留原始许可说明。
- 对未明确许可内容：不直接复制，优先以自己的语言重写或只引用链接。

3) 致谢样例（供 README 使用）

> 本项目受以下开源项目启发：Yuan1z0825/nature-skills (paragraph-flow, summary-paragraph)、opendatalab/MinerU、binary-husky/gpt_academic（设计思想）。感谢这些项目的开源贡献。有关具体来源与许可，请参阅 LICENSE_NOTICE.md。

