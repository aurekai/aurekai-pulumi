<p align="center">
  <img src="https://raw.githubusercontent.com/aurekai/aurekai/main/assets/aurekai-logo.svg" alt="Aurekai" width="520" />
</p>

# `aurekai-pulumi` · v0.8.0-alpha.5

Official Pulumi integration for Aurekai — Kubernetes Job provisioning for all 12 capability operators, local pre-deploy validation, CrossGuard policies, and Pulumi ESC secret references.

## Resources Provisioned

| Resource | Description |
|---|---|
| `aurekai-doctor-deep` | K8s Job: deep diagnostics |
| `aurekai-manifest-verify` | K8s Job: manifest validation |
| `aurekai-model-memory-pack` | K8s Job: model pack |
| `aurekai-fpq-compress` | K8s Job: FPQ compression |
| `aurekai-fpqx-align` | K8s Job: FPQx alignment |
| `aurekai-sli-auto-run` | K8s Job: SLI convergence |
| `aurekai-sae-audit` | K8s Job: SAE audit |
| `aurekai-semantic-cache-bench` | K8s Job: cache benchmark |
| `aurekai-proof-bundle-export` | K8s Job: proof bundle export |
| `aurekai-graph-lineage` | K8s Job: graph lineage |
| `aurekai-release-gate` | K8s Job: release gate |
| `aurekai-runtime-capabilities` | K8s Job: capability enumeration |
| `aurekai-pre-deploy-doctor` | Local: `akai doctor --deep --json` before deploy |

## Config

```yaml
# Pulumi.dev.yaml
config:
  aurekai:version: 0.8.0-alpha.5
  aurekai:model_tag: qwen3-8b
  aurekai:bits: 8
```

## CrossGuard Policies

```python
# policies/aurekai_policies.py
# Requires proof store and manifest to be valid before deploy
```

## Quick Start

```bash
pip install pulumi pulumi-kubernetes pulumi-command
pulumi stack init dev
pulumi up
```


Aurekai integration surface for Pulumi.

Status: active
Type: infra

## Core Template Set

- doctor-deep
- manifest-verify
- model-memory-pack
- sae-audit
- semantic-cache-bench
- proof-bundle-export
- release-gate

## Canonical References

- Platform: https://github.com/aurekai/aurekai
- Native runtime: https://github.com/aurekai/native-runtime
- Integration registry: https://github.com/aurekai/aurekai/blob/main/registry/integrations.json
- Ecosystem map: https://github.com/aurekai/aurekai/blob/main/ECOSYSTEM_NAMES.md
