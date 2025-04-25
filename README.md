# Changelog-Gen

A tool to **automatically generate** `CHANGELOG.md` and GitHub Release 
notes by parsing Conventional Commits or PR titles, producing a 
standardized, multi-section changelog, and fully automating releases via 
GitHub Actions. :contentReference[oaicite:0]{index=0}

---

## Overview

Changelog-Gen is a command-line application that groups commits (e.g. 
`feat`, `fix`, `docs`) or PR labels into sections and updates 
`CHANGELOG.md`. It also supports a one-step command to create or update a 
GitHub Release draft. With configurable options and plugin support (e.g., 
Slack notifications, email), it integrates seamlessly into any GitHub 
workflow to save hours of manual release-note writing. 
:contentReference[oaicite:1]{index=1}

---

## Features

- **Automatic Changelog Generation**: Scans commit history since the last 
git tag, groups entries (Features, Bug Fixes, Docs, Chores), and updates 
`CHANGELOG.md` in a multi-level Markdown format. 
:contentReference[oaicite:2]{index=2}  
- **Release Automation**: Run `changelog-gen release --tag vX.Y.Z` to 
create or update a GitHub Release with the generated notes. 
:contentReference[oaicite:3]{index=3}  
- **GitHub Actions Integration**: Includes example 
`.github/workflows/changelog.yml` to trigger on new tags for fully 
automated changelog and release. :contentReference[oaicite:4]{index=4}  
- **Customizable**: Use a JSON or YAML config file to customize section 
headings, exclude commit types, or adjust output paths. 
:contentReference[oaicite:5]{index=5}  
- **Plugin-Ready**: Extend functionality with plugins (e.g., Slack, email, 
web UI) via a simple plugin API. :contentReference[oaicite:6]{index=6}

---

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/yourname/changelog-gen.git
``` :contentReference[oaicite:7]{index=7}

Or clone the repository and install locally:

```bash
git clone https://github.com/yourname/changelog-gen.git
cd changelog-gen
pip install -e .
``` :contentReference[oaicite:8]{index=8}

---

## Usage Examples

### Generate Changelog Locally

```bash
# Update CHANGELOG.md for commits since tag v1.0.0
changelog-gen generate --since-tag v1.0.0
``` :contentReference[oaicite:9]{index=9}

### Create or Update GitHub Release

```bash
# Create or update a Release draft for tag v1.0.0
changelog-gen release --tag v1.0.0
``` :contentReference[oaicite:10]{index=10}

### Using with GitHub Actions

Add this workflow to `.github/workflows/changelog.yml`:

```yaml
name: Generate & Publish Changelog

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  changelog:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Install Dependencies
        run: pip install -r requirements.txt
      - name: Generate & Release
        run: |
          changelog-gen generate --since-tag ${{ github.ref_name }}
          changelog-gen release --tag ${{ github.ref_name }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
``` :contentReference[oaicite:11]{index=11}

---

## Configuration

Create `changelog-gen.config.yml` (or `.json`) in your repo root:

```yaml
# changelog-gen.config.yml
sections:
  - title: Features
    types: [feat]
  - title: Bug Fixes
    types: [fix]
  - title: Documentation
    types: [docs]
  - title: Chores
    types: [chore]
exclude:
  - test
output: CHANGELOG.md
