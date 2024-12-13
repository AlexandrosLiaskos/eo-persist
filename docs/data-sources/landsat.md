---
title: "Landsat Data"
date: 2023-12-13
draft: false
description: "Guide for using Landsat data in EO-PERSIST"
---

# Landsat Data Integration

## Overview

Landsat represents NASA's longest-running program for Earth observation satellite imagery, providing continuous data since 1972. For Arctic permafrost monitoring, we primarily utilize Landsat 8 and Landsat 9 data.

## Specifications

### Temporal Characteristics

1. Revisit Time
   - 16-day repeat cycle
   - 8-day combined coverage (L8 & L9)
   - Seasonal limitations in Arctic

2. Archive Depth
   - Landsat 8: 2013-present
   - Landsat 9: 2021-present
   - Historical data available

### Spatial Characteristics

1. Resolution Classes
   - Panchromatic: 15m
   - Multispectral: 30m
   - Thermal: 100m

2. Scene Coverage
   - 185km x 180km scene size
   - WRS-2 path/row system
   - Polar orbit optimization

### Spectral Characteristics

1. Visible and Near-Infrared
   - Band 1: Coastal/Aerosol (0.433-0.453 µm)
   - Band 2: Blue (0.450-0.515 µm)
   - Band 3: Green (0.525-0.600 µm)
   - Band 4: Red (0.630-0.680 µm)
   - Band 5: NIR (0.845-0.885 µm)

2. Shortwave Infrared
   - Band 6: SWIR-1 (1.560-1.660 µm)
   - Band 7: SWIR-2 (2.100-2.300 µm)
   - Band 9: Cirrus (1.360-1.390 µm)

3. Thermal Infrared
   - Band 10: TIR-1 (10.6-11.2 µm)
   - Band 11: TIR-2 (11.5-12.5 µm)

4. Panchromatic
   - Band 8: Pan (0.500-0.680 µm)

## Applications

### Surface Temperature Analysis

1. Processing Steps
   - Convert to Top of Atmosphere (TOA) Radiance
   - Apply atmospheric correction
   - Convert to surface temperature
   - Apply quality control filters

2. Quality Control
   - Cloud masking
   - Water masking
   - QA band filtering
   - Atmospheric correction

### Land Cover Analysis

1. Vegetation Indices
   - NDVI (Normalized Difference Vegetation Index)
   - EVI (Enhanced Vegetation Index)
   - SAVI (Soil Adjusted Vegetation Index)
   - NDMI (Normalized Difference Moisture Index)

2. Classification Methods
   - Supervised classification
   - Object-based analysis
   - Time series classification
   - Change detection

## Data Access

### Primary Sources

1. USGS Earth Explorer
   - Full archive access
   - Bulk download tools
   - Collection 2 products
   - Processing options

2. Cloud Platforms
   - Google Earth Engine
   - AWS Open Data
   - Microsoft Planetary

### Processing Levels

1. Level 1
   - L1TP: Precision terrain corrected
   - L1GT: Systematic terrain corrected
   - L1GS: Systematic corrected

2. Level 2
   - Surface reflectance
   - Surface temperature
   - Quality assessment
   - Cloud masks

## Processing

### Pre-processing Steps

1. Radiometric Correction
   - DN to radiance
   - TOA reflectance
   - Surface reflectance
   - Atmospheric correction

2. Geometric Correction
   - Orthorectification
   - Co-registration
   - Terrain correction

### Analysis Methods

1. Time Series Analysis
   - Trend detection
   - Seasonal patterns
   - Change detection
   - Gap filling

2. Spatial Analysis
   - Regional statistics
   - Spatial patterns
   - Feature extraction
   - Terrain analysis

## Integration

### EO-PERSIST Workflow

1. Data Collection
   - Scene selection
   - Quality filtering
   - Automated downloads
   - Storage management

2. Processing Chain
   - Standard procedures
   - Quality checks
   - Error handling
   - Documentation

3. Product Generation
   - Custom formats
   - Metadata creation
   - Validation steps
   - Distribution methods

## References

### Documentation
1. Landsat 8-9 User Guide
2. USGS Data Products
3. Algorithm Documentation

### Scientific Literature
1. Validation studies
2. Arctic applications
3. Method developments
