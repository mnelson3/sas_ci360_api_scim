# SAS Customer Intelligence 360

## SAS 360 API SYSTEM FOR CROSS-DOMAIN IDENTITY MANAGEMENT (SCIM) LIBRARY

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
   https://gitlab.sas.com/psd-ci-enablement/sas_ci360_api_core
<br><br>

### Installation

To install the SAS CI360 API System for Cross-Domain Identity Management Library:
 1. Open a terminal window (Unix/macOS) or command prompt (Windows)
 1. Replace `<YOUR_DEPLOY_TOKEN>` below with the read access deploy token for this project's package registry, then copy and paste the line at the cursor<br>
    pip install sasci360apiscim --extra-index-url https://sas_ci360_api_scim:<YOUR_DEPLOY_TOKEN>@gitlab.sas.com/api/v4/projects/49204/packages/pypi/simple
 1. Press "Enter"<br>
    The SAS CI360 API System for Cross-Domain Identity Management Library should install
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
    pip uninstall sasci360apicore
 1. Press "Enter"<br>
    The SAS CI360 API Core Library should uninstall
 1. Replace `<YOUR_DEPLOY_TOKEN>` below with the read access deploy token for the core project's package registry, then copy and paste the line at the cursor<br>
    pip install sasci360apicore --extra-index-url https://sas_ci360_api_core:<YOUR_DEPLOY_TOKEN>@gitlab.sas.com/api/v4/projects/35734/packages/pypi/simple
 1. Press "Enter"<br>
    The SAS CI360 API Core Library should install

To update sasci360apiscim:
 1. Open a terminal window (Unix/macOS) or command prompt (Windows)
 1. Copy and paste the following line at the cursor<br>
    pip uninstall sasci360apiscim
 1. Press "Enter"<br>
    The SAS CI360 API System for Cross-Domain Identity Management Library should uninstall
 1. Replace `<YOUR_DEPLOY_TOKEN>` below with the read access deploy token for this project's package registry, then copy and paste the line at the cursor<br>
    pip install sasci360apiscim --extra-index-url https://sas_ci360_api_scim:<YOUR_DEPLOY_TOKEN>@gitlab.sas.com/api/v4/projects/49204/packages/pypi/simple
 1. Press "Enter"<br>
    The SAS CI360 API System for Cross-Domain Identity Management Library should install
<br><br>

### Contributing

We welcome your contributions! Please read [CONTRIBUTING](CONTRIBUTING) for details on how to submit contributions to this project.
<br><br>

### License

This project is licensed under the [Apache 2.0 License](LICENSE).
<br><br>

### Additional Resources

For more information, see [REST APIs](https://go.documentation.sas.com/doc/en/cintcdc/production.a/cintapis/ch-rest-apis.htm).
<br><br>
