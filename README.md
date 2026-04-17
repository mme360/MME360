# MME360 Analyzer Support Platform

This repository contains the foundation for the MME analyzer support platform.

## Goal
Build an ERPNext-based application for after-sales support and laboratory analyzer visibility.

## Core stack
- ERPNext as the business backbone
- Marley Health for healthcare and lab workflow support
- Custom MME app for analyzer connectivity, QC, calibration, maintenance, alerts, and support evidence
- GitHub for source control, planning, and releases

## Phase 1 scope
1. Analyzer Registry
2. Customer Site mapping
3. QC Log
4. Calibration Log
5. Maintenance Log
6. Alert Rules
7. Support Case integration

## First ERPNext screens
- Fleet Dashboard
- Analyzer Detail
- Support Case View
- Customer Site View
- Alert Center

## Architecture rule
ERPNext/Marley own operational records.
The custom analyzer layer owns machine events and analyzer intelligence.
