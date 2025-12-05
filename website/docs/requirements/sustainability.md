# Sustainability Requirements

These requirements ensure the platform itself minimizes its ecological footprint.

| ID | Title | Description | Metric |
| :--- | :--- | :--- | :--- |
| **REQ-CORE-SUS-001** | **Dark Mode Default** | To reduce energy consumption on OLED screens, the default UI theme must be Dark. | Default CSS variable `--bg` is `#0f2027` (or similar dark hex). |
| **REQ-CORE-SUS-002** | **Payload Efficiency** | APIs should support field filtering (GraphQL style or partial response) to minimize data transfer energy. | API responses should be GZIP compressed. |