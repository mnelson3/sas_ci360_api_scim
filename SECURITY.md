# Security Policy

## Supported Versions

This repository holds the archived, superseded System for Cross-domain Identity Management (SCIM) REST API library for SAS Customer Intelligence 360, retained as a historical/reference repo — the maintained implementation now lives in [`sas-ci360-sdk`](https://github.com/mnelson3/sas-ci360-sdk). Only the code currently deployed on each environment branch is supported — there is no long-term support for older commits.

| Branch | Environment | Status |
|---|---|---|
| `main` | Production | Supported |
| `staging` | Staging | Supported |
| `develop` | Development | Supported |

## Reporting a Vulnerability

This repository doesn't have a public issue tracker, so please don't report security concerns that way. Use one of:

- GitHub's [private vulnerability reporting](https://github.com/mnelson3/sas_ci360_api_scim-archived/security/advisories/new) (enabled on this repo), or
- Email **support@nelsongrey.com**

Either way, include:

- A description of the vulnerability and its potential impact
- Steps to reproduce, or a proof of concept if available
- Any relevant logs, request/response samples, or affected endpoints

You should get an acknowledgement within a few business days.

## Automated Dependency Scanning

Dependabot alerts and security updates, native GitHub secret scanning (with push protection), and code scanning (CodeQL) are all enabled on this repository. Avoid committing credentials or secrets regardless — this library talks to SAS CI360 via API credentials supplied at runtime through environment variables/config passed in by the caller, never committed to source.
