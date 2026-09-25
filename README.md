# SAS Customer Intelligence 360

## SAS 360 API SYSTEM FOR CROSS-DOMAIN IDENTITY MANAGEMENT (SCIM) LIBRARY

> **Status: superseded.** This library has been replaced by [`sas-ci360-sdk`](https://github.com/mnelson3/sas-ci360-sdk) — the same SCIM API, rebuilt with mockable unit tests, typed exceptions, and safer configuration defaults, now part of the consolidated SAS CI360 SDK monorepo. This repo is kept for historical reference; start new work in `sas-ci360-sdk` instead. This repo's final implementation is frozen at the `archive/superseded` branch.

### Overview

Identity Management for SAS Customer Intelligence 360. Use this REST API to manage users and roles. The System for Cross-domain Identity Management (SCIM) API for SAS Customer Intelligence 360 is a centralized, web-based repository that enables an organization to manage identity resources such as users, groups, and roles. The SCIM REST API is based on the SCIM industry standard.

For detailed information on REST API:<br>
https://support.sas.com/documentation/onlinedoc/ci/ci360-apis/scim/v2/redoc.html
<br><br>

### Table of Contents

This topic contains the following sections:

 - <a href="#prerequisites">Prerequisites</a>
 - <a href="#installation">Installation</a>
 - <a href="#getting-started">Getting Started</a>
 - <a href="#api-system-for-cross-domain-identity-management-code">API System for Cross-Domain Identity Management Code</a>
 - <a href="#troubleshooting">Troubleshooting</a>
 - <a href="#contributing">Contributing</a>
 - <a href="#license">License</a>
 - <a href="#additional-resources">Additional Resources</a>
<br><br>

### Prerequisites

 * Required Python: >=3.6
 * Customer Intelligence 360 Tenant with Administrative Rights
 * SAS CI360 API Core Library:<br>
   https://github.com/mnelson3/sas_ci360_api_core
<br><br>

### Installation

To install the SAS CI360 API System for Cross-Domain Identity Management Library from a clone of this repository:
 1. `git clone https://github.com/mnelson3/sas_ci360_api_scim.git`
 1. `cd sas_ci360_api_scim`
 1. `pip install .`
<br><br>

### Getting Started

While this library is available for review, please note that it is considered a work in process and NOT considered "released for production".
<br><br>

### API System for Cross-Domain Identity Management Code

 1. Groups - Contains operations for managing groups.
 1. Roles - Contains operations for managing roles.
 1. Configuration and Schemas - Contains operations for configuration and schemas.
 1. Users - Contains operations for managing users.
<br><br>

### Troubleshooting

For issues specific to sasci360apicore or sasci360apiscim try updating the libraries.

To update sasci360apicore:
 1. Open a terminal window (Unix/macOS) or command prompt (Windows)
 1. Copy and paste the following line at the cursor<br>
    pip install --upgrade git+https://github.com/mnelson3/sas_ci360_api_core.git@main
 1. Press "Enter"<br>
    The SAS CI360 API Core Library should update

To update sasci360apiscim:
 1. Pull the latest changes from a clone of this repository
 1. Open a terminal window (Unix/macOS) or command prompt (Windows) in that clone
 1. Copy and paste the following line at the cursor<br>
    pip install --upgrade .
 1. Press "Enter"<br>
    The SAS CI360 API System for Cross-Domain Identity Management Library should update
<br><br>

### Contributing

We welcome your contributions! Please read [CONTRIBUTING](CONTRIBUTING) for details on how to submit contributions to this project.
<br><br>

### License

This project is licensed under the [Nelson Grey LLC Community License 1.0](LICENSE).

- **Free for individuals, education, and research**: use, modify, and distribute this software for non-commercial purposes
- **Commercial evaluation**: evaluate the software for a possible commercial use, free of charge
- **Commercial production use**: requires a commercial license from Nelson Grey LLC
- **Automatic conversion**: on December 13, 2029, this automatically converts to the Apache License 2.0

For commercial licensing inquiries, contact support@nelsongrey.com.

### Additional Resources

For more information, see [REST APIs](https://go.documentation.sas.com/doc/en/cintcdc/production.a/cintapis/ch-rest-apis.htm).
<br><br>
