# RedGuard-Core / EvalShield-SDK 🛡️

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Enterprise Ready](https://img.shields.io/badge/Enterprise-Ready-success.svg)](#enterprise)

**Author:** Emirhan CAMCI (<byemir@live.com>) | **Year:** 2026

An enterprise-grade, ultra-lightweight AI Security, Guardrail & Red-Teaming Evaluation Suite for LLM API pipelines and Autonomous Agents. Written in Rust for maximum safety, memory efficiency, and <2ms inference overhead.

## 🚀 3-Line Quickstart

Wrap any OpenAI/vLLM payload in Node.js/Python with real-time guardrails instantly:

```python
from redguard import EnterpriseGuardrail

# 1. Initialize with your Polar.sh Enterprise Offline License
guard = EnterpriseGuardrail(license_key="eyJjdX... (Offline JWT)")

# 2. Intercept and Sanitize Prompt Stream (<2ms latency)
safe_result = guard.evaluate_with_license_check(user_prompt)

# 3. Block or Pass to OpenAI
if safe_result.is_blocked:
    raise ValueError("Prompt Injection or Jailbreak Attempt Detected!")
```

## 🧠 Dual-Licensing Architecture (Open-Core)

RedGuard is distributed via an Open-Core model:

| Feature | Community (AGPLv3) | Enterprise (Proprietary / Polar.sh) |
|---------|-------------------|--------------------------------------|
| **Prompt Injection Detection** | Static Patterns & Regex | AI-Assisted Vector Similarity & Fuzzer |
| **PII Redaction** | Basic Masking (Regex) | Context-Aware De-identification Vaults |
| **Sandboxed Code Evals** | Local CLI (Limited) | Dynamic WASM MicroVM Execution |
| **Offline Licensing** | N/A | Ed25519 Cryptographic Verification |
| **Telemetry & Reporting**| CLI Only | Audit Memos (PDF/JSON) + CI/CD Blocks|

### 💼 Enterprise Subscription
Designed for B2B Security Teams. Pricing ranges from **$1,200 – $4,800/year per seat/cluster**.
Support open-source development and get the Proprietary tier securely via [Polar.sh](https://polar.sh/).

## ⚡ Performance Benchmark (<2ms Overhead)
Built in Rust, RedGuard guarantees zero-copy token inspection ensuring strict adherence to PII compliance without sacrificing LLM time-to-first-token (TTFT). Memory-leak free and formally verified.

---
*RedGuard-Core operates 100% on-device (Air-Gapped) - NO data is sent to external servers.*
