#!/usr/bin/env python3
"""Aurekai Pulumi stack — core pipeline Kubernetes Jobs."""
import pulumi
import pulumi_kubernetes as k8s

config = pulumi.Config("aurekai")
version = config.get("version") or "0.8.0-alpha.4"
image = f"ghcr.io/aurekai/aurekai:{version}"

labels = {"aurekai.io/managed-by": "pulumi", "aurekai.io/version": version}

COMMANDS = [
    ("doctor-deep", ["akai", "doctor", "--deep", "--json"]),
    ("manifest-verify", ["akai", "verify", "--manifest", "artifact.json", "--json"]),
    ("model-memory-pack", ["akai", "pack", "--tag", "latest", "--json"]),
    ("sae-audit", ["akai", "sae", "audit", "--model", "default", "--json"]),
    ("semantic-cache-bench", ["akai", "cache", "bench", "--queries", "100", "--json"]),
    ("proof-bundle-export", ["akai", "proof", "export", "--output", "/tmp/proof.tar.gz"]),
    ("release-gate", ["akai", "release", "gate", "--version", version, "--json"]),
]

jobs = {}
for name, cmd in COMMANDS:
    job = k8s.batch.v1.Job(
        f"aurekai-{name}",
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name=f"aurekai-{name}",
            labels=labels,
        ),
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

pulumi.export("version", version)
pulumi.export("image", image)
