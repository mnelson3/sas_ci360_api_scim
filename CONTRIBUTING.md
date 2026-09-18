# How to Contribute

We'd love to accept your patches and contributions to this project. There are just a few small guidelines you need to follow.

## Contributor License Agreement

Contributions to this project must be accompanied by a signed
[Contributor Agreement](CONTRIBUTOR_AGREEMENT.txt). You (or your employer) retain the copyright to your contribution, this simply gives us permission to use and redistribute your
contributions as part of the project.

## Code reviews

All submissions, including submissions by project members, require review. We use GitHub pull requests for this purpose. Consult
[GitHub Help](https://help.github.com/articles/about-pull-requests/) for more information on using pull requests.

## Branching

This project uses three long-lived branches:

 - `develop` — active development; feature branches target this branch.
 - `staging` — release candidates promoted from `develop` for pre-release verification.
 - `main` — released, production-ready code.

Open pull requests against `develop` for new work. Changes are promoted `develop` &rarr; `staging` &rarr; `main` as they're verified.

## Running tests

The test suite in `tests/` requires the internal `sasci360apicore` package (installed from SAS's internal package registry, see [README](README.md#installation)) and a live CI360 tenant. Replace the placeholder `secret_key`/`tenant_id` values in each test file's `setUp` with credentials for your own tenant before running them locally.
