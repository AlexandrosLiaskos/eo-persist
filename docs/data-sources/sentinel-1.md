# Sentinel-1

## Overview

Sentinel-1 is a radar imaging satellite mission consisting of two satellites, Sentinel-1A and Sentinel-1B, as part of the European Union's Copernicus Programme.

## Specifications

### Sensor Type

#### Radar System
- C-band Synthetic Aperture Radar (SAR)
- Center frequency: 5.405 GHz
- Polarization: VV+VH, HH+HV
- All-weather, day-and-night imaging capability

### Resolution

#### Imaging Modes
1. Strip Map Mode (SM)
   - Resolution: 5 x 5 m
   - Swath width: 80 km

2. Interferometric Wide Swath (IW)
   - Resolution: 5 x 20 m
   - Swath width: 250 km
   - Default mode over land

3. Extra-Wide Swath Mode (EW)
   - Resolution: 20 x 40 m
   - Swath width: 400 km
   - Default mode over sea-ice

4. Wave Mode (WV)
   - Resolution: 5 x 20 m
   - Vignette size: 20 x 20 km
   - Sampling: Every 100 km

### Coverage

#### Temporal Resolution
- 6-day repeat cycle (both satellites)
- 12-day repeat cycle (single satellite)
- Sub-daily coverage at polar regions

#### Spatial Coverage
- Global coverage capability
- Enhanced coverage over:
  - Polar regions
  - Shipping routes
  - Land masses

## Applications

### Permafrost Monitoring

1. Surface Deformation
   - InSAR time series
   - Subsidence mapping
   - Seasonal movement

2. Infrastructure Stability
   - Building monitoring
   - Pipeline surveillance
   - Road network assessment

3. Coastal Dynamics
   - Erosion monitoring
   - Shoreline changes
   - Storm impact assessment

### Snow and Ice Monitoring

1. Sea Ice Mapping
   - Ice type classification
   - Ice concentration
   - Ice drift tracking

2. Glacier Monitoring
   - Velocity mapping
   - Calving front position
   - Mass balance estimation

3. Snow Cover Analysis
   - Wet snow mapping
   - Snow water equivalent
   - Seasonal patterns

## Data Access

### Data Sources

1. Primary Distributors
   - Copernicus Open Access Hub
   - Alaska Satellite Facility
   - Sentinel Hub

2. Cloud Platforms
   - Google Earth Engine
   - AWS Registry of Open Data
   - Microsoft Planetary Computer

### Processing Levels

1. Level-0
   - Raw SAR data
   - Full resolution
   - Complex samples

2. Level-1
   - Single Look Complex (SLC)
     - Complex samples
     - Full resolution
     - Phase preserved
   - Ground Range Detected (GRD)
     - Detected, multi-looked
     - Ground projected
     - Square pixels

3. Level-2
   - Ocean Products
     - Wind fields
     - Wave spectra
     - Surface currents
   - Land Products
     - Surface movement
     - Soil moisture
     - Change detection

## Processing

### Pre-processing Steps

1. Radiometric Calibration
   - Sigma0 calculation
   - Beta0 calculation
   - Gamma0 calculation

2. Geometric Corrections
   - Terrain correction
   - Geocoding
   - Co-registration

3. Speckle Filtering
   - Multi-looking
   - Adaptive filters
   - Time series filtering

### Analysis Methods

1. Change Detection
   - Amplitude-based
   - Coherence-based
   - Time series analysis

2. InSAR Processing
   - DInSAR
   - PSInSAR
   - SBAS

3. Classification
   - Supervised methods
   - Object-based analysis
   - Machine learning

## Integration

### EO-PERSIST Workflow

1. Data Acquisition
   - Automated downloads
   - Quality checking
   - Metadata extraction

2. Processing Chain
   - Batch processing
   - Error handling
   - Version control

3. Product Generation
   - Standardized formats
   - Quality assessment
   - Documentation

## References

### Documentation
1. ESA Sentinel Online
2. Copernicus User Guide
3. ASF Data Handbook

### Scientific Papers
1. InSAR techniques
2. Arctic applications
3. Method validation
