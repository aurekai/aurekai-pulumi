#!/usr/bin/env python3
"""
Aurekai Pulumi stack — full capability stack.
Provisions Kubernetes Jobs for all capability operators,
plus CrossGuard-validated resources and ESC secret references.
"""
import pulumi
import pulumi_kubernetes as k8s
import pulumi_command as command

config = pulumi.Config("aurekai")
version = config.get("version") or "0.8.0-alpha.5"
model_tag = config.get("model_tag") or "qwen3-8b"
bits = config.get_int("bits") or 8
image = f"ghcr.io/aurekai/aurekai:{version}"

labels = {"aurekai.io/managed-by": "pulumi", "aurekai.io/version": version}

# ── Capability operator jobs ──────────────────────────────────────────────────

OPERATOR_COMMANDS = [
    ("doctor-deep",          ["akai", "doctor", "--deep", "--json"]),
    ("manifest-verify",      ["akai", "verify", "--manifest", "artifact.json", "--json"]),
    ("model-memory-pack",    ["akai", "pack", "--tag", model_tag, "--json"]),
    ("fpq-compress",         ["akai", "fpq", "compress", "--model", model_tag, "--bits", str(bits), "--json"]),
    ("fpqx-align",           ["akai", "fpqx", "align", "--model", model_tag, "--json"]),
    ("sli-auto-run",         ["akai", "sli", "auto-run", "--json"]),
    ("sae-audit",            ["akai", "sae", "audit", "--json"]),
    ("semantic-cache-bench", ["akai", "cache", "bench", "--json"]),
    ("proof-bundle-export",  ["akai", "proof", "bundle", "--json"]),
    ("graph-lineage",        ["akai", "graph", "lineage", "--json"]),
    ("release-gate",         ["akai", "release", "gate", "--version", version, "--json"]),
    ("runtime-capabilities", ["akai", "runtime", "capabilities", "--json"]),
]

jobs = {}
for name, cmd in OPERATOR_COMMANDS:
    job = k8s.batch.v1.Job(
        f"aurekai-{name}",
        metadata=k8s.meta.v1.ObjectMetaArgs(name=f"aurekai-{name}", labels=labels),
        spec=k8s.batch.v1.JobSpecArgs(
            template=k8s.core.v1.PodTemplateSpecArgs(
                spec=k8s.core.v1.PodSpecArgs(
                    restart_policy="Never",
                    containers=[k8s.core.v1.ContainerArgs(
                        name="akai",
                        image=image,
                        command=cmd,
                    )],
                ),
            ),
        ),
    )
    jobs[name] = job

# ── Local validation (pre-deploy) ─────────────────────────────────────────────

doctor_local = command.local.Command(
    "aurekai-pre-deploy-doctor",
    create="akai doctor --deep --json",
)

# ── Stack outputs ─────────────────────────────────────────────────────────────

pulumi.export("version", version)
pulumi.export("model_tag", model_tag)
pulumi.export("image", image)
pulumi.export("job_names", list(jobs.keys()))

