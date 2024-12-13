---
title: "MODIS Data"
date: 2023-12-13
draft: false
description: "Guide for using MODIS data in EO-PERSIST"
---

# MODIS Data Integration

## Overview

The Moderate Resolution Imaging Spectroradiometer (MODIS) provides daily global coverage with moderate spatial resolution, making it ideal for monitoring large-scale Arctic changes. MODIS instruments are aboard both the Terra and Aqua satellites.

## Available Products

### Land Products

#### Surface Temperature (MOD11)
- MOD11A1: Daily LST at 1km
- MOD11A2: 8-day composites
- MOD11B1: Daily 6km grid
- Quality indicators included

#### Snow Cover (MOD10)
- MOD10A1: Daily snow cover
- MOD10A2: 8-day composites
- Snow albedo products
- 500m resolution

#### Vegetation Indices (MOD13)
- MOD13A1: 16-day 500m
- MOD13A2: 16-day 1km
- NDVI and EVI indices
- Quality detailed QA

#### BRDF/Albedo (MCD43)
- MCD43A1: Daily BRDF
- MCD43A2: Quality flags
- MCD43A3: Albedo
- MCD43A4: Nadir BRDF

### Atmosphere Products

#### Cloud Products (MOD06)
- Cloud top properties
- Cloud phase
- Cloud fraction
- Optical properties

#### Atmospheric Profiles (MOD07)
- Temperature profiles
- Moisture profiles
- Atmospheric stability
- Total column ozone

#### Aerosol Products (MOD04)
- Aerosol optical depth
- Size distribution
- Type discrimination
- Quality assurance

### Cryosphere Products

#### Sea Ice Products (MOD29)
- Sea ice extent
- Sea ice surface temperature
- Ice age classification
- Lead detection

#### Ice Surface Temperature
- Daily measurements
- 1km resolution
- Thermal anomalies
- Quality flags

## Specifications

### Temporal Characteristics

#### Revisit Time
- Terra: 10:30 AM equator crossing
- Aqua: 1:30 PM equator crossing
- Combined daily coverage

#### Product Timeframes
- Daily products
- 8-day composites
- 16-day composites
- Monthly aggregates

### Spatial Characteristics

#### Resolution Bands
- 250m: Bands 1-2
  - Red (620-670 nm)
  - NIR (841-876 nm)

- 500m: Bands 3-7
  - Blue to SWIR
  - Land/cloud properties

- 1000m: Bands 8-36
  - Ocean color
  - Atmospheric properties
  - Thermal bands

#### Coverage
- Global coverage
- 2330 km swath width
- Polar optimization

### Spectral Characteristics

#### Visible/NIR (Bands 1-19)
- Land/cloud boundaries
- Vegetation properties
- Ocean color

#### SWIR (Bands 20-25)
- Surface/cloud temperature
- Atmospheric properties
- Fire detection

#### Thermal IR (Bands 26-36)
- Cloud top altitude
- Atmospheric temperature
- Surface temperature

## Data Access

### Primary Sources

#### NASA LAADS DAAC
- Direct download
- Order management
- User support
- Documentation

#### NSIDC DAAC
- Cryosphere products
- Arctic focus
- Value-added products
- Tools and support

#### Cloud Platforms
- Google Earth Engine
- AWS Open Data
- Microsoft Planetary

### Processing Levels

#### Level 1
- 1A: Raw counts
- 1B: Calibrated radiances

#### Level 2
- Geophysical variables
- Original swath format
- Full resolution

#### Level 3
- Gridded products
- Temporal composites
- Quality enhanced

## Processing

### Pre-processing Steps

#### Data Preparation
- Format conversion
- Quality assessment
- Cloud masking
- Reprojection

#### Calibration
- Radiometric correction
- Atmospheric correction
- BRDF normalization
- Scale factor application

### Analysis Methods

#### Time Series Analysis
- Trend detection
- Seasonal patterns
- Change detection
- Anomaly detection

#### Spatial Analysis
- Regional statistics
- Spatial patterns
- Zonal analysis
- Aggregation methods

## Integration

### EO-PERSIST Workflow

#### Data Collection
- Automated downloads
- Quality filtering
- Storage management
- Version control

#### Processing Chain
- Standard procedures
- Quality checks
- Error handling
- Documentation

#### Product Generation
- Custom formats
- Metadata creation
- Validation steps
- Distribution methods

## References

### Documentation
1. MODIS User Guide
2. Product Documentation
3. Algorithm Theoretical Basis Documents

### Scientific Literature
1. Validation studies
2. Arctic applications
3. Method developments
