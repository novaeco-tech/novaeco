# Developer Setup

## Local Development
The NovaEco Core Kernel uses **DevContainers** for one‑click setup to ensure a consistent environment for all contributors.

1. Install Docker Desktop.
2. Install the VS Code Remote Containers extension.
3. Clone the repository:  
   ```bash
   git clone https://github.com/novaeco-tech/novaeco.git
````

4.  Open the folder in VS Code.
5.  Click **"Reopen in Container"** when the popup appears.

## Running Services

Once the DevContainer is active, the core infrastructure services are mapped to your localhost:

| Service | Local URL | Credentials / Notes |
| :--- | :--- | :--- |
| **Gateway API** | `http://localhost:8000` | Public Entry point. |
| **Identity (Keycloak)** | `http://localhost:8080` | User: `admin` / Pass: `admin` |
| **Auth Verifier** | `http://localhost:9000` | Internal gRPC & Health check. |
| **Documentation** | `http://localhost:3000` | Hot-reloading docs site. |

> **Note:** The **Mission Control Dashboard** is no longer in this repo. To work on the UI, you must clone and run the `novaadmin` repository separately.

-----

## Related Pages
- [NovaEco CLI](./cli.md)
- [Workflows](./workflows.md)
- [Contribution Guide](./contribution.md)
- [API Overview](../api/overview.md)
