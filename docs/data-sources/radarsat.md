---
title: "RADARSAT Data"
date: 2023-12-13
draft: false
description: "Guide for using RADARSAT data in EO-PERSIST"
---

# RADARSAT Data Integration

## Overview

RADARSAT is a series of Canadian Earth observation satellites that use Synthetic Aperture Radar (SAR) technology. RADARSAT-2 and the RADARSAT Constellation Mission (RCM) provide valuable data for Arctic monitoring, especially during polar nights and through cloud cover.

## Satellite Systems

### RADARSAT-2

#### System Characteristics

* Launch: December 14, 2007
* Status: Operational
* Design Life: 7 years (exceeded)
* Mass: 2,200 kg

#### Orbit Parameters

* Type: Sun-synchronous
* Altitude: 798 km
* Inclination: 98.6 degrees
* Period: 100.7 minutes

#### Coverage

* Revisit: 24 days nominal
* Daily Arctic coverage
* Right and left-looking

### RADARSAT Constellation

#### System Characteristics

* Launch: June 12, 2019
* Status: Operational
* Design Life: 7 years
* Mass: 1,430 kg each

#### Orbit Parameters

* Type: Sun-synchronous
* Altitude: 592.7 km
* Inclination: 97.74 degrees
* Period: 96.4 minutes

#### Coverage

* 4-day repeat cycle
* Sub-daily Arctic coverage
* Enhanced maritime monitoring

## Imaging Capabilities

### RADARSAT-2 Modes

#### Spotlight

* Resolution: 1 x 1 m
* Scene size: 18 x 8 km
* Applications:
	+ Infrastructure monitoring
	+ Target detection
	+ Precise mapping

#### Ultra-Fine

* Resolution: 3 x 3 m
* Scene size: 20 x 20 km
* Applications:
	+ Urban monitoring
	+ Coastal mapping
	+ Ice classification

#### Wide Ultra-Fine

* Resolution: 3 x 3 m
* Scene size: 50 x 50 km
* Applications:
	+ Coastal surveillance
	+ Ship detection
	+ Ice monitoring

#### Fine

* Resolution: 8 x 8 m
* Scene size: 50 x 50 km
* Applications:
	+ Land use mapping
	+ Change detection
	+ Resource monitoring

### RCM Modes

#### Very High Resolution

* Resolution: 1 x 3 m
* Scene size: 20 x 20 km
* Applications:
	+ Infrastructure monitoring
	+ Ship detection
	+ Ice lead mapping

#### High Resolution

* Resolution: 3 x 9 m
* Scene size: 50 x 50 km
* Applications:
	+ Coastal monitoring
	+ Sea ice mapping
	+ Land use change

#### Medium Resolution

* Resolution: 16 x 30 m
* Scene size: 125 x 125 km
* Applications:
	+ Wide area monitoring
	+ Ice extent mapping
	+ Ocean surveillance

## Applications

### Arctic Monitoring

#### Sea Ice Analysis

1. Processing Steps
   - Calibrate backscatter values
   - Classify ice types
   - Extract characteristics:
     * Ice concentration
     * Ice thickness
     * Surface roughness
   - Quality assessment

#### Surface Deformation

1. InSAR Processing Chain
   - Image coregistration
   - Interferogram generation
   - Phase processing
   - Displacement calculation
   - Coherence assessment

## Data Access

### Official Sources

#### Canadian Space Agency

* Project proposals
* Research agreements
* Commercial licenses
* Training resources

#### Commercial Distributors

* MDA Corporation
* Regional providers
* Value-added resellers
* Processing services

### Data Products

#### Level 1

* Single Look Complex
* Ground Range Detected
* Path Image
* Geocoded products

#### Level 2

* Ocean wind field
* Surface movement
* Ice classification
* Ship detection

## Processing

### Pre-processing Steps

#### Radiometric Correction

* Antenna pattern
* Range spreading loss
* Incidence angle
* Calibration factors

#### Geometric Correction

* Orbit state vectors
* Digital elevation model
* Ground control points
* Geoid model

### Analysis Methods

#### Change Detection

* Amplitude-based
* Coherence-based
* Time series
* Feature tracking

#### Classification

* Supervised learning
* Object-based
* Texture analysis
* Polarimetric

## Integration

### EO-PERSIST Workflow

#### Data Management

* Acquisition planning
* Storage organization
* Version control
* Quality assurance

#### Processing Chain

* Automated processing
* Quality control
* Product generation
* Archive management

#### Analysis Pipeline

* Standard procedures
* Custom algorithms
* Validation methods
* Result delivery

## References

### Documentation

1. RADARSAT-2 Product Guide
2. RCM Product Description
3. SAR Processing Guide

### Scientific Literature

1. Arctic applications
2. Method development
3. Validation studies
