# R Observatory Data Pipeline 📡

## Overview
The **R Observatory Data Pipeline** is designed for **Satellite Laser Ranging (SLR) observatories**, automating the process of **downloading, processing, and archiving ephemerides data**. The package retrieves satellite ephemerides from the **International Laser Ranging Service (ILRS) datacenter** via **FTPS connection**, filters and compiles relevant datasets, and archives observational data efficiently.

## 🔑 Key Features
- **Automated Ephemerides Retrieval:** Downloads satellite ephemerides from the ILRS data center, excluding blacklisted satellites.
- **Sentinel A & B Retrieval:** Fetches restricted-access Sentinel satellite data via separate authentication.
- **Data Cleaning & Organization:** Parses and extracts satellite names, normalizing filenames by stripping timestamps.
- **Observational Data Archiving:** Identifies, compresses, and removes outdated observational data files.
- **Flash Drive Validation:** Ensures a flash drive is inserted before initiating archival to prevent accidental data loss.

## 📥 Ephemerides Downloading Process
1. Connects to the **ILRS FTPS server**.
2. Retrieves all available ephemerides, excluding entries listed in `BlackList.txt`.
3. Identifies satellites by **name only**, removing timestamp variations.
4. Fetches **Sentinel-3A and Sentinel-3B** ephemerides from a separate, restricted FTPS connection.
5. Compiles all retrieved ephemerides into a single structured file (`ephem`).

## 📂 Observational Data Management
### **Catalogue Clearing & Archiving**
- The program scans for specific observational data file extensions (`.oga`, `.ega`, `.esa`, `.prn`, etc.).
- Archives the identified files and deletes old directories.
- Checks for flash drive presence before initiating data wiping.

### **File Processing & Data Organization**
- Observational data is copied to a **temporary archive directory (`D:\archiv2\temp`)**.
- Directory is timestamped and compressed into a **ZIP archive**.
- Original data is safely removed to free up storage.

## 🔧 Technical Implementation
### **System Requirements**
- **OS:** Windows-based observatory system.
- **Dependencies:** Python with `ftplib`, `shutil`, `glob`, and `datetime` libraries.
- **Hardware:** Requires an **external flash drive** for archival validation.

### **Key Python Modules Used**
- **`ftplib` & `ftplib.FTP_TLS`**: Secure FTP connection for ephemerides retrieval.
- **`shutil`**: Copying, moving, and archiving files.
- **`glob`**: Pattern matching to filter relevant observational data files.
- **`datetime`**: Timestamping archived directories.
- **`ctypes` & `itertools`**: Detecting connected external drives.

## 📑 Workflow Summary
1. **Ephemerides Downloading:**
   - Connect to **ILRS FTPS**
   - Filter & retrieve **latest ephemerides**
   - Merge all datasets into **one ephemeris file**
2. **Observational Data Processing:**
   - Detects and archives **old observational data**
   - Clears specific **data extensions** from defined directories
   - Ensures **safe deletion** after compression
3. **Sentinel Data Retrieval:**
   - Fetch Sentinel A & B data via **separate authentication**
   - Append to main **ephemeris file**

## 🚀 Future Enhancements
- **Automated Scheduling:** Implement **cron job/task scheduler** for periodic downloads.
- **Cloud Integration:** Enable **remote data storage** for redundancy.
- **Enhanced Security:** Encrypt stored datasets & improve authentication protocols.
- **Multi-Observatory Support:** Extend compatibility for additional observatory networks.

---
**Developed for the Satellite Laser Ranging Observatory in Kyiv, Ukraine.**
