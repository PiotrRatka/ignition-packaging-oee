# ignition-packaging-oee

## EN/PL below.



# [EN] Packaging Line SCADA / OEE System 

Demo SCADA/MES dashboard for a packaging line built in Ignition 8.1 Perspective, connected to MS SQL Server.

## Overview

The application monitors production metrics and line status to calculate real-time OEE (Availability, Performance, Quality). It includes recipe handling via SQL queries, tag historization, alarm management, and simulated telemetry driven by a Gateway script.

## Features

- **Real-Time OEE:** Continuous calculation of Availability, Performance, and Quality based on line state and speed setpoints.
- **Recipe Management:** Format selection (500g, 1000g, 250g) pulls nominal speed and scrap limits from SQL Server via Named Queries.
- **Historian & Trends:** Live and historical speed logging displayed on a Perspective Power Chart.
- **Alarm Handling:** Alarm Status Table configured with priority filtering and acknowledgment workflow.
- **Simulation Script:** Gateway Timer Script (1000 ms) generating speed oscillations, fractional piece counts, and scrap occurrences.

## Stack

- Ignition 8.1 Perspective
- MS SQL Server (JDBC)
- Python / Jython (Gateway Events)
- User Defined Types (UDTs)

## Project Structure

- `.dashboard` - dashboard screenshot and demo files
- `.packaging_demo` - gif showcasing working programme
- `ignition-exports/` - project zip and UDT/tag definitions (JSON)
- `scripts/` - standalone Python simulation script
- `schema_and_recepies` - database schema and recipe seed data

## Setup

1. Run `sql/schema_and_recipes.sql` on your SQL Server instance.
2. Add a database connection named `PackagingDB` in Ignition Gateway (`Config > Databases > Connections`).
3. Import `ignition-exports/tags.json` in Tag Browser (`default` provider).
4. Import `ignition-exports/Packaging_Proj.zip` via Gateway Web UI (`Config > Projects > Import Project`).
5. Open the project in Perspective Workstation or browser.



# [PL] System SCADA / OEE linii pakującej

Aplikacja demonstracyjna SCADA/MES dla linii pakującej wykonana w Ignition 8.1 (Perspective) i zintegrowana z bazą MS SQL Server.

## Opis projektu

Aplikacja monitoruje parametry produkcyjne oraz stan pracy maszyny, wyliczając wskaźniki OEE (Dostępność, Wydajność, Jakość) w czasie rzeczywistym. Projekt obejmuje obsługę receptur przez zapytania SQL, archiwizację danych procesowych w Tag Historianie, obsługę alarmów oraz symulację telemetrii realizowaną przez Gateway Timer Script.

## Funkcjonalności

- **Wyliczanie OEE:** Ciągła kalkulacja Dostępności, Wydajności i Jakości na podstawie bieżącego stanu linii oraz parametrów nominalnych receptury.
- **Zarządzanie recepturami:** Wybór formatu (500g, 1000g, 250g) pobiera prędkość zadaną oraz limit odrzutów z bazy SQL Server za pomocą Named Queries.
- **Trendy i archiwizacja:** Rejestracja prędkości rzeczywistej w bazie danych i wizualizacja na komponencie Power Chart.
- **Obsługa alarmów:** Komponent Alarm Status Table z podziałem na priorytety i obsługą potwierdzania zdarzeń awaryjnych.
- **Skrypt symulacji:** Gateway Timer Script (1000 ms) generujący oscylacje prędkości, buforowanie części ułamkowych wyrobów oraz odrzuty jakościowe.

## Stos technologiczny

- Ignition 8.1 Perspective
- MS SQL Server (połączenie JDBC)
- Python / Jython (Gateway Events)
- User Defined Types (struktury UDT)

## Struktura projektu

- `packaging_gif` - gif prezentujący dzialanie programu
- `dashboard` - zrzut ekranu pulpitu operatorskiego i materiały demonstracyjne
- `ignition_exports/` - eksport projektu (.zip) oraz definicje tagów i UDT (.json)
- `scripts/` - kod źródłowy skryptu symulacji w Pythonie
- `schema_and_recepies` - schemat tabel bazodanowych i dane startowe receptur

## Uruchomienie

1. Wykonaj skrypt `sql/schema_and_recipes.sql` na instancji SQL Server.
2. Skonfiguruj połączenie bazodanowe o nazwie `PackagingDB` w bramie Ignition (`Config > Databases > Connections`).
3. Zaimportuj plik `ignition-exports/tags.json` w Tag Browserze (provider `default`).
4. Zaimportuj projekt `ignition-exports/Packaging_Proj.zip` przez Gateway Web UI (`Config > Projects > Import Project`).
5. Otwórz projekt w Perspective Workstation lub w przeglądarce.
