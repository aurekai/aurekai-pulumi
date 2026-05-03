# Quickstart — aurekai-pulumi

Pulumi stack for deploying the Aurekai pipeline on Kubernetes.

## Requirements

- Python 3.10+
- `pip install -r requirements.txt`
- Kubernetes cluster configured in `~/.kube/config`

## Deploy

```bash
pulumi up
```

## Destroy

```bash
pulumi destroy
```

## Validate

```bash
bash tests/validate-schemas.sh
bash tests/validate-scripts.sh
```
