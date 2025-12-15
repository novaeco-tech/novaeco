# 🌍 NovaEco Core

**NovaEco** is the open‑source **Digital Public Infrastructure** for the circular economy.  
It connects individuals and siloed sectors to **foster innovation**, measure impact, and **collaborate** within a federated system-of-systems.

This repository (`novaeco`) is the **Kernel** of the system. It hosts the shared infrastructure (Gateway, Auth, Documentation) that anchors the wider ecosystem.

---

## 🏗️ Architecture Overview

The Core repository provides the fundamental plumbing for the federated network.

| Service | Path | Type | Port | Public URL | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Gateway** | `/api` | Python/Flask | `8000` | `api.novaeco.tech` | **API Gateway.** Secure access and routing to all sectors. |
| **Auth** | `/auth` | Python/Flask | `9000` | `auth.novaeco.tech` | **Token Verifier.** Validates JWTs for internal services. |
| **Identity** | *(Infrastructure)* | Java | `8080` | `id.novaeco.tech` | **Identity Provider.** Keycloak instance for SSO & User Management. |
| **Docs** | `/website` | Node.js | `3000` | `novaeco.tech` | **Documentation.** Architecture and use cases. |

> **Looking for the rest of the ecosystem?** > NovaEco includes 10+ Enablers (e.g., NovaTrade) and 13+ Sectors (e.g., NovaAgro).  
> 👉 **[View Full Architecture](http://localhost:3000/docs/architecture/overview)** (once running) or visit [novaeco.tech](https://novaeco.tech).

### 🔐 The Identity Stack
The Core repo uses a standard OIDC infrastructure split into two domains:
1.  **Identity (`id.novaeco.tech`):** The **Public Provider**. This is where users are redirected to log in. It manages the user database and issues tokens.
2.  **Auth (`auth.novaeco.tech`):** The **Internal Verifier**. It acts as a bridge, allowing internal microservices to validate tokens via high-performance gRPC without hitting the public Keycloak endpoints directly.

---

## 🚀 Getting Started (Local Development)

This repository is configured to use **DevContainers** for a one-click setup.

1.  Make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
2.  Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VS Code.
3.  Clone this repository:  
    ```bash
    git clone https://github.com/novaeco-tech/novaeco.git
    ```
4.  Open the cloned folder in VS Code.
5.  A pop-up will appear: *"Folder contains a Dev Container... Reopen in Container?"*. Click **"Reopen in Container"**.

This will build the environment defined in `.devcontainer/` and automatically start the Gateway, Auth, Identity (Keycloak), and Docs.

### 🖥️ Accessing the Services

Once the container is running, the services are available locally:

* **API Gateway Health:** [http://localhost:8000/health](http://localhost:8000/health)
* **Auth Verifier:** [http://localhost:9000/health](http://localhost:9000/health)
* **Identity Console (Keycloak):** [http://localhost:8080](http://localhost:8080) *(User: admin / Pass: admin)*
* **Website/Docs:** [http://localhost:3000](http://localhost:3000)

---

## 🛠️ Development Workflow

The NovaEco Core runs multiple containers.  
When you open this repo in VS Code, it attaches to the **API (Gateway)** service by default. This is your primary terminal for running CLI commands and tests.

**✅ All services start automatically.** You do not need to run `python src/api_service.py` manually. The containers launch immediately and watch your files for changes (**hot-reload**).

### 🐛 Debugging the API (Manual Start)

By default, the API runs in the background. If you want to **attach a debugger (F5)**:

1.  Open `.devcontainer/docker-compose.yml`.
2.  Find the `api` service and change the `command` line:
    ```yaml
    # CHANGE FROM (Auto-Start):
    # command: sh -c "pip install ... && python -m src.api_service"

    # TO (Debug Mode):
    command: sleep infinity
    ```
3.  Open the Command Palette (`Ctrl+Shift+P` / `F1`) and select **"Dev Containers: Rebuild Container"**.
4.  Once rebuilt, the API will **not** be running. You can now press **F5** or run `python -m src.api_service` in the terminal to start it with the debugger attached.

### 🧰 Developer Tools (NovaEco CLI)

We use the internal `novaeco` CLI to manage versions and automation.

**Installation** The CLI is installed automatically in the DevContainer. If you need to reinstall it manually:
```bash
pip install "git+https://github.com/novaeco-tech/novaeco-devtools.git@main#subdirectory=novaeco-cli"
```

**Usage**

  * **Patching a Service (Bug Fixes):**
    Increments the patch version (e.g., `1.0.1` -\> `1.0.2`).
    ```bash
    novaeco version patch api
    ```
  * **Releasing a Feature (Minor/Major):**
    Updates the Global version and aligns ALL services (e.g., `1.1.0`).
    ```bash
    novaeco version release minor
    ```

### 💻 Switching to Website or Auth

To run commands for the Docs or Auth service (e.g., `npm install`), you must **attach** to their specific containers.

1.  **Click the "Remote Explorer" icon** in the VS Code sidebar.
2.  Look under the **"Other Containers"** list.
3.  Right-click the service (e.g., `novaeco_devcontainer-website-1`).
4.  Select **"Attach to Visual Studio Code"**.

**Result:** A **new VS Code window** opens for that service.

### ⚠️ "Port Already in Use" Warning

If you attach to the **Website** container and try to run `npm start`, you might see *"Something is already running on port 3000"*. **This is normal.** The container automatically started the server for you. Just edit files and let hot-reload do the work.

-----

## 🧪 Running Tests

The test strategy follows the V-Model. You can run these commands from the main VS Code terminal (API container):

  * **Level 5: Unit Tests (Mocked Dependencies)**

    ```bash
    # Run inside the API or Auth container
    pytest tests/unit
    ```

  * **Level 4: Integration Tests (Real Containers)**
    These tests verify the wiring between the Gateway, Auth Service, and Keycloak container.

    ```bash
    # Run inside the API container (Main Window)
    pytest tests/integration
    ```

  * **Level 3: End-to-End (E2E) Tests**
    Uses Playwright to verify the Documentation site and Gateway responses from a "user" perspective.

    ```bash
    # Run inside the API container (Main Window)
    playwright install  # (First run only)
    pytest tests/e2e
    ```

  * **Performance Tests**
    Runs micro-benchmarks on critical hot-paths (e.g., JWT validation speed).

    ```bash
    # Run inside the API container (Main Window)
    pytest tests/performance
    ```

  * **Website Tests (Node.js):**

    ```bash
    # You MUST attach to the Website container first
    npm test
    ```
